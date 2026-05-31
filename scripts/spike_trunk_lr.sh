#!/usr/bin/env bash
# spike_trunk_lr.sh — 2-arm probe of MMLLM_LR_LAYER_MULTS off the R70 harvest.
#
# Arm A: baseline (no MMLLM_LR_LAYER_MULTS).
# Arm B: per-layer LR (8 mults, one per Local layer at LOCAL_LAYERS
#        [0,1,2,12,20,29,30,31]).
#
# Both run for 1 round (100 steps) off /tmp/mmllm-cpu/chain-diverse/round-70/.
# After arm A completes we save its round-71/ aside, reset, then run arm B.
# Total wall: ~7-8 min at cpu-mini scale.
#
# Output: prints ctrl_bpc / Δ_local / Δ_net / Δ_both / synergy for each arm.
#
# Usage:  bash scripts/spike_trunk_lr.sh

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse
SPIKE_OUT=/tmp/mmllm-cpu/trunk-lr-spike
mkdir -p "$SPIKE_OUT"

# Mix env (mirrors run_chain_diverse.sh's 9-corpus mix exactly).
B=/tmp/mmllm-cpu/battery
G=/tmp/mmllm-cpu/fim-json-v3.train.bin
export MMLLM_MIX="${G}:25,${B}/cosmopedia.train.bin:10,${B}/fineweb-edu.train.bin:10,${B}/magicoder.train.bin:10,${B}/hermes-funcall.train.bin:10,${B}/toolace.train.bin:10,${B}/aesop-fables.bin.train.bin:10,${B}/open-web-math.train.bin:10,${B}/tiny-stories.train.bin:5"

# Ensure round-70 is staged.
if [ ! -d "$ARCHIVE/round-70" ] || [ "$(ls -1 $ARCHIVE/round-70 | wc -l)" -ne 34 ]; then
  bash scripts/stage_chain_diverse.sh 70
fi

# Remove any stale round-71 from prior runs (the run produces round-71/).
rm -rf "$ARCHIVE/round-71" "$SPIKE_OUT/round-71.baseline" "$SPIKE_OUT/round-71.trunklr"

extract_metrics() {
  local log_jsonl="$1"
  python3 -c "
import json, sys
with open('$log_jsonl') as f:
    for line in f:
        try: ev = json.loads(line)
        except: continue
        if ev.get('event') == 'ablation':
            print(f\"  ctrl_bpc={ev.get('control_bpc')} Δ_local={ev.get('delta_local')} Δ_net={ev.get('delta_net')} Δ_both={ev.get('delta_both')}\")
            break
"
}

echo "═══════════════════════════════════════════════════════════════"
echo "  Arm A: baseline (uniform LR)"
echo "═══════════════════════════════════════════════════════════════"
unset MMLLM_LR_LAYER_MULTS
t0=$(date +%s)
bash scripts/extend_chain.sh "$ARCHIVE" 1 100 > "$SPIKE_OUT/baseline.log" 2>&1 || true
t_a=$(($(date +%s) - t0))
echo "  baseline wall: ${t_a}s"
extract_metrics "$ARCHIVE/round-71/log.jsonl"
mv "$ARCHIVE/round-71" "$SPIKE_OUT/round-71.baseline"
cp "$ARCHIVE/round-71.train.log" "$SPIKE_OUT/baseline.train.log" 2>/dev/null || true

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  Arm B: per-layer LR (mults=2.0,1.5,1.0,0.7,0.5,0.3,0.2,0.1)"
echo "  (one mult per Local layer at [0,1,2,12,20,29,30,31])"
echo "═══════════════════════════════════════════════════════════════"
export MMLLM_LR_LAYER_MULTS="2.0,1.5,1.0,0.7,0.5,0.3,0.2,0.1"
t0=$(date +%s)
bash scripts/extend_chain.sh "$ARCHIVE" 1 100 > "$SPIKE_OUT/layerlr.log" 2>&1 || true
t_b=$(($(date +%s) - t0))
echo "  layerlr wall:  ${t_b}s"
extract_metrics "$ARCHIVE/round-71/log.jsonl"
mv "$ARCHIVE/round-71" "$SPIKE_OUT/round-71.layerlr"
cp "$ARCHIVE/round-71.train.log" "$SPIKE_OUT/layerlr.train.log" 2>/dev/null || true

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  Comparison"
echo "═══════════════════════════════════════════════════════════════"
echo "  baseline (uniform LR):"
extract_metrics "$SPIKE_OUT/round-71.baseline/log.jsonl"
echo "  layerlr  (MMLLM_LR_LAYER_MULTS=2.0,1.5,1.0,0.7,0.5,0.3,0.2,0.1):"
extract_metrics "$SPIKE_OUT/round-71.layerlr/log.jsonl"
echo ""
echo "  artifacts: $SPIKE_OUT/"
