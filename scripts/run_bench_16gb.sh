#!/usr/bin/env bash
# run_bench_16gb.sh — bench with 16 GB V_net on disk.
# V_net at sqrt_n=5600, c_net=32 → 4.01 GB per layer × 4 layers = 16 GB total.
# Larger than our 15 GB RAM → kernel page cache WILL be under pressure
# and will evict bank pages naturally. This is the actual "banks on disk"
# test: model bigger than RAM, working set paged from disk.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SKIP_NETBANK_WARMSTART=true

# 1 GB V_local (sqrt_n=720, q_dim=128) + 16 GB V_net (sqrt_n=5600, c_net=32).
export MMLLM_SQRT_N=720
export MMLLM_NET_SQRT_N=5600
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=128
export MMLLM_MEMORY_SUB_TOP_K=45
export MMLLM_NET_TOP_K=256
export MMLLM_NET_SUB_TOP_K=128

# Full features.
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true

FIM_BASE=/tmp/mmllm-cpu/fim-16
BANK_BASE=/tmp/mmllm-cpu/fim-bank-16
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000
mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v2.train.bin)" "${FIM_BASE}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v2.val.bin)" "${FIM_BASE}.val.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v2.test.bin)" "${FIM_BASE}.test.bin" 2>/dev/null || true

echo "=== Disk + memory before ==="
df -h / | head -3
free -h | head -2

echo ""
echo "=== Stage 1: materialize 16 GB V_net ckpt ==="
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
SQRT_NET   = 5600; C_NET = 32
for i in range(4):
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
    print(f"  V_local layer {i}: 720² × 128 × 4 = {a.nbytes/1024**2:.0f} MB")
for i in range(4):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
    print(f"  V_net   layer {i}: 5600² × 32 × 4 = {a.nbytes/1024**2:.0f} MB")
PY

echo ""
echo "=== Disk after bank allocation ==="
df -h / | head -3

# Materialize ckpt with right shapes.
# Skip opt-sparse-net init — at sqrt_n=5600 it allocates 32 GB of dense
# state on first step (m + v moments at V.weight's shape) and OOMs us.
# For ckpt materialization we just need dense.pt; V stays on disk.
MMLLM_LITE_CKPT=true MMLLM_SKIP_OPT_NET=true mmllm train-fim "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | tail -5

echo ""
echo "=== Stage 2: drop OS page cache (banks now cold-from-disk) ==="
sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true
free -h | head -2

echo ""
echo "=== Stage 3: bench (B=1, n_warm=64, n_time=256) ==="
echo "  Bank total: 17 GB on disk, RAM: 15 GB — kernel WILL need to evict."
(while sleep 2; do
   ps -ef -o pid,rss,pcpu,comm | awk '/mmllm bench/ && !/awk/ {printf "  bench RSS=%.0fMB %%CPU=%s\n", $2/1024, $3}'
 done) &
WATCHER=$!
trap "kill $WATCHER 2>/dev/null" EXIT
mmllm bench "$FIM_BASE" 2 "$BANK_BASE" 64 256 2>&1 | grep -E "RESULT|device=|loaded ckpt"
kill $WATCHER 2>/dev/null

echo ""
echo "=== Post-bench memory ==="
free -h | head -2
