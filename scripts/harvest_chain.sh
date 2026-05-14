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

# Marker subdir name varies across waves:
#   R30-R90: workers/<handle>/chain-diverse-${TARGET}/
#   R91+:    workers/<handle>/chain-design-r${TARGET}/  (the design-sized wave)
# We accept both; the per-worker src_prefix is discovered from the tree.
MARKER_RE="chain-(diverse-${TARGET}|design-r${TARGET})"
CAND_A=$(git branch -r 2>&1 | grep -oE "origin/claude/chaindiverse-[^[:space:]]+-r${TARGET}\$" | sort)
CAND_B=$(git branch -r 2>&1 | grep -oE "origin/claude/extend-chain-rounds-${PRIOR_NEXT}-${TARGET}-[^[:space:]]+\$" | sort)
# Catch-all: any branch with the marker file in its tree (excluding A and B).
# We avoid scanning every branch eagerly; agents that name-violate both patterns
# are the residual to find. ls-remote'd refs only — git ls-tree is cheap.
CAND_C=""
for br in $(git branch -r 2>&1 | grep -oE "origin/claude/[^[:space:]]+\$" | grep -v "$(echo "$CAND_A $CAND_B" | tr ' ' '|')" | sort); do
  if git cat-file -e "${br}:workers" 2>/dev/null; then
    # Has a workers/ dir; check if it has the marker file for this round
    if git ls-tree -r --name-only "$br" 2>/dev/null | grep -qE "^workers/[^/]+/${MARKER_RE}/V_net\.0\.bin\$"; then
      CAND_C="${CAND_C}${br}
"
    fi
  fi
done
CAND_C=$(echo "$CAND_C" | grep -v "^$" | sort)

# Combine candidate branches in priority order.
declare -A HANDLE_TO_BRANCH=()
declare -A HANDLE_TO_MARKER=()      # handle → "chain-diverse-${TARGET}" or "chain-design-r${TARGET}"
mapfile -t ALL_CAND < <(printf '%s\n%s\n%s\n' "$CAND_A" "$CAND_B" "$CAND_C" | grep -v "^$")

for br in "${ALL_CAND[@]}"; do
  br_short="${br#origin/}"
  # Each marker-bearing path in this branch's tree → (handle, marker).
  while IFS=$'\t' read -r h marker; do
    [ -z "$h" ] && continue
    if [ -z "${HANDLE_TO_BRANCH[$h]:-}" ]; then
      HANDLE_TO_BRANCH[$h]="$br_short"
      HANDLE_TO_MARKER[$h]="$marker"
    fi
  done < <(
    git ls-tree -r --name-only "$br" 2>/dev/null \
      | grep -oE "^workers/[^/]+/${MARKER_RE}/V_net\.0\.bin\$" \
      | sed -E "s|^workers/([^/]+)/(chain-(diverse-${TARGET}|design-r${TARGET}))/V_net\.0\.bin|\1\t\2|" \
      | sort -u
  )
done

if [ ${#HANDLE_TO_BRANCH[@]} -eq 0 ]; then
  echo "ERROR: no worker branches found containing workers/<handle>/chain-diverse-${TARGET}/V_net.0.bin" >&2
  exit 2
fi

# Write the discovered manifest (handle:branch:marker per line, sorted).
MANIFEST="$STAGE/.manifest"
> "$MANIFEST"
for h in $(printf '%s\n' "${!HANDLE_TO_BRANCH[@]}" | sort); do
  echo "${h}:${HANDLE_TO_BRANCH[$h]}:${HANDLE_TO_MARKER[$h]}" >> "$MANIFEST"
done
N_WORKERS=$(wc -l < "$MANIFEST")
echo "  found ${N_WORKERS} workers:"
while IFS=: read -r h br marker; do
  echo "    - ${h}  ←  ${br}  (${marker})"
done < "$MANIFEST"

# 2 + 3. Per-worker streaming: fetch → extract → leave on disk → next.
# (Disk discipline: with 20+ workers × ~1.25 GB published artifacts each,
# extracting all in /tmp before harvest peaks at 25+ GB. We keep that
# in-place size budget but reclaim .git/objects every few workers via
# git gc so the *.git* half of the pressure doesn't compound.)
#
# Each worker publishes:
#   workers/<handle>/<marker>/V_net.{0..31}.bin    (32 × 32 MB = 1 GB)
#   workers/<handle>/<marker>/dense.pt             (~3 MB)
#   workers/<handle>/<marker>/opt-sparse-net.{0..31}.pt + .meta.pt
#                                                  (32 × 2-13 MB + meta ≈ 242 MB)
#   workers/<handle>/<marker>/round-${TARGET}.log.jsonl
echo ""
echo "── 2+3. fetching + extracting ${N_WORKERS} workers (with retry) ──"
w_idx=0
while IFS=: read -r h br marker; do
  w_idx=$((w_idx + 1))
  echo "  [${w_idx}/${N_WORKERS}] ${h} ← ${br} (${marker})"
  # Fetch with retry.
  for i in 1 2 3 4; do
    if git fetch origin "$br" 2>&1 | tail -1 | grep -qE "(FETCH_HEAD|up to date|new branch)"; then
      break
    fi
    case $i in 1) sleep 2;; 2) sleep 4;; 3) sleep 8;; 4) sleep 16;; esac
  done

  dst="$STAGE/$h"
  src_prefix="workers/${h}/${marker}"
  mkdir -p "$dst"

  # V_net layers.
  for i in $(seq 0 31); do
    git show "origin/${br}:${src_prefix}/V_net.${i}.bin" > "$dst/V_net.${i}.bin" 2>/dev/null
    [ ! -s "$dst/V_net.${i}.bin" ] && echo "      WARN V_net.${i} empty" && rm -f "$dst/V_net.${i}.bin"
  done
  # Dense.
  git show "origin/${br}:${src_prefix}/dense.pt" > "$dst/dense.pt" 2>/dev/null

  # opt-sparse-net: prefer chunks (R91+ format), fall back to legacy single-file (R20-R90).
  git show "origin/${br}:${src_prefix}/opt-sparse-net.meta.pt" > "$dst/opt-sparse-net.meta.pt" 2>/dev/null
  if [ -s "$dst/opt-sparse-net.meta.pt" ]; then
    for i in $(seq 0 31); do
      git show "origin/${br}:${src_prefix}/opt-sparse-net.${i}.pt" > "$dst/opt-sparse-net.${i}.pt" 2>/dev/null
      [ ! -s "$dst/opt-sparse-net.${i}.pt" ] && rm -f "$dst/opt-sparse-net.${i}.pt"
    done
    n_opt_chunks=$(ls "$dst"/opt-sparse-net.*.pt 2>/dev/null | grep -v meta | wc -l)
    opt_desc="opt-chunks ${n_opt_chunks}/32"
  else
    rm -f "$dst/opt-sparse-net.meta.pt"
    git show "origin/${br}:${src_prefix}/opt-sparse-net.pt" > "$dst/opt-sparse-net.pt" 2>/dev/null
    [ ! -s "$dst/opt-sparse-net.pt" ] && rm -f "$dst/opt-sparse-net.pt"
    opt_desc="opt-single $([ -f "$dst/opt-sparse-net.pt" ] && echo present || echo absent)"
  fi

  # Per-round log.
  git show "origin/${br}:${src_prefix}/round-${TARGET}.log.jsonl" > "$dst/round-${TARGET}.log.jsonl" 2>/dev/null || true

  n_vnet=$(ls "$dst"/V_net.*.bin 2>/dev/null | wc -l)
  echo "      ${n_vnet}/32 V_net + dense + ${opt_desc} + log"

  # Reclaim .git/objects every 4 workers — keeps the .git side of disk
  # pressure flat at ~5 GB rather than growing linearly to 25+ GB.
  if [ $((w_idx % 4)) -eq 0 ] && [ $w_idx -lt $N_WORKERS ]; then
    git gc --auto --quiet 2>/dev/null || true
  fi
done < "$MANIFEST"

# Final gc before harvest — frees any remaining loose objects before
# harvest_chain.py loads everything from /tmp.
git gc --auto --quiet 2>/dev/null || true

# 4. FedAvg + publish.
echo ""
echo "── 4. FedAvg V_net + dense + opt-state + V_local Gaussian init + publish ──"
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
