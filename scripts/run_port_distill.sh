#!/usr/bin/env bash
# run_port_distill.sh — fix the NEW version's distillation IN PLACE, preserving
# its 70/30 wake/sleep design. Resumes the sym24 chain head (round-44) and
# extends one round with the production recipe UNCHANGED except for the genuine
# distillation bug-fixes + the working (round-9) loss form. extend_chain.sh is
# pure local compute — NO git push.
#
# Design preserved (extend_chain defaults — NOT overridden here):
#   warmup = 70% of steps        wake phase = warmup window
#   LB LR mult 3.0 -> 0.001       (wake: LB high; sleep: LB locks in)
#   NB LR mult 0.001 -> 5.0       (wake: NB frozen; sleep: NB absorbs)
#   distill coef 0.5 -> 5.0       (ramps up in the sleep phase)
#   dense LR mult 0.05 -> 0.005   LR=3e-2   8 Local Banks (genesis layout)
#
# Usage:  bash scripts/run_port_distill.sh [STEPS]   (default 600)
# Env:    MMLLM_EVAL_EVERY / MMLLM_ABLATE_EVERY (default 100), MMLLM_NUM_THREADS
set -euo pipefail
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"
[ -z "${VIRTUAL_ENV:-}" ] && [ -f .venv/bin/activate ] && source .venv/bin/activate

STEPS="${1:-600}"
STAGE=/tmp/mmllm-cpu
ARCHIVE="$STAGE/port-distill"
HEAD=workers/dispatcher/harvest-2way-r44_sym24/round-44
REF=workers/dispatcher/harvest-0way-r0_sym24/round-0

echo "▶ PORT DISTILL (new-version design, distill fixed): resume r44 → +1 round × $STEPS steps  ($(date -u +%H:%M:%SZ))"

# 1) Stage FIM corpus from in-repo parts (no network).
mkdir -p "$STAGE"
[ -s "$STAGE/fim-json-v3.train.bin" ] || cat workers/dispatcher/corpora/fim-json-v3.train.bin.part-* > "$STAGE/fim-json-v3.train.bin"
cp -n workers/dispatcher/corpora/fim-json-v3.val.bin  "$STAGE/" 2>/dev/null || true
cp -n workers/dispatcher/corpora/fim-json-v3.test.bin "$STAGE/" 2>/dev/null || true

# 2) Reconstruct r44 full V_net (sparse delta → full) + dense + opt.
rm -rf "$ARCHIVE"; mkdir -p "$ARCHIVE/round-44"
python3 scripts/_delta_sparse_net.py apply "$REF" "$HEAD" "$ARCHIVE/round-44" 2>&1 | tail -2
cp "$HEAD/dense.pt" "$ARCHIVE/round-44/"
cp "$HEAD"/opt-sparse-net.* "$ARCHIVE/round-44/" 2>/dev/null || true

# 3) ── CI-COMPATIBLE distill fix (works under grad-checkpoint=true) ──
# (a) Topology: restore the genesis 24 Local Banks (the live default regressed
#     to 8 -> [0 1 2 12 20 29 30 31]). Per-layer distill then covers 24/32
#     NetBanks (the 8 net-only layers 24-31 stay carriers).
export MMLLM_LOCAL_BANK_LAYERS="0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23"
# (b) grad-checkpoint ON — the 7GB CI runner requires it. Distill now threads
#     per-block through the checkpoint (block_forward -> checkpointed_block_forward
#     return), so it is NO LONGER disabled by checkpointing. Per-layer (default
#     DISTILL_MODE) is per-block => checkpoint-compatible; aggregate-local is
#     cross-block and only works grad-checkpoint OFF.
export MMLLM_GRAD_CHECKPOINT=true
# (c) Working loss form (round-9): full magnitude-aware MSE, NOT the
#     direction-only + magnitude_coef=1.0 that zeroed the direction term.
export MMLLM_DISTILL_DIRECTION_ONLY=false
export MMLLM_DISTILL_MAGNITUDE_COEF=0.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=0.0
# (d) Distill coef: left at the design default (0.5->5.0). Per-layer raw MSE is
#     small (~0.09, divided by the live 3-way-layer count), so unlike the
#     unbounded aggregate (~32) it does NOT need rescaling and is stable.

# Retrieval bandwidth: FULL (design defaults from extend_chain) on GPU; reduced
# on CPU only for tractability (top-k is not a bank dim, so this loads the same
# checkpoint either way). The M5 GPU handles full bandwidth on this small model.
if [ "${MMLLM_DEVICE:-cpu}" = "mps" ] || [ "${MMLLM_DEVICE:-cpu}" = "cuda" ]; then
  export PYTORCH_ENABLE_MPS_FALLBACK=1   # unsupported ops fall back to CPU
  export MMLLM_ENABLE_PKM_CPP=false      # C++ PKM kernel is CPU-only; GPU uses torch ops
  echo "  device=$MMLLM_DEVICE — FULL retrieval bandwidth (design defaults)"
else
  export MMLLM_MEMORY_TOP_K=16 MMLLM_MEMORY_SUB_TOP_K=16
  export MMLLM_NET_TOP_K=64    MMLLM_NET_SUB_TOP_K=8
  export MMLLM_ENABLE_PKM_CPP=false
  echo "  device=cpu — REDUCED bandwidth for tractability"
fi
export MMLLM_PRINT_EVERY=25
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-100}"
export MMLLM_NUM_THREADS="${MMLLM_NUM_THREADS:-8}"

# 4) Extend the chain by ONE round of $STEPS steps with the design recipe.
bash scripts/extend_chain.sh "$ARCHIVE" 1 "$STEPS"
echo "✓ port-distill (design-preserving) done — archive: $ARCHIVE"
