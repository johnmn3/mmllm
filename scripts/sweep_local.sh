#!/usr/bin/env bash
# sweep_local.sh — 0→70 (Local phase) sweep on cpu-MINI × N=16 trunks.
# Reports control bpc + Δ_local + Δ_net + Δ_both at step 70.
#
# Usage:  bash scripts/sweep_local.sh <name> [-- KEY=VAL ...]
#
# Example sweeps:
#   bash scripts/sweep_local.sh bank-mult-10 -- MMLLM_LR_BANK_MULT=10
#   bash scripts/sweep_local.sh init-0.05    -- INIT_SCALE=0.05

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

SWEEP_NAME="${1:-default}"; shift || true

WORK_FIM="/tmp/mmllm-cpu/local-sweep-${SWEEP_NAME}.fim"
WORK_BANK="/tmp/mmllm-cpu/local-sweep-${SWEEP_NAME}.bank"
N_TRUNKS="${MMLLM_N_TRUNKS:-16}"

# Recipe defaults (cpu-mini stack-3e-2-5.0 + clamped lr_b). Caller overrides via -- KEY=VAL.
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=64
export MMLLM_NET_C_NET=8                # cpu-mini
export MMLLM_MEMORY_TOP_K="${MMLLM_MEMORY_TOP_K:-16}"
export MMLLM_MEMORY_SUB_TOP_K="${MMLLM_MEMORY_SUB_TOP_K:-16}"
export MMLLM_NET_TOP_K="${MMLLM_NET_TOP_K:-64}"
export MMLLM_NET_SUB_TOP_K="${MMLLM_NET_SUB_TOP_K:-8}"
export MMLLM_N_TRUNKS=$N_TRUNKS
export MMLLM_SPARSE_OPT="${MMLLM_SPARSE_OPT:-adam-cpu}"
export MMLLM_BATCH="${MMLLM_BATCH:-1}"

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
export MMLLM_REPLAY_EVERY="${MMLLM_REPLAY_EVERY:-10}"
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD="${MMLLM_REPLAY_THRESHOLD:-0.5}"
export MMLLM_SKIP_NETBANK_WARMSTART="${MMLLM_SKIP_NETBANK_WARMSTART:-false}"
export MMLLM_NET_V_WARMSTART_FROM_LOCAL="${MMLLM_NET_V_WARMSTART_FROM_LOCAL:-true}"
export MMLLM_ABLATE_EVERY=0
export MMLLM_MAX_STEPS=70

INIT_SCALE="${INIT_SCALE:-0.02}"

if [ "$1" = "--" ]; then shift; fi
while [ $# -gt 0 ]; do
  if [[ "$1" == INIT_SCALE=* ]]; then
    INIT_SCALE="${1#INIT_SCALE=}"
  elif [[ "$1" =~ ^[A-Z_]+=.+ ]]; then
    export "$1"
  fi
  shift
done

echo "═══════════════════════════════════════════════════════════════"
echo "  sweep_local: name=$SWEEP_NAME  (cpu-MINI, N=$N_TRUNKS)"
echo "  knobs:"
for v in MMLLM_LR MMLLM_LR_BANK_MULT MMLLM_LR_DENSE_MULT MMLLM_LR_WARMUP \
         MMLLM_REPLAY_EVERY MMLLM_REPLAY_THRESHOLD MMLLM_MEMORY_TOP_K \
         MMLLM_MEMORY_SUB_TOP_K MMLLM_SPARSE_OPT MMLLM_DISTILL_COEF; do
  printf "    %-32s = %s\n" "$v" "${!v}"
done
echo "    INIT_SCALE                       = $INIT_SCALE"
echo "═══════════════════════════════════════════════════════════════"

mkdir -p "$(dirname $WORK_FIM)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${WORK_FIM}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)"   "${WORK_FIM}.val.bin"   2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)"  "${WORK_FIM}.test.bin"  2>/dev/null || true

rm -rf "${WORK_FIM}.ckpts" "${WORK_FIM}.log.jsonl"
rm -f  "${WORK_BANK}".*.bin "${WORK_BANK}"-net.*.bin
mkdir -p "${WORK_FIM}.ckpts"
# cpu-mini: cold start, no dense seed

python3 - "${WORK_BANK}" "$N_TRUNKS" "$INIT_SCALE" <<'PY'
import numpy as np, sys
bank_base  = sys.argv[1]
n_trunks   = int(sys.argv[2])
INIT_SCALE = float(sys.argv[3])
SQRT_LOCAL = 226;  Q_DIM = 16
SQRT_NET   = 64;   C_NET = 8
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
n_per_trunk = SQRT_LOCAL * SQRT_LOCAL
local_n = n_trunks * n_per_trunk
rng = np.random.default_rng(42)
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+", shape=(local_n, Q_DIM))
    CHUNK = 4096
    for s in range(0, local_n, CHUNK):
        e = min(s + CHUNK, local_n)
        a[s:e] = (rng.standard_normal((e - s, Q_DIM)) * INIT_SCALE).astype(np.float32)
    a.flush()
for i in range(32):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+", shape=(SQRT_NET*SQRT_NET, C_NET))
    a[:] = (rng.standard_normal(a.shape) * INIT_SCALE).astype(np.float32)
    a.flush()
print(f"  banks Gaussian-init (σ={INIT_SCALE}): 8 V_local × {n_trunks} trunks, 32 V_net")
PY

mmllm train-fim-mini "$WORK_FIM" "$WORK_BANK" 101 101 110
