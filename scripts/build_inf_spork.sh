#!/usr/bin/env bash
# build_inf_spork.sh — stage the trained chain end-state as an
# inference-ready ckpt + bank, then run eval-bpc (quality) and a
# batched decode benchmark (tok/sec).
#
# Inputs: archive dir of a completed chain (must have
#         round-N/{dense.pt, V_net.*.bin, opt-sparse-net.pt}).
# Outputs:
#   /tmp/mmllm-cpu/inf-spork.fim.ckpts/step-1/dense.pt   (loaded by bench)
#   /tmp/mmllm-cpu/inf-spork.bank.<i>.bin                (V_local Gaussian fresh)
#   /tmp/mmllm-cpu/inf-spork.bank-net.<i>.bin            (V_net from chain end)
#   stdout: eval bpc + tok/sec @ B=1 and B=16

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

ARCHIVE="${1:-/tmp/mmllm-cpu/chain-stack-0507}"
LAST_ROUND="${2:-10}"
SRC="$ARCHIVE/round-$LAST_ROUND"

if [ ! -d "$SRC" ]; then
  echo "ERROR: $SRC not found" >&2
  exit 2
fi

BASE=/tmp/mmllm-cpu/inf-spork.fim
BANK=/tmp/mmllm-cpu/inf-spork.bank

echo "═══════════════════════════════════════════════════════════════"
echo "  Building inf-spork from $SRC"
echo "═══════════════════════════════════════════════════════════════"

# Wipe + stage
rm -rf "${BASE}.ckpts" "${BASE}.log.jsonl"
rm -f  "${BANK}".*.bin "${BANK}"-net.*.bin
mkdir -p "${BASE}.ckpts/step-1"
for split in train val test; do
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.${split}.bin)" "${BASE}.${split}.bin" 2>/dev/null || true
done

# Dense from chain end
cp "$SRC/dense.pt" "${BASE}.ckpts/step-1/dense.pt"
echo 1 > "${BASE}.ckpts/step-1/step.txt"

# V_net from chain end — copy all 32 layers
for i in $(seq 0 31); do
  cp "$SRC/V_net.${i}.bin" "${BANK}-net.${i}.bin"
done

# V_local: Gaussian-init fresh (won't be trained at inf time, but
# the architecture requires the tensor to exist)
python3 - "${BANK}" <<'PY'
import numpy as np, sys
bank = sys.argv[1]
SQRT_LOCAL, Q_DIM = 226, 16
N_TRUNKS = 16  # match training-time layout
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
n = N_TRUNKS * SQRT_LOCAL * SQRT_LOCAL
rng = np.random.default_rng(0)
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank}.{i}.bin", dtype=np.float32, mode="w+", shape=(n, Q_DIM))
    CHUNK = 4096
    for s in range(0, n, CHUNK):
        e = min(s + CHUNK, n)
        a[s:e] = (rng.standard_normal((e - s, Q_DIM)) * 0.02).astype(np.float32)
    a.flush()
print(f"  V_local Gaussian-init: 8 layers × 16 trunks (q_dim={Q_DIM})")
PY

# Bank size check
echo "  V_net   layer 0: $(ls -la ${BANK}-net.0.bin | awk '{print $5}') bytes"
echo "  V_local layer 0: $(ls -la ${BANK}.0.bin     | awk '{print $5}') bytes"
echo "  dense.pt:        $(ls -la ${BASE}.ckpts/step-1/dense.pt | awk '{print $5}') bytes"

# Inf evaluation: quality + tps via a Python wrapper that uses the
# cpu-mini config directly (no train-fim-mini, no training loop).
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  Eval (bpc) + TPS bench"
echo "═══════════════════════════════════════════════════════════════"

# C++ PKM kernels are net 0 at training time (cpu-mini scale) but a
# real win at INFERENCE — pkm_full_forward fuses the whole PKM forward
# (score → topk → outer-sum-topk → gather → softmax-weighted-sum) into
# one kernel call, ~4.5× per-PKM-call vs Python, ~1.2× end-to-end after
# Amdahl. Enable for the inf-spork run.
export MMLLM_ENABLE_PKM_CPP=true

# Set the same env as cpu-mini training (so build-model picks the
# right shapes when we call it from Python).
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=64
export MMLLM_NET_C_NET=8
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_N_TRUNKS=16
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true

python3 scripts/inf_spork_eval.py "${BASE}" "${BANK}"
