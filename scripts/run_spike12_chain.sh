#!/usr/bin/env bash
# run_spike12_chain.sh — chain round 2 of consolidation.
#
# Resumes from spike6-reproduced-0342 end-state (Δ_net=0.078, matches
# original spike 6's 0.081 within 0.003). Same spike-6 recipe replayed
# from step 1.
#
# The question: does Δ_net at step 1000 of this run END HIGHER than
# the step-1000 Δ_net of spike 6 (0.078)? If yes → consolidation
# compounds across runs.
#
# Pass criteria:
#   step 100  Δ_net ≈ 0.078     (state persisted, no regression)
#   step 1000 Δ_net > 0.078     (compounding works)

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# ── Spike-6 config (same as run_spike6.sh) ──────────────────────────────────
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
SOURCE=/tmp/mmllm-cpu/spike6-reproduced-0342

# Sanity check archive exists.
for f in "$SOURCE/dense.pt" \
         "$SOURCE/V_local.0.bin" "$SOURCE/V_local.1.bin" "$SOURCE/V_local.2.bin" "$SOURCE/V_local.3.bin" \
         "$SOURCE/V_net.0.bin"   "$SOURCE/V_net.1.bin"   "$SOURCE/V_net.2.bin"   "$SOURCE/V_net.3.bin"; do
  if [ ! -f "$f" ]; then echo "MISSING: $f" >&2; exit 1; fi
done
echo "  ✓ archive present: $SOURCE"

# Wipe ckpts/log so schedule replays from step 1.
rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"

# Stage spike-6-end dense at step-1.
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "$SOURCE/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

# CRITICAL DIFFERENCE FROM run_spike6.sh:
# Do NOT zero-init V_local — carry it forward from spike 6's end-state.
# Do NOT restore V_net from round-6 fp16 seed — carry it forward from spike 6.
cp "$SOURCE/V_local.0.bin" "${BANK_BASE}.0.bin"
cp "$SOURCE/V_local.1.bin" "${BANK_BASE}.1.bin"
cp "$SOURCE/V_local.2.bin" "${BANK_BASE}.2.bin"
cp "$SOURCE/V_local.3.bin" "${BANK_BASE}.3.bin"
cp "$SOURCE/V_net.0.bin"   "${BANK_BASE}-net.0.bin"
cp "$SOURCE/V_net.1.bin"   "${BANK_BASE}-net.1.bin"
cp "$SOURCE/V_net.2.bin"   "${BANK_BASE}-net.2.bin"
cp "$SOURCE/V_net.3.bin"   "${BANK_BASE}-net.3.bin"
echo "  ✓ V_local + V_net restored from spike 6 end-state"

mmllm train-fim "$FIM_BASE" "$BANK_BASE" 1001 100 1000 2>&1 | tee /tmp/mmllm-cpu/spike12.train.log
