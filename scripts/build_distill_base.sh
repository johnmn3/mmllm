#!/usr/bin/env bash
# build_distill_base.sh — train cpu-tiny N=1 B=4 from scratch through
# step 70 (the end of the Local phase) and snapshot:
#   - ckpts/step-70/{dense.pt, opt-dense.pt, opt-sparse.pt, opt-sparse-net.pt}
#   - V_local mmap files (8 layers, trained)
#   - V_net mmap files (32 layers, post-warm-start)
# to ${MMLLM_DISTILL_BASE:-/tmp/mmllm-cpu/distill-base}/.
#
# The sweep launcher (scripts/sweep_distill.sh) then copies this snapshot
# into a fresh working dir and runs steps 70→100 with knob overrides.
# Each sweep is ~3 minutes (vs ~9 minutes building from step 0 each time).
#
# Schedule note: MMLLM_MAX_STEPS=70 stops the run at step 70 but the LR /
# distill cosines are evaluated against total-steps=101 — so the schedule
# state at step 70 is identical to step 70 of a full 100-step run. The
# resume from step 70 to 100 picks up exactly where the schedule left off.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

DISTILL_BASE="${MMLLM_DISTILL_BASE:-/tmp/mmllm-cpu/distill-base}"
WORK_FIM=/tmp/mmllm-cpu/fim-distill-build
WORK_BANK=/tmp/mmllm-cpu/fim-distill-build-bank

echo "═══════════════════════════════════════════════════════════════"
echo "  build_distill_base: cpu-tiny N=1 B=4, train 0→70, snapshot"
echo "  target: $DISTILL_BASE"
echo "═══════════════════════════════════════════════════════════════"

# --- Recipe (spike-6 verbatim except SPARSE_OPT default + warm-start enabled).
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=64
export MMLLM_NET_C_NET=32
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_N_TRUNKS=1
export MMLLM_SPARSE_OPT="${MMLLM_SPARSE_OPT:-adam-cpu}"
export MMLLM_BATCH=4

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
export MMLLM_LR_WARMUP=70
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_SKIP_NETBANK_WARMSTART="${MMLLM_SKIP_NETBANK_WARMSTART:-false}"
export MMLLM_NET_V_WARMSTART_FROM_LOCAL="${MMLLM_NET_V_WARMSTART_FROM_LOCAL:-true}"
export MMLLM_ABLATE_EVERY=0
# NB: LITE_CKPT NOT set — we need full opt state at step 70 so the sweep
# resume has Adam moments for opt-dense / opt-sparse / opt-sparse-net.
# Without these, the first ~5-10 sweep steps run with fresh Adam moments
# (effectively larger initial steps), which distorts the schedule
# continuity and Δ_net comparisons across sweeps.
export MMLLM_MAX_STEPS=70                   # ← the cap

ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000
mkdir -p "$(dirname $WORK_FIM)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${WORK_FIM}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)"   "${WORK_FIM}.val.bin"   2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)"  "${WORK_FIM}.test.bin"  2>/dev/null || true

# Fresh state.
rm -rf "${WORK_FIM}.ckpts" "${WORK_FIM}.log.jsonl"
rm -f  "${WORK_BANK}".*.bin "${WORK_BANK}"-net.*.bin
mkdir -p "${WORK_FIM}.ckpts/step-1"
cp "${ROUND6_BASE}/dense.pt" "${WORK_FIM}.ckpts/step-1/dense.pt"
echo 1 > "${WORK_FIM}.ckpts/step-1/step.txt"

# Gaussian-init banks (same recipe as run_shared_trunk.sh).
python3 - "$WORK_BANK" 1 <<'PY'
import numpy as np, sys
bank_base = sys.argv[1]
SQRT_LOCAL = 226;  Q_DIM = 128
SQRT_NET   = 64;   C_NET = 32
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
local_n = SQRT_LOCAL * SQRT_LOCAL
INIT_SCALE = 0.02
rng = np.random.default_rng(42)
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+", shape=(local_n, Q_DIM))
    CHUNK = 4096
    for s in range(0, local_n, CHUNK):
        e = min(s + CHUNK, local_n)
        a[s:e] = (rng.standard_normal((e - s, Q_DIM)) * INIT_SCALE).astype(np.float32)
    a.flush()
for i in range(32):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+", shape=(SQRT_NET*SQRT_NET, C_NET))
    a[:] = (rng.standard_normal(a.shape) * INIT_SCALE).astype(np.float32)
    a.flush()
print(f"  banks gaussian-init'd: 8 V_local × 1 trunks, 32 V_net")
PY

# Run with total-steps=101 (so the LR / distill schedule is calibrated for
# a 100-step run) but stop at step 70 via MMLLM_MAX_STEPS.
# Args: total-steps eval-every ckpt-every. EVAL_EVERY=101 (no mid-train
# eval); CKPT_EVERY=80 (no mid-train ckpt — the MAX_STEPS branch saves
# the step-70 ckpt explicitly on exit).
mmllm train-fim "$WORK_FIM" "$WORK_BANK" 101 101 80

# Snapshot to DISTILL_BASE.
echo "═══ snapshotting step-70 ckpt + banks → $DISTILL_BASE ═══"
rm -rf "$DISTILL_BASE"
mkdir -p "$DISTILL_BASE/ckpts" "$DISTILL_BASE/banks"
# Find the highest-step ckpt under WORK_FIM.ckpts (should be step-70).
last_ckpt=$(ls -d "${WORK_FIM}.ckpts"/step-* 2>/dev/null | grep -E "step-[0-9]+$" | sort -t- -k2 -n | tail -1)
echo "  source ckpt: $last_ckpt"
cp -r "$last_ckpt" "$DISTILL_BASE/ckpts/"
# Also bring the step-1 seed dir so resume can find dense.pt seed.
cp -r "${WORK_FIM}.ckpts/step-1" "$DISTILL_BASE/ckpts/"
# Bank files.
cp "${WORK_BANK}".*.bin     "$DISTILL_BASE/banks/" 2>/dev/null
cp "${WORK_BANK}"-net.*.bin "$DISTILL_BASE/banks/" 2>/dev/null

echo "  done. Sweep with: bash scripts/sweep_distill.sh <sweep-name> [env-overrides]"
echo "  snapshot layout:"
ls -la "$DISTILL_BASE/ckpts/" "$DISTILL_BASE/banks/" | head -20
