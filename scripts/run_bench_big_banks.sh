#!/usr/bin/env bash
# run_bench_big_banks.sh — actually measure inference tok/sec on 1+2 GB banks.
#
# 1. Train 2 steps with ckpt-every=1 to materialize a dense.pt at the
#    production bank shapes (K_a/K_b sized to sqrt_n=720 and 2000).
# 2. Drop OS page cache so banks start cold-from-disk.
# 3. Run `mmllm bench` (B=1 inference tok/sec).
# 4. Watch RSS during bench in a sidecar.

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Production bank sizes + scaled top_k.
export MMLLM_SQRT_N=720
export MMLLM_NET_SQRT_N=2000
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=128
export MMLLM_MEMORY_SUB_TOP_K=45
export MMLLM_NET_TOP_K=256
export MMLLM_NET_SUB_TOP_K=128

# Architecture-matching env (so the model build at bench time uses the
# same shape as the materializing train-fim call).
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_LITE_CKPT=false       # NEED full ckpt this time so bench can load opt-* placeholders

# CRITICAL: keep banks on CPU/mmap, NOT GPU. memory.py defaults
# MMLLM_BANK_ON_GPU="true" — we want false for "banks on disk" inference.
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_DEVICE=cpu

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

echo "=== Stage 1: materialize a 2-step ckpt at production shapes ==="
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
PY

# Train 2 steps, save ckpt at step 1.  Use lite-ckpt to keep the save
# small (just dense.pt) — bench only needs dense.pt + V banks.
MMLLM_LITE_CKPT=true mmllm train-fim "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | tail -15
echo ""
ls -la "${FIM_BASE}.ckpts/step-1/" 2>/dev/null

echo ""
echo "=== Stage 2: drop OS page cache (banks now cold-from-disk) ==="
sync
echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || echo "  (drop_caches needs root; continuing — kernel will manage cache normally)"
free -h | head -3

echo ""
echo "=== Stage 3: bench inference (B=1, n_warm=64, n_time=256) ==="
# Watch RSS in background to capture peak memory during bench.
(while sleep 1; do
   ps -ef -o pid,rss,pcpu,comm | awk '/mmllm bench/ && !/awk/ {printf "  RSS=%.0fMB %%CPU=%s\n", $2/1024, $3}'
 done) &
WATCHER=$!
trap "kill $WATCHER 2>/dev/null" EXIT

mmllm bench "$FIM_BASE" 2 "$BANK_BASE" 64 256 2>&1 | tail -40

kill $WATCHER 2>/dev/null
echo ""
echo "=== Final memory ==="
free -h | head -3
