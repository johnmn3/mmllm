#!/usr/bin/env bash
# sweep_distill.sh — resume from the step-70 distill base and train steps
# 70→100 with knob overrides. Use to iterate quickly on distillation
# settings (DISTILL_*, LR_NET_MULT*, etc.) without re-training the Local
# phase each time.
#
# Usage:
#   bash scripts/sweep_distill.sh <sweep-name> [-- env=val ...]
#
# Sets up env in this order:
#   1. Spike-6 defaults (mirrored from build_distill_base.sh; baseline run)
#   2. The caller's exported MMLLM_* env vars (override defaults)
#   3. Any KEY=VAL positional args after `--` (override exports)
#
# Example sweeps:
#   bash scripts/sweep_distill.sh coef-end-10 -- MMLLM_DISTILL_COEF_END=10
#   bash scripts/sweep_distill.sh lr-net-mult-end-0.5 -- MMLLM_LR_NET_MULT_END=0.5
#   bash scripts/sweep_distill.sh mag-coef-on -- MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
#
# Outputs:
#   /tmp/mmllm-cpu/sweep-<name>.log         — full stdout
#   /tmp/mmllm-cpu/sweep-<name>.fim.*       — work dir for this sweep
#   stdout tail of "ablation summary" with Δ_local / Δ_net / Δ_both
#
# Each sweep is independent — banks + ckpts are copies of the base
# snapshot, so concurrent sweeps don't collide.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

SWEEP_NAME="${1:-default}"; shift || true

DISTILL_BASE="${MMLLM_DISTILL_BASE:-/tmp/mmllm-cpu/distill-base}"
if [ ! -d "$DISTILL_BASE/ckpts" ]; then
  echo "ERROR: $DISTILL_BASE/ckpts not found." >&2
  echo "  Run: bash scripts/build_distill_base.sh   first" >&2
  exit 2
fi

WORK_FIM="/tmp/mmllm-cpu/sweep-${SWEEP_NAME}.fim"
WORK_BANK="/tmp/mmllm-cpu/sweep-${SWEEP_NAME}.bank"

# Recipe defaults (spike-6 + adam-cpu + warm-start, identical to
# build_distill_base.sh — must match so the schedule continuity works).
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=64
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_N_TRUNKS=1
export MMLLM_SPARSE_OPT="${MMLLM_SPARSE_OPT:-adam-cpu}"
export MMLLM_BATCH=4

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
export MMLLM_LR_BANK_MULT="${MMLLM_LR_BANK_MULT:-30.0}"
export MMLLM_LR_BANK_MULT_END="${MMLLM_LR_BANK_MULT_END:-0.001}"
export MMLLM_LR_NET_MULT="${MMLLM_LR_NET_MULT:-0.001}"
export MMLLM_LR_NET_MULT_END="${MMLLM_LR_NET_MULT_END:-0.1}"
export MMLLM_LR_DENSE_MULT="${MMLLM_LR_DENSE_MULT:-0.05}"
export MMLLM_LR_DENSE_MULT_END="${MMLLM_LR_DENSE_MULT_END:-0.005}"
export MMLLM_LR="${MMLLM_LR:-3e-3}"
export MMLLM_LR_MIN="${MMLLM_LR_MIN:-3e-3}"
export MMLLM_LR_WARMUP="${MMLLM_LR_WARMUP:-70}"
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true    # resume — don't re-warm
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-0}"
export MMLLM_LITE_CKPT=true
unset MMLLM_MAX_STEPS                        # train fully through total-steps

# Apply positional overrides KEY=VAL (e.g. -- MMLLM_DISTILL_COEF_END=10).
if [ "$1" = "--" ]; then shift; fi
while [ $# -gt 0 ]; do
  if [[ "$1" =~ ^[A-Z_]+=.+ ]]; then
    export "$1"
  else
    echo "WARN: ignoring unrecognized arg: $1" >&2
  fi
  shift
done

echo "═══════════════════════════════════════════════════════════════"
echo "  sweep_distill: name=$SWEEP_NAME"
echo "  resuming from: $DISTILL_BASE"
echo "  working dir:   $WORK_FIM"
echo "  knobs:"
for v in MMLLM_DISTILL_COEF MMLLM_DISTILL_COEF_END MMLLM_DISTILL_TARGET \
         MMLLM_DISTILL_DIRECTION_ONLY MMLLM_DISTILL_MAGNITUDE_COEF_END \
         MMLLM_LR_NET_MULT MMLLM_LR_NET_MULT_END MMLLM_LR_BANK_MULT_END \
         MMLLM_SPARSE_OPT; do
  printf "    %-36s = %s\n" "$v" "${!v}"
done
echo "═══════════════════════════════════════════════════════════════"

# Clone the base snapshot into this sweep's working dir.
rm -rf "${WORK_FIM}.ckpts" "${WORK_FIM}.log.jsonl"
rm -f  "${WORK_BANK}".*.bin "${WORK_BANK}"-net.*.bin
mkdir -p "$(dirname $WORK_FIM)" "${WORK_FIM}.ckpts"
cp -r "$DISTILL_BASE/ckpts/"* "${WORK_FIM}.ckpts/"
# Banks: rename from base path to sweep path.
for f in "$DISTILL_BASE/banks/"*.bin; do
  bn=$(basename "$f")
  # base files look like 'fim-distill-build-bank.0.bin' →
  # rewrite the prefix to WORK_BANK.
  new="${WORK_BANK}.${bn#*-bank.}"
  # net files are 'fim-distill-build-bank-net.0.bin' →
  # rewrite to WORK_BANK-net.0.bin.
  if [[ "$bn" == *"-net."* ]]; then
    new="${WORK_BANK}-net.${bn##*-net.}"
  fi
  cp "$f" "$new"
done

ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${WORK_FIM}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)"   "${WORK_FIM}.val.bin"   2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)"  "${WORK_FIM}.test.bin"  2>/dev/null || true

# Resume to step 100 (total-steps=101 → train 71→101, end-of-train
# ablation fires on exit). The schedule is calibrated to the same
# 100-step window as the base run, so steps 71→100 see the correct
# end-of-cosine LR values.
mmllm train-fim "$WORK_FIM" "$WORK_BANK" 101 101 110
