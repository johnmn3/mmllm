#!/usr/bin/env bash
# run_spoon_lengths.sh — LR_BANK_MULT sweep at 50, 100, 200, 600.
# 4 single-spoon runs from baseline at 100 steps each.
# Production-scale banks: 1 GB V_local + 2 GB V_net.
# Tests how high LR_BANK_MULT can go on bigger banks before destabilizing.

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Bank sizes.
export MMLLM_SQRT_N=720                    # V_local 1 GB
export MMLLM_NET_SQRT_N=2000               # V_net 2 GB
export MMLLM_NET_C_NET=32

# Spike-6 recipe.
export MMLLM_NETBANK_ENABLED=true
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
# MMLLM_LR_BANK_MULT is the swept variable — set per-run inside run_spoon.
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=0.1
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_LITE_CKPT=true

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

SUMMARY=/tmp/mmllm-cpu/spoon-lengths.summary.log
: > "$SUMMARY"
echo "lr_mult,Δ_local,Δ_net,Δ_both,ctrl_bpc" >> "$SUMMARY"

# Fixed step length per spoon (100 steps); only LR_BANK_MULT varies.
STEP_LEN=100
WARMUP_STEPS=70
ABLATE_EVERY=25

export MMLLM_LR_WARMUP=$WARMUP_STEPS
export MMLLM_ABLATE_EVERY=$ABLATE_EVERY

run_spoon() {
  local lr_mult=$1
  export MMLLM_LR_BANK_MULT=$lr_mult

  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "  SPOON  LR_BANK_MULT=$lr_mult  step_len=$STEP_LEN  warmup=$WARMUP_STEPS"
  echo "═══════════════════════════════════════════════════════════════"

  # Reset state for each spoon (fresh baseline).
  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  python3 - "$BANK_BASE" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
SQRT_LOCAL = 720;  Q_DIM = 128
SQRT_NET   = 2000; C_NET = 32
for i in range(4):
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
for i in range(4):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
print("  V_local + V_net zero-initialized")
PY

  local TRAIN_LOG=/tmp/mmllm-cpu/spoon-lr-${lr_mult}.train.log
  local TOTAL=$((STEP_LEN + 1))
  local CKPT_EVERY=$((STEP_LEN + 10))   # don't fire (lite ckpt safety)
  mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL" "$ABLATE_EVERY" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG" \
    | grep -E "ablation Δ at step|Δ_local|Δ_net|Δ_both|training complete|step .*lr_b" || true

  # Extract final ablation values from the structured log.
  python3 - "$lr_mult" >> "$SUMMARY" <<'PY'
import sys, json
from pathlib import Path
lr_mult = sys.argv[1]
log = Path("/tmp/mmllm-cpu/fim-json-v3.log.jsonl")
last = None
for line in log.read_text().splitlines():
    try: ev = json.loads(line)
    except: continue
    if ev.get("event") == "ablation_intermediate":
        last = ev
if last is None:
    print(f"{lr_mult},,,,(no ablation)")
else:
    print(f"{lr_mult},{last['delta_local']:.4f},{last['delta_net']:.4f},{last['delta_both']:.4f},{last['control_bpc']:.4f}")
PY
}

for lr_mult in 50 100 200 600; do
  run_spoon "$lr_mult"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  SPOON LENGTHS SUMMARY"
echo "═══════════════════════════════════════════════════════════════"
column -t -s, < "$SUMMARY"
