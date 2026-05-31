#!/usr/bin/env bash
# sweep_distill.sh — resume from cpu-MINI step-70 distill base and train
# 70→100 with knob overrides. cpu-mini × N=16 trunks.
#
# Usage:  bash scripts/sweep_distill.sh <name> [-- KEY=VAL ...]

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

SWEEP_NAME="${1:-default}"; shift || true

DISTILL_BASE="${MMLLM_DISTILL_BASE:-/tmp/mmllm-cpu/distill-base}"
if [ ! -d "$DISTILL_BASE/ckpts" ]; then
  echo "ERROR: $DISTILL_BASE/ckpts not found. Run scripts/build_distill_base.sh first." >&2
  exit 2
fi

WORK_FIM="/tmp/mmllm-cpu/sweep-${SWEEP_NAME}.fim"
WORK_BANK="/tmp/mmllm-cpu/sweep-${SWEEP_NAME}.bank"
N_TRUNKS="${MMLLM_N_TRUNKS:-16}"

# Recipe defaults — must match build_distill_base for schedule continuity.
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=64
export MMLLM_NET_C_NET=8
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_N_TRUNKS=$N_TRUNKS
export MMLLM_SPARSE_OPT="${MMLLM_SPARSE_OPT:-adam-cpu}"
export MMLLM_BATCH=1

export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_DISTILL_COEF="${MMLLM_DISTILL_COEF:-0.5}"
export MMLLM_DISTILL_COEF_END="${MMLLM_DISTILL_COEF_END:-5.0}"
export MMLLM_DISTILL_TARGET="${MMLLM_DISTILL_TARGET:-residual}"
export MMLLM_DISTILL_DIRECTION_ONLY="${MMLLM_DISTILL_DIRECTION_ONLY:-true}"
export MMLLM_DISTILL_MAGNITUDE_COEF="${MMLLM_DISTILL_MAGNITUDE_COEF:-0.0}"
export MMLLM_DISTILL_MAGNITUDE_COEF_END="${MMLLM_DISTILL_MAGNITUDE_COEF_END:-1.0}"
export MMLLM_DISTILL_MAGNITUDE_CLAMP="${MMLLM_DISTILL_MAGNITUDE_CLAMP:-10.0}"
export MMLLM_LR_BANK_MULT="${MMLLM_LR_BANK_MULT:-3.0}"
export MMLLM_LR_BANK_MULT_END="${MMLLM_LR_BANK_MULT_END:-0.001}"
export MMLLM_LR_NET_MULT="${MMLLM_LR_NET_MULT:-0.001}"
export MMLLM_LR_NET_MULT_END="${MMLLM_LR_NET_MULT_END:-5.0}"
export MMLLM_LR_DENSE_MULT="${MMLLM_LR_DENSE_MULT:-0.05}"
export MMLLM_LR_DENSE_MULT_END="${MMLLM_LR_DENSE_MULT_END:-0.005}"
export MMLLM_LR="${MMLLM_LR:-3e-2}"
export MMLLM_LR_MIN="${MMLLM_LR_MIN:-3e-2}"
export MMLLM_LR_WARMUP="${MMLLM_LR_WARMUP:-70}"
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true     # resume — don't re-warm
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-0}"
unset MMLLM_MAX_STEPS

if [ "$1" = "--" ]; then shift; fi
while [ $# -gt 0 ]; do
  if [[ "$1" =~ ^[A-Z_]+=.+ ]]; then
    export "$1"
  fi
  shift
done

echo "═══════════════════════════════════════════════════════════════"
echo "  sweep_distill: $SWEEP_NAME (cpu-MINI, N=$N_TRUNKS, resume step 70)"
for v in MMLLM_DISTILL_COEF_END MMLLM_DISTILL_TARGET MMLLM_LR_NET_MULT_END MMLLM_LR; do
  printf "    %-32s = %s\n" "$v" "${!v}"
done
echo "═══════════════════════════════════════════════════════════════"

rm -rf "${WORK_FIM}.ckpts" "${WORK_FIM}.log.jsonl"
rm -f  "${WORK_BANK}".*.bin "${WORK_BANK}"-net.*.bin
mkdir -p "$(dirname $WORK_FIM)" "${WORK_FIM}.ckpts"
cp -r "$DISTILL_BASE/ckpts/"* "${WORK_FIM}.ckpts/"
for f in "$DISTILL_BASE/banks/"*.bin; do
  bn=$(basename "$f")
  new="${WORK_BANK}.${bn#*-bank.}"
  if [[ "$bn" == *"-net."* ]]; then
    new="${WORK_BANK}-net.${bn##*-net.}"
  fi
  cp "$f" "$new"
done

ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${WORK_FIM}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)"   "${WORK_FIM}.val.bin"   2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)"  "${WORK_FIM}.test.bin"  2>/dev/null || true

mmllm train-fim-mini "$WORK_FIM" "$WORK_BANK" 101 101 110
