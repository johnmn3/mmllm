#!/usr/bin/env bash
# run_spike8_chain2.sh — round 2 of the consolidation chain.
#
# Setup: full 1k-step spike-6-config run, resuming from spike 7's
# end-state (which equals spike 6's end-state at Δ_net=0.080, persistence
# already verified by spike 7).
#
# Key choices:
#   - Dense + opt state from spike 7 step-1101 staged at step-1, schedule
#     replays 0% → 100% (LR_BANK warmup 10→0.001, LR_NET 0.001→0.1, distill
#     0.5→5.0, mag_coef 0→1.0, warmup=700)
#   - V_local and V_net stay in-place at /tmp/mmllm-cpu/fim-bank-v3*.bin
#     (already reflect spike 7 end-state). MMLLM_SKIP_NETBANK_WARMSTART=true
#     tells core.lpy to use them as-is rather than warm-start from local.
#   - Same corpus as spike 6/7 (fim-json-v3 = xlam-based).
#
# Pass/fail for the consolidation-chain question:
#   - step-100 ablation Δ_net ≈ 0.08 (state persisted as before, confirms
#     spike 7 didn't disturb anything)
#   - step-1000 ablation Δ_net > 0.08 (chain still climbing — Local
#     contributing new signal to Net)
#   - step-1000 ablation Δ_net ≈ 0.08 (saturated already on round 2 —
#     unlikely but possible for narrow corpus)
#   - step-1000 ablation Δ_net < 0.08 (regression — distill or LR is
#     destructive at this saturation level, schedule needs adjustment)

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

HANDLE="spike8-chain2"

# ── Spike-6 config (the winning recipe) ────────────────────────────────────
export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true

export MMLLM_DISTILL_COEF=0.5
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_DISTILL_MAGNITUDE_COEF=0.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
export MMLLM_DISTILL_MAGNITUDE_CLAMP=10.0

export MMLLM_LR_BANK_MULT=10.0
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=0.1
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3
export MMLLM_LR_WARMUP=700

export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false

export MMLLM_ABLATE_EVERY=100

# Use spike 6/7's base path so V banks carry over in-place.
FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3

# ── Re-stage from spike 7's step-1101 dense.pt as step-1 ───────────────────
# This gives a fresh schedule replay (start_step=1 / total_steps=1000) so
# all the dynamics that drove the spike-6 climb get a second swing.
SOURCE_DENSE=/tmp/mmllm-cpu/spike7-end-state-archive/dense.pt
if [ ! -f "$SOURCE_DENSE" ]; then
  echo "missing $SOURCE_DENSE — re-archive spike 7's end-state first" >&2; exit 1
fi

# Sanity check V banks are in place.
for f in "${BANK_BASE}.0.bin" "${BANK_BASE}.1.bin" "${BANK_BASE}.2.bin" "${BANK_BASE}.3.bin" \
         "${BANK_BASE}-net.0.bin" "${BANK_BASE}-net.1.bin" "${BANK_BASE}-net.2.bin" "${BANK_BASE}-net.3.bin"; do
  if [ ! -f "$f" ]; then
    echo "missing V bank: $f" >&2; exit 1
  fi
done

# Wipe ckpts dir and stage at step-1 for a clean schedule replay.
rm -rf "${FIM_BASE}.ckpts"
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "$SOURCE_DENSE" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
# Empty opt-sparse-net so the resume code path doesn't try to load it
# from a non-NetBank ckpt (round-10 pattern).
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

echo "── spike 8 (chain round 2) ──"
echo "  resume dense:    ${SOURCE_DENSE} (spike 7 step-1101, ≈ spike 6 end-state)"
echo "  V_local:         ${BANK_BASE}.{0..3}.bin (in-place)"
echo "  V_net:           ${BANK_BASE}-net.{0..3}.bin (in-place)"
echo "  config:          spike-6 schedule, full replay 0% → 100%"
echo "  ablations:       every 100 steps"

TRAIN_LOG=/tmp/mmllm-cpu/${HANDLE}.train.log
TOTAL_STEPS=1001
EVAL_EVERY=100
CKPT_EVERY=1000

mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

echo ""
echo "── chain-round-2 ablation trajectory ──"
python3 - "${FIM_BASE}.log.jsonl" <<'PY'
import json, sys
from pathlib import Path
log = Path(sys.argv[1])
rows = []
# Pick up only this run's events: between the latest "session" boundary
# and end of file. We approximate by taking events with step in [50, 1001]
# emitted in the tail of the log file.
all_events = []
for line in log.read_text().splitlines():
    try:    ev = json.loads(line)
    except: continue
    if ev.get("event") in ("ablation","ablation_intermediate"):
        all_events.append(ev)
# Take events from the last contiguous chain (step monotonically increasing).
chain = []
for ev in reversed(all_events):
    if chain and ev.get("step",0) >= chain[-1].get("step",0):
        break
    chain.append(ev)
chain.reverse()
print(f"{'step':>6}  {'Δ_local':>9}  {'Δ_net':>9}  {'Δ_both':>9}  syn")
for ev in chain:
    s  = ev.get("step")
    dl = ev.get("delta_local"); dn = ev.get("delta_net"); db = ev.get("delta_both")
    syn = "n/a"
    if isinstance(dl,(int,float)) and isinstance(dn,(int,float)) and isinstance(db,(int,float)):
        syn = f"{db-dl-dn:+.4f}"
    dl_s = f"{dl:.4f}" if isinstance(dl,(int,float)) else "n/a"
    dn_s = f"{dn:.4f}" if isinstance(dn,(int,float)) else "n/a"
    db_s = f"{db:.4f}" if isinstance(db,(int,float)) else "n/a"
    print(f"{s:>6}  {dl_s:>9}  {dn_s:>9}  {db_s:>9}  {syn}")
print()
print("chain context:")
print("  round 1 (spike 6): Δ_net 0.054 → 0.081 (+0.027)")
print("  this round (chain 2): step-100 should ≈ 0.08; step-1000 tells us if Net still climbs")
PY
