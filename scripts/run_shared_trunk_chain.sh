#!/usr/bin/env bash
# run_shared_trunk_chain.sh — N rounds of shared-trunk sporks back-to-back.
#
# Recipe per round (default config):
#   N=16 trunks, B_per_trunk=1, B_eff=16
#   100 train steps, ABLATE_EVERY=25 (4 ablations + 1 end-ablation)
#   MMLLM_SPARSE_OPT=sgd (zero V_local opt state — N-independent memory)
#   32-layer asymmetric arch, Local at 8 layers, NetBank at all 32
#
# Round 1 starts from round-6 baseline:
#   - dense.pt copied from /home/user/mmllm/core/round-6/step-5000
#     (40/86 dense param tensors skip-load due to shape mismatch — the
#     bank K_a/K_b projection shapes differ between round-6 and the
#     asym config; non-bank dense weights load cleanly.)
#   - V_local: zero-init at (N_TRUNKS * sqrt_n², q_dim) shape
#   - V_net:   zero-init at (sqrt_n_net², c_net) shape × 32 layers.
#     We can't reuse round-6's fp16 NetBank (sqrt_n=1024 × c_net=32 × 4
#     layers) — shape doesn't match our sqrt_n=64 × 32-layer config.
#
# Rounds 2..N inherit dense.pt + V_net from the previous round;
# V_local is re-zeroed each round (matches the spike-6 hill-climber +
# consolidator pattern — Local explores fresh, Net accumulates).
#
# Archives every round's end-state under /tmp/mmllm-cpu/spork-chain-<ts>/
# round-N/, plus a summary parsed from the per-round log.jsonl.
#
# Usage:  bash scripts/run_shared_trunk_chain.sh [N_ROUNDS] [N_TRUNKS] [STEPS]
#         N_ROUNDS:  number of back-to-back sporks; default 5
#         N_TRUNKS:  trunks per spork; default 16
#         STEPS:     training steps per spork; default 100

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

N_ROUNDS="${1:-5}"
N_TRUNKS="${2:-16}"
STEPS="${3:-100}"

# Per-round config (matches run_shared_trunk.sh's working recipe).
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226                # V_local sqrt_n
export MMLLM_NET_SQRT_N=64             # V_net sqrt_n (64²=4096 rows × 32 layers ≈ 16 MB)
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8

export MMLLM_N_TRUNKS=$N_TRUNKS
export MMLLM_BATCH=1                   # B_per_trunk; B_eff = N_TRUNKS × 1 = 16 at N=16
export MMLLM_SPARSE_OPT=sgd            # zero V_local opt state

# Spike-6 recipe (verbatim from run_asym_spoon.sh / round-10-2). DO NOT
# REMOVE INDIVIDUAL ENTRIES — each was added to address a documented
# failure mode (round-7..10 narratives in docs/journal/).
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
export MMLLM_LR_WARMUP=$((STEPS * 70 / 100))
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
# Ablation policy: end-only. ABLATE_EVERY=0 disables mid-training ablations;
# the end-of-train ablation in train-long still fires unconditionally per
# round. This matches the shared-trunk recipe (run_shared_trunk.sh) — mid-
# ablations add ~45s of eval-bpc each plus a memory spike to ~15 GB, which
# is dead overhead given the per-round end-ablation already gives us the
# Δ_local / Δ_net trajectory across rounds.
export MMLLM_ABLATE_EVERY=0
export MMLLM_LITE_CKPT=true

FIM_BASE=/tmp/mmllm-cpu/fim-shared-trunk-chain
BANK_BASE=/tmp/mmllm-cpu/fim-bank-shared-trunk-chain
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000
ARCHIVE_ROOT=/tmp/mmllm-cpu/spork-chain-$(date -u +%H%M)
mkdir -p "$ARCHIVE_ROOT"

LOCAL_LAYERS=(0 1 2 12 20 29 30 31)
NET_LAYERS=$(seq 0 31)

# Ensure FIM-corpus symlinks exist (link from fim-json-v3 prepped by
# build_glaive_fim_corpus.sh).
mkdir -p "$(dirname $FIM_BASE)"
for split in train val test; do
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.${split}.bin)" \
         "${FIM_BASE}.${split}.bin" 2>/dev/null || true
done

echo "═══════════════════════════════════════════════════════════════"
echo "  SPORK CHAIN  rounds=$N_ROUNDS  N_TRUNKS=$N_TRUNKS  steps=$STEPS"
echo "  archive: $ARCHIVE_ROOT"
echo "═══════════════════════════════════════════════════════════════"

run_round() {
  local round_num=$1
  local resume_dense=$2     # path to dense.pt OR "BASELINE"
  local resume_v_net=$3     # path-prefix OR "FP16_SEED"

  echo ""
  echo "── ROUND $round_num ─────────────────────────────────────────"

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"

  # Stage dense.pt.
  if [ "$resume_dense" = "BASELINE" ]; then
    cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
  else
    cp "$resume_dense" "${FIM_BASE}.ckpts/step-1/dense.pt"
  fi
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  # Stage V_net. Round 1 zero-inits a fresh V_net (the round-6 fp16 seed
  # has shape sqrt_n=1024 × c_net=32 × 4 layers, which doesn't match our
  # current sqrt_n=64 × 32 layers; reshaping isn't well-defined, so we
  # start NetBank from zero). Subsequent rounds carry V_net forward.
  if [ "$resume_v_net" = "FRESH" ]; then
    python3 - "${BANK_BASE}" <<'PY'
import sys, numpy as np
bank_base = sys.argv[1]
SQRT_NET = 64;  C_NET = 32
N_LAYERS = 32
for layer in range(N_LAYERS):
    arr = np.memmap(f"{bank_base}-net.{layer}.bin", dtype=np.float32,
                    mode="w+", shape=(SQRT_NET * SQRT_NET, C_NET))
    arr[:] = 0.0; arr.flush()
print(f"  V_net: zero-init 32 layers × 64²×32 = 16 MB total")
PY
  else
    for i in $NET_LAYERS; do
      cp "${resume_v_net}.${i}.bin" "${BANK_BASE}-net.${i}.bin"
    done
    echo "  V_net: carried forward from $(basename $(dirname $resume_v_net))"
  fi

  # Stage V_local — zero-init per round (hill-climber pattern; bank wakes
  # from empty each spoon, accumulates content during training, sleep
  # wipes back to zero before the next round).
  # Shape: (N_TRUNKS × sqrt_n², q_dim) per layer × 8 Local Bank layers.
  python3 - "${BANK_BASE}" "${N_TRUNKS}" <<'PY'
import sys, numpy as np
bank_base  = sys.argv[1]
n_trunks   = int(sys.argv[2])
SQRT_LOCAL = 226;  Q_DIM = 128
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
n_per_trunk = SQRT_LOCAL * SQRT_LOCAL
n_total     = n_trunks * n_per_trunk
for layer in LOCAL_LAYERS:
    arr = np.memmap(f"{bank_base}.{layer}.bin", dtype=np.float32,
                    mode="w+", shape=(n_total, Q_DIM))
    arr[:] = 0.0; arr.flush()
PY
  echo "  V_local: zero-init 8 layers × $N_TRUNKS trunks × 226²×128"

  # Train. eval-every set > STEPS so no mid-training eval fires; the
  # end-of-train ablation (in train-long after the step loop) still runs.
  # ckpt-every > STEPS so no mid-run ckpt fires (LITE_CKPT keeps end-ckpt small).
  echo "  → training $STEPS steps…"
  local TRAIN_LOG="$ARCHIVE_ROOT/round-${round_num}.train.log"
  mmllm train-fim "$FIM_BASE" "$BANK_BASE" \
        $((STEPS + 1)) $((STEPS + 1)) $((STEPS + 10)) 2>&1 \
    | tee "$TRAIN_LOG" \
    | grep --line-buffered -E "control  bpc|ablated  bpc|Δ bpc|training complete" \
    || true

  # Archive end-state.
  local ROUND_DIR="$ARCHIVE_ROOT/round-${round_num}"
  mkdir -p "$ROUND_DIR"
  for i in $NET_LAYERS; do
    cp "${BANK_BASE}-net.${i}.bin" "$ROUND_DIR/V_net.${i}.bin"
  done
  local LATEST=$(ls -1d "${FIM_BASE}.ckpts/step-"* 2>/dev/null | sort -V | tail -1)
  cp "$LATEST/dense.pt"          "$ROUND_DIR/dense.pt"
  cp "${FIM_BASE}.log.jsonl"     "$ROUND_DIR/log.jsonl" 2>/dev/null || true
  echo "  → archived to $ROUND_DIR"
}

# Round 1: dense warm-start from round-6, NetBank fresh (shape mismatch
# with round-6 prevents direct seed transfer; see run_round's V_net path).
run_round 1 BASELINE FRESH

# Subsequent rounds: carry dense + V_net forward.
for r in $(seq 2 $N_ROUNDS); do
  prev=$((r - 1))
  run_round "$r" \
    "$ARCHIVE_ROOT/round-${prev}/dense.pt" \
    "$ARCHIVE_ROOT/round-${prev}/V_net"
done

# Per-round summary parsed from the .log.jsonl files.
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  SPORK CHAIN SUMMARY"
echo "═══════════════════════════════════════════════════════════════"
python3 - "$ARCHIVE_ROOT" "$N_ROUNDS" <<'PY'
import json, sys
from pathlib import Path
root = Path(sys.argv[1]); n_rounds = int(sys.argv[2])
print(f"{'round':>5}  {'step':>5}  {'Δ_local':>9}  {'Δ_net':>9}  {'Δ_both':>9}")
for r in range(1, n_rounds + 1):
    rd = root / f"round-{r}"
    log = rd / "log.jsonl"
    if not log.exists():
        print(f"{r:>5}  {'(no log)':>30}")
        continue
    last_step = -1
    for line in log.read_text().splitlines():
        try: ev = json.loads(line)
        except: continue
        if ev.get("event") == "ablation_intermediate":
            print(f"{r:>5}  {ev['step']:>5}  {ev.get('delta_local', 0):>+9.4f}  "
                  f"{ev.get('delta_net', 0):>+9.4f}  {ev.get('delta_both', 0):>+9.4f}")
            last_step = ev['step']
    print()
print(f"  archives at: {root}")
PY
