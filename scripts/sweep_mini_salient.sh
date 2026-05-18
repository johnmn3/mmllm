#!/usr/bin/env bash
# sweep_mini_salient.sh — the 6 canonical back-half sweeps remaining
# on cpu-MINI × N=16 (baseline + lr-net-0.5 already done, recorded
# in /tmp/sweep-mini-baseline.log + /tmp/sweep-mini-lr-net-0.5.log).
#
# Sweeps:
#   lr-net-1.0:   MMLLM_LR_NET_MULT_END=1.0    (cpu-tiny pattern said monotonic Δ_net)
#   coef-end-20:  MMLLM_DISTILL_COEF_END=20    (cpu-tiny said saturated — is it here?)
#   coef-end-50:  MMLLM_DISTILL_COEF_END=50
#   mag-coef-on:  magnitude term ON
#   lr-1e-2:      MMLLM_LR=1e-2                (cpu-tiny: huge ctrl bpc gain, no Δ_net)
#   lr-3e-2:      MMLLM_LR=3e-2                (same as default — skip if confirmed)

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

MASTER=/tmp/sweep-mini-master.log

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

run_sweep lr-net-1.0    MMLLM_LR_NET_MULT_END=1.0
run_sweep coef-end-20   MMLLM_DISTILL_COEF_END=20
run_sweep coef-end-50   MMLLM_DISTILL_COEF_END=50
run_sweep mag-coef-on   MMLLM_DISTILL_MAGNITUDE_COEF=1.0 MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
run_sweep lr-1e-2       MMLLM_LR=1e-2 MMLLM_LR_MIN=1e-2
run_sweep lr-3e-2-low-net MMLLM_LR=3e-2 MMLLM_LR_MIN=3e-2 MMLLM_LR_NET_MULT_END=0.1

echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
echo "  sweep_mini_salient complete"                                     | tee -a "$MASTER"
echo "═══════════════════════════════════════════════════════════════" | tee -a "$MASTER"
