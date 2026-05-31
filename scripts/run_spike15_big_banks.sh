#!/usr/bin/env bash
# run_spike15_big_banks.sh — restore production-scale bank sizes.
#
# V_local: sqrt_n=720, q_dim=128 (from cpu-tiny architecture) → 1.0 GB
# V_net:   sqrt_n=2500, c_net=32                              → 3.2 GB
# Trunk:   cpu-tiny dense from round-6/step-5000 (load with topology
#          tolerance — K_a/K_b/expander will fresh-init at new shape)
#
# Single 100-step spoon to verify the bigger banks train cleanly before
# scaling to multi-round chains.

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Bank sizes (the change).
export MMLLM_SQRT_N=720                    # V_local: 720² × 128 × 4 × 4 = 1.0 GB
export MMLLM_NET_SQRT_N=2500               # V_net:  2500² × 32 × 4 × 4 = 3.2 GB
export MMLLM_NET_C_NET=32                  # unchanged (dense compatibility for expander)

# Rest of the spike-6 recipe (unchanged).
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

export MMLLM_LR_BANK_MULT=10.0
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

# Skip warmstart from round-6 (V_net seed shape no longer compatible).
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY=25

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin

# Trunk weights from round-6 (cpu-tiny dense — incompatible bank params will
# be silently skipped on load and fresh-init at the new shapes).
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

# Zero-init both banks at the new bigger shapes.
python3 - "${BANK_BASE}" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
# V_local: 720² entries × 128 q_dim × fp32 = 253 MB per layer
sqrt_local = 720
q_dim = 128
for i in range(4):
    arr = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                    shape=(sqrt_local * sqrt_local, q_dim))
    arr[:] = 0.0
    arr.flush()
    sz = arr.nbytes / 1024**2
    print(f"  V_local layer {i}: {sqrt_local}² × {q_dim} = {sz:.0f} MB")
# V_net: 2500² entries × 32 c_net × fp32 = 800 MB per layer
sqrt_net = 2500
c_net = 32
for i in range(4):
    arr = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                    shape=(sqrt_net * sqrt_net, c_net))
    arr[:] = 0.0
    arr.flush()
    sz = arr.nbytes / 1024**2
    print(f"  V_net   layer {i}: {sqrt_net}² × {c_net} = {sz:.0f} MB")
PY

du -sh "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin 2>/dev/null | tail -8
echo "  total banks on disk:"
du -shc "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin 2>/dev/null | tail -1

mmllm train-fim "$FIM_BASE" "$BANK_BASE" 101 25 100 2>&1 | tee /tmp/mmllm-cpu/spike15.train.log
