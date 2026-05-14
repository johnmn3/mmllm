#!/usr/bin/env bash
# extend_chain.sh — continue an existing chain archive by running
# N additional rounds. Reads dense.pt + V_net + opt-sparse-net from
# the latest existing round in the archive and chains forward.
#
# Usage:  bash scripts/extend_chain.sh <archive_dir> <N_MORE> [STEPS]

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

ARCHIVE_ROOT="${1:?archive dir required}"
N_MORE="${2:-2}"
STEPS="${3:-100}"

if [ ! -d "$ARCHIVE_ROOT" ]; then
  echo "ERROR: $ARCHIVE_ROOT does not exist" >&2
  exit 2
fi

# Find the highest existing round. Trailing slash restricts to directories
# (otherwise round-N.train.log files would be matched and the round number
# parsed from them — which silently breaks the resume after a partial run).
START_FROM=$(ls -1d "$ARCHIVE_ROOT"/round-*/ 2>/dev/null | grep -oE 'round-[0-9]+' | grep -oE '[0-9]+' | sort -n | tail -1)
if [ -z "$START_FROM" ]; then
  echo "ERROR: no round-N dirs in $ARCHIVE_ROOT" >&2
  exit 2
fi
END_AT=$((START_FROM + N_MORE))

echo "═══════════════════════════════════════════════════════════════"
echo "  EXTEND CHAIN: archive=$ARCHIVE_ROOT"
echo "  continuing from round $START_FROM → $END_AT  (N_MORE=$N_MORE)"
echo "  steps/round=$STEPS"
echo "═══════════════════════════════════════════════════════════════"

# Recipe — must match the original chain.
#
# ┌──────────────────────────────────────────────────────────┐
# │  DESIGNED BANK SIZES — stamped here so I don't forget    │
# │    NetBank V_net   total          1 GB    (~32 MB/layer)  │
# │    Local Bank V_loc total       100 MB                   │
# │    Routers (16)    each           1 MB                   │
# │  Net > Local. Net is the DURABLE long-term memory.       │
# │  Anything that shrinks Net below 1 GB is a regression.   │
# └──────────────────────────────────────────────────────────┘
export MMLLM_DEVICE=cpu
export MMLLM_BANK_ON_GPU=false
export MMLLM_NET_BANK_ON_GPU=false
# Local Bank sized so each router is 1 MB:
#   per-router V: sqrt_local² × q_dim × 4B = 128² × 16 × 4 = 1.05 MB
#   16 routers / local bank = 16 MB per layer
#   8 local banks in training = 128 MB total (≈ designed 100 MB)
export MMLLM_SQRT_N=128
# NetBank sized for ~1 GB total across 32 layers:
#   per layer: sqrt_n² × c_net × 4B = 1024² × 8 × 4 = 33.5 MB
#   32 layers = 1.07 GB total (= designed 1 GB)
export MMLLM_NET_SQRT_N=1024
export MMLLM_NET_C_NET=8
export MMLLM_MEMORY_TOP_K=16
export MMLLM_MEMORY_SUB_TOP_K=16
export MMLLM_NET_TOP_K=64
export MMLLM_NET_SUB_TOP_K=8
export MMLLM_N_TRUNKS=16
export MMLLM_SPARSE_OPT=adam-cpu
export MMLLM_BATCH=1
export MMLLM_NETBANK_ENABLED=true
export MMLLM_LONG_TIER_MIX=switch
export MMLLM_ALPHA_NET=true
export MMLLM_GATE_NET_DEFAULT=true
export MMLLM_DISTILL_COEF=0.5
export MMLLM_DISTILL_COEF_END=5.0
export MMLLM_DISTILL_TARGET=residual
export MMLLM_DISTILL_DIRECTION_ONLY=true
export MMLLM_DISTILL_MAGNITUDE_COEF=1.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=1.0
export MMLLM_DISTILL_MAGNITUDE_CLAMP=10.0
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
export MMLLM_SKIP_NETBANK_WARMSTART=true     # extending — V_net is carried forward; don't re-warm
export MMLLM_ABLATION_EVAL_CAP="${MMLLM_ABLATION_EVAL_CAP:-25000}"
unset MMLLM_LITE_CKPT
unset MMLLM_MAX_STEPS

FIM_BASE=/tmp/mmllm-cpu/fim-chain-stack
BANK_BASE=/tmp/mmllm-cpu/fim-bank-chain-stack

LOCAL_LAYERS=(0 1 2 12 20 29 30 31)
NET_LAYERS=$(seq 0 31)
SQRT_LOCAL=128;  Q_DIM=16
SQRT_NET=1024;   C_NET=8
INIT_SCALE=0.02

mkdir -p "$(dirname $FIM_BASE)"
for split in train val test; do
  ln -sf "$(readlink -f /tmp/mmllm-cpu/fim-json-v3.${split}.bin)" \
         "${FIM_BASE}.${split}.bin" 2>/dev/null || true
done

run_round() {
  local round_num=$1
  local resume_dense=$2
  local resume_v_net=$3
  local resume_opt_net=$4    # path to single-file opt-sparse-net.pt, OR
                             # path to dir containing opt-sparse-net.meta.pt
                             # + opt-sparse-net.<i>.pt chunks (see below).

  echo ""
  echo "── ROUND $round_num ─────────────────────────────────────────"
  local t0=$(date +%s)

  rm -rf "${FIM_BASE}.ckpts" "${FIM_BASE}.log.jsonl"
  rm -f  "${BANK_BASE}".*.bin "${BANK_BASE}"-net.*.bin
  mkdir -p "${FIM_BASE}.ckpts/step-1"
  cp "$resume_dense" "${FIM_BASE}.ckpts/step-1/dense.pt"
  echo 1 > "${FIM_BASE}.ckpts/step-1/step.txt"
  # opt-sparse-net resume: at design-sized V_net the file is ~230 MB
  # which exceeds GitHub's 100 MB per-file limit. We split per-layer
  # (32 chunks × 2-13 MB) for publish + harvest, and merge on resume.
  # Legacy single-file is still accepted for back-compat.
  if [ -d "$resume_opt_net" ] && [ -f "$resume_opt_net/opt-sparse-net.meta.pt" ]; then
    python3 scripts/_opt_sparse_net_chunk.py merge \
      "$resume_opt_net" "${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt"
  elif [ -f "$resume_opt_net" ]; then
    cp "$resume_opt_net" "${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt"
  else
    python3 -c "import torch; torch.save({}, '${FIM_BASE}.ckpts/step-1/opt-sparse-net.pt')"
  fi

  python3 - "${BANK_BASE}" "16" <<PY
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
  echo "  V_local: Gaussian σ=$INIT_SCALE fresh"

  for i in $NET_LAYERS; do
    cp "${resume_v_net}.${i}.bin" "${BANK_BASE}-net.${i}.bin"
  done
  echo "  V_net: carried forward from $(basename $(dirname $resume_v_net))"

  echo "  → training $STEPS steps (LR=$MMLLM_LR, LR_NET_MULT_END=$MMLLM_LR_NET_MULT_END, mag_coef=$MMLLM_DISTILL_MAGNITUDE_COEF)…"
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
  # Split opt-sparse-net.pt into per-layer chunks so the round dir is
  # publishable under GitHub's 100 MB/file limit. The chunked layout is
  # what the next-round resume + harvest_chain.py expect.
  if [ -f "$LATEST/opt-sparse-net.pt" ]; then
    python3 scripts/_opt_sparse_net_chunk.py split \
      "$LATEST/opt-sparse-net.pt" "$ROUND_DIR" 2>&1 | sed 's/^/    /'
  fi
  cp "${FIM_BASE}.log.jsonl"     "$ROUND_DIR/log.jsonl" 2>/dev/null || true

  echo "  ── round $round_num ablation summary (wall ${elapsed}s) ──"
  grep -A 4 "ablation summary" "$TRAIN_LOG" || echo "    (no ablation in log)"
  echo "$round_num $elapsed" >> "$ARCHIVE_ROOT/wall.tsv"
}

for r in $(seq $((START_FROM + 1)) $END_AT); do
  prev=$((r - 1))
  prev_dir="$ARCHIVE_ROOT/round-${prev}"
  # Prefer chunked opt-sparse-net.{i}.pt if present (the new format);
  # fall back to legacy single-file; else pass empty marker to trigger
  # fresh Adam moments in run_round.
  if [ -f "$prev_dir/opt-sparse-net.meta.pt" ]; then
    prev_opt_net="$prev_dir"          # dir → run_round merges chunks
  elif [ -f "$prev_dir/opt-sparse-net.pt" ]; then
    prev_opt_net="$prev_dir/opt-sparse-net.pt"
  else
    touch_file="$prev_dir/opt-sparse-net.empty.pt"
    python3 -c "import torch; torch.save({}, '$touch_file')"
    prev_opt_net="$touch_file"
  fi
  run_round "$r" \
    "$prev_dir/dense.pt" \
    "$prev_dir/V_net" \
    "$prev_opt_net"
done

# Updated summary across all rounds.
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  CHAIN SUMMARY (now $END_AT rounds total)"
echo "═══════════════════════════════════════════════════════════════"
echo "  archive: $ARCHIVE_ROOT"
echo ""
python3 - "$ARCHIVE_ROOT" "$END_AT" <<'PY'
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
                ctrl = ev.get("control_bpc"); dl = ev.get("delta_local")
                dn = ev.get("delta_net"); db = ev.get("delta_both")
                try:
                    dnv = float(dn) if dn not in (None, "null") else 0.0
                    syn = float(db) - (float(dl) + dnv)
                except: syn = None
    def fmt(v, w, p=4, sign=False):
        if v is None: return f"{'-':>{w}}"
        try:
            v = float(v); return f"{v:>+{w}.{p}f}" if sign else f"{v:>{w}.{p}f}"
        except: return f"{str(v):>{w}}"
    print(f"  {r:>5} {wall.get(r,'-'):>7} {fmt(ctrl,9)} {fmt(dl,9,sign=True)} "
          f"{fmt(dn,9,sign=True)} {fmt(db,9,sign=True)} {fmt(syn,9,sign=True)}")
PY
