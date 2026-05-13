#!/usr/bin/env bash
# harvest_chain.sh — end-to-end harvest of a chain-diverse wave.
#
# Usage:  bash scripts/harvest_chain.sh <target_round> [--no-push]
#
# Workflow:
#   1. discover worker branches via content scan (find branches that
#      contain workers/<handle>/chain-diverse-${TARGET}/V_net.0.bin),
#      dedup by handle (preferring claude/chaindiverse-* naming over
#      claude/extend-chain-rounds-* and other variants)
#   2. fetch each canonical branch (with retry)
#   3. extract per-worker artifacts to /tmp/mmllm-cpu/harvest-r${TARGET}/<handle>/
#   4. FedAvg V_net + dense (scripts/harvest_chain.py --publish)
#   5. stage to inf-spork-r${TARGET}.* (scripts/stage_inf_spork.py)
#   6. run 7-dataset battery (scripts/run_eval_battery.py, env-paramed)
#   7. generate results.md (scripts/generate_harvest_results.py)
#   8. generate next-round dispatch prompt (scripts/generate_dispatch_prompt.py)
#   9. commit + push to claude/fim-training-cycle-T3giJ
#
# The R60 wave surfaced the discovery brittleness: one worker pushed to
# claude/extend-chain-rounds-51-60-VYJX9 (non-standard) instead of
# claude/chaindiverse-claude-r60ext-r60. The pattern-match-only discovery
# missed it. Content-based scan catches all naming variants.
#
# Total wall: ~3-5 min for steps 1-3 (HTTP fetches), 10s for FedAvg,
# 2 min for battery, instant for results/dispatch generation.

set -e
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

TARGET="${1:?target round required (e.g. 40 for harvesting R31-R40 wave)}"
PRIOR=$((TARGET - 10))
PRIOR_NEXT=$((PRIOR + 1))
PUSH=true
[ "$2" = "--no-push" ] && PUSH=false

STAGE=/tmp/mmllm-cpu/harvest-r${TARGET}
DISPATCHER_BRANCH=$(git rev-parse --abbrev-ref HEAD)

echo "═══════════════════════════════════════════════════════════════"
echo "  HARVEST CHAIN: target round ${TARGET} (prior harvest at r${PRIOR})"
echo "  dispatcher branch: ${DISPATCHER_BRANCH}"
echo "  push at end: ${PUSH}"
echo "═══════════════════════════════════════════════════════════════"

# 1. Discover worker branches via content scan.
# Multi-pattern + dedup-by-handle. Candidate patterns are tried in
# priority order; the first branch that publishes a given handle wins.
#   Pattern A (preferred): claude/chaindiverse-<handle>-r${TARGET}
#   Pattern B (fallback):  claude/extend-chain-rounds-${PRIOR_NEXT}-${TARGET}-*
#   Pattern C (catch-all): any branch whose tree contains
#                          workers/<X>/chain-diverse-${TARGET}/V_net.0.bin
echo ""
echo "── 1. discovering worker branches (content scan, dedup by handle) ──"
mkdir -p "$STAGE"
git fetch origin --prune 2>/dev/null || true

# Build the candidate branch list, A then B then catch-all C minus dupes.
CAND_A=$(git branch -r 2>&1 | grep -oE "origin/claude/chaindiverse-[^[:space:]]+-r${TARGET}\$" | sort)
CAND_B=$(git branch -r 2>&1 | grep -oE "origin/claude/extend-chain-rounds-${PRIOR_NEXT}-${TARGET}-[^[:space:]]+\$" | sort)
# Catch-all: any branch with the marker file in its tree (excluding A and B).
# We avoid scanning every branch eagerly; agents that name-violate both patterns
# are the residual to find. ls-remote'd refs only — git ls-tree is cheap.
CAND_C=""
for br in $(git branch -r 2>&1 | grep -oE "origin/claude/[^[:space:]]+\$" | grep -v "$(echo "$CAND_A $CAND_B" | tr ' ' '|')" | sort); do
  if git cat-file -e "${br}:workers" 2>/dev/null; then
    # Has a workers/ dir; check if it has the marker file for this round
    if git ls-tree -r --name-only "$br" 2>/dev/null | grep -qE "^workers/[^/]+/chain-diverse-${TARGET}/V_net\.0\.bin\$"; then
      CAND_C="${CAND_C}${br}
"
    fi
  fi
done
CAND_C=$(echo "$CAND_C" | grep -v "^$" | sort)

# Combine candidate branches in priority order.
declare -A HANDLE_TO_BRANCH=()
mapfile -t ALL_CAND < <(printf '%s\n%s\n%s\n' "$CAND_A" "$CAND_B" "$CAND_C" | grep -v "^$")

for br in "${ALL_CAND[@]}"; do
  br_short="${br#origin/}"
  # Find every handle in this branch's tree that has the marker file
  mapfile -t br_handles < <(
    git ls-tree -r --name-only "$br" 2>/dev/null \
      | grep -oE "^workers/[^/]+/chain-diverse-${TARGET}/V_net\.0\.bin\$" \
      | sed -E "s|^workers/([^/]+)/chain-diverse-${TARGET}/V_net\.0\.bin|\1|" \
      | sort -u
  )
  for h in "${br_handles[@]}"; do
    [ -z "$h" ] && continue
    if [ -z "${HANDLE_TO_BRANCH[$h]:-}" ]; then
      HANDLE_TO_BRANCH[$h]="$br_short"
    fi
  done
done

if [ ${#HANDLE_TO_BRANCH[@]} -eq 0 ]; then
  echo "ERROR: no worker branches found containing workers/<handle>/chain-diverse-${TARGET}/V_net.0.bin" >&2
  exit 2
fi

# Write the discovered manifest (handle:branch per line, sorted).
MANIFEST="$STAGE/.manifest"
> "$MANIFEST"
for h in $(printf '%s\n' "${!HANDLE_TO_BRANCH[@]}" | sort); do
  echo "${h}:${HANDLE_TO_BRANCH[$h]}" >> "$MANIFEST"
done
N_WORKERS=$(wc -l < "$MANIFEST")
echo "  found ${N_WORKERS} workers:"
while IFS=: read -r h br; do
  echo "    - ${h}  ←  ${br}"
done < "$MANIFEST"

# 2. Fetch each canonical branch with retry.
echo ""
echo "── 2. fetching ${N_WORKERS} canonical worker branches (with retry) ──"
while IFS=: read -r h br; do
  echo "  fetching ${br}"
  for i in 1 2 3 4; do
    if git fetch origin "$br" 2>&1 | tail -1 | grep -qE "(FETCH_HEAD|up to date|new branch)"; then
      break
    fi
    case $i in 1) sleep 2;; 2) sleep 4;; 3) sleep 8;; 4) sleep 16;; esac
  done
done < "$MANIFEST"

# 3. Extract artifacts per worker.
echo ""
echo "── 3. extracting per-worker artifacts to ${STAGE}/<handle>/ ──"
while IFS=: read -r h br; do
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
done < "$MANIFEST"

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
    WORKER_HANDLES=$(cut -d: -f1 "$MANIFEST" | sort | tr '\n' ' ')
    FIRST_HANDLE=$(cut -d: -f1 "$MANIFEST" | head -1)
    git commit -m "harvest-${N_WORKERS}way-r${TARGET}: ${FIRST_HANDLE}+others FedAvg + battery + R${NEXT} dispatch

Auto-generated by scripts/harvest_chain.sh.

Workers: ${WORKER_HANDLES}

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
