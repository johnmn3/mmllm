#!/usr/bin/env bash
# run_asym_spoon.sh — full 100-step spike-6 spoon on the asymmetric
# 32-layer / 8-Local architecture. ~1-2 hours wall time given the 8×
# trunk depth.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226                   # V_local per layer ~25 MB × 8 layers = 200 MB
export MMLLM_NET_SQRT_N=8                 # V_net per layer ~8 KB × 32 layers = 256 KB
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8

# Spike-6 schedule.
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_DISTILL_COEF=0.5
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_DISTILL_MAGNITUDE_COEF=0.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
export MMLLM_DISTILL_MAGNITUDE_CLAMP=10.0
export MMLLM_LR_BANK_MULT=30.0
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=0.1
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3
export MMLLM_LR_WARMUP=70
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY=25
export MMLLM_LITE_CKPT=true

FIM_BASE=/tmp/mmllm-cpu/fim-asym-spoon
BANK_BASE=/tmp/mmllm-cpu/fim-bank-asym-spoon
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)" "${FIM_BASE}.val.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)" "${FIM_BASE}.test.bin" 2>/dev/null || true

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

python3 - "$BANK_BASE" <<'PY'
import numpy as np
import sys
bank_base = sys.argv[1]
SQRT_LOCAL = 226;  Q_DIM = 128
SQRT_NET   = 8;    C_NET = 32
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
for i in range(32):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
print(f"  banks zero-init'd: 8 V_local, 32 V_net")
PY

mmllm train-fim "$FIM_BASE" "$BANK_BASE" 101 25 110 2>&1 | tee /tmp/mmllm-cpu/asym-spoon.train.log \
  | grep -E "step    [0-9]|ablation Δ|Δ_local|Δ_net|Δ_both|training complete|router-metrics" || true
