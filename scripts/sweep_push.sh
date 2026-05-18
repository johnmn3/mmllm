#!/usr/bin/env bash
# sweep_push.sh — push the winning recipe further.
#
# stack-3e-2-2.0 was the prior winner: ctrl=2.65, Δ_net=+0.0368, synergy=+0.19.
# These two test the ceiling on Δ_net and the value of even more base LR.
#
# Sweeps:
#   stack-3e-2-5.0: LR=3e-2 + LR_NET_MULT_END=5.0   (peak lr_n = 0.15)
#   stack-1e-1-2.0: LR=1e-1 + LR_NET_MULT_END=2.0   (peak lr_n = 0.20, base lr 33× baseline)
#
# Watch for: training instability (NaN loss, exploding bpc), Δ_local
# collapsing to 0 (Net has fully consumed Local — that's consolidation,
# not failure).

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

MASTER=/tmp/sweep-push-master.log
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

run_sweep stack-3e-2-5.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=5.0
run_sweep stack-1e-1-2.0 MMLLM_LR=1e-1 MMLLM_LR_MIN=1e-1 MMLLM_LR_NET_MULT_END=2.0

echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
echo "  sweep_push complete — see $MASTER for all summaries"           | tee -a "$MASTER"
echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
