#!/usr/bin/env bash
# run_spoon_lengths.sh — 4 single-spoon runs from baseline at 50, 100, 200, 600 steps.
# Production-scale banks: 1 GB V_local + 2 GB V_net.
# No chain, no resume — each spoon starts from round-6 trunk + zero banks.
# Reports per-spoon final ablation (Δ_local, Δ_net, Δ_both).
#
# Tests how much V_local / V_net accumulate as a function of training
# duration on bigger banks.

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
export MMLLM_LR_BANK_MULT=30.0
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
echo "step_len,Δ_local,Δ_net,Δ_both,ctrl_bpc" >> "$SUMMARY"

run_spoon() {
  local step_len=$1
  local warmup_steps=$((step_len * 70 / 100))
  local ablate_every=$((step_len / 4))
  [ "$ablate_every" -lt 25 ] && ablate_every=$step_len   # for step_len=50, ablate only at end (step 50)

  export MMLLM_LR_WARMUP=$warmup_steps
  export MMLLM_ABLATE_EVERY=$ablate_every

  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "  SPOON  step_len=$step_len  warmup=$warmup_steps  ablate_every=$ablate_every"
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

  local TRAIN_LOG=/tmp/mmllm-cpu/spoon-len-${step_len}.train.log
  local TOTAL=$((step_len + 1))
  local CKPT_EVERY=$((step_len + 10))   # don't fire (lite ckpt safety)
  mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL" "$ablate_every" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG" \
    | grep -E "ablation Δ at step|Δ_local|Δ_net|Δ_both|training complete|step .*lr_b" || true

  # Extract final ablation values from the structured log.
  python3 - "$step_len" >> "$SUMMARY" <<'PY'
import sys, json
from pathlib import Path
step_len = int(sys.argv[1])
log = Path("/tmp/mmllm-cpu/fim-json-v3.log.jsonl")
last = None
for line in log.read_text().splitlines():
    try: ev = json.loads(line)
    except: continue
    if ev.get("event") == "ablation_intermediate":
        last = ev
if last is None:
    print(f"{step_len},,,,(no ablation)")
else:
    print(f"{step_len},{last['delta_local']:.4f},{last['delta_net']:.4f},{last['delta_both']:.4f},{last['control_bpc']:.4f}")
PY
}

for step_len in 50 100 200 600; do
  run_spoon "$step_len"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  SPOON LENGTHS SUMMARY"
echo "═══════════════════════════════════════════════════════════════"
column -t -s, < "$SUMMARY"
