#!/usr/bin/env bash
# prep_chain_diverse_corpora.sh — idempotent corpus prep for the
# 9-corpus diverse-mix chain (run_chain_diverse.sh).
#
# Brings up everything the chain-diverse training run will mix from:
#   /tmp/mmllm-cpu/fim-json-v3.{train,val,test}.bin     (Glaive FIM)
#   /tmp/mmllm-cpu/battery/cosmopedia.{train,val,test}.bin
#   /tmp/mmllm-cpu/battery/fineweb-edu.{train,val,test}.bin
#   /tmp/mmllm-cpu/battery/magicoder.{train,val,test}.bin
#   /tmp/mmllm-cpu/battery/hermes-funcall.{train,val,test}.bin
#   /tmp/mmllm-cpu/battery/toolace.{train,val,test}.bin
#   /tmp/mmllm-cpu/battery/tiny-stories.{train,val,test}.bin
#   /tmp/mmllm-cpu/battery/aesop-fables.bin.{train,val,test}.bin
#   /tmp/mmllm-cpu/battery/open-web-math.{train,val,test}.bin
#
# Each step skips when its output already exists at non-zero size, so
# re-running is cheap.
#
# Usage:  bash scripts/prep_chain_diverse_corpora.sh

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

BATTERY=/tmp/mmllm-cpu/battery
mkdir -p "$BATTERY"

echo "═══ [1/6] Glaive FIM corpus ═══"
bash scripts/build_glaive_fim_corpus.sh

echo ""
echo "═══ [2/6] cosmopedia + fineweb-edu (build_eval_battery.sh) ═══"
bash scripts/build_eval_battery.sh

echo ""
echo "═══ [3/6] hermes-funcall + toolace + magicoder (alternates) ═══"
bash scripts/build_eval_battery_alternates.sh

echo ""
echo "═══ [4/6] tiny-stories ═══"
if [ -s "${BATTERY}/tiny-stories.train.bin" ]; then
  echo "[skip] tiny-stories already prepared"
else
  echo "  prepare-hf-dataset tiny-stories → ${BATTERY}/tiny-stories"
  mmllm prepare-hf-dataset tiny-stories "${BATTERY}/tiny-stories" \
    $((20 * 1024 * 1024)) $((2 * 1024 * 1024)) $((2 * 1024 * 1024)) \
    2>&1 | grep -vE "Downloading|^$" | tail -8
fi

echo ""
echo "═══ [5/6] aesop-fables (in-house generator) ═══"
# Filename quirk: --out aesop-fables.bin → aesop-fables.bin.{train,val,test}.bin
# run_chain_diverse.sh's mix string references aesop-fables.bin.train.bin so
# we keep the double-extension naming for compatibility.
if [ -s "${BATTERY}/aesop-fables.bin.train.bin" ]; then
  echo "[skip] aesop-fables already prepared"
else
  echo "  generating aesop-fables corpus (10000 records) …"
  python3 -m mmllm.aesop.generate \
    --out "${BATTERY}/aesop-fables.bin" \
    --n 10000 \
    --val-bytes $((2 * 1024 * 1024)) \
    --test-bytes $((2 * 1024 * 1024)) \
    2>&1 | tail -8
fi

echo ""
echo "═══ [6/6] open-web-math (filling the math gap) ═══"
# OpenWebMath: 14.7B-token corpus of mathematical web text (proofs,
# derivations, math.SE answers, lecture notes). Chat-wrapped by
# fmt_open_web_math at format time. Added for the 9-corpus mix —
# Llama 3 anneal saw +24% GSM8K from a small math upshift.
if [ -s "${BATTERY}/open-web-math.train.bin" ]; then
  echo "[skip] open-web-math already prepared"
else
  echo "  prepare-hf-dataset open-web-math → ${BATTERY}/open-web-math"
  mmllm prepare-hf-dataset open-web-math "${BATTERY}/open-web-math" \
    $((50 * 1024 * 1024)) $((2 * 1024 * 1024)) $((2 * 1024 * 1024)) \
    2>&1 | grep -vE "Downloading|^$" | tail -8
fi

echo ""
echo "═══ summary ═══"
echo "  Glaive:"
ls -lh /tmp/mmllm-cpu/fim-json-v3.train.bin 2>/dev/null | awk '{print "    " $5 "  " $9}'
echo "  Battery train.bin's used by MMLLM_MIX:"
for key in cosmopedia fineweb-edu magicoder hermes-funcall toolace tiny-stories open-web-math; do
  ls -lh "${BATTERY}/${key}.train.bin" 2>/dev/null | awk '{print "    " $5 "  " $9}'
done
ls -lh "${BATTERY}/aesop-fables.bin.train.bin" 2>/dev/null | awk '{print "    " $5 "  " $9}'

echo ""
df -h /tmp | tail -1
