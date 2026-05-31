#!/usr/bin/env bash
# sweep_stack.sh — follow-on battery from the first 8-sweep result. The
# original sweep showed LR_NET_MULT_END is the only knob that moves
# Δ_net (monotonic to ~5.9× baseline at MULT_END=1.0), and base LR=3e-2
# alone drops ctrl bpc 3.78→2.74 without moving Δ_net (held back by
# LR_NET_MULT_END=0.1). This battery:
#   (a) pushes LR_NET_MULT_END past 1.0 to find the Δ_net ceiling
#   (b) stacks LR=3e-2 with high LR_NET_MULT_END to combine both gains
#
# Sweeps:
#   lr-net-2.0:        LR_NET_MULT_END=2.0   (alone)
#   lr-net-5.0:        LR_NET_MULT_END=5.0   (alone — may be unstable)
#   stack-3e-2-1.0:    LR=3e-2 + LR_NET_MULT_END=1.0  (peak lr_n = 3e-2)
#   stack-3e-2-2.0:    LR=3e-2 + LR_NET_MULT_END=2.0  (peak lr_n = 6e-2)

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

MASTER=/tmp/sweep-stack-master.log
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

run_sweep lr-net-2.0     MMLLM_LR_NET_MULT_END=2.0
run_sweep lr-net-5.0     MMLLM_LR_NET_MULT_END=5.0
run_sweep stack-3e-2-1.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=1.0
run_sweep stack-3e-2-2.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=2.0

echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
echo "  sweep_stack complete — see $MASTER for all summaries"          | tee -a "$MASTER"
echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
