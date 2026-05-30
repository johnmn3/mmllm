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
: ${MMLLM_DEVICE:=cpu} ; export MMLLM_DEVICE              # honor a pre-set device (e.g. mps)
: ${MMLLM_BANK_ON_GPU:=false} ; export MMLLM_BANK_ON_GPU  # on GPU, set true to keep bank V
: ${MMLLM_NET_BANK_ON_GPU:=false} ; export MMLLM_NET_BANK_ON_GPU  # on-device (avoid CPU↔GPU hop)
# Knobs below are wave defaults but can be overridden by passing the env
# var BEFORE invoking this script. Birds with constrained RAM (15-16 GB
# containers) typically lower MMLLM_BATCH and SUB_TOP_K to fit; see
# comments next to each knob for the memory math.
#
# Local Bank sized so each router is 1 MB:
#   per-router V: sqrt_local² × q_dim × 4B = 128² × 16 × 4 = 1.05 MB
#   16 routers / local bank = 16 MB per layer
#   8 local banks in training = 128 MB total (≈ designed 100 MB)
: ${MMLLM_SQRT_N:=128}        ; export MMLLM_SQRT_N
# NetBank sized for ~1 GB total across 32 layers:
#   per layer: sqrt_n² × c_net × 4B = 1024² × 8 × 4 = 33.5 MB
#   32 layers = 1.07 GB total (= designed 1 GB)
: ${MMLLM_NET_SQRT_N:=1024}   ; export MMLLM_NET_SQRT_N
: ${MMLLM_NET_C_NET:=8}       ; export MMLLM_NET_C_NET
# Retrieval bandwidth — 8× the original cpu-mini defaults. Size-neutral
# (no bank-size impact). Total info pulled per query (fp32):
#   Local: memory-top-k × q_dim = 128 × 16  = 2048
#   Net:   net-top-k × c_net    = 512 × 8   = 4096
# = 6144 fp32 per query, comparable to ~3 Gemma attention heads worth
# of per-token bandwidth.
#
# RAM cost: the per-block activation snapshot at effective batch
# N_TRUNKS×MMLLM_BATCH=16 (with current defaults) and full bandwidth
# is ~450 MB × 32 layers ≈ 14 GB without gradient checkpointing.
# MMLLM_GRAD_CHECKPOINT=true (set below) drops each block's
# intermediates after the block returns and recomputes them during
# backward — fits the recipe in ~24 GB containers. Tight (<= 16 GB)
# containers may still OOM during backward at this bandwidth; they
# need either smaller NET_TOP_K (recipe change) or further refactor.
: ${MMLLM_MEMORY_TOP_K:=128}     ; export MMLLM_MEMORY_TOP_K
# SUB_TOP_K bounds: sub² must be ≥ TOP_K (topk picks top-K from sub²
# elements). At MEMORY_TOP_K=128, sub_min = ceil(sqrt(128)) = 12; at
# NET_TOP_K=512, sub_min = ceil(sqrt(512)) = 23. Using sub=24 keeps both
# legal and cuts the materialized outer-sum tensor from 1 GB to 36 MB
# per local layer (vs the old default 128 → sub²=16384, where the
# (B×T×sub²×4B) tensor was the dominant per-layer activation at full
# wave-2 batch). The C++ PKMFusedTopK kernel (enabled below) skips
# this temp entirely on the Local PKM path; NetBank has no equivalent
# kernel yet, so its sub_top_k value still matters there.
: ${MMLLM_MEMORY_SUB_TOP_K:=24}  ; export MMLLM_MEMORY_SUB_TOP_K
: ${MMLLM_NET_TOP_K:=512}        ; export MMLLM_NET_TOP_K
: ${MMLLM_NET_SUB_TOP_K:=24}     ; export MMLLM_NET_SUB_TOP_K
# Enable the C++ PKM kernel for the Local PKM path. The kernel does
# fused outer-sum + top-K with a per-row min-heap, skipping the
# (B, T, sub²) materialization that's the Local PKM's biggest single
# activation tensor at training time. CLAUDE.md flagged 0% wall
# speedup at cpu-mini × the old wave-1 recipe — but at wave-2's
# higher bandwidth (and especially at higher MMLLM_MEMORY_SUB_TOP_K
# values, where the temp grows quadratically), the memory benefit is
# substantial. Bit-exact vs Python path (modulo top-K ties).
: ${MMLLM_ENABLE_PKM_CPP:=true}  ; export MMLLM_ENABLE_PKM_CPP
# N_TRUNKS is a misnomer — these are the 16 ROUTERS per Local Bank
# layer (1 MB each × 16 = 16 MB; CLAUDE.md "16 routers per local bank").
# The dense backbone is a SINGLE shared trunk; only the env var is
# misnamed. Renaming requires a coordinated change across core.lpy +
# scripts + ckpt manifests, deferred.
: ${MMLLM_N_TRUNKS:=16}          ; export MMLLM_N_TRUNKS
: ${MMLLM_SPARSE_OPT:=adam-cpu}  ; export MMLLM_SPARSE_OPT
# MMLLM_BATCH is per-ROUTER. Effective training batch is
# MMLLM_N_TRUNKS × MMLLM_BATCH (i.e. 16 × 1 = 16 here). The wave-2
# commit 7e45963 bumped this 1→16 thinking it controlled total batch;
# that produced an effective batch of 256, which combined with the 8×
# bandwidth bump from the same commit needed ~32 GB peak RAM. The
# wave-1 effective batch of 16 already came from MMLLM_BATCH=1 ×
# N_TRUNKS=16, so this default reverts to that.
: ${MMLLM_BATCH:=1}              ; export MMLLM_BATCH
: ${MMLLM_NETBANK_ENABLED:=true} ; export MMLLM_NETBANK_ENABLED
: ${MMLLM_LONG_TIER_MIX:=switch} ; export MMLLM_LONG_TIER_MIX
: ${MMLLM_ALPHA_NET:=true}       ; export MMLLM_ALPHA_NET
: ${MMLLM_GATE_NET_DEFAULT:=true}; export MMLLM_GATE_NET_DEFAULT
: ${MMLLM_DISTILL_COEF:=0.5}     ; export MMLLM_DISTILL_COEF
: ${MMLLM_DISTILL_COEF_END:=5.0} ; export MMLLM_DISTILL_COEF_END
: ${MMLLM_DISTILL_TARGET:=residual}      ; export MMLLM_DISTILL_TARGET
# Distill loss FORM: full magnitude-aware MSE (round-9's proven-consolidating
# form). The broken form was direction-only + magnitude_coef=1.0, which zeroes
# the direction term (the docstring itself notes it "broke the consolidation
# transfer") — a key reason birds stopped consolidating.
#
# FORCED (=, not :=) on the prod cron path so a stray runner/Actions env var
# cannot silently flip the chain back to the broken magnitude-only form and
# de-consolidate every fork. DIRECTION_ONLY is the decisive knob: when false,
# the distill is plain MSE(net, target) and MAGNITUDE_COEF is ignored entirely
# (attention_kernel._compute_block_distill_inline / collect-distill-loss).
# Experiment scripts set these directly and don't route through extend_chain.
export MMLLM_DISTILL_DIRECTION_ONLY=false
export MMLLM_DISTILL_MAGNITUDE_COEF=0.0
export MMLLM_DISTILL_MAGNITUDE_COEF_END=0.0
: ${MMLLM_DISTILL_MAGNITUDE_CLAMP:=10.0} ; export MMLLM_DISTILL_MAGNITUDE_CLAMP
: ${MMLLM_LR_BANK_MULT:=3.0}     ; export MMLLM_LR_BANK_MULT
: ${MMLLM_LR_BANK_MULT_END:=0.001}; export MMLLM_LR_BANK_MULT_END
: ${MMLLM_LR_NET_MULT:=0.001}    ; export MMLLM_LR_NET_MULT
: ${MMLLM_LR_NET_MULT_END:=5.0}  ; export MMLLM_LR_NET_MULT_END
: ${MMLLM_LR_DENSE_MULT:=0.05}   ; export MMLLM_LR_DENSE_MULT
: ${MMLLM_LR_DENSE_MULT_END:=0.005}; export MMLLM_LR_DENSE_MULT_END
# Base LR for chain extensions. Stays at 3e-2 (stack-3e-2-5.0).
#
# History (2026-05-25): commit 5c5f9b7 flipped this to 1e-1 based on
# a SINGLE-bird spike (U59yk r115-r119) that showed mean Δ_net=+0.0159
# while running OFF an LR=3e-2 chain head. Once the prod cron ran a
# full harvest at 1e-1, the dynamics inverted:
#
#   harvest | LR    | best ctrl_bpc | mean Δ_net/round
#   r119    | 3e-2  | 0.9135        | +0.0098
#   r121    | 3e-2  | 0.9290        | +0.0117
#   r124    | 1e-1  | 1.3377        | +0.0025    ← regression
#
# ctrl_bpc jumped +0.40 (44%) and Δ_net dropped 4-5× vs the prior
# LR=3e-2 wave. The spike's "consolidation cost is ~40% ctrl_bpc"
# claim was the warning the prod data confirmed — but the spike's
# *Δ_net gain* didn't carry over to multi-bird FedAvg. Best read:
# at the higher LR each bird drifts further from the harvested basis
# faster than distillation can re-anchor V_net, so the row-aware
# FedAvg sees per-row variance that destroys Net's accumulated signal.
#
# The CLAUDE.md "stack-1e-1-5.0" recipe is still valid for SINGLE-bird
# consolidation rounds (e.g. the very last spork before packaging an
# inference checkpoint). It is NOT the cron-prod default for an
# ongoing federated chain. Workers can opt into it manually via the
# train.yml `lr` workflow_dispatch input.
: ${MMLLM_LR:=3e-2}              ; export MMLLM_LR
: ${MMLLM_LR_MIN:=3e-2}          ; export MMLLM_LR_MIN
: ${MMLLM_LR_WARMUP:=$((STEPS * 70 / 100))} ; export MMLLM_LR_WARMUP
: ${MMLLM_REPLAY_EVERY:=10}      ; export MMLLM_REPLAY_EVERY
: ${MMLLM_REPLAY_BUFFER_SIZE:=256}; export MMLLM_REPLAY_BUFFER_SIZE
: ${MMLLM_REPLAY_THRESHOLD:=0.5} ; export MMLLM_REPLAY_THRESHOLD
: ${MMLLM_ABLATE_EVERY:=0}       ; export MMLLM_ABLATE_EVERY
: ${MMLLM_SKIP_NETBANK_WARMSTART:=true}; export MMLLM_SKIP_NETBANK_WARMSTART     # extending — V_net is carried forward; don't re-warm
# One-shot K_a/K_b realignment knobs. TEMPORARILY DEFAULT-ON to break
# the wave-2 random-K_a/K_b cycle (Net's keys started random at chain
# genesis; gate-suppression has kept them from realigning; Δ_net stays
# at +0.005-+0.012 per round regardless of STEPS depth). The harvest
# cycle will spread the realigned keys across every fork's next round.
#
# Plan: leave default-on for ~1-3 cron ticks, watch Δ_net on the
# resulting birds. If Δ_net jumps to >+0.04 the hypothesis is
# confirmed; consider keeping K_ALIGN_COEF on (>0) for ongoing
# pressure but flip REWARM_NETBANK_KEYS back to false (one-shot kick
# done, don't re-clobber each round).
#
# REWARM_NETBANK_KEYS / K_ALIGN_COEF: BOTH DEFAULT OFF.
#   Verified regression vector (sweep 2026-05-24): when chain rounds
#   give Net time to train into its K_a/K_b commitments (STEPS≥7 ×
#   N_ROUNDS≥5), the per-round K_a/K_b rewarm shocks orphan V_net's
#   learned content (rows are now indexed at addresses that don't
#   match), and the k_align MSE pressure keeps pulling keys around
#   so V_net can never stabilize. Result: Δ_net flips NEGATIVE
#   (smoke #4 5×7 r88: −0.0067; Net actively harming output).
#   With both off, smoke #5 5×7 hit Δ_net = +0.0195, matching /
#   exceeding the pre-PR-#11 Jz1HH r66 era baseline (+0.0137).
#   Set true / 0.005 only at chain GENESIS when K_a/K_b legitimately
#   need aligning, never on extensions.
: ${MMLLM_REWARM_NETBANK_KEYS:=false} ; export MMLLM_REWARM_NETBANK_KEYS
: ${MMLLM_K_ALIGN_COEF:=0}            ; export MMLLM_K_ALIGN_COEF
# Per-block gradient checkpointing: drops each block's intermediates
# (NetBank latent, Local-PKM combined_scores, SDPA scratch) after the
# block returns and recomputes them during backward. ~30% wall hit,
# ~16-32× lower peak RAM. Without this, the wave-2 bandwidth recipe
# (NET_TOP_K=512, MEMORY_SUB_TOP_K=128) doesn't fit common containers
# — the 32-layer activation snapshot reaches ~36 GB at effective batch
# 16 and ~576 GB at the default effective batch of 256.
: ${MMLLM_GRAD_CHECKPOINT:=true} ; export MMLLM_GRAD_CHECKPOINT
export MMLLM_ABLATION_EVAL_CAP="${MMLLM_ABLATION_EVAL_CAP:-25000}"
unset MMLLM_LITE_CKPT
unset MMLLM_MAX_STEPS

FIM_BASE=/tmp/mmllm-cpu/fim-chain-stack
BANK_BASE=/tmp/mmllm-cpu/fim-bank-chain-stack

# SPIKE 2 — Local Bank layer positions. Default is the asymmetric 8 (CLAUDE.md
# "8 local banks in training"). Override via MMLLM_LOCAL_BANK_LAYERS env var
# (comma-separated layer indices, e.g. "0,1,2,...,31" for symmetric all-32).
# When overridden:
#   - the bash LOCAL_LAYERS array drives V_local.bin file generation here
#   - MMLLM_LOCAL_BANK_LAYERS is passed through to core.lpy's
#     pick-local-bank-layers, which honors the same env var
if [ -n "${MMLLM_LOCAL_BANK_LAYERS:-}" ]; then
  IFS=',' read -ra LOCAL_LAYERS <<< "$MMLLM_LOCAL_BANK_LAYERS"
  export MMLLM_LOCAL_BANK_LAYERS   # already set, but ensure it's exported
  echo "  SPIKE-2: MMLLM_LOCAL_BANK_LAYERS override active — ${#LOCAL_LAYERS[@]} layers: ${LOCAL_LAYERS[*]}"
else
  LOCAL_LAYERS=(0 1 2 12 20 29 30 31)
fi
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

  # Pass the LOCAL_LAYERS bash array to the python heredoc via a
  # space-separated env var so spike-2's override propagates cleanly.
  export MMLLM_BASH_LOCAL_LAYERS="${LOCAL_LAYERS[*]}"
  python3 - "${BANK_BASE}" "16" <<PY
import numpy as np, sys, os
bank_base = sys.argv[1]
n_trunks  = int(sys.argv[2])
SQRT_LOCAL = $SQRT_LOCAL;  Q_DIM = $Q_DIM
LOCAL_LAYERS = [int(x) for x in os.environ.get("MMLLM_BASH_LOCAL_LAYERS",
                                               "0 1 2 12 20 29 30 31").split()]
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
  echo "  V_local: Gaussian σ=$INIT_SCALE fresh (${#LOCAL_LAYERS[@]} layers)"

  for i in $NET_LAYERS; do
    cp "${resume_v_net}.${i}.bin" "${BANK_BASE}-net.${i}.bin"
  done
  echo "  V_net: carried forward from $(basename $(dirname $resume_v_net))"

  echo "  → training $STEPS steps (LR=$MMLLM_LR, LR_NET_MULT_END=$MMLLM_LR_NET_MULT_END, mag_coef=$MMLLM_DISTILL_MAGNITUDE_COEF)…"
  local TRAIN_LOG="$ARCHIVE_ROOT/round-${round_num}.train.log"
  mmllm train-fim-mini "$FIM_BASE" "$BANK_BASE" \
        $((STEPS + 1)) "${MMLLM_EVAL_EVERY:-$((STEPS + 1))}" $((STEPS + 10)) > "$TRAIN_LOG" 2>&1 || true

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

  # Disk hygiene: once this round's log.jsonl exists, round-(N-2)'s
  # weights are no longer needed for resume (extend_chain.sh's resume
  # only reads from round-(N-1)). Strip its V_net/dense/opt-state files
  # but keep log.jsonl so the per-round table stays intact.
  #
  # At design banks, each round dir is ~1.4 GB. Without this prune, a
  # 10-round wave peaks at ~14 GB under /tmp/mmllm-cpu/chain-diverse/.
  # With it, peak is ~3 GB (round-(N-1) + round-N live) plus ~0.1 GB
  # of trailing logs+dense_skeletons across all completed rounds.
  local stale=$((round_num - 2))
  if [ "$stale" -ge 1 ]; then
    local STALE_DIR="$ARCHIVE_ROOT/round-${stale}"
    if [ -d "$STALE_DIR" ] && [ -f "$STALE_DIR/log.jsonl" ]; then
      rm -f "$STALE_DIR"/V_net.*.bin \
            "$STALE_DIR"/dense.pt \
            "$STALE_DIR"/opt-sparse-net.*.pt 2>/dev/null
    fi
  fi
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
