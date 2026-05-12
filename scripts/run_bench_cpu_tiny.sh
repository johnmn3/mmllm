#!/usr/bin/env bash
# run_bench_cpu_tiny.sh — bench inference at original cpu-tiny defaults.
# Compares to the production-banks bench (67 tok/sec) to attribute the
# slowdown.

set -e
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# CPU-TINY defaults (no overrides for sqrt_n / top_k).
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_DEVICE=cpu
# Leave sqrt_n unset → uses cpu-tiny default (256 local, 8192 net)
# Wait — pick-netbank-sqrt-n defaults to 8192. Let's match round-6 baseline (1024).
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32
# top_k unset → cpu-tiny defaults (16 local, 64 net)

FIM_BASE=/tmp/mmllm-cpu/fim-tiny
BANK_BASE=/tmp/mmllm-cpu/fim-bank-tiny
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

# Symlink corpus from v3.
mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)" "${FIM_BASE}.val.bin"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)" "${FIM_BASE}.test.bin"

echo "=== Stage 1: materialize 2-step ckpt at cpu-tiny shapes ==="
rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

# V_net from fp16 seed; V_local zero-init via builder default.
python3 - "${ROUND6_BASE}" "${BANK_BASE}" <<'PY'
import sys, numpy as np
from pathlib import Path
src_dir = Path(sys.argv[1]); bank_base = sys.argv[2]
for fp16_file in sorted(src_dir.glob("bank-net-latest.*.fp16.bin")):
    layer = int(fp16_file.name.split(".")[1])
    arr16 = np.fromfile(fp16_file, dtype=np.float16)
    Path(f"{bank_base}-net.{layer}.bin").write_bytes(arr16.astype(np.float32).tobytes())
PY

MMLLM_LITE_CKPT=true mmllm train-fim "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | tail -5

echo ""
echo "=== Stage 2: drop OS page cache ==="
sync
echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true
free -h | head -3

echo ""
echo "=== Stage 3: bench (B=1, n_warm=64, n_time=256) ==="
mmllm bench "$FIM_BASE" 2 "$BANK_BASE" 64 256 2>&1 | grep -E "device=|loaded|warmup|timed|RESULT|Traceback|Error" | head -20

echo ""
echo "=== Final memory ==="
free -h | head -3
