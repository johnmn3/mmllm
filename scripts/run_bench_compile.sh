#!/usr/bin/env bash
# run_bench_compile.sh — test if torch.compile is the missing speedup.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32

FIM_BASE=/tmp/mmllm-cpu/fim-cmp
BANK_BASE=/tmp/mmllm-cpu/fim-bank-cmp
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
  env | grep -E "^MMLLM_(COMPILE|DENSE_DTYPE|NETBANK_ENABLED|LONG_TIER_MIX)" | sort

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"
  if [ "${MMLLM_NETBANK_ENABLED:-true}" = "true" ]; then
    python3 - "${ROUND6_BASE}" "${BANK_BASE}" <<'PY'
import sys, numpy as np
from pathlib import Path
src_dir = Path(sys.argv[1]); bank_base = sys.argv[2]
for fp16_file in sorted(src_dir.glob("bank-net-latest.*.fp16.bin")):
    layer = int(fp16_file.name.split(".")[1])
    arr16 = np.fromfile(fp16_file, dtype=np.float16)
    Path(f"{bank_base}-net.{layer}.bin").write_bytes(arr16.astype(np.float32).tobytes())
PY
  fi
  MMLLM_LITE_CKPT=true mmllm train-fim "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | tail -3
  sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true
  mmllm bench "$FIM_BASE" 2 "$BANK_BASE" 64 256 2>&1 | grep -E "RESULT|device=|compile|enabled|failed"
}

# Lean baseline.
export MMLLM_NETBANK_ENABLED=false
export MMLLM_LONG_TIER_MIX=sum
export MMLLM_ALPHA_NET=false
export MMLLM_GATE_NET_DEFAULT=false
unset MMLLM_DENSE_DTYPE MMLLM_COMPILE

run_bench "A: lean (no NetBank), no compile, fp32 (control)"

# Lean + compile.
export MMLLM_COMPILE=true
run_bench "B: lean + MMLLM_COMPILE=true"

# Lean + compile + bf16.
export MMLLM_DENSE_DTYPE=bf16
run_bench "C: lean + compile + bf16"

# Full config + compile (everything on).
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
unset MMLLM_DENSE_DTYPE
run_bench "D: full features + compile (no bf16)"
