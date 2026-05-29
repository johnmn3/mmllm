#!/usr/bin/env bash
# run_port_distill.sh — PROOF run for the distillation port (branch
# port-distill-24layer). Resumes the sym24 chain head (round-44) and extends it
# by ONE long round using the round-9 *working* recipe + aggregate-local distill,
# so the distill signal reaches ALL 32 NetBanks (not just the 8 Local-bank
# layers). extend_chain.sh is pure local compute — NO git push / PR.
#
# Usage:  bash scripts/run_port_distill.sh [STEPS]    (default 1500)
# Env:    MMLLM_ABLATE_EVERY (default 250), MMLLM_NUM_THREADS (default 4)
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"
[ -z "${VIRTUAL_ENV:-}" ] && [ -f .venv/bin/activate ] && source .venv/bin/activate

STEPS="${1:-1500}"
STAGE=/tmp/mmllm-cpu
ARCHIVE="$STAGE/port-distill"
HEAD=workers/dispatcher/harvest-2way-r44_sym24/round-44
REF=workers/dispatcher/harvest-0way-r0_sym24/round-0

echo "▶ PORT DISTILL proof: resume r44 → +1 round × $STEPS steps  ($(date -u +%H:%M:%SZ))"

# 1) Stage FIM corpus from in-repo parts (no network).
mkdir -p "$STAGE"
[ -s "$STAGE/fim-json-v3.train.bin" ] || cat workers/dispatcher/corpora/fim-json-v3.train.bin.part-* > "$STAGE/fim-json-v3.train.bin"
cp -n workers/dispatcher/corpora/fim-json-v3.val.bin  "$STAGE/" 2>/dev/null || true
cp -n workers/dispatcher/corpora/fim-json-v3.test.bin "$STAGE/" 2>/dev/null || true

# 2) Reconstruct r44 full V_net (sparse delta → full) into the archive, + dense + opt.
rm -rf "$ARCHIVE"; mkdir -p "$ARCHIVE/round-44"
python3 scripts/_delta_sparse_net.py apply "$REF" "$HEAD" "$ARCHIVE/round-44" 2>&1 | tail -2
cp "$HEAD/dense.pt" "$ARCHIVE/round-44/"
cp "$HEAD"/opt-sparse-net.* "$ARCHIVE/round-44/" 2>/dev/null || true

# 24/24 TOPOLOGY (sym24 genesis intent): Local Bank on layers 0–23. The live
# config default was regressed to 8 ([0 1 2 12 20 29 30 31]); restore the
# genesis 24 so per-layer distill covers all 24 Local↔Net pairs (round-9's 4/4
# mechanism, scaled). extend_chain's SPIKE-2 path honors this env override.
export MMLLM_LOCAL_BANK_LAYERS="0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23"

# Reduced retrieval bandwidth (wave-1 cpu-mini scale) so 24-Local CPU steps are
# tractable on the M5. Bank V shapes are unchanged (top-k is not an arch dim).
export MMLLM_MEMORY_TOP_K=16 MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64    MMLLM_NET_SUB_TOP_K=8
export MMLLM_ENABLE_PKM_CPP=false                # Apple Clang can't build the kernel; skip JIT attempt
export MMLLM_PRINT_EVERY=1                        # stream every step

# 3) round-9 working recipe — per-layer distill (default mode), full magnitude-aware MSE.
export MMLLM_GRAD_CHECKPOINT=false               # gate last_*_out stashes must survive the forward
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=false        # full magnitude-aware MSE (round-9), not dir-only
export MMLLM_DISTILL_MAGNITUDE_COEF=0.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=0.0
export MMLLM_DISTILL_COEF=0.0
export MMLLM_DISTILL_COEF_END=1.0
export MMLLM_LR=3e-3 ; export MMLLM_LR_MIN=3e-3
export MMLLM_LR_BANK_MULT=10.0 ; export MMLLM_LR_BANK_MULT_END=10.0
export MMLLM_LR_NET_MULT=0.001 ; export MMLLM_LR_NET_MULT_END=5.0
export MMLLM_LR_WARMUP=0                          # ramp distill + Net wake from step 0 (round-9)
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-250}"
export MMLLM_NUM_THREADS="${MMLLM_NUM_THREADS:-4}"

# 4) Extend the chain by ONE long round (round-45) of $STEPS steps.
bash scripts/extend_chain.sh "$ARCHIVE" 1 "$STEPS"
echo "✓ port-distill proof done — archive: $ARCHIVE"
