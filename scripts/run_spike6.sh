#!/usr/bin/env bash
# run_spike6.sh — re-run the spike-6 winning recipe from round-6/step-5000.
# 1k steps, ablation every 100. Expected: Δ_net 0.054 → ~0.08.

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32
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
export MMLLM_LR_WARMUP=700

export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5

export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY=100

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin

mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

python3 - "${ROUND6_BASE}" "${BANK_BASE}" <<'PY'
import sys, numpy as np
from pathlib import Path
src_dir = Path(sys.argv[1]); bank_base = sys.argv[2]
# V_net from round-6 fp16 seed (expand to fp32)
for fp16_file in sorted(src_dir.glob("bank-net-latest.*.fp16.bin")):
    layer = int(fp16_file.name.split(".")[1])
    arr16 = np.fromfile(fp16_file, dtype=np.float16)
    Path(f"{bank_base}-net.{layer}.bin").write_bytes(arr16.astype(np.float32).tobytes())
    print(f"  V_net layer {layer} restored from fp16 seed")
# V_local explicitly zero-init (65536 entries × 128 head_dim) — matches the
# original spike staging. Without this, train-fim falls back to random init,
# which gives the Bernoulli gate a "Local is hurting" signal from step 1 and
# locks Local out per-layer.
for i in range(4):
    arr = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+", shape=(65536, 128))
    arr[:] = 0.0
    arr.flush()
    print(f"  V_local layer {i} zero-initialized (65536 × 128)")
PY

mmllm train-fim "$FIM_BASE" "$BANK_BASE" 1001 100 1000 2>&1 | tee /tmp/mmllm-cpu/spike6.train.log
