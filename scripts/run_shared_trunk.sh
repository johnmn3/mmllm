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

# Sparse-optimizer state. Defaults to sgd here because at N≥16 on a
# 15 GB box, both adam variants OOM mid-training as the per-row m/v
# state for V_local approaches 6.7 GB. SGD has zero state.
#
# Three options via MMLLM_SPARSE_OPT (caller-overridable):
#   adam-cpu (default here): mmllm.optim.CPUOffloadSparseAdam — touched-
#                            row-sparse m/v on host RAM; ~500 MB at
#                            spoon scale, scales with unique rows ×
#                            q_dim × 8 bytes × N. Safe at N≤8 on this box.
#                            REQUIRED for the recipe to actually train V:
#                            CPUSparseSGD's pure `index_add_(-lr * grad)`
#                            doesn't move V when lr * grad << init scale,
#                            which is the regime distill produces. With
#                            sgd, distill_loss fires every step but V_net
#                            stays at init (cos(V_final, V_seed) = 1.0,
#                            Δ_net ≈ noise). Adam normalizes per-row step
#                            magnitude → V actually moves → Δ_local goes
#                            from +0.0006 (sgd) to +1.68 (adam) at 100
#                            steps. See CLAUDE.md "Δ-ablation is NOT proof".
#   sgd:                     mmllm.optim.CPUSparseSGD — zero state.
#                            Fits at any N but cripples distillation as
#                            described above. ONLY use when adam-cpu OOMs
#                            (N>8 on a 15 GiB sandbox). Override with
#                            `MMLLM_SPARSE_OPT=sgd bash …`.
#   adam:                    stock torch.optim.SparseAdam (dense state).
#                            DON'T use at N>1 — guaranteed OOM.
export MMLLM_SPARSE_OPT="${MMLLM_SPARSE_OPT:-adam-cpu}"

# Spike-6 recipe (restored verbatim from run_asym_spoon.sh / round-10-2).
# SwitchGate + GATE_NET_DEFAULT (Bernoulli-Local, the round-9 fix for
# 3-way gate collapse), residual direction-only distill (the consolidator
# path), cosine LR schedules (Local wakes/cools, Net ramps up). DO NOT
# REMOVE INDIVIDUAL ENTRIES WITHOUT EXPLICIT AUTHORIZATION — each was
# added to fix a specific failure mode documented in docs/journal/.
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
# NetBank warm-start: copy Local's K_a/K_b into NetBank's first 2048 rows
# so retrieval geometry is bootstrapped instead of cold. Without this,
# Net's K_a/K_b stay random while Local trains, so Net retrieves at
# different addresses than Local — distill MSE pushes V_net at Net's
# rows, which don't align with Local's. V_net learns averaged Local
# content at random rows = diluted, Δ_net stays at noise.
#
# Previous setting `MMLLM_SKIP_NETBANK_WARMSTART=true` was a round-7
# carry-over for harvester-seeded runs (where externally-loaded V_net
# would be clobbered by the warm-start). For fresh starts there's
# nothing to clobber, so default to enabled. Set explicitly to "true"
# only when the run seeds V_net from a harvester output.
export MMLLM_SKIP_NETBANK_WARMSTART="${MMLLM_SKIP_NETBANK_WARMSTART:-false}"
export MMLLM_NET_V_WARMSTART_FROM_LOCAL="${MMLLM_NET_V_WARMSTART_FROM_LOCAL:-true}"
# Ablation policy: end-only by default (ABLATE_EVERY=0 disables mid-
# training ablations; the end-of-train ablation in train-long still
# fires unconditionally). Caller can override by exporting the env var
# before invoking — useful when you want trajectory data, e.g.
#   MMLLM_ABLATE_EVERY=25 bash scripts/run_shared_trunk.sh 16 1 100
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-0}"
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
# Don't seed an empty opt-sparse-net.pt at step-1 — train-long's NetBank
# warm-start gate fires only when (start-step == 0) OR (the step-N/opt-
# sparse-net.pt file doesn't exist). Seeding an empty {} satisfied the
# existence check and blocked warm-start, leaving Net's K_a/K_b random
# while Local's trained — distill couldn't transfer because retrieval
# addresses didn't align. Absence triggers warm-start; opt-sparse-net
# state initializes fresh either way (load-checkpoint warns 'param_groups'
# missing and falls back to fresh state).

# Bank init: per-trunk V_local files sized (N_TRUNKS * sqrt_n² , q_dim),
# per-layer V_net files sized (sqrt_n_net² , c_net). Local files contain
# N_TRUNKS contiguous slices laid out (trunk0_rows, trunk1_rows, …).
#
# Gaussian-init (scale 0.02) — matches mmllm.memory._mmap_value_tensor's
# default. Bug #3 of the 5 bank-engagement bugs (commit 85a507a's commit
# msg) was that zero-init makes ∂loss/∂V = 0 wherever V appears as a
# softmax-weighted sum — V can't bootstrap, banks stay near-zero, and
# ablation Δ_local stays at 0 regardless of how many steps we train.
# Small Gaussian gives V a real (if tiny) contribution at step 0 so the
# gradient signal can shape it from step 1.
python3 - "$BANK_BASE" "$N_TRUNKS" <<'PY'
import numpy as np, sys
bank_base = sys.argv[1]
n_trunks  = int(sys.argv[2])
SQRT_LOCAL = 226;  Q_DIM = 128
SQRT_NET   = 64;   C_NET = 32
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
n_per_trunk = SQRT_LOCAL * SQRT_LOCAL
local_n = n_trunks * n_per_trunk
INIT_SCALE = 0.02
rng = np.random.default_rng(42)
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(local_n, Q_DIM))
    CHUNK = 4096
    for s in range(0, local_n, CHUNK):
        e = min(s + CHUNK, local_n)
        a[s:e] = (rng.standard_normal((e - s, Q_DIM)) * INIT_SCALE).astype(np.float32)
    a.flush()
for i in range(32):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+",
                  shape=(SQRT_NET * SQRT_NET, C_NET))
    a[:] = (rng.standard_normal(a.shape) * INIT_SCALE).astype(np.float32)
    a.flush()
print(f"  banks gaussian-init'd (scale={INIT_SCALE}): 8 V_local × {n_trunks} trunks, 32 V_net")
PY

# train-fim args: total-steps eval-every ckpt-every
# When MMLLM_ABLATE_EVERY is set > 0, also set eval-every to the same
# cadence so the per-step ablation block (which gates on
# `pos? ablate-every` AND `zero? (mod step eval-every)`) actually fires.
# Otherwise both are set > STEPS so only the end-of-train ablation runs.
if [ "${MMLLM_ABLATE_EVERY:-0}" -gt 0 ]; then
  EVAL_EVERY=$MMLLM_ABLATE_EVERY
else
  EVAL_EVERY=$((STEP_LEN + 1))
fi
mmllm train-fim "$FIM_BASE" "$BANK_BASE" $((STEP_LEN + 1)) $EVAL_EVERY $((STEP_LEN + 10))
