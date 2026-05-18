#!/usr/bin/env bash
# sweep_local_battery.sh — explore the Local hill-climbing knobs at
# step 0-70 to maximize Δ_local at the end of the Local phase. The
# back-half distillation can only transfer what Local has actually
# pulled in, so a bigger Δ_local at step 70 is the upper bound on
# downstream Δ_net potential.
#
# Baseline for this battery: chain recipe (stack-3e-2-5.0 + LR_BANK_MULT=3
# clamp). Reference: round 1 of chain-stack3 produced Δ_local=+0.0052
# at step 100 (so probably ~similar at step 70 — Local is barely
# engaged).
#
# Sweeps:
#   baseline-local:   no overrides (current chain recipe)
#   bank-mult-10:     LR_BANK_MULT=10           (effective lr_b=0.3, 3.3× current)
#   bank-mult-30:     LR_BANK_MULT=30           (effective lr_b=0.9, the spike-6 setting)
#   init-0.05:        INIT_SCALE=0.05           (larger Gaussian → more initial signal)
#   init-0.1:         INIT_SCALE=0.1            (much larger)
#   top-k-32:         MEMORY_TOP_K=32           (broader retrieval → more rows touched)
#   replay-off:       REPLAY_EVERY=0            (no replay → simpler dynamics)
#   high-replay:      REPLAY_EVERY=5            (more frequent replay)

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

MASTER=/tmp/sweep-local-master.log
: > "$MASTER"

run_sweep() {
  local name=$1; shift
  local log=/tmp/sweep-local-${name}.log
  echo "═══════════════════════════════════════════════════════════════"   | tee -a "$MASTER"
  echo "  sweep_local[$name]  $(date +%H:%M:%S)  overrides: $*"             | tee -a "$MASTER"
  echo "═══════════════════════════════════════════════════════════════"   | tee -a "$MASTER"
  bash scripts/sweep_local.sh "$name" -- "$@" > "$log" 2>&1
  echo "  ── summary for $name (step-70 ablation) ──"                       | tee -a "$MASTER"
  grep -A 4 "ablation Δ at step cap" "$log" | tee -a "$MASTER"
  echo "" | tee -a "$MASTER"
}

run_sweep baseline-local
run_sweep bank-mult-10  MMLLM_LR_BANK_MULT=10
run_sweep bank-mult-30  MMLLM_LR_BANK_MULT=30
run_sweep init-0.05     INIT_SCALE=0.05
run_sweep init-0.1      INIT_SCALE=0.1
run_sweep top-k-32      MMLLM_MEMORY_TOP_K=32
run_sweep replay-off    MMLLM_REPLAY_EVERY=0
run_sweep high-replay   MMLLM_REPLAY_EVERY=5

echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
echo "  sweep_local_battery complete — see $MASTER"                    | tee -a "$MASTER"
echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
