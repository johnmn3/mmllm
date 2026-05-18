#!/usr/bin/env bash
# run_spike7_persistence.sh — does spike 6's end-state actually carry over?
#
# Question: spike 6 ended at Δ_net=0.081 (step 1000). If we resume from
# its full state and continue with the SAME sleep-phase regime, does the
# first ablation in the new session read ≈ 0.08, or does it slide back
# to the round-6 baseline of 0.054?
#
# Test setup:
#   - resume from /tmp/mmllm-cpu/fim-json-v3.ckpts/step-1001 (full state:
#     dense.pt with trunk+gate+α_net, opt-dense, opt-sparse, opt-sparse-net,
#     plus V_local at fim-bank-v3.{0..3}.bin and V_net at fim-bank-v3-net)
#   - lock ALL LR multipliers + distill_coef + mag_coef at spike 6's
#     end-of-run values (start=end so cosine is flat — no schedule
#     motion to confound the persistence reading)
#   - no warmup (we're past it)
#   - 200 additional steps, ablate every 50 → first ablation at step 1050
#
# Pass: step-1050 ablation reads Δ_net ≈ 0.08 (state persisted).
# Fail: step-1050 ablation reads Δ_net ≈ 0.05 (something resets between runs).

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

HANDLE="spike7-persistence"

# Spike 6 config, frozen at sleep-phase-end values (start=end so the
# cosine schedule is flat across this 200-step continuation).
export MMLLM_NETBANK_ENABLED=true
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=32
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true

# Distill: hold at spike-6 sleep-phase-end values.
export MMLLM_DISTILL_COEF=5.0
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_DISTILL_MAGNITUDE_COEF=1.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
export MMLLM_DISTILL_MAGNITUDE_CLAMP=10.0

# LR multipliers: hold at spike-6 sleep-phase-end values.
export MMLLM_LR_BANK_MULT=0.001
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.1
export MMLLM_LR_NET_MULT_END=0.1
export MMLLM_LR_DENSE_MULT=0.005
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3
export MMLLM_LR_WARMUP=0

# Replay (matched to spike 6).
# Skip NetBank warmstart — we want spike 6's V_net to flow through untouched.
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false

# Frequent ablations so we catch the first reading early.
export MMLLM_ABLATE_EVERY=50

# Use spike 6's base path (where its ckpts/banks already live).
FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3

echo "── spike 7 persistence test ──"
echo "  resume seed: ${FIM_BASE}.ckpts/step-1001 (spike 6 end-state)"
echo "  V_local:     ${BANK_BASE}.{0..3}.bin"
echo "  V_net:       ${BANK_BASE}-net.{0..3}.bin"
echo "  config:      spike-6 sleep-end values, frozen (start=end)"
echo "  ablations:   every 50 steps starting at step 1050"

# Sanity check: required ckpt files exist.
for f in "${FIM_BASE}.ckpts/step-1001/dense.pt" \
         "${FIM_BASE}.ckpts/step-1001/opt-dense.pt" \
         "${FIM_BASE}.ckpts/step-1001/opt-sparse.pt" \
         "${FIM_BASE}.ckpts/step-1001/opt-sparse-net.pt" \
         "${BANK_BASE}.0.bin" "${BANK_BASE}.1.bin" "${BANK_BASE}.2.bin" "${BANK_BASE}.3.bin" \
         "${BANK_BASE}-net.0.bin" "${BANK_BASE}-net.1.bin" "${BANK_BASE}-net.2.bin" "${BANK_BASE}-net.3.bin"; do
  if [ ! -f "$f" ]; then
    echo "MISSING: $f" >&2; exit 1
  fi
done
echo "  ✓ all spike 6 artifacts present"

TRAIN_LOG=/tmp/mmllm-cpu/${HANDLE}.train.log
TOTAL_STEPS=1101       # start=1001 + 100 more steps; ablations at 1050 + 1100
EVAL_EVERY=100
CKPT_EVERY=10000       # no intermediate ckpt — saves ~1.3 GB on disk

mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL_STEPS" "$EVAL_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG"

echo ""
echo "── persistence-test ablation trajectory ──"
python3 - "${FIM_BASE}.log.jsonl" <<'PY'
import json, sys
from pathlib import Path
log = Path(sys.argv[1])
rows = []
for line in log.read_text().splitlines():
    try:    ev = json.loads(line)
    except: continue
    if ev.get("event") in ("ablation","ablation_intermediate"):
        s = ev.get("step") or 0
        if s >= 1001:
            rows.append((s, ev.get("delta_local"), ev.get("delta_net"), ev.get("delta_both")))
print(f"{'step':>6}  {'Δ_local':>9}  {'Δ_net':>9}  {'Δ_both':>9}")
for s, dl, dn, db in rows:
    dl = f"{dl:.4f}" if isinstance(dl,(int,float)) else "n/a"
    dn = f"{dn:.4f}" if isinstance(dn,(int,float)) else "n/a"
    db = f"{db:.4f}" if isinstance(db,(int,float)) else "n/a"
    print(f"{s:>6}  {dl:>9}  {dn:>9}  {db:>9}")
print()
print("expected if state persists: step-1050 Δ_net ≈ 0.08 (spike-6 end was 0.0807)")
print("if Δ_net at step 1050 ≈ 0.05 instead, something resets between runs")
PY
