#!/usr/bin/env bash
# run_asym_smoke.sh — quick smoke test of 32-layer asymmetric architecture.
# Just runs train-fim for 25 steps to verify model builds, forward+backward
# work, save-checkpoint completes. No bench, no chain.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226                   # ~100 MB V_local per layer (× 8 layers = 800 MB)
export MMLLM_NET_SQRT_N=8                 # 32 KB V_net per layer
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_DISTILL_COEF=0.5
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_LR_BANK_MULT=30.0
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=0.1
export MMLLM_LR_DENSE_MULT=0.05
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

FIM_BASE=/tmp/mmllm-cpu/fim-asym
BANK_BASE=/tmp/mmllm-cpu/fim-bank-asym
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

# 8 V_local files (only the layers that have Local Bank: 0, 1, 2, 12, 20, 29, 30, 31)
# 32 V_net files (every layer)
python3 - "$BANK_BASE" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
SQRT_LOCAL = 226;  Q_DIM = 128
SQRT_NET   = 8;    C_NET = 32
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
N_LAYERS = 32
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
print(f"  V_local: {len(LOCAL_LAYERS)} files × 226² × 128 × 4 = {len(LOCAL_LAYERS)*SQRT_LOCAL*SQRT_LOCAL*Q_DIM*4/1024**2:.0f} MB total")
for i in range(N_LAYERS):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
print(f"  V_net: {N_LAYERS} files × 8² × 32 × 4 = {N_LAYERS*SQRT_NET*SQRT_NET*C_NET*4} bytes total")
PY

echo ""
echo "=== Train 26 steps (first ablation at step 25 + post-ablation step 26) ==="
mmllm train-fim "$FIM_BASE" "$BANK_BASE" 26 25 30 2>&1 | tee /tmp/mmllm-cpu/asym-smoke.train.log | tail -40
