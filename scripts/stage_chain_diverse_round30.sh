#!/usr/bin/env bash
# stage_chain_diverse_round30.sh — copy the published harvested-round-30
# state from the repo into /tmp/mmllm-cpu/chain-diverse/round-30/ so
# run_chain_diverse.sh can pick it up as the chain's starting round.
#
# Source: workers/dispatcher/harvest-5way-r30/round-30/ (15 MB, 32 V_net
# layers + dense.pt + opt-sparse-net.pt). This is the 5-way FedAvg of
# the 5 second-wave workers' chain-diverse round-30 endpoints; on the
# 7-dataset battery it beats the R20 harvest by -22% OOD mean bpc (and
# -3% on Glaive itself).
#
# Idempotent — skips if destination already populated with 34 files.
#
# Usage:  bash scripts/stage_chain_diverse_round30.sh

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

SRC="workers/dispatcher/harvest-5way-r30/round-30"
DST="/tmp/mmllm-cpu/chain-diverse/round-30"

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
