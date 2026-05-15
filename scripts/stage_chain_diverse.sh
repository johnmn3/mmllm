#!/usr/bin/env bash
# stage_chain_diverse.sh — copy the dispatcher's current reference state
# into /tmp/mmllm-cpu/chain-diverse/round-${ROUND}/ so run_chain_diverse.sh
# can pick it up as the chain's starting round.
#
# Two modes:
#   bash stage_chain_diverse.sh           # no arg: follow workers/dispatcher/current/
#                                          symlink (the latest harvest's round dir)
#   bash stage_chain_diverse.sh <round>   # explicit: harvest-*way-r<round>/round-<round>/
#
# Idempotent — skips if destination already populated.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

if [ -z "${1:-}" ]; then
  CURRENT="workers/dispatcher/current"
  if [ ! -L "$CURRENT" ] && [ ! -d "$CURRENT" ]; then
    echo "ERROR: no round arg given and workers/dispatcher/current/ doesn't exist." >&2
    echo "       Either pass a round number or pull the dispatcher branch which" >&2
    echo "       maintains the symlink." >&2
    exit 2
  fi
  SRC=$(readlink -f "$CURRENT")
  # Wave-agnostic mode: stage the reference as round-0/ regardless of the
  # source's absolute round number. extend_chain.sh then trains round-1
  # through round-10, so the worker's chat outputs and log files use
  # wave-relative numbering ("Round 1 done", "Round 2 done", …) instead
  # of leaking the dispatcher's absolute wave counter.
  ROUND=0
  echo "  using dispatcher current → $SRC (wave-relative round-0)"
else
  ROUND="$1"
  SRC=$(ls -d workers/dispatcher/harvest-*way-r${ROUND}/round-${ROUND} \
              workers/dispatcher/harvest-cooked-r${ROUND}/round-${ROUND} 2>/dev/null | head -1)
  if [ -z "$SRC" ] || [ ! -d "$SRC" ]; then
    echo "ERROR: no source dir matching workers/dispatcher/harvest-*-r${ROUND}/round-${ROUND}/" >&2
    exit 2
  fi
fi

DST="/tmp/mmllm-cpu/chain-diverse/round-${ROUND}"

n_src=$(ls -1 "$SRC" 2>/dev/null | wc -l)
# Layout 1: 34 files (legacy single-file opt-sparse-net.pt, R20-R90 era)
# Layout 2: 66 files (chunked opt-sparse-net + meta, R91+ design-banks era)
if [ "$n_src" -lt 34 ]; then
  echo "ERROR: $SRC has $n_src files; expected ≥34 (32× V_net + dense.pt + opt-state)" >&2
  exit 2
fi

mkdir -p "$DST"
n_dst=$(ls -1 "$DST" 2>/dev/null | wc -l)
if [ "$n_dst" -ge "$n_src" ]; then
  echo "[skip] $DST already populated with $n_dst files"
else
  echo "  copying $SRC → $DST ($n_src files)…"
  cp "$SRC"/* "$DST"/
  echo "  done: $(ls -1 $DST | wc -l) files, $(du -sh $DST | awk '{print $1}')"
fi
