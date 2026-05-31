#!/usr/bin/env bash
# run_hogwild.sh — multi-trunk Hogwild training.
#
# Spawns N trunks in parallel. Each:
#   - has its own dense weights + V_local mmap files + ckpt dir + log
#   - SHARES the V_net mmap files with all other trunks (Hogwild — kernel
#     arbitrates writes, race-tolerated as per the original paper)
#
# Net is the consolidator. Every trunk's distill writes into the same
# V_net rows; over time Net averages signal from all trunks.
#
# Usage:  bash scripts/run_hogwild.sh <N_TRUNKS> [BATCH_SIZE]
#         N_TRUNKS:    1-8 (cores=4; >4 is oversubscribed)
#         BATCH_SIZE:  per-trunk batch; default 8
#
# Aggregate compute per wall hour caps at the 4-core ceiling — running
# more trunks just spreads that cap across more processes, with Net
# benefiting from more diverse gradients per slice.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

N_TRUNKS="${1:-4}"
BATCH_SIZE="${2:-8}"
STEP_LEN="${MMLLM_HOGWILD_STEPS:-100}"

if [ "$N_TRUNKS" -lt 1 ] || [ "$N_TRUNKS" -gt 16 ]; then
  echo "N_TRUNKS must be 1-16, got $N_TRUNKS" >&2; exit 1
fi

# Shared V_net mmap path — all trunks write here. Per-trunk V_local
# stays separate (each trunk specializes).
SHARED_NET=/tmp/mmllm-cpu/hogwild-shared-net
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

# Allocate the shared V_net files once. All trunks mmap them.
echo "═══════════════════════════════════════════════════════════════"
echo "  Hogwild: $N_TRUNKS trunks, B=$BATCH_SIZE each, step_len=$STEP_LEN"
echo "═══════════════════════════════════════════════════════════════"
rm -f "${SHARED_NET}".*.bin
python3 - <<'PY'
import numpy as np
SQRT_NET = 8;  C_NET = 32;  N_LAYERS = 32
for i in range(N_LAYERS):
    a = np.memmap(f"/tmp/mmllm-cpu/hogwild-shared-net.{i}.bin",
                  dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
print(f"  shared V_net: 32 files × 8² × 32 × 4 = 256 KB (mmap'd by all trunks)")
PY

# Common config for every trunk.
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=8
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_DISTILL_COEF=0.5
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_LR_BANK_MULT=30.0
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=0.1
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-3
export MMLLM_LR_MIN=3e-3
export MMLLM_LR_WARMUP=$((STEP_LEN * 70 / 100))
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
export MMLLM_ABLATE_EVERY=$((STEP_LEN / 4))
export MMLLM_LITE_CKPT=true
export MMLLM_BATCH=$BATCH_SIZE
# Pin per-process thread count low so N trunks don't all grab all 4 cores.
# Each trunk gets max(1, 4/N) intra-op threads.
export MMLLM_NUM_THREADS=$(( (4 + N_TRUNKS - 1) / N_TRUNKS ))

# Per-trunk staging + launch.
PIDS=()
LOGS=()
for t in $(seq 0 $((N_TRUNKS - 1))); do
  FIM_BASE=/tmp/mmllm-cpu/hogwild-t${t}
  BANK_BASE=/tmp/mmllm-cpu/hogwild-t${t}-bank
  TRAIN_LOG=/tmp/mmllm-cpu/hogwild-t${t}.train.log

  mkdir -p "$(dirname $FIM_BASE)"
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin" 2>/dev/null || true
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)" "${FIM_BASE}.val.bin" 2>/dev/null || true
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)" "${FIM_BASE}.test.bin" 2>/dev/null || true

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

  # Per-trunk V_local (separate per trunk — each trunk specializes).
  # Shared V_net (symlink to the common path).
  python3 - "$BANK_BASE" "$t" <<'PY'
import sys, os, numpy as np
bank_base = sys.argv[1]; t = int(sys.argv[2])
SQRT_LOCAL = 226;  Q_DIM = 128
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_LOCAL * SQRT_LOCAL, Q_DIM))
    a[:] = 0.0; a.flush()
# Symlink V_net to the shared file.
for i in range(32):
    src = f"/tmp/mmllm-cpu/hogwild-shared-net.{i}.bin"
    dst = f"{bank_base}-net.{i}.bin"
    if os.path.exists(dst): os.unlink(dst)
    os.symlink(src, dst)
print(f"  trunk {t}: own V_local 8 files, V_net symlinks to shared")
PY

  echo "  → spawning trunk $t (B=$BATCH_SIZE, threads=$MMLLM_NUM_THREADS)"
  TOTAL=$((STEP_LEN + 1))
  CKPT_EVERY=$((STEP_LEN + 10))   # don't fire — lite ckpt + no save mid-run
  EVAL_EVERY=$MMLLM_ABLATE_EVERY
  mmllm train-fim "$FIM_BASE" "$BANK_BASE" "$TOTAL" "$EVAL_EVERY" "$CKPT_EVERY" \
    >"$TRAIN_LOG" 2>&1 &
  PIDS+=($!)
  LOGS+=("$TRAIN_LOG")
done

# Wait for all trunks.
echo ""
echo "  $N_TRUNKS trunks running in parallel. Waiting for all to finish."
echo ""
for pid in "${PIDS[@]}"; do
  wait "$pid" || echo "  trunk pid $pid exited non-zero"
done

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  Per-trunk final ablation"
echo "═══════════════════════════════════════════════════════════════"
for t in $(seq 0 $((N_TRUNKS - 1))); do
  echo ""
  echo "--- trunk $t ---"
  grep -E "ablation Δ at step|Δ_local|Δ_net|Δ_both" "/tmp/mmllm-cpu/hogwild-t${t}.train.log" | tail -12
done
