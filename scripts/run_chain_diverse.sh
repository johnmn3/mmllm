#!/usr/bin/env bash
# run_chain_diverse.sh — extend a staged chain by N more rounds using
# an 8-corpus diverse training mix instead of Glaive-only.
#
# Starting state: the highest existing round-N/ under $ARCHIVE. The
# dispatcher stages a FedAvg-harvested checkpoint there before launching.
# Known starting points:
#   round-20 (4-way FedAvg of dispatcher's spork-chain-10 extension):
#     ctrl_bpc=1.1764 ppl=2.26
#   round-30 (5-way FedAvg of chain-diverse-30 extension; Glaive-val
#     bpc=1.4375; OOD mean -22% vs round-20 harvest):
#     workers/dispatcher/harvest-5way-r30/round-30/
#
# Training mix (MMLLM_MIX env, weights sum-normalized to 1 by sampler):
#   25  glaive-fim-v3      JSON tool-calls (FIM-format, in-domain)
#   10  cosmopedia         English textbook (chat-wrapped)
#   10  fineweb-edu        English web (chat-wrapped)
#   10  magicoder          Python instruction code (already chat-wrapped)
#   10  hermes-funcall     function-call corpus (chat-wrapped)
#   10  toolace            function-call corpus (chat-wrapped)
#   10  aesop-fables       in-house Clojure + tool-calls (chat-wrapped)
#   10  open-web-math      math reasoning (proofs, math.SE, lecture notes; chat-wrapped)
#    5  tiny-stories       simple English grammar (chat-wrapped)
#
# fim_loss_mask handles mixed corpora correctly: FIM-marked records
# (Glaive) get middle-only masking; non-FIM records get all-1 mask =
# full causal LM training (per fim/loss_mask.py docstring).
#
# Recipe: stack-3e-2-5.0 + mag-coef-on (the proven winner from the
# sweep battery — see CLAUDE.md "Winning bank-engagement recipes").
#
# Usage:  bash scripts/run_chain_diverse.sh [N_MORE] [STEPS]
#         N_MORE: rounds to add past the highest staged round; default 10
#         STEPS:  training steps per round; default 100

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse
N_MORE="${1:-10}"
STEPS="${2:-100}"

# Find the highest existing round (extend_chain.sh does the same).
HIGHEST=$(ls -d "$ARCHIVE"/round-* 2>/dev/null | grep -oE 'round-[0-9]+' | grep -oE '[0-9]+' | sort -n | tail -1)
if [ -z "$HIGHEST" ]; then
  echo "ERROR: no round-N dirs in $ARCHIVE. Stage a starting round first." >&2
  exit 2
fi
echo "Starting from $ARCHIVE/round-${HIGHEST}"

# ── Default 9-corpus FIM mix (callers can override MMLLM_MIX) ──
B=/tmp/mmllm-cpu/battery
G=/tmp/mmllm-cpu/fim-json-v3.train.bin
: "${MMLLM_MIX:=${G}:25,${B}/cosmopedia.train.bin:10,${B}/fineweb-edu.train.bin:10,${B}/magicoder.train.bin:10,${B}/hermes-funcall.train.bin:10,${B}/toolace.train.bin:10,${B}/aesop-fables.bin.train.bin:10,${B}/open-web-math.train.bin:10,${B}/tiny-stories.train.bin:5}"
export MMLLM_MIX

# ── Asymmetric V per-layer V_local LR multipliers ──
# Mults 7,3,1,0.5,0.3,0.7,2,5 — asymmetric V (steep on the front, shallow
# on the back), trough at layer 4 (0.3×), peaks at layer 0 (7×) and layer
# 7 (5×). Mean 2.4375, span 0.3×–7×.
#
# Background: the symmetric V (7,5,3,2,1,3,5,7) was the R71-R80 default
# and produced the chain's first regression (+1.1% OOD R70→R80). At
# 1-round single-spork comparison this asymmetric variant is within the
# ±0.025 noise floor of every other tested config, but it produces a
# CLEAR per-layer movement footprint (mean|V_local| ranges 0.0160-0.0228)
# that the movement-gate (below) can discriminate cleanly.
#
# Router LR is LOW by design (routers = low-level primitives).
# Don't override MMLLM_LR_LOCAL_MULT — optim.py defaults it to 0.05
# (which puts effective V_local LR at bank_lr × 0.05 ≈ 4.5e-3 at peak,
# 20× below bank, comparable to dense). The R71-R90 waves had this
# silently jacked back up to 1.0 by this very script — a bug. Fixed:
# we now let the optim.py default stand.
: "${MMLLM_LR_LAYER_MULTS:=7.0,3.0,1.0,0.5,0.3,0.7,2.0,5.0}"
export MMLLM_LR_LAYER_MULTS

# ── Movement-signal distill gate ──
# Per-layer mean(|V_local|) vs Gaussian-init baseline 0.016. Used as a
# clean discriminator (probe wall ~0.1s vs 100s+ for ablation). At
# 1-round scale the gate produces +0.011 Δ_net advantage over no-gate
# at ±0 ctrl_bpc cost (within noise) — direction is consistent across
# runs even though the per-round magnitude is at the noise floor.
# Effect at 10-round chain scale is the actual test.
: "${MMLLM_DISTILL_GATE_BY_ABLATION:=true}"
: "${MMLLM_DISTILL_GATE_SIGNAL:=movement}"
export MMLLM_DISTILL_GATE_BY_ABLATION MMLLM_DISTILL_GATE_SIGNAL

echo "═══════════════════════════════════════════════════════════════"
echo "  CHAIN-DIVERSE: extending highest staged round with 9-corpus mix"
echo "  N_MORE=$N_MORE  STEPS=$STEPS  archive=$ARCHIVE"
echo "═══════════════════════════════════════════════════════════════"
echo "  mix weights:"
echo "$MMLLM_MIX" | tr ',' '\n' | sed 's/^/    /'
echo ""

# Sanity-check every corpus exists. Use process substitution so `fail`
# remains in the parent shell (vs `echo | while` which puts the loop in
# a subshell and loses the assignment — that was the bug that let
# rounds 41-50 launch with open-web-math missing and crash in 5-75s).
echo "  corpus paths:"
fail=0
while IFS=: read -r path weight; do
  if [ -f "$path" ]; then
    sz=$(du -h "$path" | awk '{print $1}')
    echo "    OK  ${sz}  w=${weight}  ${path}"
  else
    echo "    MISSING  w=${weight}  ${path}"
    fail=1
  fi
done < <(echo "$MMLLM_MIX" | tr ',' '\n')
if [ "$fail" = "1" ]; then
  echo ""
  echo "ERROR: one or more MMLLM_MIX corpora missing." >&2
  echo "  Run: bash scripts/prep_chain_diverse_corpora.sh" >&2
  exit 3
fi

# Hand off to extend_chain.sh — it picks up MMLLM_MIX from env automatically
# (pick-mix in core.lpy reads it). extend_chain.sh's recipe defaults
# (stack-3e-2-5.0 + mag-coef-on, MMLLM_ABLATION_EVAL_CAP=25000) carry through.
bash scripts/extend_chain.sh "$ARCHIVE" "$N_MORE" "$STEPS"
