#!/usr/bin/env bash
# prep_basics_genesis.sh — tier-1/2 clean-provenance "basics" corpora for the
# skill-module genesis. THREE foundational, maximally-distinct atoms (language,
# math, dialogue), each capped at 100 MB so they're small and easy to master.
# CPU-only tokenization (no GPU/memory risk). Add the remaining atoms in later
# stages (see prep_basics_corpora.sh / the staged-cooling plan).
set -euo pipefail

B="${BATTERY:-/tmp/mmllm-cpu/battery}"
mkdir -p "$B"

CAP=100000000     # 100 MB flat byte stream per module
VAL=4000000       # 4 MB held-out val  (the per-corpus mastery metric)
TEST=4000000      # 4 MB held-out test

# genesis 3:  key  ->  skill
MODULES=(
  "gutenberg-prose"          # language / grammar / reading   (tier-1 PD)
  "amps-math"                # basic arithmetic / math        (tier-2 Apache/SW)
  "stackexchange-dialogue"   # basic talking / Q&A            (tier-2 CC-BY-SA)
)

for key in "${MODULES[@]}"; do
  out="$B/${key}.bin"
  if [ -s "${out}.train.bin" ]; then
    echo "[skip] ${key} already prepared"
    continue
  fi
  echo "═══ prep ${key} (cap 100 MB) ═══"
  mmllm prepare-hf-dataset "$key" "$out" "$CAP" "$VAL" "$TEST"
done

echo "═══ genesis-3 corpus sizes ═══"
for key in "${MODULES[@]}"; do
  ls -lh "$B/${key}.train.bin" 2>/dev/null | awk '{print "    " $5 "  " $9}'
done
echo "Next: point a 3-bank module genesis at these (one bank per corpus); see the staged-cooling plan."
