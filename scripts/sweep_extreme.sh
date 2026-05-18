#!/usr/bin/env bash
# sweep_extreme.sh — peak both knobs and push net-mult further at the
# best base LR. Prior winners:
#   stack-3e-2-5.0  ctrl=2.59  Δ_net=+0.052  synergy=+0.18 (best ctrl)
#   stack-1e-1-2.0  ctrl=2.84  Δ_net=+0.189  synergy=+0.68 (best consolidation)
#
# Sweeps:
#   stack-1e-1-5.0:   LR=1e-1 + LR_NET_MULT_END=5.0   (peak lr_n=0.5)
#   stack-3e-2-10.0:  LR=3e-2 + LR_NET_MULT_END=10.0  (peak lr_n=0.3, lower base)
#
# At lr_n=0.5 we may see runaway / NaN. Adam normalizes per-row but the
# step magnitude is now 100× a "normal" Adam step. Watching for blow-up.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

MASTER=/tmp/sweep-extreme-master.log
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

run_sweep stack-1e-1-5.0  MMLLM_LR=1e-1 MMLLM_LR_MIN=1e-1 MMLLM_LR_NET_MULT_END=5.0
run_sweep stack-3e-2-10.0 MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=10.0

echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
echo "  sweep_extreme complete — see $MASTER for all summaries"        | tee -a "$MASTER"
echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
