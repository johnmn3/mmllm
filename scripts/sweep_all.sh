#!/usr/bin/env bash
# sweep_all.sh — run a fixed battery of distill knob sweeps serially.
# Each sweep resumes the step-70 base ckpt and trains 70→100 with one
# knob overridden. ~3 min per sweep × 7 sweeps ≈ 21 min total.
#
# Output:
#   /tmp/sweep-<name>.log     — full stdout per sweep
#   /tmp/sweep-all-master.log — concatenated headers + ablation summaries
#
# Knob legend (vs baseline):
#   baseline:        spike-6 verbatim (already validated)
#   lr-net-0.5:      MMLLM_LR_NET_MULT_END=0.5  (5× peak Net LR)
#   lr-net-1.0:      MMLLM_LR_NET_MULT_END=1.0  (10× peak Net LR)
#   coef-end-20:     MMLLM_DISTILL_COEF_END=20  (4× peak distill weight)
#   coef-end-50:     MMLLM_DISTILL_COEF_END=50  (10×)
#   mag-coef-on:     MMLLM_DISTILL_MAGNITUDE_COEF=1.0  +  _END=1.0 (constant magnitude term)
#   lr-1e-2:         MMLLM_LR=1e-2 + LR_MIN=1e-2  (3.3× base LR)
#   lr-3e-2:         MMLLM_LR=3e-2 + LR_MIN=3e-2  (10× base LR)

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

MASTER=/tmp/sweep-all-master.log
: > "$MASTER"

run_sweep() {
  local name=$1; shift
  local log=/tmp/sweep-${name}.log
  echo "═══════════════════════════════════════════════════════════════"   | tee -a "$MASTER"
  echo "  sweep[$name]  $(date +%H:%M:%S)  overrides: $*"                   | tee -a "$MASTER"
  echo "═══════════════════════════════════════════════════════════════"   | tee -a "$MASTER"
  bash scripts/sweep_distill.sh "$name" -- "$@" > "$log" 2>&1
  echo "  ── summary for $name ──" | tee -a "$MASTER"
  grep -A 4 "ablation summary" "$log" | tee -a "$MASTER"
  echo "" | tee -a "$MASTER"
}

run_sweep baseline
run_sweep lr-net-0.5   MMLLM_LR_NET_MULT_END=0.5
run_sweep lr-net-1.0   MMLLM_LR_NET_MULT_END=1.0
run_sweep coef-end-20  MMLLM_DISTILL_COEF_END=20
run_sweep coef-end-50  MMLLM_DISTILL_COEF_END=50
run_sweep mag-coef-on  MMLLM_DISTILL_MAGNITUDE_COEF=1.0 MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
run_sweep lr-1e-2      MMLLM_LR=1e-2 MMLLM_LR_MIN=1e-2
run_sweep lr-3e-2      MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2

echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
echo "  sweep_all complete — see $MASTER for all summaries"            | tee -a "$MASTER"
echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
