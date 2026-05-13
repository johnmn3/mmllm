#!/usr/bin/env bash
# Build the 5-dataset eval battery test slices via mmllm prepare-hf-dataset.
# Each gets a small val + test (50 MB each) and a thin train slice (~100 MB)
# so we don't blow the disk on data we won't train on yet.
#
# Output: /tmp/mmllm-cpu/battery/<key>.{train,val,test}.bin
#
# These pair with evals.py:default_eval_battery which expects
# <root>/<key>.test.bin paths.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

OUT=/tmp/mmllm-cpu/battery
mkdir -p "$OUT"

# Per-dataset caps (bytes). Total ~1 GB across 5 datasets.
# val + test are the eval-relevant slices; train is documentation-only.
MAX=$((200 * 1024 * 1024))   # 200 MB total per dataset
VAL=$((50 * 1024 * 1024))    # 50 MB val
TEST=$((50 * 1024 * 1024))   # 50 MB test

for key in cosmopedia fineweb-edu the-stack-v2-py commitpackft-py xlam; do
  out="${OUT}/${key}"
  if [ -f "${out}.test.bin" ] && [ -s "${out}.test.bin" ]; then
    echo "[skip] ${key} already prepared ($(du -h ${out}.test.bin | awk '{print $1}') test.bin)"
    continue
  fi
  echo "═══ prepare-hf-dataset ${key} → ${out} ═══"
  echo "  start: $(date +%H:%M:%S)"
  mmllm prepare-hf-dataset "$key" "$out" "$MAX" "$VAL" "$TEST" 2>&1 \
    | grep -vE "Downloading|^$" | tail -8
  echo "  done:  $(date +%H:%M:%S)  → $(du -sh ${out}.* 2>/dev/null | awk '{print $1, $2}' | head -3 | tr '\n' ' ')"
done

echo ""
echo "═══ summary ═══"
ls -lh "${OUT}"/*.test.bin 2>/dev/null
echo ""
df -h /tmp | tail -1
