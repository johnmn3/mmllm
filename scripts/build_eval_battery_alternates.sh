#!/usr/bin/env bash
# Fetch non-gated alternatives for the blocked battery datasets.
#
# Substitutions:
#   xlam            → hermes-funcall (NousResearch/hermes-function-calling-v1)
#                     + toolace      (Team-ACE/ToolACE)
#   the-stack-v2-py → magicoder      (ise-uiuc/Magicoder-Evol-Instruct-110K)
#   commitpackft-py → no clean substitute; skipping
#
# All are wired in datasets.py and are public (no HF auth required).

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

OUT=/tmp/mmllm-cpu/battery
mkdir -p "$OUT"

MAX=$((20 * 1024 * 1024))     # 20 MB cap (these are SFT-scale, smaller than pretrain corpora)
VAL=$((2 * 1024 * 1024))      # 2 MB val
TEST=$((2 * 1024 * 1024))     # 2 MB test

for key in hermes-funcall toolace magicoder; do
  out="${OUT}/${key}"
  if [ -f "${out}.test.bin" ] && [ -s "${out}.test.bin" ]; then
    echo "[skip] ${key} already prepared"
    continue
  fi
  echo "═══ prepare-hf-dataset ${key} → ${out} ═══"
  echo "  start: $(date +%H:%M:%S)"
  mmllm prepare-hf-dataset "$key" "$out" "$MAX" "$VAL" "$TEST" 2>&1 \
    | grep -vE "Downloading|^$" | tail -8
  if [ -f "${out}.test.bin" ]; then
    echo "  done:  $(date +%H:%M:%S)  → test=$(du -h ${out}.test.bin | awk '{print $1}')"
  else
    echo "  FAILED at $(date +%H:%M:%S)"
  fi
done

echo ""
echo "═══ summary ═══"
ls -lh "${OUT}"/*.test.bin 2>/dev/null
df -h /tmp | tail -1
