#!/usr/bin/env bash
# run_round10.sh — LR_BANK_MULT sweep on the full xlam corpus.
#
# Round-9 v3 (direction-only residual + LR_NET ramp + LR_BANK cosine cool)
# produced the first fully stable runs: ctrl_bpc held [0.259, 0.290] for
# all 20 ablations across multiple workers, Δ_both 0.15-0.20 sustained,
# per-layer specialization sharp. Both prior failure modes (early
# destructive interference, late magnitude explosion) eliminated.
#
# Open question from those runs: Local's plasticity was set conservatively
# (LR_BANK_MULT=10×). We don't have empirical data on how much higher
# Local's LR can go before falling over. Round-10 sweeps it across 5
# workers and holds everything else constant so any differences in
# Δ_local / Δ_net / Δ_both / ctrl_bpc are attributable to LR_BANK.
#
# Worker assignments (one LR per worker):
#   round10-0 → LR_BANK_MULT=10  (round-9 v3 baseline)
#   round10-1 → LR_BANK_MULT=20
#   round10-2 → LR_BANK_MULT=30
#   round10-3 → LR_BANK_MULT=40
#   round10-4 → LR_BANK_MULT=50
#
# All cool to LR_BANK_MULT_END=0.001 by end-of-run via cosine, so they
# converge to similar effective-frozen Local states. The difference is
# how much Local accumulates during the wake phase.
#
# Corpus: full xlam-json (18,539 docs, all tool families), the same
# distribution round-6 used to produce the FedAvg merge baseline
# (fim_eval=5.804, format_validity=0.110). Robust, well-tested. No
# family-shard divergence to confound the LR signal.
#
# Resumes from core/round-6/step-5000 (same as all prior rounds).
#
# Usage:  bash scripts/run_round10.sh <HANDLE> <LR_BANK_MULT>
#
#   LR_BANK_MULT is a positive number (10, 20, 30, 40, or 50 in the
#   standard sweep; other values welcome for follow-up runs).

set -e

HANDLE="${1:-}"
LR_BANK_MULT="${2:-}"
if [ -z "$HANDLE" ] || [ -z "$LR_BANK_MULT" ]; then
  echo "usage: bash scripts/run_round10.sh <HANDLE> <LR_BANK_MULT>" >&2
  echo "       e.g. bash scripts/run_round10.sh round10-2 30" >&2
  exit 1
fi
# Validate LR_BANK_MULT is a positive number
if ! [[ "$LR_BANK_MULT" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
  echo "LR_BANK_MULT must be a positive number, got: $LR_BANK_MULT" >&2
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

# ── Net-default Bernoulli gate ──────────────────────────────────────────────
export MMLLM_GATE_NET_DEFAULT=true

# ── Distillation (direction-only residual, cosine-scheduled coef) ──────────
export MMLLM_DISTILL_COEF=0.0
export MMLLM_DISTILL_COEF_END=1.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true

# ── Replay ──────────────────────────────────────────────────────────────────
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5

# ── LR balance — THE SWEPT VARIABLE is LR_BANK_MULT (start) ────────────────
# All workers cool Local to 0.001× by end-of-run; only the *start* value
# differs across workers. Cosine schedule spreads the change smoothly so
# higher-LR workers spend more time in the high-plasticity regime.
export MMLLM_LR_BANK_MULT="$LR_BANK_MULT"
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=1.0
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3

# ── Init warmup (NEW — addresses round-10 LR-sweep U-curve) ────────────────
# Round-10 evidence: every high-LR worker (20/30/40/50) had Δ_local go
# NEGATIVE for some window — zeroing Local actively improved bpc. Cause:
# Local's V got hit with full peak LR from step 0 while V was still
# random; updates kicked V into chaotic regimes faster than coherent
# gradient signal could establish. LR=20 stayed negative for 2750 steps;
# LR=30 never fully recovered.
#
# MMLLM_LR_WARMUP=N applies linear ramp 0 → max-lr over N steps to the
# global LR. The per-tier multipliers stay at start values during this
# window (per mult-cosine-interp), so effective Local LR = (warmup-
# ramped global) × MMLLM_LR_BANK_MULT. By the end of warmup, Local has
# accumulated coherent V at gradually-rising LR; the cosine cooldown
# then takes over from peak.
#
# 500 steps = 10% of the 5000-step run. By step 250 (first ablation),
# effective Local LR is 50% of peak — below the chaos threshold the
# round-10 sweep exposed.
export MMLLM_LR_WARMUP=500

# ── Resume contract (preserve harvested NetBank V) ─────────────────────────
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false

export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-250}"

# ── 0. Preflight ────────────────────────────────────────────────────────────
bash scripts/preflight_fim_run.sh || { echo "preflight failed; aborting" >&2; exit 1; }
source /tmp/mmllm-cpu/preflight.env

if [[ "${RESUME_FROM:-}" != *"round-6"* ]]; then
  echo "round-10 needs core/round-6/step-5000 as resume seed but preflight selected: ${RESUME_FROM:-(none)}" >&2
  exit 1
fi
echo "  ✓ resuming from round-6 community core: ${RESUME_FROM}"
echo "  ✓ LR_BANK_MULT swept value: ${LR_BANK_MULT} (cosine → 0.001)"

# ── 1. Corpus (full xlam, no shard) ─────────────────────────────────────────
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
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  BANK_BASE=/tmp/mmllm-cpu/fim-bank
  RESUME_DIR=$(dirname "${RESUME_FROM}")
  python3 - "${RESUME_DIR}" "${BANK_BASE}" <<'PY'
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
    print(f"  NetBank V layer {layer} restored ({out.stat().st_size/1e6:.1f} MB fp32)")
PY
fi

BANK_BASE=/tmp/mmllm-cpu/fim-bank

# ── 3. Train ────────────────────────────────────────────────────────────────
TRAIN_LOG=/tmp/mmllm-cpu/round10-${HANDLE}.train.log
TOTAL_STEPS="${MMLLM_TOTAL_STEPS:-5000}"
EVAL_EVERY="${MMLLM_EVAL_EVERY:-250}"
CKPT_EVERY="${MMLLM_CKPT_EVERY:-1000}"
mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

# ── 4. Evals ────────────────────────────────────────────────────────────────
FIM_EVAL_JSONL=/tmp/mmllm-cpu/fim-eval.jsonl
if [ ! -f "$FIM_EVAL_JSONL" ]; then
  python scripts/build_fim_eval.py
fi
FIM_EVAL_LOG=/tmp/mmllm-cpu/round10-${HANDLE}.fim-eval.txt
mmllm fim-eval "${FIM_BASE}.ckpts" "$FIM_EVAL_JSONL" "${TOTAL_STEPS}" 2>&1 | tee "$FIM_EVAL_LOG"

AGENT_EVAL_LOG=/tmp/mmllm-cpu/round10-${HANDLE}.agent-eval.txt
mmllm eval-agent "$FIM_BASE" "${TOTAL_STEPS}" "$BANK_BASE" \
    "$SRC/xlam-synth.test.bin" xlam 100 256 2>&1 | tee "$AGENT_EVAL_LOG" || true

# ── 5. Stage worker artifacts ───────────────────────────────────────────────
WORKER_DIR="workers/$HANDLE/step-${TOTAL_STEPS}"
mkdir -p "$WORKER_DIR"
cp "${FIM_BASE}.ckpts/step-${TOTAL_STEPS}/dense.pt" "$WORKER_DIR/dense.pt"

python3 - "${BANK_BASE}" "${WORKER_DIR}" <<'PY'
import sys, numpy as np
from pathlib import Path
bank_base = sys.argv[1]
wdir      = Path(sys.argv[2])
for src in sorted(Path("/tmp/mmllm-cpu").glob(f"{Path(bank_base).name}-net.*.bin")):
    parts = src.name.split(".")
    try:    layer = int(parts[1])
    except: continue
    arr32 = np.fromfile(src, dtype=np.float32)
    dst   = wdir / f"bank-net-latest.{layer}.fp16.bin"
    arr32.astype(np.float16).tofile(dst)
    print(f"  staged NetBank V layer {layer}: {dst.stat().st_size/1e6:.1f} MB fp16")
PY

cp "${FIM_BASE}.log.jsonl" "$WORKER_DIR/log.jsonl" 2>/dev/null || true

python3 - "$HANDLE" "$LR_BANK_MULT" "$TRAIN_LOG" "$FIM_EVAL_LOG" "$AGENT_EVAL_LOG" "$WORKER_DIR" "$TOTAL_STEPS" <<'PY'
import json, re, sys
from pathlib import Path
handle, lr_bank, tlog, felog, aelog, wdir, total_steps = sys.argv[1:8]
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
    "round":          10,
    "tokens_trained": total_steps * 4 * 128,
    "steps":          total_steps,
    "label":          handle,
    "corpus":         "full xlam (18539 docs)",
    "fim": {
        "resume_from":            "core/round-6/step-5000 (FedAvg merge baseline)",
        "lr_bank_mult_start":     float(lr_bank),
        "lr_bank_mult_end":       0.001,
        "lr_net_mult":            "0.001 → 1.0 cosine",
        "lr_dense_mult":          "0.05 → 0.005 cosine",
        "distill_coef":           "0.0 → 1.0 cosine",
        "distill_target":         "residual",
        "distill_direction_only": True,
        "gate_net_default":       True,
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
JOURNAL="docs/journal/${TS}-round10-${HANDLE}.md"
mkdir -p docs/journal
cat > "$JOURNAL" <<EOF
# Round 10 — LR_BANK sweep — ${HANDLE} (LR=${LR_BANK_MULT})

## Sweep position
- swept variable: MMLLM_LR_BANK_MULT
- this worker's value: ${LR_BANK_MULT}× base (effective Local LR at step 0: $(python3 -c "print(${LR_BANK_MULT} * 3e-3)"))
- all other workers in this round vary only LR_BANK_MULT (10, 20, 30, 40, 50)
- corpus, resume seed, all other knobs identical across the sweep

## Config (identical across the sweep)
- corpus: full xlam (18539 docs, all 19 tools, no shard)
- resume seed: core/round-6/step-5000 (FedAvg merge)
- distill: target=residual, direction-only, coef cosine 0.0 → 1.0
- LR_NET cosine 0.001 → 1.0, LR_DENSE cosine 0.05 → 0.005
- LR_BANK cosine ${LR_BANK_MULT} → 0.001 (this worker)
- Bernoulli-gated Local, no sleep cycle

## Headline checks
- ctrl_bpc stays in [0.25, 0.32] across all 20 ablations (no spikes)
- Δ_local trajectory: monotonic rise then plateau as LR_BANK cools
- Δ_net trajectory: stable/rising, no late-run explosion
- distill_loss sustained 1e-3 to 1e-1 (direction-only band)
- fim_eval vs round-6 baseline 5.804

## Setup
- date (UTC): $(date -u)
- handle: ${HANDLE}
- LR_BANK_MULT: ${LR_BANK_MULT}
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
<agent: report (1) Δ_local trajectory — did higher LR_BANK produce more
accumulated content?, (2) Δ_net trajectory — did Local's extra content
transfer to Net?, (3) any instability — early spikes or late explosions,
(4) ctrl_bpc range across the run, (5) fim_eval/format_validity vs the
round-6 baseline. Compare to known sweep-mates if their journals have
landed (LR_BANK ∈ {10, 20, 30, 40, 50}). Identify the LR at which the
architecture starts to fall over, if any.>
EOF
echo "wrote $JOURNAL"

# ── 7. Commit + push (with race retry) ──────────────────────────────────────
if [ "${MMLLM_SKIP_COMMIT:-false}" = "true" ]; then
  echo "── SKIP-COMMIT ──  artifacts at $WORKER_DIR + $JOURNAL"
else
  BRANCH=$(git branch --show-current)
  git add "$WORKER_DIR" "$JOURNAL"
  git commit -m "round-10 worker: ${HANDLE} (LR_BANK_MULT=${LR_BANK_MULT})"
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
