#!/usr/bin/env bash
# run_shared_trunk_mini.sh — shared-trunk training on the cpu-mini config
# (d_model=32, d_ff=128, q_dim=16). ~35× smaller dense trunk than
# cpu-tiny. Otherwise identical to run_shared_trunk.sh: spike-6 recipe
# verbatim with shared-trunk knobs (MMLLM_N_TRUNKS, MMLLM_BATCH=B/trunk,
# MMLLM_SPARSE_OPT=sgd by default) layered on top.
#
# Hypothesis being tested (per discussion):
#   With a dense trunk small enough that it CAN'T solve byte-level FIM
#   alone, the bank tier should be forced into adoption. Compare end-of-
#   train Δ_local against the cpu-tiny shared-trunk run.
#
# Usage:  bash scripts/run_shared_trunk_mini.sh <N_TRUNKS> [B_PER_TRUNK] [STEPS]

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

N_TRUNKS="${1:-4}"
B_PER_TRUNK="${2:-4}"
STEP_LEN="${3:-100}"

if [ "$N_TRUNKS" -lt 1 ] || [ "$N_TRUNKS" -gt 32 ]; then
  echo "N_TRUNKS must be 1-32, got $N_TRUNKS" >&2; exit 1
fi

echo "═══════════════════════════════════════════════════════════════"
echo "  Shared-trunk MINI: N_TRUNKS=$N_TRUNKS  B_PER_TRUNK=$B_PER_TRUNK"
echo "  steps=$STEP_LEN  cfg=cpu-mini (d_model=32, d_ff=128, q_dim=16)"
echo "  Effective batch: $((N_TRUNKS * B_PER_TRUNK)) rows per step"
echo "═══════════════════════════════════════════════════════════════"

# Asymmetric 32-layer arch with the mini trunk dims. Same Local Bank
# layer set as cpu-tiny; banks scale with q_dim=16 (1/8 of cpu-tiny).
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226                # V_local sqrt_n (rows)
export MMLLM_NET_SQRT_N=64             # V_net sqrt_n
export MMLLM_NET_C_NET=8               # NetBank bottleneck dim (≤ q_dim=16)
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8

# Shared-trunk knobs (the only additions on top of the spike-6 recipe).
export MMLLM_N_TRUNKS=$N_TRUNKS
export MMLLM_SPARSE_OPT="${MMLLM_SPARSE_OPT:-sgd}"
export MMLLM_BATCH=$B_PER_TRUNK

# Spike-6 recipe verbatim (DO NOT MODIFY — see run_shared_trunk.sh).
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
export MMLLM_ABLATE_EVERY="${MMLLM_ABLATE_EVERY:-0}"
export MMLLM_LITE_CKPT=true

FIM_BASE=/tmp/mmllm-cpu/fim-shared-trunk-mini
BANK_BASE=/tmp/mmllm-cpu/fim-bank-shared-trunk-mini
ROUND6_BASE=/home/user/mmllm/core/round-6/step-5000

mkdir -p "$(dirname $FIM_BASE)"
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.train.bin)" "${FIM_BASE}.train.bin" 2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.val.bin)"   "${FIM_BASE}.val.bin"   2>/dev/null || true
ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.test.bin)"  "${FIM_BASE}.test.bin"  2>/dev/null || true

rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
mkdir -p "${FIM_BASE}.ckpts"
# Don't seed a step-1 directory — cpu-mini's parameter shapes don't
# match round-6's dense.pt, so we have nothing to resume from. Empty
# ckpts/ → train-long starts at step 0 with fresh dense init.

# Bank init at q_dim=16 (cpu-mini's q_dim), per-trunk slices for V_local
# laid out (trunk0_rows, trunk1_rows, …). Zero-init matches the spike-6
# launcher pattern.
python3 - "$BANK_BASE" "$N_TRUNKS" <<'PY'
import numpy as np, sys
bank_base = sys.argv[1]
n_trunks  = int(sys.argv[2])
SQRT_LOCAL = 226;  Q_DIM = 16    # ← cpu-mini q_dim, not 128
SQRT_NET   = 64;   C_NET = 8     # ← cpu-mini NetBank c_net
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
print(f"  banks zero-init'd: 8 V_local × {n_trunks} trunks (q_dim=16), 32 V_net (c_net=8)")
PY

# train-fim-mini args: total-steps eval-every ckpt-every.
# Same MMLLM_ABLATE_EVERY-honoring logic as the cpu-tiny launcher.
if [ "${MMLLM_ABLATE_EVERY:-0}" -gt 0 ]; then
  EVAL_EVERY=$MMLLM_ABLATE_EVERY
else
  EVAL_EVERY=$((STEP_LEN + 1))
fi
mmllm train-fim-mini "$FIM_BASE" "$BANK_BASE" $((STEP_LEN + 1)) $EVAL_EVERY $((STEP_LEN + 10))
