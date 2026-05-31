#!/usr/bin/env bash
# build_distill_base.sh — train cpu-MINI (d_model=32, ~2.4 MB shared
# dense router) × N=16 trunks from scratch through step 70 and
# snapshot the base for sweep iteration.
#
# Snapshot:
#   ckpts/step-70/{dense.pt, opt-dense.pt, opt-sparse.pt, opt-sparse-net.pt}
#   V_local mmap files (8 layers × N_TRUNKS slices, q_dim=16)
#   V_net mmap files (32 layers, c_net=8)
# to ${MMLLM_DISTILL_BASE:-/tmp/mmllm-cpu/distill-base}/.
#
# Schedule note: MMLLM_MAX_STEPS=70 stops at step 70 but the LR / distill
# cosines are evaluated against total-steps=101 — so the schedule state
# at step 70 is identical to step 70 of a full 100-step run.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

N_TRUNKS="${MMLLM_N_TRUNKS:-16}"
DISTILL_BASE="${MMLLM_DISTILL_BASE:-/tmp/mmllm-cpu/distill-base}"
WORK_FIM=/tmp/mmllm-cpu/fim-distill-build
WORK_BANK=/tmp/mmllm-cpu/fim-distill-build-bank

echo "═══════════════════════════════════════════════════════════════"
echo "  build_distill_base: cpu-MINI (d_model=32), N_TRUNKS=$N_TRUNKS, 0→70, snapshot"
echo "  target: $DISTILL_BASE"
echo "═══════════════════════════════════════════════════════════════"

# Recipe (stack-3e-2-5.0 + LR_BANK_MULT=3 clamp).
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=64
export MMLLM_NET_C_NET=8                # cpu-mini: c_net=8 (≤ q_dim=16)
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_N_TRUNKS=$N_TRUNKS
export MMLLM_SPARSE_OPT="${MMLLM_SPARSE_OPT:-adam-cpu}"
export MMLLM_BATCH=1                    # per-trunk; B_eff = N_TRUNKS × 1

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
export MMLLM_LR_BANK_MULT=3.0           # clamped from spike-6's 30 (see CLAUDE.md)
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=5.0
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-2
export MMLLM_LR_MIN=3e-2
export MMLLM_LR_WARMUP=70
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART="${MMLLM_SKIP_NETBANK_WARMSTART:-false}"
export MMLLM_NET_V_WARMSTART_FROM_LOCAL="${MMLLM_NET_V_WARMSTART_FROM_LOCAL:-true}"
export MMLLM_ABLATE_EVERY=0
export MMLLM_MAX_STEPS=70

mkdir -p "$(dirname $WORK_FIM)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${WORK_FIM}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)"   "${WORK_FIM}.val.bin"   2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)"  "${WORK_FIM}.test.bin"  2>/dev/null || true

# Fresh state. cpu-mini starts cold (round-6 dense.pt has different shape
# and can't seed cpu-mini); no step-1 dir.
rm -rf "${WORK_FIM}.ckpts" "${WORK_FIM}.log.jsonl"
rm -f  "${WORK_BANK}".*.bin "${WORK_BANK}"-net.*.bin
mkdir -p "${WORK_FIM}.ckpts"

# Gaussian-init banks at cpu-mini q_dim=16 + c_net=8.
python3 - "$WORK_BANK" "$N_TRUNKS" <<'PY'
import numpy as np, sys
bank_base = sys.argv[1]
n_trunks  = int(sys.argv[2])
SQRT_LOCAL = 226;  Q_DIM = 16          # cpu-mini
SQRT_NET   = 64;   C_NET = 8           # cpu-mini
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
print(f"  banks gaussian-init: 8 V_local × {n_trunks} trunks (q_dim=16), 32 V_net (c_net=8)")
PY

# train-fim-mini reads cpu-mini config. total-steps=101 calibrates the
# schedule for a 100-step run; MMLLM_MAX_STEPS=70 stops execution at
# step 70 (the new MAX_STEPS branch runs an ablation before exit).
mmllm train-fim-mini "$WORK_FIM" "$WORK_BANK" 101 101 110

# Snapshot.
echo "═══ snapshotting step-70 ckpt + banks → $DISTILL_BASE ═══"
rm -rf "$DISTILL_BASE"
mkdir -p "$DISTILL_BASE/ckpts" "$DISTILL_BASE/banks"
last_ckpt=$(ls -d "${WORK_FIM}.ckpts"/step-* 2>/dev/null | grep -E "step-[0-9]+$" | sort -t- -k2 -n | tail -1)
echo "  source ckpt: $last_ckpt"
cp -r "$last_ckpt" "$DISTILL_BASE/ckpts/"
cp "${WORK_BANK}".*.bin     "$DISTILL_BASE/banks/" 2>/dev/null
cp "${WORK_BANK}"-net.*.bin "$DISTILL_BASE/banks/" 2>/dev/null

echo "  done. Sweep with: bash scripts/sweep_distill.sh <name> [overrides]"
ls -la "$DISTILL_BASE/ckpts/" "$DISTILL_BASE/banks/" | head -10
