#!/usr/bin/env bash
# run_balanced_spoon.sh — 100-step spike at production banks WITH scaled top_k.
#
# Hypothesis: bank coverage was the gap. cpu-tiny top_k=16 / sub_top_k=16
# over sqrt_n=256 gives 12.5% per-step V-row coverage. Same top_k over
# sqrt_n=720 production gives only 1.6% — V can't accumulate.
#
# Fix: scale top_k and sub_top_k with sqrt_n.
#   Local: sqrt_n 256→720 is √8 = 2.83× linear. top_k 16→128 (8×, area-scaling).
#   Net:   sqrt_n 1024→2000 is √4 = 2.0× linear. top_k 64→256 (4×).
#
# Pass: V_net develops nonzero contribution by step 75–100. Δ_local roughly
# proportional to cpu-tiny's 0.03 over the 1k spike-6 run.

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Bank sizes.
export MMLLM_SQRT_N=720
export MMLLM_NET_SQRT_N=2000
export MMLLM_NET_C_NET=32

# Scaled top_k / sub_top_k — proportional to bank-area increase.
export MMLLM_MEMORY_TOP_K=128
export MMLLM_MEMORY_SUB_TOP_K=45
export MMLLM_NET_TOP_K=256
export MMLLM_NET_SUB_TOP_K=128

# Spike-6 recipe.
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
export MMLLM_ABLATE_EVERY=25
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_LITE_CKPT=true

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin

mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

python3 - "$BANK_BASE" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
SQRT_LOCAL = 720;  Q_DIM = 128
SQRT_NET   = 2000; C_NET = 32
for i in range(4):
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
for i in range(4):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
print("  V_local + V_net zero-initialized")
PY

mmllm train-fim "$FIM_BASE" "$BANK_BASE" 101 25 110 2>&1 | tee /tmp/mmllm-cpu/balanced-spoon.train.log
