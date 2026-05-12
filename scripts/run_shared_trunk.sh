#!/usr/bin/env bash
# run_shared_trunk.sh — option-A shared-trunk multi-stream training.
#
# Single mmllm process. One model. The shared trunk (dense weights, K_a,
# K_b, q_norm, NetBank V_net) is updated by every batch row; each Local
# Bank V_local has N=MMLLM_N_TRUNKS slices and per-row trunk_ids route
# each batch row to its own slice.
#
# This is the architectural opposite of the prior multi-process hogwild:
# we share the trunk and split only the value bank — much smaller RAM
# footprint at N=8/16/32, and one optimizer step per micro-batch instead
# of N races on the same dense Adam state.
#
# Usage:  bash scripts/run_shared_trunk.sh <N_TRUNKS> [B_PER_TRUNK] [STEPS]
#         N_TRUNKS:     1-32 (memory ceiling ~32 on 15 GB box)
#         B_PER_TRUNK:  per-trunk batch rows; default 4
#         STEPS:        train steps (one optimizer step per micro-batch); default 100

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

N_TRUNKS="${1:-4}"
B_PER_TRUNK="${2:-4}"
STEP_LEN="${3:-100}"

if [ "$N_TRUNKS" -lt 1 ] || [ "$N_TRUNKS" -gt 32 ]; then
  echo "N_TRUNKS must be 1-32, got $N_TRUNKS" >&2; exit 1
fi

echo "═══════════════════════════════════════════════════════════════"
echo "  Shared-trunk: N_TRUNKS=$N_TRUNKS, B_PER_TRUNK=$B_PER_TRUNK, steps=$STEP_LEN"
echo "  Effective batch: $((N_TRUNKS * B_PER_TRUNK)) rows per step"
echo "═══════════════════════════════════════════════════════════════"

# Asymmetric arch (32 layers, Local at 8) — same as run_asym_spoon.sh.
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226                # V_local per layer: 226² × 128 × 4 = 26 MB × 8 layers = 209 MB × N
export MMLLM_NET_SQRT_N=64             # V_net per layer:   64²  × 32  × 4 = 524 KB × 32 layers = 16 MB shared
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8

# N_TRUNKS: the new knob. Routes per-batch-row gathers into V_local slices.
export MMLLM_N_TRUNKS=$N_TRUNKS

# Sparse-optimizer state: REQUIRED at N>1. Stock torch.optim.SparseAdam
# allocates DENSE (V_local_total × q_dim × 4) × 2 moments — at N=16 that's
# 6.7 GB just for V_local optimizer state, before any activations. The
# mmllm.optim.CPUOffloadSparseAdam keeps state touched-row-sparse, scaling
# with unique-rows-touched × q_dim × 8 bytes — typically <500 MB at the
# spoon scale. Without this the shared-trunk OOMs at N≥8 on a 15 GB box.
export MMLLM_CPU_OFFLOAD=true

# Spike-6 schedule (same training recipe as the asym spoon).
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
export MMLLM_LR_WARMUP=$((STEP_LEN * 70 / 100))
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART=true
export MMLLM_NET_V_WARMSTART_FROM_LOCAL=false
# Ablation policy: end-only. ABLATE_EVERY=0 disables mid-training ablations;
# the end-of-train ablation in train-long still fires unconditionally.
export MMLLM_ABLATE_EVERY=0
export MMLLM_LITE_CKPT=true
# Per-trunk batch size — train-long reads MMLLM_BATCH as B-per-trunk
# when MMLLM_N_TRUNKS>1.
export MMLLM_BATCH=$B_PER_TRUNK

FIM_BASE=/tmp/mmllm-cpu/fim-shared-trunk
BANK_BASE=/tmp/mmllm-cpu/fim-bank-shared-trunk
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)"   "${FIM_BASE}.val.bin"   2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)"  "${FIM_BASE}.test.bin"  2>/dev/null || true

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
mkdir -p "${FIM_BASE}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${FIM_BASE}.ckpts/step-1/dense.pt"
echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"

# Bank init: per-trunk V_local files sized (N_TRUNKS * sqrt_n² , q_dim),
# per-layer V_net files sized (sqrt_n_net² , c_net). Local files contain
# N_TRUNKS contiguous slices laid out (trunk0_rows, trunk1_rows, …).
python3 - "$BANK_BASE" "$N_TRUNKS" <<'PY'
import numpy as np, sys
bank_base = sys.argv[1]
n_trunks  = int(sys.argv[2])
SQRT_LOCAL = 226;  Q_DIM = 128
SQRT_NET   = 64;   C_NET = 32
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
n_per_trunk = SQRT_LOCAL * SQRT_LOCAL
local_n = n_trunks * n_per_trunk
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(local_n, Q_DIM))
    a[:] = 0.0; a.flush()
for i in range(32):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = 0.0; a.flush()
print(f"  banks zero-init'd: 8 V_local × {n_trunks} trunks, 32 V_net (shared)")
PY

# train-fim args: total-steps eval-every ckpt-every
# eval-every set to STEP_LEN+1 so eval-bpc never fires mid-training; the
# end-of-train ablation (in train-long after the step loop) still runs.
# ckpt-every set high so no mid-run ckpt — MMLLM_LITE_CKPT=true anyway.
mmllm train-fim "$FIM_BASE" "$BANK_BASE" $((STEP_LEN + 1)) $((STEP_LEN + 1)) $((STEP_LEN + 10))
