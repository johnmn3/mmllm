#!/usr/bin/env bash
# run_round8.sh — restore the consolidation pipeline I broke.
#
# What round-6/7 did wrong vs the original design:
#   - distill OFF      → no Local→Net transfer (the whole point)
#   - LR_NET HIGH      → backwards: wake Net should be slow
#   - LR_BANK normal   → backwards: wake Local should be fast (hill-climb)
#   - LR_DENSE normal  → backwards: trunk should move very slowly
#   - replay OFF       → drops earlier wins
#
# Round-8 restores the design:
#   - distill ON          (MSE(net_out, local_out.detach()), the existing transfer)
#   - LR_BANK high        (Local hill-climbs wake patterns)
#   - LR_NET low          (slow consolidation receiver)
#   - LR_DENSE 5% of bank (trunk barely moves)
#   - replay restored
#
# Resumes from core/round-6/step-5000 (the FedAvg-merged community core:
# fim_eval=5.804, format_validity=0.110).
#
# Usage:  bash scripts/run_round8.sh <HANDLE>

set -e

HANDLE="${1:-}"
if [ -z "$HANDLE" ]; then
  echo "usage: bash scripts/run_round8.sh <HANDLE>" >&2
  exit 1
fi

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# ── NetBank knobs (must be set before preflight) ────────────────────────────
export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32

# ── 3-way SwitchGate + alpha_net ────────────────────────────────────────────
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true

# ── Consolidation distillation ──────────────────────────────────────────────
# collect-distill-loss in core.lpy walks every SwitchGate, computes
# MSE(net_out, local_out.detach()) averaged across layers, adds to the
# backward loss. Local is detached so the gradient only modifies Net.
# This is the Local→Net transfer mechanism: as Local accumulates wake
# patterns, the MSE pushes Net to mimic Local's contribution.
export MMLLM_DISTILL_COEF=0.1
export MMLLM_DISTILL_DIRECTION_ONLY=false  # round-4: direction-only made Net redundant

# ── Replay (RESTORED) ───────────────────────────────────────────────────────
# When Local masters a position (plain-CE < threshold), stash in replay
# buffer and re-train on it periodically. Stops Local from forgetting
# earlier wins as it pushes into harder patterns during wake.
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5

# ── LR balance per design ───────────────────────────────────────────────────
# Local: hill-climbs novel patterns → high LR
# Net:   slow consolidation receiver → low LR
# Trunk: at 5% of bank LR → barely moves
export MMLLM_LR_BANK_MULT=10.0
export MMLLM_LR_BANK_MULT_END=10.0
export MMLLM_LR_NET_MULT=0.5
export MMLLM_LR_NET_MULT_END=0.5
export MMLLM_LR_DENSE_MULT=0.5      # 5% of bank's 10×
export MMLLM_LR_DENSE_MULT_END=0.5
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3

# ── Round-6 → 8 resume contract ─────────────────────────────────────────────
# Keep harvested NetBank V; don't overwrite it from Local at startup.
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false

# ── Net-default routing (straight-through Bernoulli Local) ──────────────────
# SwitchGate runs Net + sdpa unconditionally and gates Local on a per-
# (B, H, T) Bernoulli decision. Init bias=-2.0 → sigmoid(-2.0) ≈ 12% of
# queries fire Local at step 0. Net is structurally the default; Local
# is on-demand for "things Net doesn't cover yet". Gate is end-to-end
# trainable via straight-through (forward=hard 0/1, backward=sigmoid grad).
# Telemetry adds last_local_firing_rate per gate per forward.
export MMLLM_GATE_NET_DEFAULT=true

export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-250}"

# ── 0. Preflight ────────────────────────────────────────────────────────────
bash scripts/preflight_fim_run.sh || { echo "preflight failed; aborting" >&2; exit 1; }
source /tmp/mmllm-cpu/preflight.env

if [[ "${RESUME_FROM:-}" != *"round-6"* ]]; then
  echo "round-8 needs core/round-6/step-5000/ as resume seed but preflight selected: ${RESUME_FROM:-(none)}" >&2
  exit 1
fi
echo "  ✓ resuming from round-6 community core: ${RESUME_FROM}"

# ── 1. Corpus (full, no sharding) ───────────────────────────────────────────
SRC=/tmp/mmllm-cpu/sources
mkdir -p "$SRC"
if [ ! -f "$SRC/xlam-synth.train.bin" ]; then
  python scripts/prep_xlam_synth.py "$SRC/xlam-synth" 20000 500000 500000
fi

JSON_DIR="$SRC/xlam-json"
if [ ! -d "$JSON_DIR" ] || [ -z "$(ls "$JSON_DIR" 2>/dev/null)" ]; then
  mkdir -p "$JSON_DIR"
  python3 - <<'PY'
from pathlib import Path
data = Path("/tmp/mmllm-cpu/sources/xlam-synth.train.bin").read_bytes()
docs = [d for d in data.split(b"\n\n") if 100 < len(d) < 4096][:20000]
out = Path("/tmp/mmllm-cpu/sources/xlam-json")
for i, d in enumerate(docs):
    (out / f"doc-{i:05d}.json").write_bytes(d)
print(f"wrote {len(docs)} files")
PY
fi

FIM_BASE=/tmp/mmllm-cpu/fim-json
if [ ! -f "${FIM_BASE}.train.bin" ]; then
  mmllm fim-build-corpus json "$JSON_DIR" "$FIM_BASE" 0.7 0.5 42
fi

# ── 2. Resume seed staging ──────────────────────────────────────────────────
if [ -n "${RESUME_FROM:-}" ] && [ -f "${RESUME_FROM}" ]; then
  rm -rf "${FIM_BASE}.ckpts"
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${RESUME_FROM}" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  echo "  resuming from ${RESUME_FROM} (staged at step-1; ckpts dir wiped first)"

  # Belt-and-suspenders alongside MMLLM_SKIP_NETBANK_WARMSTART: empty
  # opt-sparse-net.pt is the path-existence signal load-checkpoint! uses.
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  # Expand harvested NetBank V (round-6 fp16) into the runtime mmap.
  RESUME_DIR=$(dirname "${RESUME_FROM}")
  python3 - "${RESUME_DIR}" "/tmp/mmllm-cpu/fim-bank" <<'PY'
import sys, numpy as np
from pathlib import Path
resume_dir = Path(sys.argv[1])
bank_base  = sys.argv[2]
restored = 0
for fp16_file in sorted(resume_dir.glob("bank-net-latest.*.fp16.bin")):
    parts = fp16_file.name.split(".")
    if len(parts) < 4: continue
    try:    layer = int(parts[1])
    except: continue
    arr16 = np.fromfile(fp16_file, dtype=np.float16)
    out   = Path(f"{bank_base}-net.{layer}.bin")
    out.parent.mkdir(parents=True, exist_ok=True)
    arr16.astype(np.float32).tofile(out)
    restored += 1
    print(f"  NetBank V layer {layer} restored from round-6 core "
          f"({out.stat().st_size/1e6:.1f} MB fp32)")
PY
fi

# ── 3. Train ────────────────────────────────────────────────────────────────
BANK_BASE=/tmp/mmllm-cpu/fim-bank
TRAIN_LOG=/tmp/mmllm-cpu/round8-${HANDLE}.train.log
TOTAL_STEPS="${MMLLM_TOTAL_STEPS:-5000}"
EVAL_EVERY="${MMLLM_EVAL_EVERY:-250}"
CKPT_EVERY="${MMLLM_CKPT_EVERY:-1000}"
mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

# ── 4. Evals ────────────────────────────────────────────────────────────────
FIM_EVAL_JSONL=/tmp/mmllm-cpu/fim-eval.jsonl
if [ ! -f "$FIM_EVAL_JSONL" ]; then
  python scripts/build_fim_eval.py
fi
FIM_EVAL_LOG=/tmp/mmllm-cpu/round8-${HANDLE}.fim-eval.txt
mmllm fim-eval "${FIM_BASE}.ckpts" "$FIM_EVAL_JSONL" "${TOTAL_STEPS}" 2>&1 | tee "$FIM_EVAL_LOG"

AGENT_EVAL_LOG=/tmp/mmllm-cpu/round8-${HANDLE}.agent-eval.txt
mmllm eval-agent "$FIM_BASE" "${TOTAL_STEPS}" "$BANK_BASE" \
    "$SRC/xlam-synth.test.bin" xlam 100 256 2>&1 | tee "$AGENT_EVAL_LOG" || true

# ── 5. Stage + meta ─────────────────────────────────────────────────────────
WORKER_DIR="workers/$HANDLE/step-${TOTAL_STEPS}"
mkdir -p "$WORKER_DIR"
cp "${FIM_BASE}.ckpts/step-${TOTAL_STEPS}/dense.pt" "$WORKER_DIR/dense.pt"

python3 - "${BANK_BASE}" "${WORKER_DIR}" <<'PY'
import sys, numpy as np
from pathlib import Path
bank_base = sys.argv[1]
wdir      = Path(sys.argv[2])
shipped   = 0
for src in sorted(Path("/tmp/mmllm-cpu").glob(f"{Path(bank_base).name}-net.*.bin")):
    parts = src.name.split(".")
    try:    layer = int(parts[1])
    except: continue
    arr32 = np.fromfile(src, dtype=np.float32)
    dst   = wdir / f"bank-net-latest.{layer}.fp16.bin"
    arr32.astype(np.float16).tofile(dst)
    shipped += 1
    print(f"  staged NetBank V layer {layer}: {dst.name} ({dst.stat().st_size/1e6:.1f} MB fp16)")
PY

cp "${FIM_BASE}.log.jsonl" "$WORKER_DIR/log.jsonl" 2>/dev/null || true

python3 - "$HANDLE" "$TRAIN_LOG" "$FIM_EVAL_LOG" "$AGENT_EVAL_LOG" "$WORKER_DIR" "$TOTAL_STEPS" <<'PY'
import json, re, sys
from pathlib import Path
handle, tlog, felog, aelog, wdir, total_steps = sys.argv[1:7]
total_steps = int(total_steps)

def grep_last(path, pat, cast=float):
    try:
        ms = re.findall(pat, Path(path).read_text())
        return cast(ms[-1]) if ms else None
    except FileNotFoundError:
        return None

ablation_trajectory = []
log_jsonl = Path(wdir) / "log.jsonl"
if log_jsonl.exists():
    for line in log_jsonl.read_text().splitlines():
        try:    ev = json.loads(line)
        except: continue
        if ev.get("event") in ("ablation", "ablation_intermediate"):
            ablation_trajectory.append({
                "step":              ev.get("step"),
                "kind":              ev.get("event"),
                "delta_local":       ev.get("delta_local"),
                "delta_net":         ev.get("delta_net"),
                "delta_both":        ev.get("delta_both"),
                "consolidation_idx": ev.get("consolidation_idx"),
            })

meta = {
    "round":          8,
    "tokens_trained": total_steps * 4 * 128,
    "steps":          total_steps,
    "label":          handle,
    "fim": {
        "resume_from":            "core/round-6/step-5000 (FedAvg merge baseline)",
        "distill_coef":           0.1,
        "lr_bank_mult":           10.0,
        "lr_net_mult":            0.5,
        "lr_dense_mult":          0.5,
        "val_bpc_final":          grep_last(tlog,  r"bpc=(\d+\.\d+)\s+ppl="),
        "ablation_delta_local_final": grep_last(tlog, r"Δ_local:\s*\S+\s*→\s*([+\-\d\.]+)"),
        "ablation_delta_net_final":   grep_last(tlog, r"Δ_net:\s*\S+\s*→\s*([+\-\d\.]+)"),
        "ablation_trajectory":    ablation_trajectory,
        "fim_eval_bpc":           grep_last(felog, r"OVERALL\s+\S+\s+\S+\s+(\d+\.\d+)"),
        "fim_eval_exact_pct":     grep_last(felog, r"OVERALL\s+\S+\s+\S+\s+\S+\s+(\d+\.\d+)"),
        "agent_format_validity":  grep_last(aelog, r"format[=:]?\s*([\d\.]+)"),
        "agent_name_match":       grep_last(aelog, r"name[=:]?\s*([\d\.]+)"),
        "agent_args_match":       grep_last(aelog, r"args[=:]?\s*([\d\.]+)"),
    },
}
Path(f"{wdir}/meta.json").write_text(json.dumps(meta, indent=2))
print(json.dumps(meta, indent=2))
PY

# ── 6. Journal stub ─────────────────────────────────────────────────────────
TS=$(date -u +%Y-%m-%d-%H%M)
JOURNAL="docs/journal/${TS}-round8-${HANDLE}.md"
mkdir -p docs/journal
cat > "$JOURNAL" <<EOF
# Round 8 — Consolidation pipeline restored — ${HANDLE}

## What changed from round-6/7 (and why)
- distill ON (\`MMLLM_DISTILL_COEF=0.1\`) — the Local→Net transfer.
- LR_BANK 10×, LR_NET 0.5×, LR_DENSE 0.5× (5% of bank).
- replay ON (mastery-threshold buffer).
- resumes from \`core/round-6/step-5000\` (the FedAvg merge: fim_eval=5.804, fmt=0.110).

## Setup
- date (UTC): $(date -u)
- handle: ${HANDLE}
- resume from: ${RESUME_FROM:-}
- NetBank: sqrt_n=${MMLLM_NET_SQRT_N}, c_net=${MMLLM_NET_C_NET}

## Results
See: ${WORKER_DIR}/meta.json

## Train log tail
\`\`\`
$(tail -25 "$TRAIN_LOG")
\`\`\`

## FIM eval
\`\`\`
$(cat "$FIM_EVAL_LOG")
\`\`\`

## Agent eval
\`\`\`
$(cat "$AGENT_EVAL_LOG")
\`\`\`

## Narrative
<agent: Report (1) distill_loss trajectory across steps from log.jsonl,
(2) Δ_net trajectory across ablations, (3) whether Δ_net grew over the
run, and (4) fim_eval + format_validity vs the round-6 baseline
(5.804 / 0.110). The single question for this round: did Local→Net
transfer occur?>
EOF
echo "wrote $JOURNAL"

# ── 7. Commit + push ────────────────────────────────────────────────────────
if [ "${MMLLM_SKIP_COMMIT:-false}" = "true" ]; then
  echo "── SKIP-COMMIT ──  artifacts at $WORKER_DIR + $JOURNAL"
else
  BRANCH=$(git branch --show-current)
  git add "$WORKER_DIR" "$JOURNAL"
  git commit -m "round-8 worker: ${HANDLE} (distill restored, LRs corrected)"
  # Push-race retry: parallel workers regularly race on this branch.
  # If push is rejected (non-fast-forward), rebase on origin and retry.
  for attempt in 1 2 3 4 5; do
    if git push -u origin "$BRANCH"; then
      echo "── DONE ──  $HANDLE on $BRANCH (push attempt $attempt)"
      break
    fi
    if [ "$attempt" = "5" ]; then
      echo "── FAILED ──  push rejected after 5 attempts" >&2
      exit 1
    fi
    echo "── push race: rebasing and retrying (attempt $((attempt + 1))/5) ──"
    sleep "$attempt"
    git fetch origin "$BRANCH"
    git pull --rebase origin "$BRANCH" || { echo "rebase failed" >&2; exit 1; }
  done
fi
