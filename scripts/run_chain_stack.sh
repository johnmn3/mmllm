#!/usr/bin/env bash
# run_chain_stack.sh — N rounds of cpu-MINI × N=16 trunks sporks
# back-to-back using the stack-3e-2-5.0 recipe (best-balance bank
# engagement from the sweep battery). Each round trains 100 steps,
# inheriting state from the previous as:
#
#   dense.pt        — carried forward (the ~2.4 MB shared router)
#   V_net           — carried forward (NetBank holds consolidated features)
#   V_local         — Gaussian-init fresh each round (sleep-wipe pattern)
#   opt-sparse-net  — round 1: missing → warm-start fires
#                     round 2+: carried forward so warm-start is blocked
#
# Architecture: shared-trunk Option A — ONE 2.4 MB dense router shared
# across 16 V_local slices (each slice 226² × 16 fp32 = ~3.3 MB per
# layer × 8 layers = ~26 MB per trunk of bank), plus one shared V_net
# (64² × 8 fp32 = 128 KB × 32 layers = 4 MB).
#
# Recipe per round (stack-3e-2-5.0 + LR_BANK_MULT=3 clamp):
#   MMLLM_SPARSE_OPT=adam-cpu
#   MMLLM_LR=3e-2, MMLLM_LR_MIN=3e-2
#   MMLLM_LR_BANK_MULT=3 (effective lr_b=0.09)
#   MMLLM_LR_NET_MULT_END=5.0
#   + spike-6 SwitchGate / distill / warmup
#
# Usage:  bash scripts/run_chain_stack.sh [N_ROUNDS] [STEPS]

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

N_ROUNDS="${1:-3}"
STEPS="${2:-100}"
N_TRUNKS="${MMLLM_N_TRUNKS:-16}"

# Recipe.
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
export MMLLM_SQRT_N=226
export MMLLM_NET_SQRT_N=64
export MMLLM_NET_C_NET=8                # cpu-mini
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_N_TRUNKS=$N_TRUNKS
export MMLLM_SPARSE_OPT=adam-cpu
export MMLLM_BATCH="${MMLLM_BATCH:-1}"  # per-trunk; B_eff = N_TRUNKS × 1 = 16
                                        # B=2 tested: 2.1× slower per step
                                        # at cpu-mini scale (bank top-K +
                                        # gather scale linearly with B,
                                        # amortization doesn't materialize).
                                        # Net tok/s slightly worse than B=1.
export MMLLM_ABLATION_EVAL_CAP="${MMLLM_ABLATION_EVAL_CAP:-25000}"
                                        # 25k tokens still gives 4dp on
                                        # Δ_net ~+0.17 (well above noise)
                                        # but takes 25% of the 100k cap's
                                        # wall time. Halves the
                                        # end-of-round ablation block.

export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_DISTILL_COEF=0.5
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_DISTILL_MAGNITUDE_COEF=1.0      # mag-coef-on winning knob from cpu-mini battery:
export MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0  # +9% Δ_net vs off. Banks have room at cpu-mini
export MMLLM_DISTILL_MAGNITUDE_CLAMP=10.0    # scale to grow their magnitude, not just direction.
export MMLLM_LR_BANK_MULT=3.0
export MMLLM_LR_BANK_MULT_END=0.001
export MMLLM_LR_NET_MULT=0.001
export MMLLM_LR_NET_MULT_END=5.0
export MMLLM_LR_DENSE_MULT=0.05
export MMLLM_LR_DENSE_MULT_END=0.005
export MMLLM_LR=3e-2
export MMLLM_LR_MIN=3e-2
export MMLLM_LR_WARMUP=$((STEPS * 70 / 100))
export MMLLM_REPLAY_EVERY=10
export MMLLM_REPLAY_BUFFER_SIZE=256
export MMLLM_REPLAY_THRESHOLD=0.5
export MMLLM_ABLATE_EVERY=0
unset MMLLM_LITE_CKPT
unset MMLLM_MAX_STEPS

FIM_BASE=/tmp/mmllm-cpu/fim-chain-stack
BANK_BASE=/tmp/mmllm-cpu/fim-bank-chain-stack
ARCHIVE_ROOT=/tmp/mmllm-cpu/chain-stack-$(date -u +%H%M)
mkdir -p "$ARCHIVE_ROOT"

LOCAL_LAYERS=(0 1 2 12 20 29 30 31)
NET_LAYERS=$(seq 0 31)
SQRT_LOCAL=226;  Q_DIM=16               # cpu-mini
SQRT_NET=64;     C_NET=8                # cpu-mini
INIT_SCALE=0.02

mkdir -p "$(dirname $FIM_BASE)"
for split in train val test; do
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.${split}.bin)" \
         "${FIM_BASE}.${split}.bin" 2>/dev/null || true
done

echo "═══════════════════════════════════════════════════════════════"
echo "  CHAIN (cpu-MINI, stack-3e-2-5.0)  rounds=$N_ROUNDS  N=$N_TRUNKS  steps=$STEPS/round"
echo "  recipe: adam-cpu + Gaussian init + warm-start + LR=3e-2 + LR_BANK_MULT=3 + LR_NET_MULT_END=5.0"
echo "  archive: $ARCHIVE_ROOT"
echo "═══════════════════════════════════════════════════════════════"

run_round() {
  local round_num=$1
  local resume_dense=$2     # path or "FRESH" (cpu-mini has no round-6 seed)
  local resume_v_net=$3     # path-prefix or "FRESH_WARMSTART"
  local resume_opt_net=$4   # path or "NONE" (NONE → warm-start fires)

  echo ""
  echo "── ROUND $round_num ─────────────────────────────────────────"
  local t0=$(date +%s)

  if [ "$resume_opt_net" = "NONE" ]; then
    export MMLLM_SKIP_NETBANK_WARMSTART=false
  else
    export MMLLM_SKIP_NETBANK_WARMSTART=true
  fi

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts"

  # Stage dense (rounds 2+ carry forward; round 1 starts cold for cpu-mini).
  if [ "$resume_dense" != "FRESH" ]; then
    mkdir -p "${FIM_BASE}.ckpts/step-1"
    cp "$resume_dense" "${FIM_BASE}.ckpts/step-1/dense.pt"
    echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
    if [ "$resume_opt_net" != "NONE" ]; then
      cp "$resume_opt_net" "${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt"
    fi
  fi

  # V_local: Gaussian-init fresh every round.
  python3 - "${BANK_BASE}" "${N_TRUNKS}" <<PY
import numpy as np, sys
bank_base = sys.argv[1]
n_trunks  = int(sys.argv[2])
SQRT_LOCAL = $SQRT_LOCAL;  Q_DIM = $Q_DIM
LOCAL_LAYERS = [0, 1, 2, 12, 20, 29, 30, 31]
INIT_SCALE = $INIT_SCALE
rng = np.random.default_rng(42 + ${round_num})
n_per_trunk = SQRT_LOCAL * SQRT_LOCAL
local_n = n_trunks * n_per_trunk
for i in LOCAL_LAYERS:
    a = np.memmap(f"{bank_base}.{i}.bin", dtype=np.float32, mode="w+", shape=(local_n, Q_DIM))
    CHUNK = 4096
    for s in range(0, local_n, CHUNK):
        e = min(s + CHUNK, local_n)
        a[s:e] = (rng.standard_normal((e - s, Q_DIM)) * INIT_SCALE).astype(np.float32)
    a.flush()
PY
  echo "  V_local: Gaussian σ=$INIT_SCALE fresh (8 layers × $N_TRUNKS trunks, q_dim=$Q_DIM)"

  # V_net: round 1 = Gaussian fresh + warm-start fires; rounds 2+ = carry forward.
  if [ "$resume_v_net" = "FRESH_WARMSTART" ]; then
    python3 - "${BANK_BASE}" <<PY
import numpy as np, sys
bank_base = sys.argv[1]
SQRT_NET = $SQRT_NET;  C_NET = $C_NET
INIT_SCALE = $INIT_SCALE
rng = np.random.default_rng(7)
for i in range(32):
    a = np.memmap(f"{bank_base}-net.{i}.bin", dtype=np.float32, mode="w+", shape=(SQRT_NET*SQRT_NET, C_NET))
    a[:] = (rng.standard_normal(a.shape) * INIT_SCALE).astype(np.float32)
    a.flush()
PY
    echo "  V_net: Gaussian σ=$INIT_SCALE fresh (warm-start will project Local into V_net)"
  else
    for i in $NET_LAYERS; do
      cp "${resume_v_net}.${i}.bin" "${BANK_BASE}-net.${i}.bin"
    done
    echo "  V_net: carried forward from $(basename $(dirname $resume_v_net))"
  fi

  echo "  → training $STEPS steps (LR=$MMLLM_LR, LR_NET_MULT_END=$MMLLM_LR_NET_MULT_END)…"
  local TRAIN_LOG="$ARCHIVE_ROOT/round-${round_num}.train.log"
  mmllm train-fim-mini "$FIM_BASE" "$BANK_BASE" \
        $((STEPS + 1)) $((STEPS + 1)) $((STEPS + 10)) > "$TRAIN_LOG" 2>&1 || true

  local elapsed=$(($(date +%s) - t0))

  local ROUND_DIR="$ARCHIVE_ROOT/round-${round_num}"
  mkdir -p "$ROUND_DIR"
  for i in $NET_LAYERS; do
    cp "${BANK_BASE}-net.${i}.bin" "$ROUND_DIR/V_net.${i}.bin"
  done
  local LATEST=$(ls -1d "${FIM_BASE}.ckpts/step-"* 2>/dev/null | grep -E "step-[0-9]+$" | sort -t- -k2 -n | tail -1)
  cp "$LATEST/dense.pt"          "$ROUND_DIR/dense.pt"
  if [ -f "$LATEST/opt-sparse-net.pt" ]; then
    cp "$LATEST/opt-sparse-net.pt" "$ROUND_DIR/opt-sparse-net.pt"
  fi
  cp "${FIM_BASE}.log.jsonl"     "$ROUND_DIR/log.jsonl" 2>/dev/null || true

  echo "  ── round $round_num ablation summary (wall ${elapsed}s) ──"
  grep -A 4 "ablation summary" "$TRAIN_LOG" || echo "    (no ablation in log)"
  echo "$round_num $elapsed" >> "$ARCHIVE_ROOT/wall.tsv"
}

# Round 1: dense FRESH (no round-6 seed for cpu-mini), V_net fresh (warm-start fires).
run_round 1 FRESH FRESH_WARMSTART NONE

# Rounds 2..N: carry dense + V_net + opt-sparse-net forward.
for r in $(seq 2 $N_ROUNDS); do
  prev=$((r - 1))
  prev_opt_net="$ARCHIVE_ROOT/round-${prev}/opt-sparse-net.pt"
  if [ ! -f "$prev_opt_net" ]; then
    touch_file="$ARCHIVE_ROOT/round-${prev}/opt-sparse-net.empty.pt"
    python3 -c "import torch; torch.save({}, '$touch_file')"
    prev_opt_net="$touch_file"
  fi
  run_round "$r" \
    "$ARCHIVE_ROOT/round-${prev}/dense.pt" \
    "$ARCHIVE_ROOT/round-${prev}/V_net" \
    "$prev_opt_net"
done

# Final summary table.
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  CHAIN SUMMARY (cpu-MINI stack-3e-2-5.0 × $N_ROUNDS rounds)"
echo "═══════════════════════════════════════════════════════════════"
echo "  archive: $ARCHIVE_ROOT"
echo ""
python3 - "$ARCHIVE_ROOT" "$N_ROUNDS" <<'PY'
import json, sys
from pathlib import Path
root = Path(sys.argv[1]); n = int(sys.argv[2])
print(f"  {'round':>5} {'wall_s':>7} {'ctrl_bpc':>9} {'Δ_local':>9} {'Δ_net':>9} {'Δ_both':>9} {'synergy':>9}")
wall = {}
if (root / "wall.tsv").exists():
    for line in (root / "wall.tsv").read_text().splitlines():
        r, s = line.split(); wall[int(r)] = int(s)
for r in range(1, n + 1):
    rd = root / f"round-{r}"
    log = rd / "log.jsonl"
    ctrl = dl = dn = db = syn = None
    if log.exists():
        for line in log.read_text().splitlines():
            try: ev = json.loads(line)
            except: continue
            if ev.get("event") == "ablation":
                ctrl = ev.get("control_bpc")
                dl = ev.get("delta_local")
                dn = ev.get("delta_net")
                db = ev.get("delta_both")
                try:
                    dnv = float(dn) if dn not in (None, "null") else 0.0
                    syn = float(db) - (float(dl) + dnv)
                except: syn = None
    def fmt(v, w, p=4, sign=False):
        if v is None: return f"{'-':>{w}}"
        try:
            v = float(v)
            return f"{v:>+{w}.{p}f}" if sign else f"{v:>{w}.{p}f}"
        except: return f"{str(v):>{w}}"
    print(f"  {r:>5} {wall.get(r,'-'):>7} {fmt(ctrl,9)} {fmt(dl,9,sign=True)} "
          f"{fmt(dn,9,sign=True)} {fmt(db,9,sign=True)} {fmt(syn,9,sign=True)}")
PY
