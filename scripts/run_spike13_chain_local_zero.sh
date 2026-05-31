#!/usr/bin/env bash
# run_spike13_chain_local_zero.sh — chain round 3 with V_local zero-init.
#
# The hypothesis: Net consolidates Local's residual across rounds, but
# only if Local has fresh hill-climbs to feed it. Same-corpus chain
# (spike 12) saturated Local quickly, so Net got no new residual to
# absorb. Zeroing V_local each round forces Local to re-explore from
# scratch, generating a fresh distill signal for Net to absorb.
#
# Setup:
#   - V_net carried forward from spike12-chain2-end-state-0357 (= 0.0785)
#   - V_local ZERO-INIT (fresh hill climb)
#   - dense.pt staged at step-1 from spike 12 end-state
#   - Same spike-6 schedule
#
# Pass: step 1000 Δ_net > 0.0785 (Net compounded via Local re-exploration).

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
SOURCE=/tmp/mmllm-cpu/spike12-chain2-end-state-0357

for f in "$SOURCE/dense.pt" \
         "$SOURCE/V_net.0.bin" "$SOURCE/V_net.1.bin" "$SOURCE/V_net.2.bin" "$SOURCE/V_net.3.bin"; do
  if [ ! -f "$f" ]; then echo "MISSING: $f" >&2; exit 1; fi
done
echo "  ✓ archive present: $SOURCE"

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin

mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "$SOURCE/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

# V_net carried forward from spike 12 (the consolidating bank).
cp "$SOURCE/V_net.0.bin" "${BANK_BASE}-net.0.bin"
cp "$SOURCE/V_net.1.bin" "${BANK_BASE}-net.1.bin"
cp "$SOURCE/V_net.2.bin" "${BANK_BASE}-net.2.bin"
cp "$SOURCE/V_net.3.bin" "${BANK_BASE}-net.3.bin"
echo "  ✓ V_net restored from spike 12 (Δ_net=0.0785 start)"

# V_local explicitly zero-init — the hill climber gets a clean slate.
python3 - "${BANK_BASE}" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
for i in range(4):
    arr = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+", shape=(65536, 128))
    arr[:] = 0.0
    arr.flush()
    print(f"  V_local layer {i} zero-initialized")
PY

mmllm train-fim "$FIM_BASE" "$BANK_BASE" 1001 100 1000 2>&1 | tee /tmp/mmllm-cpu/spike13.train.log
