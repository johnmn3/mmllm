#!/usr/bin/env bash
# run_bench_lru.sh — bench production banks with LRU residence cap.
# Banks total 3 GB on disk (V_local 1 GB + V_net 2 GB).
# MMLLM_BANK_RESIDENT_BYTES caps each PagedMmapStorage at that byte size.
# Pages beyond the cap get MADV_DONTNEED'd → page-fault on next access.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SKIP_NETBANK_WARMSTART=true

# Production bank sizes.
export MMLLM_SQRT_N=720
export MMLLM_NET_SQRT_N=2000
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=128
export MMLLM_MEMORY_SUB_TOP_K=45
export MMLLM_NET_TOP_K=256
export MMLLM_NET_SUB_TOP_K=128

# Full feature set (Bernoulli + switch + alpha_net + NetBank).
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true

FIM_BASE=/tmp/mmllm-cpu/fim-lru
BANK_BASE=/tmp/mmllm-cpu/fim-bank-lru
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000
mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)" "${FIM_BASE}.val.bin"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)" "${FIM_BASE}.test.bin"

run_bench() {
  local label=$1
  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "  $label"
  echo "═══════════════════════════════════════════════════════════════"
  env | grep -E "^MMLLM_BANK_RESIDENT_BYTES" || echo "  MMLLM_BANK_RESIDENT_BYTES=(unset; no cap)"

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
  MMLLM_LITE_CKPT=true mmllm train-fim "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | tail -3
  sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true
  free -h | head -2
  mmllm bench "$FIM_BASE" 2 "$BANK_BASE" 64 256 2>&1 | grep -E "RESULT|device="
  echo "  post-bench RAM:"
  free -h | head -2
}

# A: no LRU cap — full residence (3 GB resident).
unset MMLLM_BANK_RESIDENT_BYTES
run_bench "A: full residence (no LRU cap, all 3 GB in page cache)"

# B: cpu-tiny equivalent residence — 80 MB per storage × 8 storages = 640 MB total.
export MMLLM_BANK_RESIDENT_BYTES=83886080   # 80 MiB per storage
run_bench "B: 80 MiB per storage cap (~640 MB total resident, vs 3 GB on disk)"

# C: tighter — 32 MB per storage = 256 MB total resident (1/12 of bank).
export MMLLM_BANK_RESIDENT_BYTES=33554432   # 32 MiB per storage
run_bench "C: 32 MiB per storage cap (~256 MB total resident)"
