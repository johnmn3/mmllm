#!/usr/bin/env bash
# sweep_mini_battery.sh — re-run on cpu-MINI × N=16 the same back-half
# knob sweeps that ran on cpu-tiny × N=1 earlier:
#   sweep_all     (8 knobs): baseline + lr-net-* + coef-end-* + mag-coef-on + lr-{1e-2,3e-2}
#   sweep_stack   (4 knobs): lr-net-2.0, lr-net-5.0, stack-3e-2-1.0, stack-3e-2-2.0
#   sweep_push    (2 knobs): stack-3e-2-5.0, stack-1e-1-2.0
#   sweep_extreme (2 knobs): stack-1e-1-5.0, stack-3e-2-10.0
#
# Each sweep resumes the cpu-mini step-70 base ckpt and runs 70→100
# with the named overrides. ~3 min/sweep × 16 sweeps ≈ 48 min total.
#
# Output:
#   /tmp/sweep-mini-<name>.log         — full stdout per sweep
#   /tmp/sweep-mini-master.log         — concatenated summaries

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

MASTER=/tmp/sweep-mini-master.log
: > "$MASTER"

run_sweep() {
  local name=$1; shift
  local log=/tmp/sweep-mini-${name}.log
  echo "═══════════════════════════════════════════════════════════════"   | tee -a "$MASTER"
  echo "  sweep[$name]  $(date +%H:%M:%S)  overrides: $*"                   | tee -a "$MASTER"
  echo "═══════════════════════════════════════════════════════════════"   | tee -a "$MASTER"
  bash scripts/sweep_distill.sh "mini-${name}" -- "$@" > "$log" 2>&1
  echo "  ── summary for $name ──" | tee -a "$MASTER"
  grep -A 4 "════ ablation summary ════" "$log" | tee -a "$MASTER"
  echo "" | tee -a "$MASTER"
}

# Phase 1: sweep_all (8 individual knobs)
run_sweep baseline
run_sweep lr-net-0.5   MMLLM_LR_NET_MULT_END=0.5
run_sweep lr-net-1.0   MMLLM_LR_NET_MULT_END=1.0
run_sweep coef-end-20  MMLLM_DISTILL_COEF_END=20
run_sweep coef-end-50  MMLLM_DISTILL_COEF_END=50
run_sweep mag-coef-on  MMLLM_DISTILL_MAGNITUDE_COEF=1.0 MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
run_sweep lr-1e-2      MMLLM_LR=1e-2 MMLLM_LR_MIN=1e-2
run_sweep lr-3e-2      MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2

# Phase 2: sweep_stack (push net mult higher, combine with base LR)
run_sweep lr-net-2.0     MMLLM_LR_NET_MULT_END=2.0
run_sweep lr-net-5.0     MMLLM_LR_NET_MULT_END=5.0
run_sweep stack-3e-2-1.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=1.0
run_sweep stack-3e-2-2.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=2.0

# Phase 3: sweep_push (best 3e-2 + Δ_net peak)
run_sweep stack-3e-2-5.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=5.0
run_sweep stack-1e-1-2.0 MMLLM_LR=1e-1 MMLLM_LR_MIN=1e-1 MMLLM_LR_NET_MULT_END=2.0

# Phase 4: sweep_extreme (peak both knobs)
run_sweep stack-1e-1-5.0  MMLLM_LR=1e-1 MMLLM_LR_MIN=1e-1 MMLLM_LR_NET_MULT_END=5.0
run_sweep stack-3e-2-10.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=10.0

echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
echo "  sweep_mini_battery complete — see $MASTER for all summaries"   | tee -a "$MASTER"
echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
