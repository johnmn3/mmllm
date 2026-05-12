#!/usr/bin/env bash
# run_spoon_chain_big.sh — adaptive-doubling spoon chain at production-scale banks.
#
# Bank sizes (10 MB router / 1 GB local / 3.2 GB net):
#   trunk      ~11 MB
#   V_local    sqrt_n=720,  q_dim=128  → 1.0 GB total
#   V_net      sqrt_n=2500, c_net=32   → 3.2 GB total
#
# Adaptive chain:
#   - Round 1: 100-step spoon from round-6 trunk + zero banks
#   - After each round:
#       if end Δ_net > best Δ_net so far → keep step_len, advance best archive
#       else                              → step_len *= 2 (cap 800), resume
#                                           from best (not just-completed) round
#   - Stop at step_len > 800 OR after 10 rounds
#   - Disk-frugal: keep only ONE "best" archive at a time (overwritten on improvement)
#
# Pass: Δ_net at the final best round > Δ_net at round 1.

set -e

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Production-scale bank sizes.
export MMLLM_SQRT_N=720
export MMLLM_NET_SQRT_N=2000         # 2 GB V_net — fits in 15 GiB RAM
                                     # for training (dense SparseAdam state
                                     # 4 GB), keeps disk paging unnecessary.
                                     # bigger V_net works for inference but
                                     # makes training >7 min per ablation.
export MMLLM_NET_C_NET=32
# Scaled top_k / sub_top_k — proportional to bank-area increase, so
# per-step V-row coverage matches cpu-tiny (12.5% Local / 3.3% Net).
export MMLLM_MEMORY_TOP_K=128
export MMLLM_MEMORY_SUB_TOP_K=45
export MMLLM_NET_TOP_K=256
export MMLLM_NET_SUB_TOP_K=128

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
# Skip opt-state + bank-latest writes at ckpt time. The chain replays
# the schedule fresh each round so Adam moments aren't needed for
# resume, and V banks are already on disk via the live mmap path.
# At sqrt_n=720 V_local + sqrt_n=2500 V_net, the full ckpt is ~12 GB
# (opt-sparse-net 5 GB + opt-sparse 2 GB + bank-latest 4 GB); lite
# ckpt is ~16 MB (just dense.pt). Critical on a 7 GB-free sandbox.
export MMLLM_LITE_CKPT=true

FIM_BASE=/tmp/mmllm-cpu/fim-json-v3
BANK_BASE=/tmp/mmllm-cpu/fim-bank-v3
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000
BEST_ARCHIVE=/tmp/mmllm-cpu/spoon-big-best
mkdir -p "$BEST_ARCHIVE"

CHAIN_LOG=/tmp/mmllm-cpu/spoon-chain-big.summary.log
: > "$CHAIN_LOG"

# Per-round runner: stages dense + banks, trains, returns end Δ_net.
run_round() {
  local round_num=$1
  local step_len=$2
  local resume_dense=$3     # "BASELINE" or path to dense.pt
  local resume_v_net=$4     # "ZERO" or path-prefix to V_net.<i>.bin
  local warmup_steps=$((step_len * 70 / 100))
  local ablate_every=$((step_len / 4))

  export MMLLM_LR_WARMUP=$warmup_steps
  export MMLLM_ABLATE_EVERY=$ablate_every

  echo ""
  echo "═══════════════════════════════════════════════════════════════"
  echo "  ROUND $round_num  step_len=$step_len  warmup=$warmup_steps  ablate=$ablate_every"
  echo "═══════════════════════════════════════════════════════════════"

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"

  if [ "$resume_dense" = "BASELINE" ]; then
    cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
  else
    cp "$resume_dense" "${FIM_BASE}.ckpts/step-1/dense.pt"
  fi
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  # Zero-init V_local always (fresh hill climber per round).
  # Init V_net: ZERO for round 1, or restore from best archive.
  python3 - "$BANK_BASE" "$resume_v_net" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]; resume_v_net = sys.argv[2]
SQRT_LOCAL = 720;   Q_DIM = 128
SQRT_NET   = 2000;  C_NET = 32
for i in range(4):
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
if resume_v_net == "ZERO":
    for i in range(4):
        a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                      shape=(SQRT_NET * SQRT_NET, C_NET))
        a[:] = 0.0; a.flush()
    print("  V_net zero-init")
else:
    import shutil
    for i in range(4):
        shutil.copy(f"{resume_v_net}.{i}.bin", f"{bank_base}-net.{i}.bin")
    print("  V_net carried from best archive")
PY

  local TRAIN_LOG=/tmp/mmllm-cpu/spoon-big-r${round_num}.train.log
  local TOTAL=$((step_len + 1))
  local CKPT_EVERY=$step_len   # save once at the end
  mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL" "$ablate_every" "$CKPT_EVERY" 2>&1 | tee "$TRAIN_LOG" \
    | grep -E "ablation Δ at step|Δ_local|Δ_net|Δ_both|training complete|step .*lr_b" || true

  # Extract final Δ_net (last ablation_intermediate event).
  local END_DNET
  END_DNET=$(grep '"event":"ablation_intermediate"' /tmp/mmllm-cpu/fim-json-v3.log.jsonl \
    | python3 -c "import sys,json; ev=[json.loads(l) for l in sys.stdin]; print(ev[-1]['delta_net'] if ev else 0)")
  echo "  → round $round_num end Δ_net = $END_DNET" | tee -a "$CHAIN_LOG"
  echo "$round_num,$step_len,$END_DNET" >> "$CHAIN_LOG"
  echo "$END_DNET"
}

archive_current_as_best() {
  rm -rf "$BEST_ARCHIVE"
  mkdir -p "$BEST_ARCHIVE"
  local LATEST=$(ls -1d "${FIM_BASE}.ckpts/step-"* 2>/dev/null | sort -V | tail -1)
  cp "$LATEST/dense.pt" "$BEST_ARCHIVE/dense.pt"
  for i in 0 1 2 3; do
    cp "${BANK_BASE}-net.${i}.bin" "$BEST_ARCHIVE/V_net.${i}.bin"
  done
  echo "  → archived as new best"
}

# ─── Chain loop ─────────────────────────────────────────────────────────────
step_len=100
best_dnet=0
have_best=0

for round_num in 1 2 3 4 5 6 7 8 9 10; do
  if [ "$have_best" = "0" ]; then
    dnet=$(run_round "$round_num" "$step_len" BASELINE ZERO | tail -1)
  else
    dnet=$(run_round "$round_num" "$step_len" "$BEST_ARCHIVE/dense.pt" "$BEST_ARCHIVE/V_net" | tail -1)
  fi
  # Sanitize: strip whitespace, default to 0 if extraction returned empty.
  dnet=$(echo "$dnet" | tr -d '[:space:]')
  if [ -z "$dnet" ]; then dnet=0; fi

  is_better=$(python3 -c "print(1 if float('$dnet') > float('$best_dnet') else 0)")
  if [ "$is_better" = "1" ]; then
    archive_current_as_best
    best_dnet="$dnet"
    have_best=1
    echo "  → improved: best Δ_net now $best_dnet (step_len stays $step_len)"
  else
    new_len=$((step_len * 2))
    if [ "$new_len" -gt 800 ]; then
      echo "  → regressed at step_len=$step_len; doubling would exceed 800. Stopping."
      break
    fi
    step_len=$new_len
    echo "  → regressed: doubling step_len to $step_len, resuming from best (Δ_net=$best_dnet)"
  fi
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  SPOON CHAIN SUMMARY"
echo "═══════════════════════════════════════════════════════════════"
echo "round,step_len,end_dnet"
grep -E "^[0-9]+," "$CHAIN_LOG"
echo ""
echo "best Δ_net: $best_dnet"
echo "best archive: $BEST_ARCHIVE"
