#!/usr/bin/env bash
# run_round9.sh — round-8 evidence applied.
#
# Round-8 produced three firsts: distill_loss flowing, consolidation_idx
# positive, val_bpc tight (0.22–0.24). But individual fim_eval regressed
# to 7.5–7.8 vs round-6's 5.804, format_validity collapsed 0.110 → 0.000.
#
# Worker telemetry converged on the cause: in the 3-way softmax gate,
# `w_local` collapsed from 0.148 → 0.008 across the first cycle. The
# optimizer routed around Local; distill's MSE target shrank with it;
# Net got ~5e-5 effective gradient (three orders of magnitude under
# the main loss). The pipeline worked mechanically but the transfer
# starved on a vanishing input.
#
# Round-9 deltas vs round-8:
#   1. MMLLM_GATE_NET_DEFAULT=true   straight-through Bernoulli gate
#                                    on Local. Net + sdpa always run;
#                                    Local fires per (B, H, T) Bernoulli
#                                    decision (init sigmoid(-2.0) ≈ 12%).
#                                    No `w_local` to collapse — Local is
#                                    invoked explicitly when the gate
#                                    decides this query needs it.
#   2. MMLLM_DISTILL_COEF 0.1 → 1.0  with the Bernoulli gate preventing
#                                    Local from being routed around, the
#                                    distill target is meaningful; the
#                                    coefficient gets a proportional
#                                    share of the backward budget.
#   3. LR_NET cosine 0.5 → 5.0       Net is a slow receiver early (when
#                                    Local is accumulating wake content)
#                                    and a fast consolidator late (when
#                                    distill has something to transfer).
#                                    Round-8 ran flat 0.5×; Net's V
#                                    barely moved across cycles.
#   4. tool-family shards (opt arg)  partition the xlam corpus by
#                                    primary-tool family (5 disjoint
#                                    families: comm / search_info /
#                                    productivity / media / ops). Each
#                                    worker sees genuinely different
#                                    content, not just different doc-ids
#                                    of the same patterns (round-7's
#                                    hash-shard failure mode).
#
# Resumes from core/round-6/step-5000 (FedAvg merge baseline:
# fim_eval=5.804, format_validity=0.110).
#
# Usage:  bash scripts/run_round9.sh <HANDLE> [<FAMILY>]
#
#   FAMILY ∈ {comm, search_info, productivity, media, ops}. Optional;
#   if omitted the worker trains on the full corpus.

set -e

HANDLE="${1:-}"
FAMILY="${2:-}"
if [ -z "$HANDLE" ]; then
  echo "usage: bash scripts/run_round9.sh <HANDLE> [<FAMILY>]" >&2
  echo "       FAMILY ∈ {comm, search_info, productivity, media, ops}" >&2
  exit 1
fi
if [ -n "$FAMILY" ]; then
  case "$FAMILY" in
    comm|search_info|productivity|media|ops) ;;
    *) echo "unknown family: $FAMILY" >&2; exit 1 ;;
  esac
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

# ── Net-default routing (delta 1) ───────────────────────────────────────────
# SwitchGate runs Net + sdpa unconditionally; Local fires per straight-
# through Bernoulli. There is no `w_local` for the optimizer to collapse.
# Initial firing rate sigmoid(-2.0) ≈ 12%; gate learns from gradient.
export MMLLM_GATE_NET_DEFAULT=true

# ── Distillation (residual target + direction-only + cosine schedule) ──────
# Coefficient 0.0 (start) → 1.0 (end), cosine-scheduled across the run.
# Target: (local_out − sdpa_out).detach() — Net learns Local's unique
# contribution beyond sdpa, not Local's full output (round-5/8 twin basin).
# Direction-only: Net matches the *direction* of the residual; magnitude is
# set independently by α_net × gate weight (both bounded).
#
# Why direction-only on top of residual: round-9 re-runs showed two failure
# modes with magnitude-aware residual distill:
#
#   1. Early (steps 250-500, search_info worker): Local≈0 so target ≈
#      −sdpa. Net's V drifts toward anti-sdpa direction → gate sums
#      sdpa+Net partially cancel → ctrl_bpc spike (0.30→1.06).
#   2. Late (steps 3000+, comm/productivity workers): residual magnitude
#      grows unbounded. Net's V grows to match → small perturbations
#      swing net_out massively → dense path destabilizes → ctrl_bpc
#      explodes (0.31→2.71 in 250 steps for comm worker).
#
# Direction-only addresses both: target direction is bounded (unit vector),
# Net's V doesn't need to grow unboundedly to match. Workers 3 (media) and
# 4 (ops) showed the architectural fix works (Δ_net 0.28–0.34 sustained);
# direction-only removes the magnitude pathway that destabilized others.
#
# Combined with the schedule (low coef early), Net stays near init while
# Local accumulates real content, then engages with bounded magnitude.
export MMLLM_DISTILL_COEF=0.0
export MMLLM_DISTILL_COEF_END=1.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true

# ── Replay ──────────────────────────────────────────────────────────────────
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5

# ── LR balance — wake → consolidate temporal sequence ──────────────────────
# Local: cosine 10× → 0.001×. High during wake (Local hill-climbs new
#        content), cools to effectively-frozen by end so it stops
#        accumulating once distill has had time to copy its content into
#        Net. Symmetric with the LR_NET ramp below — Local hands off as
#        Net takes over.
# Net:   cosine 0.001× → 1×. Near-zero start prevents Net's V from
#        drifting while target = (local − sdpa) is poisonous (Local≈0).
#        Plastic late once Local has accumulated content worth absorbing.
# Trunk: cosine 0.05× → 0.005×. Very-low dense LR + further decay so the
#        residual `(local − sdpa)` doesn't shrink (worker 1's "shrinking
#        target" finding — dense absorbs Local's add otherwise).
#
# The prior round-9 redo had LR_BANK_MULT flat at 10× throughout — Local
# never stopped being plastic, so Δ_local and Δ_net converged to parity
# (Local keeps growing in parallel with Net) rather than executing the
# wake→consolidate handoff. This iteration adds Local cooling to drive
# the temporal separation.
export MMLLM_LR_BANK_MULT=10.0
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=1.0
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3

# ── Resume contract (preserve harvested NetBank V) ─────────────────────────
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false

export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-250}"

# ── 0. Preflight ────────────────────────────────────────────────────────────
bash scripts/preflight_fim_run.sh || { echo "preflight failed; aborting" >&2; exit 1; }
source /tmp/mmllm-cpu/preflight.env

if [[ "${RESUME_FROM:-}" != *"round-6"* ]]; then
  echo "round-9 needs core/round-6/step-5000 as resume seed but preflight selected: ${RESUME_FROM:-(none)}" >&2
  exit 1
fi
echo "  ✓ resuming from round-6 community core: ${RESUME_FROM}"

# ── 1. Corpus (full or family-sharded) ──────────────────────────────────────
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

if [ -z "$FAMILY" ]; then
  FIM_BASE=/tmp/mmllm-cpu/fim-json
  CORPUS_JSON_DIR="$JSON_DIR"
else
  CORPUS_JSON_DIR="$SRC/xlam-json-family-${FAMILY}"
  FIM_BASE=/tmp/mmllm-cpu/fim-json-family-${FAMILY}
  if [ ! -d "$CORPUS_JSON_DIR" ] || [ -z "$(ls "$CORPUS_JSON_DIR" 2>/dev/null)" ]; then
    python scripts/shard_by_tool_family.py "$JSON_DIR" "$CORPUS_JSON_DIR" "$FAMILY"
  fi
fi

if [ ! -f "${FIM_BASE}.train.bin" ]; then
  mmllm fim-build-corpus json "$CORPUS_JSON_DIR" "$FIM_BASE" 0.7 0.5 42
fi

# ── 2. Resume seed staging ──────────────────────────────────────────────────
if [ -n "${RESUME_FROM:-}" ] && [ -f "${RESUME_FROM}" ]; then
  rm -rf "${FIM_BASE}.ckpts"
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${RESUME_FROM}" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  echo "  resuming from ${RESUME_FROM} (staged at step-1; ckpts dir wiped first)"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  # Per-family bank base path so workers can run side-by-side without clobbering.
  if [ -z "$FAMILY" ]; then
    BANK_BASE=/tmp/mmllm-cpu/fim-bank
  else
    BANK_BASE=/tmp/mmllm-cpu/fim-bank-family-${FAMILY}
  fi

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

# Restate bank base for the train command (the if-block sets it locally).
if [ -z "$FAMILY" ]; then
  BANK_BASE=/tmp/mmllm-cpu/fim-bank
else
  BANK_BASE=/tmp/mmllm-cpu/fim-bank-family-${FAMILY}
fi

# ── 3. Train ────────────────────────────────────────────────────────────────
TRAIN_LOG=/tmp/mmllm-cpu/round9-${HANDLE}.train.log
TOTAL_STEPS="${MMLLM_TOTAL_STEPS:-5000}"
EVAL_EVERY="${MMLLM_EVAL_EVERY:-250}"
CKPT_EVERY="${MMLLM_CKPT_EVERY:-1000}"
mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

# ── 4. Evals ────────────────────────────────────────────────────────────────
FIM_EVAL_JSONL=/tmp/mmllm-cpu/fim-eval.jsonl
if [ ! -f "$FIM_EVAL_JSONL" ]; then
  python scripts/build_fim_eval.py
fi
FIM_EVAL_LOG=/tmp/mmllm-cpu/round9-${HANDLE}.fim-eval.txt
mmllm fim-eval "${FIM_BASE}.ckpts" "$FIM_EVAL_JSONL" "${TOTAL_STEPS}" 2>&1 | tee "$FIM_EVAL_LOG"

AGENT_EVAL_LOG=/tmp/mmllm-cpu/round9-${HANDLE}.agent-eval.txt
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

python3 - "$HANDLE" "$FAMILY" "$TRAIN_LOG" "$FIM_EVAL_LOG" "$AGENT_EVAL_LOG" "$WORKER_DIR" "$TOTAL_STEPS" <<'PY'
import json, re, sys
from pathlib import Path
handle, family, tlog, felog, aelog, wdir, total_steps = sys.argv[1:8]
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
    "round":          9,
    "tokens_trained": total_steps * 4 * 128,
    "steps":          total_steps,
    "label":          handle,
    "family":         family or "full",
    "fim": {
        "resume_from":            "core/round-6/step-5000 (FedAvg merge baseline)",
        "distill_coef":           1.0,
        "gate_net_default":       True,
        "lr_bank_mult":           10.0,
        "lr_net_mult":            0.5,
        "lr_net_mult_end":        5.0,
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
JOURNAL="docs/journal/${TS}-round9-${HANDLE}.md"
mkdir -p docs/journal
cat > "$JOURNAL" <<EOF
# Round 9 — Net-default Bernoulli + raised distill + LR_NET cosine — ${HANDLE}

## Deltas vs round-8
- MMLLM_GATE_NET_DEFAULT=true       Bernoulli-gated Local
- MMLLM_DISTILL_COEF                0.1 → 1.0
- LR_NET                            0.5 (flat) → 0.5 → 5.0 (cosine)
- corpus                            family=${FAMILY:-full} (tool-family sharded if set)

## Round-8 root cause
3-way softmax \`w_local\` collapsed 0.148 → 0.008 in cycle 1. Distill's
target shrank with it; Net got ~5e-5 effective gradient. Round-9 removes
the routing collapse mode by replacing \`w_local\` with a Bernoulli gate
that runs Local only when explicitly invoked, and raises distill_coef
so the now-meaningful transfer signal lands.

## Resume seed
core/round-6/step-5000 (FedAvg merge: fim_eval=5.804, format_validity=0.110)

## Headline checks
- Δ_net rises across the run (round-8 was flat-to-declining mid-run)
- distill_loss meaningful (>0.005) and grows (round-8 settled at 5e-4)
- consolidation_idx stays positive across all 20 ablations
- val_bpc < 0.32 (round-8 hit 0.22–0.24)
- fim_eval, format_validity vs round-6 baseline (5.804 / 0.110)

## Setup
- date (UTC): $(date -u)
- handle: ${HANDLE}
- family: ${FAMILY:-full}
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
<agent: report (1) Δ_net trajectory across ablations, (2) distill_loss
trajectory, (3) consolidation_idx range, (4) local_firing_rate per
ablation (new Bernoulli telemetry), (5) fim_eval/format_validity
vs round-6 baseline.>
EOF
echo "wrote $JOURNAL"

# ── 7. Commit + push ────────────────────────────────────────────────────────
if [ "${MMLLM_SKIP_COMMIT:-false}" = "true" ]; then
  echo "── SKIP-COMMIT ──  artifacts at $WORKER_DIR + $JOURNAL"
else
  BRANCH=$(git branch --show-current)
  git add "$WORKER_DIR" "$JOURNAL"
  git commit -m "round-9 worker: ${HANDLE} (family=${FAMILY:-full})"
  # Push-race retry: parallel workers regularly race on this branch.
  # If push is rejected (non-fast-forward), rebase on origin and retry.
  # Up to 5 attempts with short backoff before giving up.
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
