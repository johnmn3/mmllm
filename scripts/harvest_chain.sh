#!/usr/bin/env bash
# harvest_chain.sh — end-to-end harvest of a chain-diverse wave.
#
# Usage:  bash scripts/harvest_chain.sh <target_round> [--no-push]
#
# Workflow:
#   1. discover all origin/claude/chaindiverse-*-r${TARGET} branches
#   2. fetch each (with retry)
#   3. extract per-worker artifacts to /tmp/mmllm-cpu/harvest-r${TARGET}/<handle>/
#   4. FedAvg V_net + dense (scripts/harvest_chain.py --publish)
#   5. stage to inf-spork-r${TARGET}.* (scripts/stage_inf_spork.py)
#   6. run 7-dataset battery (scripts/run_eval_battery.py, env-paramed)
#   7. generate results.md (scripts/generate_harvest_results.py)
#   8. generate next-round dispatch prompt (scripts/generate_dispatch_prompt.py)
#   9. commit + push to claude/fim-training-cycle-T3giJ
#
# Total wall: ~3-5 min for steps 1-3 (HTTP fetches), 10s for FedAvg,
# 2 min for battery, instant for results/dispatch generation.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

TARGET="${1:?target round required (e.g. 40 for harvesting R31-R40 wave)}"
PRIOR=$((TARGET - 10))
PUSH=true
[ "$2" = "--no-push" ] && PUSH=false

STAGE=/tmp/mmllm-cpu/harvest-r${TARGET}
DISPATCHER_BRANCH=$(git rev-parse --abbrev-ref HEAD)

echo "═══════════════════════════════════════════════════════════════"
echo "  HARVEST CHAIN: target round ${TARGET} (prior harvest at r${PRIOR})"
echo "  dispatcher branch: ${DISPATCHER_BRANCH}"
echo "  push at end: ${PUSH}"
echo "═══════════════════════════════════════════════════════════════"

# 1. Discover worker branches.
echo ""
echo "── 1. discovering worker branches matching claude/chaindiverse-*-r${TARGET} ──"
git fetch origin --prune 2>/dev/null || true
WORKER_BRANCHES=$(git branch -r 2>&1 \
  | grep -oE "origin/claude/chaindiverse-[^[:space:]]+-r${TARGET}\$" | sort)
if [ -z "$WORKER_BRANCHES" ]; then
  echo "ERROR: no remote branches matching origin/claude/chaindiverse-*-r${TARGET}" >&2
  exit 2
fi
WORKERS=$(echo "$WORKER_BRANCHES" | sed -E "s|origin/claude/chaindiverse-(.+)-r${TARGET}|\1|")
N_WORKERS=$(echo "$WORKERS" | wc -l)
echo "  found ${N_WORKERS} workers:"
echo "$WORKERS" | sed 's/^/    - /'

# 2. Fetch each branch with retry.
echo ""
echo "── 2. fetching ${N_WORKERS} worker branches (with retry) ──"
mkdir -p "$STAGE"
echo "$WORKERS" | while read -r h; do
  br="claude/chaindiverse-${h}-r${TARGET}"
  echo "  fetching ${br}"
  for i in 1 2 3 4; do
    if git fetch origin "$br" 2>&1 | tail -1 | grep -qE "(FETCH_HEAD|up to date|new branch)"; then
      break
    fi
    case $i in 1) sleep 2;; 2) sleep 4;; 3) sleep 8;; 4) sleep 16;; esac
  done
done

# 3. Extract artifacts per worker.
echo ""
echo "── 3. extracting per-worker artifacts to ${STAGE}/<handle>/ ──"
echo "$WORKERS" | while read -r h; do
  br="claude/chaindiverse-${h}-r${TARGET}"
  dst="$STAGE/$h"
  src_prefix="workers/${h}/chain-diverse-${TARGET}"
  mkdir -p "$dst"
  for i in $(seq 0 31); do
    git show "origin/${br}:${src_prefix}/V_net.${i}.bin" > "$dst/V_net.${i}.bin" 2>/dev/null
    [ ! -s "$dst/V_net.${i}.bin" ] && echo "    WARN ${h} V_net.${i} empty" && rm -f "$dst/V_net.${i}.bin"
  done
  git show "origin/${br}:${src_prefix}/dense.pt"          > "$dst/dense.pt" 2>/dev/null
  git show "origin/${br}:${src_prefix}/opt-sparse-net.pt" > "$dst/opt-sparse-net.pt" 2>/dev/null
  git show "origin/${br}:${src_prefix}/round-${TARGET}.log.jsonl" > "$dst/round-${TARGET}.log.jsonl" 2>/dev/null || true
  n_vnet=$(ls "$dst"/V_net.*.bin 2>/dev/null | wc -l)
  echo "  ${h}: ${n_vnet}/32 V_net + dense + opt + log"
done

# 4. FedAvg + publish.
echo ""
echo "── 4. FedAvg V_net + dense + V_local Gaussian init + publish to workers/dispatcher/ ──"
python3 scripts/harvest_chain.py "$TARGET" --publish

# 5. Stage to inf-spork-r${TARGET}.* for the battery.
echo ""
echo "── 5. staging harvested → inf-spork-r${TARGET} format ──"
python3 scripts/stage_inf_spork.py "$TARGET"

# 6. Run battery.
echo ""
echo "── 6. running 7-dataset eval battery ──"
BATTERY_OUT="workers/dispatcher/harvest-${N_WORKERS}way-r${TARGET}/eval_battery.jsonl"
MMLLM_ENABLE_PKM_CPP=true \
  MMLLM_INF_BASE="/tmp/mmllm-cpu/inf-spork-r${TARGET}.fim" \
  MMLLM_INF_BANK="/tmp/mmllm-cpu/inf-spork-r${TARGET}.bank" \
  MMLLM_BATTERY_OUT="$BATTERY_OUT" \
  python3 scripts/run_eval_battery.py 2>&1 | tail -30

# 7. Generate results.md with comparison to prior.
echo ""
echo "── 7. generating results.md (R${PRIOR} vs R${TARGET}) ──"
python3 scripts/generate_harvest_results.py "$PRIOR" "$TARGET" --n-workers "$N_WORKERS"

# 8. Generate next-round dispatch prompt.
NEXT=$((TARGET + 10))
DISPATCH_OUT="docs/spork-chain-diverse-dispatch-r${NEXT}.md"
if [ -f scripts/generate_dispatch_prompt.py ]; then
  echo ""
  echo "── 8. generating dispatch prompt for R${TARGET}→R${NEXT} ──"
  python3 scripts/generate_dispatch_prompt.py "$TARGET" "$NEXT" --n-workers "$N_WORKERS" \
    --out "$DISPATCH_OUT"
else
  echo "  (skipping — scripts/generate_dispatch_prompt.py not present yet)"
fi

# 9. Commit + push.
if [ "$PUSH" = "true" ]; then
  echo ""
  echo "── 9. committing + pushing to ${DISPATCHER_BRANCH} ──"
  git add scripts/ workers/dispatcher/ docs/ 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "  (no changes to commit)"
  else
    git commit -m "harvest-${N_WORKERS}way-r${TARGET}: $(echo "$WORKERS" | head -1 | xargs)+others FedAvg + battery + R${NEXT} dispatch

Auto-generated by scripts/harvest_chain.sh.

Workers: $(echo "$WORKERS" | tr '\n' ' ')

https://claude.ai/code/session_01B5gEG2Z9BsZcVP9QYWB1oi"
    for i in 1 2 3 4; do
      if git push -u origin "$DISPATCHER_BRANCH" 2>&1 | tail -3; then break; fi
      case $i in 1) sleep 2;; 2) sleep 4;; 3) sleep 8;; 4) sleep 16;; esac
    done
  fi
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  HARVEST COMPLETE — round ${TARGET}"
echo "═══════════════════════════════════════════════════════════════"
echo "  battery JSONL:    ${BATTERY_OUT}"
echo "  results.md:       workers/dispatcher/harvest-${N_WORKERS}way-r${TARGET}/results.md"
echo "  staged artifacts: workers/dispatcher/harvest-${N_WORKERS}way-r${TARGET}/round-${TARGET}/"
echo "  next dispatch:    ${DISPATCH_OUT}"
echo "═══════════════════════════════════════════════════════════════"
