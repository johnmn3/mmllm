#!/usr/bin/env bash
# stage_chain_diverse_round20.sh — copy the published harvested-round-20
# state from the repo into /tmp/mmllm-cpu/chain-diverse/round-20/ so
# run_chain_diverse.sh can pick it up as the chain's starting round.
#
# Source: workers/dispatcher/chain-diverse/round-20/ (15 MB, 32 V_net
# layers + dense.pt + opt-sparse-net.pt). This is the 5-way FedAvg of
# the 4 first-wave workers' round-20 endpoints (ctrl_bpc=1.1764).
#
# Idempotent — skips if destination already populated with 34 files.
#
# Usage:  bash scripts/stage_chain_diverse_round20.sh

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

SRC="workers/dispatcher/chain-diverse/round-20"
DST="/tmp/mmllm-cpu/chain-diverse/round-20"

if [ ! -d "$SRC" ]; then
  echo "ERROR: $SRC missing — pull the branch and confirm the files are present." >&2
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
