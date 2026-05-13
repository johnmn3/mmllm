#!/usr/bin/env bash
# run_chain_diverse.sh — extend the harvested round-20 chain by 10 more
# rounds (21-30) using an 8-corpus diverse training mix instead of
# Glaive-only.
#
# Starting state: /tmp/mmllm-cpu/chain-diverse/round-20/ — the 5-way
# FedAvg harvest of the 4 workers' round-20 states + dense.pt:
#   ctrl_bpc=1.1764 ppl=2.26  (the best model state we have so far)
#
# Training mix (MMLLM_MIX env, weights sum-normalized to 1 by sampler):
#   25  glaive-fim-v3      JSON tool-calls (FIM-format, in-domain)
#   15  cosmopedia         English textbook (chat-wrapped)
#   15  fineweb-edu        English web (chat-wrapped)
#   10  magicoder          Python instruction code (already chat-wrapped)
#   10  hermes-funcall     function-call corpus (chat-wrapped)
#   10  toolace            function-call corpus (chat-wrapped)
#   10  aesop-fables       in-house Clojure + tool-calls (chat-wrapped)
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
#         N_MORE: rounds to add past round-20; default 10 (→ round 30)
#         STEPS:  training steps per round; default 100

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse
N_MORE="${1:-10}"
STEPS="${2:-100}"

if [ ! -d "$ARCHIVE/round-20" ]; then
  echo "ERROR: $ARCHIVE/round-20 not staged. Run stage script first." >&2
  exit 2
fi

# ── 8-corpus mix ──
B=/tmp/mmllm-cpu/battery
G=/tmp/mmllm-cpu/fim-json-v3.train.bin
export MMLLM_MIX="${G}:25,${B}/cosmopedia.train.bin:15,${B}/fineweb-edu.train.bin:15,${B}/magicoder.train.bin:10,${B}/hermes-funcall.train.bin:10,${B}/toolace.train.bin:10,${B}/aesop-fables.bin.train.bin:10,${B}/tiny-stories.train.bin:5"

echo "═══════════════════════════════════════════════════════════════"
echo "  CHAIN-DIVERSE: extending harvested round-20 with 8-corpus mix"
echo "  N_MORE=$N_MORE  STEPS=$STEPS  archive=$ARCHIVE"
echo "═══════════════════════════════════════════════════════════════"
echo "  mix weights:"
echo "$MMLLM_MIX" | tr ',' '\n' | sed 's/^/    /'
echo ""

# Sanity-check every corpus exists
echo "  corpus paths:"
fail=0
echo "$MMLLM_MIX" | tr ',' '\n' | while IFS=: read -r path weight; do
  if [ -f "$path" ]; then
    sz=$(du -h "$path" | awk '{print $1}')
    echo "    OK  ${sz}  w=${weight}  ${path}"
  else
    echo "    MISSING  w=${weight}  ${path}"
    fail=1
  fi
done

# Hand off to extend_chain.sh — it picks up MMLLM_MIX from env automatically
# (pick-mix in core.lpy reads it). extend_chain.sh's recipe defaults
# (stack-3e-2-5.0 + mag-coef-on, MMLLM_ABLATION_EVAL_CAP=25000) carry through.
bash scripts/extend_chain.sh "$ARCHIVE" "$N_MORE" "$STEPS"
