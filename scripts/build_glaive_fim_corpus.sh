#!/usr/bin/env bash
# build_glaive_fim_corpus.sh — three-step FIM corpus build for the
# shared-trunk spork.
#
# 1. Pull glaiveai/glaive-function-calling-v2 via prepare-hf-dataset,
#    formatting each record into <|sys|>...<|asst|>...<|end|> chat
#    transcripts. ~200 MB → /tmp/mmllm-cpu/glaive.{train,val,test}.bin.
# 2. Unpack the chat .bin into per-doc .json files (split on <|sys|>),
#    filtered 100 < len < 4096. → /tmp/mmllm-cpu/sources/glaive/*.json.
# 3. fim-build-corpus json with json-value-boundary splitter +
#    fim_ratio=0.7 / psm_ratio=0.5 (matches round-6 config).
#    → /tmp/mmllm-cpu/fim-json-v3.{train,val,test}.bin.
#
# Idempotent on each stage: skips a step whose output already exists at
# nonzero size.
set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

GLAIVE_PREFIX=/tmp/mmllm-cpu/glaive
SOURCES_DIR=/tmp/mmllm-cpu/sources/glaive
FIM_PREFIX=/tmp/mmllm-cpu/fim-json-v3

# ── Step 1: prepare-hf-dataset ───────────────────────────────────────
if [ -s "${GLAIVE_PREFIX}.train.bin" ]; then
  echo "  [1/3] glaive .bin exists — skipping prepare-hf-dataset"
else
  echo "  [1/3] preparing glaive-funcall from HF (~200 MB)…"
  mmllm prepare-hf-dataset glaive-funcall "$GLAIVE_PREFIX" \
    200000000 5000000 5000000
fi

# ── Step 2: unpack chat .bin → per-doc .json ─────────────────────────
if [ -d "$SOURCES_DIR" ] && [ "$(ls -1 "$SOURCES_DIR" | wc -l)" -gt 0 ]; then
  echo "  [2/3] $SOURCES_DIR populated — skipping unpack"
else
  echo "  [2/3] unpacking chat transcripts → per-doc .json…"
  python3 scripts/unpack_chat_bin_to_json.py \
    "${GLAIVE_PREFIX}.train.bin" "$SOURCES_DIR" 100 4096
fi

# ── Step 3: fim-build-corpus json ────────────────────────────────────
if [ -s "${FIM_PREFIX}.train.bin" ]; then
  echo "  [3/3] FIM corpus exists — skipping fim-build-corpus"
else
  echo "  [3/3] building FIM corpus with json-value-boundary splitter…"
  mmllm fim-build-corpus json "$SOURCES_DIR" "$FIM_PREFIX" 0.7 0.5
fi

echo ""
echo "  ready:"
ls -la "${FIM_PREFIX}".*.bin
