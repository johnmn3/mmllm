#!/usr/bin/env bash
# stage_chain_diverse.sh — copy the dispatcher's harvested round-${ROUND}
# state into /tmp/mmllm-cpu/chain-diverse/round-${ROUND}/ so
# run_chain_diverse.sh can pick it up as the chain's starting round.
#
# Replaces the per-round stage_chain_diverse_round{20,30,40,...}.sh
# scripts. Auto-discovers the source at:
#   workers/dispatcher/harvest-*way-r${ROUND}/round-${ROUND}/
#
# Idempotent — skips if destination already populated with 34 files.
#
# Usage:  bash scripts/stage_chain_diverse.sh <round>

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

ROUND="${1:?round number required (e.g. 40 or 50)}"
DST="/tmp/mmllm-cpu/chain-diverse/round-${ROUND}"

# Find source dir: workers/dispatcher/harvest-{N}way-r${ROUND}/round-${ROUND}/
SRC=$(ls -d workers/dispatcher/harvest-*way-r${ROUND}/round-${ROUND} 2>/dev/null | head -1)
if [ -z "$SRC" ] || [ ! -d "$SRC" ]; then
  echo "ERROR: no source dir matching workers/dispatcher/harvest-*way-r${ROUND}/round-${ROUND}/" >&2
  echo "       pull origin/claude/fim-training-cycle-T3giJ and confirm the files are present." >&2
  exit 2
fi

n_src=$(ls -1 "$SRC" 2>/dev/null | wc -l)
if [ "$n_src" -ne 34 ]; then
  echo "ERROR: $SRC has $n_src files; expected 34 (32× V_net + dense.pt + opt-sparse-net.pt)" >&2
  exit 2
fi

mkdir -p "$DST"
n_dst=$(ls -1 "$DST" 2>/dev/null | wc -l)
if [ "$n_dst" -eq 34 ]; then
  echo "[skip] $DST already populated with 34 files"
else
  echo "  copying $SRC → $DST …"
  cp "$SRC"/* "$DST"/
  echo "  done: $(ls -1 $DST | wc -l) files, $(du -sh $DST | awk '{print $1}')"
fi
