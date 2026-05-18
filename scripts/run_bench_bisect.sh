#!/usr/bin/env bash
# run_bench_bisect.sh — bench at 3 historical points to find regression.
# Returns to current branch after.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

bench_at() {
  local commit=$1
  local label=$2
  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "  $label  ($commit)"
  echo "═══════════════════════════════════════════════════════════════"
  git -c advice.detachedHead=false checkout "$commit" 2>&1 | tail -2
  git log --format="    %ci %s" -1

  # Force basilisp to recompile by clearing any cached .lpyc.
  find /home/user/mmllm/src -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
  find /home/user/mmllm/src -name "*.lpyc" -delete 2>/dev/null || true

  # Minimal cpu-tiny config (no NetBank, no Bernoulli, smallest path).
  export MMLLM_DEVICE=cpu
  export MMLLM_BANK_ON_GPU=false
  unset MMLLM_NETBANK_ENABLED MMLLM_LONG_TIER_MIX MMLLM_ALPHA_NET MMLLM_GATE_NET_DEFAULT
  unset MMLLM_DENSE_DTYPE MMLLM_SQRT_N MMLLM_NET_SQRT_N MMLLM_NET_C_NET
  unset MMLLM_MEMORY_TOP_K MMLLM_MEMORY_SUB_TOP_K MMLLM_NET_TOP_K MMLLM_NET_SUB_TOP_K

  FIM_BASE=/tmp/mmllm-cpu/fim-bi
  BANK_BASE=/tmp/mmllm-cpu/fim-bank-bi
  rm -rf "${FIM_BASE}"* "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "$(dirname $FIM_BASE)"
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin"
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)" "${FIM_BASE}.val.bin"
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)" "${FIM_BASE}.test.bin"

  # Materialize a small ckpt. With no MMLLM_NETBANK_ENABLED, default is off
  # on most commits. Just run train-cpu (or train-fim if present) briefly.
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp /home/user/mmllm/core/round-6/step-5000/dense.pt "${FIM_BASE}.ckpts/step-1/dense.pt" 2>/dev/null || true
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"

  # Try train-fim with 2 steps (recent commits) — if it fails, try train-cpu.
  if mmllm train-fim "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | tail -3; then
    BENCH_STEP=2
  else
    mmllm train-cpu "$FIM_BASE" "$BANK_BASE" 2 99 1 2>&1 | tail -3
    BENCH_STEP=2
  fi

  sync; echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true
  mmllm bench "$FIM_BASE" "$BENCH_STEP" "$BANK_BASE" 64 256 2>&1 | grep -E "RESULT|device=|loaded ckpt" | head -3
}

# Three points: HEAD, just after first NetBank/3-way/Bernoulli feature
# work landed (a928194 = May 11 20:19), original cpu-tiny commit
# (ab1eadb = May 10 19:55).
bench_at "$CURRENT_BRANCH" "HEAD: current (full features)"
bench_at "a928194"          "May 11 20:19: 'Net-default + Bernoulli' added"
bench_at "ab1eadb"          "May 10 19:55: cpu-tiny config introduced"

# Return to current branch.
echo ""
git checkout "$CURRENT_BRANCH" 2>&1 | tail -2
