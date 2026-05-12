#!/usr/bin/env bash
# run_bench_isolate.sh — bench at progressive feature subtraction to find
# what's eating inference throughput.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

# Common cpu-tiny config.
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SKIP_NETBANK_WARMSTART=true
# CRITICAL: NetBank sqrt_n defaults to 8192 in the env-var picker
# (8 GB V_net = OOM). Pin to round-6 baseline 1024.
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32

FIM_BASE=/tmp/mmllm-cpu/fim-iso
BANK_BASE=/tmp/mmllm-cpu/fim-bank-iso
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
  # Show effective env.
  env | grep -E "^MMLLM_(NETBANK_ENABLED|LONG_TIER_MIX|GATE_NET_DEFAULT|ALPHA_NET|NET_SQRT_N)" | sort

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

  MMLLM_LITE_CKPT=true mmllm train-fim "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | grep -E "train-fim|WARN|topology" | tail -3
  sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true
  mmllm bench "$FIM_BASE" 2 "$BANK_BASE" 64 256 2>&1 | grep -E "RESULT|device="
}

# Test 1: full current config (Bernoulli gate + Net-default + SwitchGate)
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
run_bench "Test 1: full current (switch + Bernoulli + alpha_net + NetBank)"

# Test 2: disable Bernoulli gate (Net-default off)
export MMLLM_GATE_NET_DEFAULT=false
run_bench "Test 2: switch + alpha_net + NetBank, NO Bernoulli"

# Test 3: drop alpha_net
export MMLLM_ALPHA_NET=false
run_bench "Test 3: switch + NetBank only (no alpha_net, no Bernoulli)"

# Test 4: drop SwitchGate (use sum gate — simplest)
export MMLLM_LONG_TIER_MIX=sum
run_bench "Test 4: sum gate + NetBank (no switch, no alpha_net, no Bernoulli)"

# Test 5: disable NetBank entirely
export MMLLM_NETBANK_ENABLED=false
run_bench "Test 5: NO NetBank (sum gate, no NetBank at all)"
