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

# Pick a Python with numpy + torch. System python3 on some boxes is bare;
# fall back to a project venv if one exists. Setting PYTHON via env var
# overrides discovery for one-off runs.
if [ -z "${PYTHON:-}" ]; then
  for cand in \
      "$ROOT/.venv/bin/python" \
      "$ROOT/papers/spiral-quant/.venv/bin/python" \
      "$(command -v python3)"; do
    if [ -x "$cand" ] && "$cand" -c 'import numpy, torch' 2>/dev/null; then
      PYTHON="$cand"; break
    fi
  done
fi
if [ -z "${PYTHON:-}" ]; then
  echo "ERROR: no Python with numpy + torch found. Set PYTHON=/path/to/python" >&2
  exit 2
fi
echo "  python: $PYTHON"

# Argument modes:
#   bash harvest_chain.sh                # auto: discover unprocessed
#                                          claude/chaindiverse-* branches, group
#                                          by their last published round, harvest
#                                          the highest round's group.
#   bash harvest_chain.sh <target_round> # explicit: harvest only branches whose
#                                          marker dir is at <target_round>.
#   bash harvest_chain.sh [<target>] --no-push   # build artifacts but don't push.
MANIFEST_FILE="workers/dispatcher/.harvest-manifest.json"

PUSH=true
case "$#" in
  0) TARGET="" ;;
  1)
    if [ "$1" = "--no-push" ]; then TARGET=""; PUSH=false
    else TARGET="$1"
    fi
    ;;
  *)
    TARGET="$1"
    [ "$2" = "--no-push" ] && PUSH=false
    ;;
esac

# Auto-discover TARGET if no arg was given. Lists unprocessed
# chaindiverse-* branches via ls-remote, peeks at each branch's tree to
# find its marker round (cheap: partial-clone --filter=blob:none), then
# picks the highest round. Branches already recorded in
# .harvest-manifest.json (by sha) are skipped.
if [ -z "$TARGET" ]; then
  echo "── auto-discovering target round from unprocessed branches ──"
  REMOTE_REFS=$(git ls-remote origin "refs/heads/claude/chaindiverse-*" 2>&1)
  if [ -z "$REMOTE_REFS" ]; then
    echo "  no claude/chaindiverse-* branches on origin"
    exit 0
  fi
  if [ -f "$MANIFEST_FILE" ]; then
    PROCESSED_SHAS=$("$PYTHON" -c "
import json
m = json.load(open('$MANIFEST_FILE'))
print('\n'.join(m.get('processed', {}).keys()))
" 2>/dev/null)
  else
    PROCESSED_SHAS=""
  fi
  # Filter to unprocessed (branch_sha not in manifest).
  declare -A UNPROCESSED_BR=()      # br_short → sha
  while read -r sha ref; do
    [ -z "$sha" ] && continue
    if echo "$PROCESSED_SHAS" | grep -qFx "$sha"; then continue; fi
    br="${ref#refs/heads/}"
    UNPROCESSED_BR["$br"]="$sha"
  done <<< "$REMOTE_REFS"
  if [ ${#UNPROCESSED_BR[@]} -eq 0 ]; then
    echo "  all claude/chaindiverse-* branches already in $MANIFEST_FILE"
    exit 0
  fi
  echo "  ${#UNPROCESSED_BR[@]} unprocessed branch(es); peeking trees to find rounds…"
  declare -A BRANCH_ROUND=()
  declare -A BRANCH_HANDLE=()    # tree-derived handle (handles fim- prefix etc)
  for br in "${!UNPROCESSED_BR[@]}"; do
    git fetch origin "$br" --filter=blob:none --depth=1 2>&1 \
      | tail -1 | grep -qE "(FETCH_HEAD|new branch|up to date)" || {
        echo "    WARN: fetch failed for $br, skipping"; continue
      }
    marker=$(git ls-tree -r --name-only "origin/$br" 2>/dev/null \
      | grep -oE "workers/[^/]+/chain-(diverse-[0-9]+|design-r[0-9]+(-[0-9]+)?)/" \
      | head -1)
    if [ -z "$marker" ]; then
      echo "    WARN: no chain-* marker dir in $br tree, skipping"
      continue
    fi
    round=$(echo "$marker" | grep -oE "[0-9]+" | tail -1)
    # Extract the actual worker dir name from the tree, not from the
    # branch name. Branch names may carry a category prefix (fim-, etc.)
    # that's not part of the handle on disk.
    handle=$(echo "$marker" | sed -E 's|^workers/([^/]+)/.*|\1|')
    BRANCH_ROUND["$br"]="$round"
    BRANCH_HANDLE["$br"]="$handle"
    echo "    $br → round $round, handle $handle"
  done
  if [ ${#BRANCH_ROUND[@]} -eq 0 ]; then
    echo "  no branches with usable marker dirs"
    exit 0
  fi
  TARGET=$(printf '%s\n' "${BRANCH_ROUND[@]}" | sort -n | tail -1)
  echo "  selected TARGET=$TARGET (highest round among unprocessed branches)"
fi

# PRIOR = wave-relative round just-prior. For wave-prefixed targets
# like "2-10" (wave 2, round 10 of that wave), the worker extended from
# "<prior-wave>-r10" (the reference produced by the previous wave's
# harvest). Bash arithmetic on the LAST numeric segment of TARGET:
TARGET_ROUND="${TARGET##*-}"   # "2-10" -> "10";  "10" -> "10"
PRIOR=$((TARGET_ROUND - 10))
PRIOR_NEXT=$((PRIOR + 1))

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

# Discovery via `git ls-remote` (refs only — no objects fetched). This
# replaces the prior `git branch -r` scan which silently returns nothing
# on a shallow clone (the `--prune` fetch doesn't pull new branches that
# weren't already tracked). ls-remote works regardless of clone state.
#
# Marker subdir name is inferred from TARGET:
#   R30-R90:  workers/<handle>/chain-diverse-${TARGET}/
#   R91+:     workers/<handle>/chain-design-r${TARGET}/  (design-sized wave)
# A worker that uses the other marker for its round won't be picked up —
# this is acceptable since all waves at a given round use one convention.
# Marker subdir name. Workers publish to:
#   workers/<handle>/chain-design-r${LAST}/
# where LAST is the highest round in the worker's local archive. In
# wave-agnostic mode workers stage the reference as round-0 and train
# round-1..10, so LAST=10 universally. Legacy waves had absolute round
# numbers (R30-R90 used `chain-diverse-${TARGET}`, R91+ used
# `chain-design-r${TARGET}`); those are all already harvested and in
# the manifest, so this script only needs to recognize the current
# `chain-design-r${TARGET}` form.
MARKER="chain-design-r${TARGET}"
echo "  using marker subdir: ${MARKER}"

REMOTE_REFS=$(git ls-remote origin 2>&1 | awk '{print $2}' | grep -E "^refs/heads/")

# Candidate branches at this TARGET:
#   A) claude/chaindiverse-<handle>-r${TARGET}            (old wave-suffixed naming)
#   B) claude/extend-chain-rounds-${PRIOR_NEXT}-${TARGET}-* (legacy alt naming)
#   C) claude/chaindiverse-<handle>-<UTC_TS>              (new wave-agnostic naming,
#                                                          target inferred from tree)
CAND_A=$(echo "$REMOTE_REFS" | grep -oE "refs/heads/claude/chaindiverse-[^[:space:]]+-r${TARGET}\$" \
         | sed 's|refs/heads/||' | sort)
CAND_B=$(echo "$REMOTE_REFS" | grep -oE "refs/heads/claude/extend-chain-rounds-${PRIOR_NEXT}-${TARGET}-[^[:space:]]+\$" \
         | sed 's|refs/heads/||' | sort)
# Catch wave-agnostic branches (chaindiverse-<HANDLE>-<UTC_TS>) whose tree
# contains the TARGET marker dir but whose names don't encode the round.
# If auto-discovery already populated BRANCH_ROUND, reuse it (cheap). If
# TARGET was passed explicitly with no auto-discovery, do partial-clone
# fetches here to peek trees.
CAND_C=""
A_OR_B_PIPED=$(printf '%s\n%s\n' "$CAND_A" "$CAND_B" | grep -v '^$' | tr '\n' '|' | sed 's/|$//')
if [ "${#BRANCH_ROUND[@]}" -gt 0 ]; then
  # Reuse the auto-discovery scan.
  for br in "${!BRANCH_ROUND[@]}"; do
    if [ "${BRANCH_ROUND[$br]}" != "$TARGET" ]; then continue; fi
    if [ -n "$A_OR_B_PIPED" ] && echo "$br" | grep -qE "^($A_OR_B_PIPED)\$"; then continue; fi
    CAND_C="${CAND_C}${br}
"
  done
else
  # Explicit TARGET passed; do a fresh partial-clone scan over all chaindiverse-*.
  declare -A BRANCH_HANDLE=()    # populated here too so the handle-resolution
                                 # path below uses tree-derived handles.
  ALL_CHAINDIV=$(echo "$REMOTE_REFS" | grep -oE "refs/heads/claude/chaindiverse-[^[:space:]]+\$" \
                 | sed 's|refs/heads/||' | sort -u)
  for br in $ALL_CHAINDIV; do
    if [ -n "$A_OR_B_PIPED" ] && echo "$br" | grep -qE "^($A_OR_B_PIPED)\$"; then continue; fi
    git fetch origin "$br" --filter=blob:none --depth=1 2>&1 | tail -1 | \
      grep -qE "(FETCH_HEAD|new branch|up to date)" || continue
    # Accept either format the worker may have published in:
    #   legacy: workers/<h>/<MARKER>/V_net.0.bin
    #   sparse-delta: workers/<h>/<MARKER>/delta-sparse-net.meta.pt
    marker_path=$(git ls-tree -r --name-only "origin/$br" 2>/dev/null \
      | grep -E "^workers/[^/]+/${MARKER}/(V_net\.0\.bin|delta-sparse-net\.meta\.pt)\$" \
      | head -1)
    if [ -n "$marker_path" ]; then
      CAND_C="${CAND_C}${br}
"
      handle=$(echo "$marker_path" | sed -E 's|^workers/([^/]+)/.*|\1|')
      BRANCH_HANDLE["$br"]="$handle"
    fi
  done
fi
CAND_C=$(echo "$CAND_C" | grep -v "^$" | sort)

# Handle inference. Three patterns:
declare -A HANDLE_TO_BRANCH=()
declare -A HANDLE_TO_MARKER=()
for br in $CAND_A; do
  h=$(echo "$br" | sed -E "s|^claude/chaindiverse-(.+)-r${TARGET}\$|\1|")
  if [ -z "${HANDLE_TO_BRANCH[$h]:-}" ]; then
    HANDLE_TO_BRANCH[$h]="$br"
    HANDLE_TO_MARKER[$h]="$MARKER"
  fi
done
for br in $CAND_B; do
  h=$(echo "$br" | sed -E "s|^claude/extend-chain-rounds-${PRIOR_NEXT}-${TARGET}-(.+)\$|\1|")
  if [ -z "${HANDLE_TO_BRANCH[$h]:-}" ]; then
    HANDLE_TO_BRANCH[$h]="$br"
    HANDLE_TO_MARKER[$h]="$MARKER"
  fi
done
for br in $CAND_C; do
  # Prefer the tree-derived handle (BRANCH_HANDLE) when auto-discovery
  # populated it — branch names may carry a category prefix (fim-, etc.)
  # that's not part of the worker dir on disk. Fall back to the branch-
  # name regex if BRANCH_HANDLE is unset (explicit-TARGET mode).
  if [ -n "${BRANCH_HANDLE[$br]:-}" ]; then
    h="${BRANCH_HANDLE[$br]}"
  else
    h=$(echo "$br" | sed -E "s|^claude/chaindiverse-(.+)-[0-9]{8}-[0-9]{6}\$|\1|;s|^claude/chaindiverse-(.+)\$|\1|")
  fi
  if [ -z "${HANDLE_TO_BRANCH[$h]:-}" ]; then
    HANDLE_TO_BRANCH[$h]="$br"
    HANDLE_TO_MARKER[$h]="$MARKER"
  fi
done

if [ ${#HANDLE_TO_BRANCH[@]} -eq 0 ]; then
  echo "ERROR: no worker branches matching pattern claude/chaindiverse-*-r${TARGET} or" >&2
  echo "       claude/extend-chain-rounds-${PRIOR_NEXT}-${TARGET}-* on origin." >&2
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

# Reference V_net for sparse-delta encoding. Workers that pushed full
# V_net.{0..31}.bin (legacy format, pre-rewrite) are converted to deltas
# on the harvester side: subtract this reference, sparsify, fold into the
# row-aware accumulator. Workers that already pushed delta chunks skip
# the conversion. Either way, the accumulator path is row-aware after
# this point — the dilution bug in naive V_net mean is bypassed even for
# legacy workers.
REFERENCE_DIR=""
# Try `current` first (covers wave-prefixed targets where PRIOR=0).
# Safety: never accept a `current` that points at the CURRENT target's
# own harvest dir — that's a leftover from a prior failed attempt at
# the same target, and using it as the reference produces self-referential
# garbage (the prior attempt's bogus output becomes the "ground truth"
# this attempt builds on top of).
if [ -L workers/dispatcher/current ] || [ -d workers/dispatcher/current ]; then
  cand_cur=$(readlink -f workers/dispatcher/current 2>/dev/null)
  if [ -d "$cand_cur" ] && [ -f "$cand_cur/V_net.0.bin" ] \
     && [[ "$cand_cur" != */harvest-*-r${TARGET}/round-${TARGET} ]]; then
    REFERENCE_DIR="$cand_cur"
  fi
fi
# Fall back to the legacy r${PRIOR} glob if `current` isn't set.
if [ -z "$REFERENCE_DIR" ]; then
  for cand in workers/dispatcher/harvest-*-r${PRIOR}/round-${PRIOR} \
              workers/dispatcher/harvest-cooked-r${PRIOR}/round-${PRIOR}; do
    if [ -d "$cand" ] && [ -f "$cand/V_net.0.bin" ]; then
      REFERENCE_DIR="$cand"; break
    fi
  done
fi
if [ -n "$REFERENCE_DIR" ]; then
  echo "  reference V_net (for on-the-fly delta encoding): ${REFERENCE_DIR}"
else
  echo "  no local reference V_net found at workers/dispatcher/{current,harvest-*-r${PRIOR}}/round-${PRIOR}"
  echo "  legacy workers will fall through to naive-mean FedAvg (dilution bug applies)"
fi

# 2-4. Streaming harvest: per-worker fetch → extract → fold-into-accumulator
# → delete worker dir → git gc. Peak disk stays at ~one-worker (~1.25 GB)
# plus accumulator state (~2 GB) regardless of N. This replaces the
# old "extract everything to /tmp then load all 25 GB at once" path
# which hit OOM/disk limits at N≥10.
ACCUM="$STAGE/.accum"
rm -rf "$ACCUM"
mkdir -p "$ACCUM"

echo ""
echo "── 2-4. streaming harvest of ${N_WORKERS} workers ──"
w_idx=0
while IFS=: read -r h br marker; do
  w_idx=$((w_idx + 1))
  echo ""
  echo "[${w_idx}/${N_WORKERS}] ${h} ← ${br} (${marker})"

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

  # V_net path: prefer sparse delta (delta-sparse-net.meta.pt + per-pid
  # chunks, ~10-50 MB total) if the worker pushed one. Fall back to
  # legacy full V_net.{0..31}.bin (1 GB) only if no delta meta is
  # present in the worker's tree.
  #
  # All `git show` probes need `|| true` under `set -e` — git show
  # against a non-existent path exits 128 and would kill the script.
  git show "origin/${br}:${src_prefix}/delta-sparse-net.meta.pt" > "$dst/delta-sparse-net.meta.pt" 2>/dev/null || true
  if [ -s "$dst/delta-sparse-net.meta.pt" ]; then
    for i in $(seq 0 31); do
      git show "origin/${br}:${src_prefix}/delta-sparse-net.${i}.pt" > "$dst/delta-sparse-net.${i}.pt" 2>/dev/null || true
      [ ! -s "$dst/delta-sparse-net.${i}.pt" ] && rm -f "$dst/delta-sparse-net.${i}.pt"
    done
    n_delta_chunks=$(ls "$dst"/delta-sparse-net.[0-9]*.pt 2>/dev/null | wc -l)
    vnet_desc="delta-chunks ${n_delta_chunks}/32"
  else
    rm -f "$dst/delta-sparse-net.meta.pt"
    for i in $(seq 0 31); do
      git show "origin/${br}:${src_prefix}/V_net.${i}.bin" > "$dst/V_net.${i}.bin" 2>/dev/null || true
      [ ! -s "$dst/V_net.${i}.bin" ] && rm -f "$dst/V_net.${i}.bin"
    done
    n_vnet=$(ls "$dst"/V_net.*.bin 2>/dev/null | wc -l)
    vnet_desc="full V_net ${n_vnet}/32"
  fi
  # Dense.
  git show "origin/${br}:${src_prefix}/dense.pt" > "$dst/dense.pt" 2>/dev/null || true

  # opt-sparse-net: prefer chunks (R91+), fall back to legacy single-file.
  git show "origin/${br}:${src_prefix}/opt-sparse-net.meta.pt" > "$dst/opt-sparse-net.meta.pt" 2>/dev/null || true
  if [ -s "$dst/opt-sparse-net.meta.pt" ]; then
    for i in $(seq 0 31); do
      git show "origin/${br}:${src_prefix}/opt-sparse-net.${i}.pt" > "$dst/opt-sparse-net.${i}.pt" 2>/dev/null || true
      [ ! -s "$dst/opt-sparse-net.${i}.pt" ] && rm -f "$dst/opt-sparse-net.${i}.pt"
    done
    n_opt_chunks=$(ls "$dst"/opt-sparse-net.[0-9]*.pt 2>/dev/null | wc -l)
    opt_desc="opt-chunks ${n_opt_chunks}/32"
  else
    rm -f "$dst/opt-sparse-net.meta.pt"
    git show "origin/${br}:${src_prefix}/opt-sparse-net.pt" > "$dst/opt-sparse-net.pt" 2>/dev/null || true
    [ ! -s "$dst/opt-sparse-net.pt" ] && rm -f "$dst/opt-sparse-net.pt"
    opt_desc="opt-single $([ -f "$dst/opt-sparse-net.pt" ] && echo present || echo absent)"
  fi

  # Per-round log → harvest-side reads it for ctrl_bpc reporting.
  git show "origin/${br}:${src_prefix}/round-${TARGET}.log.jsonl" > "$dst/round-${TARGET}.log.jsonl" 2>/dev/null || true

  # Stash the worker's meta.json so finalize can recover the wave's
  # reference V_net path (extended_from). Worker dirs get rm'd after
  # stream-update folds them in, so we copy the meta to the accumulator.
  git show "origin/${br}:${src_prefix}/meta.json" > "$dst/meta.json" 2>/dev/null || true
  if [ -s "$dst/meta.json" ] && [ ! -f "$ACCUM/.first-worker-meta.json" ]; then
    cp "$dst/meta.json" "$ACCUM/.first-worker-meta.json"
  fi

  echo "    extracted: ${vnet_desc} + dense + ${opt_desc}"

  # Skip workers that didn't produce any usable artifacts. Happens when
  # a branch named -r${TARGET} actually only pushed an earlier round's
  # marker dir (e.g. kbykh-r101 has workers/kbykh/chain-diverse-100/
  # not workers/kbykh/chain-design-r101/). Without this guard, an empty
  # extract reaches stream-update which then fails on the 0-byte
  # dense.pt with EOFError.
  if [ ! -s "$dst/dense.pt" ]; then
    echo "    WARN: dense.pt missing/empty — worker did not push to ${src_prefix}"
    echo "    skipping ${h} and shedding its git refs"
    rm -rf "$dst"
    git update-ref -d "refs/remotes/origin/${br}" 2>/dev/null || true
    rm -f .git/FETCH_HEAD
    continue
  fi

  # On-the-fly delta conversion for legacy full-V_net workers.
  # If the worker pushed V_net.{i}.bin AND we have a reference, compute
  # delta sparse-encode and drop the V_net.bin files. The stream-update
  # call below then takes the row-aware delta path automatically (it
  # detects delta-sparse-net.meta.pt first). This gives legacy workers
  # the same row-aware FedAvg semantics as native-delta workers and
  # drops /tmp from ~1 GB → ~60 MB per worker mid-fold.
  if [ -n "$REFERENCE_DIR" ] && [ ! -f "$dst/delta-sparse-net.meta.pt" ] \
     && ls "$dst"/V_net.*.bin >/dev/null 2>&1; then
    echo "    → encoding sparse delta on-the-fly vs ${REFERENCE_DIR}"
    "$PYTHON" scripts/_delta_sparse_net.py encode \
      "$REFERENCE_DIR" "$dst" "$dst" 2>&1 | sed 's/^/      /'
    rm -f "$dst"/V_net.*.bin
    vnet_desc="${vnet_desc} → delta-on-the-fly"
    echo "    /tmp worker dir after conversion: $(du -sh $dst 2>&1 | awk '{print $1}')"
  fi

  # Pull ctrl_bpc out of the log for the accumulator's bpcs dict.
  CTRL_BPC=""
  if [ -f "$dst/round-${TARGET}.log.jsonl" ]; then
    CTRL_BPC=$("$PYTHON" -c "
import json,sys
for line in open('$dst/round-${TARGET}.log.jsonl'):
    try: ev = json.loads(line)
    except: continue
    if ev.get('event') == 'ablation' and ev.get('control_bpc') is not None:
        print(ev['control_bpc']); break
" 2>/dev/null || true)
  fi
  CTRL_ARGS=""
  [ -n "$CTRL_BPC" ] && CTRL_ARGS="--ctrl-bpc $CTRL_BPC"

  # Fold into streaming accumulator.
  "$PYTHON" scripts/harvest_chain.py --mode=stream-update "$ACCUM" "$dst" "$h" $CTRL_ARGS

  # Free this worker's /tmp AND shed its git objects from .git/objects/.
  # The two are independent — /tmp is the extracted-files staging dir,
  # .git/objects is where `git fetch origin <branch>` deposited the
  # worker's pack (~1.25 GB per worker in legacy mode). Without aggressive
  # pruning we accumulate every worker's pack and hit OOM-disk on shallow
  # repos before reaching N=8.
  rm -rf "$dst"
  git update-ref -d "refs/remotes/origin/${br}" 2>/dev/null || true
  rm -f .git/FETCH_HEAD
done < "$MANIFEST"

# Bulk gc once after all workers folded. With sparse-delta workers each
# adding ~50 MB after pack-dedup, 7 workers ≈ 350 MB — `git gc --auto`
# will skip the repack unless it actually crosses git's loose-object
# threshold. The expensive --prune=now full repack from per-worker gc
# was a legacy-format (1.25 GB worker) mitigation that's no longer needed.
echo ""
echo "── 4a. bulk gc --auto (only runs if git thinks it's needed) ──"
git gc --auto --quiet 2>&1 | tail -3 || true

# Finalize: divide accumulator sums by N, write harvested outputs, publish.
# Delta-mode workers need a reference V_net to add their merged delta back
# on top of. The reference is whatever this wave was extended from. We
# auto-discover via two paths in priority order:
#   1. Any worker's meta.json "extended_from" field (most authoritative).
#   2. Glob workers/dispatcher/harvest-*-r${PRIOR}/round-${PRIOR}/ (covers
#      both the typical harvest-Nway and the one-off harvest-cooked layout).
# Pass-through if no delta workers were folded (legacy mode is fine).
REFERENCE_DIR=""
# (1) First worker's meta.json "extended_from" is authoritative.
if [ -f "$ACCUM/.first-worker-meta.json" ]; then
  cand=$("$PYTHON" -c "
import json
try:
    m = json.load(open('$ACCUM/.first-worker-meta.json'))
    print(m.get('extended_from', '').split(' ')[0])
except: pass
" 2>/dev/null)
  if [ -n "$cand" ] && [ -d "$cand" ] && [ -f "$cand/V_net.0.bin" ]; then
    REFERENCE_DIR="$cand"
  fi
fi
# (2) Glob across ALL prior harvests for a dir with V_net.bin — the chain's
# delta-encode reference is whatever harvest carries the full V_net, not
# necessarily the most-recent one (which may itself be sparse-delta and
# therefore unsuitable as a reference). Walk descending by round; first
# match wins. Covers both harvest-Nway and one-off harvest-cooked layouts.
if [ -z "$REFERENCE_DIR" ]; then
  for cand in $(ls -1d workers/dispatcher/harvest-*-r*/round-*/ \
                       workers/dispatcher/harvest-cooked-r*/round-*/ \
                       2>/dev/null \
               | sed 's|/$||' \
               | awk -F/round- '{print $2 "\t" $0}' \
               | sort -rn | cut -f2-); do
    if [ -d "$cand" ] && [ -f "$cand/V_net.0.bin" ]; then
      REFERENCE_DIR="$cand"; break
    fi
  done
fi
# (3) If still no full V_net reference in the working tree, restore the
# chain anchor from git history. The team intentionally dropped
# `workers/dispatcher/harvest-5way-r10/round-10/` from HEAD in commit
# c6504b0 ("disk cleanup; recoverable from git history") — the blobs
# persist at commit 8608bc3e and are reachable from this branch's
# ancestry. Sparse-delta workers are encoded against this anchor; without
# it the harvester can't reconstruct V_net = reference + delta.
if [ -z "$REFERENCE_DIR" ]; then
  ANCHOR_COMMIT=8608bc3e
  ANCHOR_PATH=workers/dispatcher/harvest-5way-r10/round-10
  echo "  no V_net reference in working tree; restoring chain anchor from ${ANCHOR_COMMIT}"
  # Local checkout first — works if blobs are reachable. If only some
  # blobs are local (partial-fetch leftovers, gc pruned), the checkout
  # silently materializes a partial dir. Verify by counting V_net files
  # and force an unfiltered fetch when incomplete.
  git checkout "$ANCHOR_COMMIT" -- "$ANCHOR_PATH/" 2>/dev/null || true
  N_VNET=$(ls "$ANCHOR_PATH"/V_net.*.bin 2>/dev/null | wc -l)
  if [ "$N_VNET" -lt 32 ]; then
    echo "  partial anchor (${N_VNET}/32 V_net blobs local); forcing unfiltered fetch"
    timeout 600 git fetch origin "$ANCHOR_COMMIT" --depth=1 --no-filter 2>&1 | tail -2
    git checkout "$ANCHOR_COMMIT" -- "$ANCHOR_PATH/" 2>/dev/null || true
    N_VNET=$(ls "$ANCHOR_PATH"/V_net.*.bin 2>/dev/null | wc -l)
  fi
  if [ "$N_VNET" -eq 32 ]; then
    REFERENCE_DIR="$ANCHOR_PATH"
    echo "  restored ← ${ANCHOR_PATH} (32/32 V_net blobs)"
  else
    echo "  WARN: restored only ${N_VNET}/32 V_net blobs; finalize will fail"
  fi
fi
# If REFERENCE_DIR is still empty and any worker pushed sparse-delta,
# the python finalize will exit 2 with a clear error of its own.
echo ""
echo "── 5. stream-finalize: divide by N=${N_WORKERS}, write outputs, publish ──"
echo "    reference V_net dir: ${REFERENCE_DIR:-<none, legacy full-V_net mode only>}"
REF_ARGS=""
[ -n "$REFERENCE_DIR" ] && REF_ARGS="--reference-dir $REFERENCE_DIR"
"$PYTHON" scripts/harvest_chain.py --mode=stream-finalize "$TARGET" "$ACCUM" --publish $REF_ARGS

# 5a. Update workers/dispatcher/current → this harvest's round dir, and
# record the folded branches' SHAs in .harvest-manifest.json so the
# auto-discovery mode skips them next time. Done before the battery so
# a battery failure doesn't lose the symlink/manifest state.
echo ""
echo "── 5a. updating dispatcher current symlink + manifest ──"
HARVEST_REL="harvest-${N_WORKERS}way-r${TARGET}/round-${TARGET}"
ln -snf "$HARVEST_REL" "workers/dispatcher/current"
echo "  workers/dispatcher/current → $HARVEST_REL"

"$PYTHON" - <<PY
import json, os, datetime
manifest = "$MANIFEST_FILE"
ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
target = int("$TARGET")
m = {}
if os.path.exists(manifest):
    m = json.load(open(manifest))
m.setdefault("processed", {})
import subprocess
for line in open("$MANIFEST"):
    line = line.strip()
    if not line:
        continue
    handle, branch, marker = line.split(":")
    sha = subprocess.check_output(
        ["git", "ls-remote", "origin", "refs/heads/" + branch],
        text=True).split()[0] if branch else ""
    if not sha:
        continue
    m["processed"][sha] = {
        "branch": branch,
        "handle": handle,
        "round": target,
        "harvested_at": ts,
    }
os.makedirs(os.path.dirname(manifest), exist_ok=True)
with open(manifest, "w") as f:
    json.dump(m, f, indent=2, sort_keys=True)
    f.write("\n")
print(f"  recorded {len(open('$MANIFEST').readlines())} branch(es) in {manifest}")
print(f"  total processed: {len(m['processed'])}")
PY

# 6. Stage to inf-spork-r${TARGET}.* for the battery.
echo ""
echo "── 6. staging harvested → inf-spork-r${TARGET} format ──"
"$PYTHON" scripts/stage_inf_spork.py "$TARGET"

# 7. Run battery.
echo ""
echo "── 7. running 7-dataset eval battery ──"
BATTERY_OUT="workers/dispatcher/harvest-${N_WORKERS}way-r${TARGET}/eval_battery.jsonl"
MMLLM_ENABLE_PKM_CPP=true \
  MMLLM_INF_BASE="/tmp/mmllm-cpu/inf-spork-r${TARGET}.fim" \
  MMLLM_INF_BANK="/tmp/mmllm-cpu/inf-spork-r${TARGET}.bank" \
  MMLLM_BATTERY_OUT="$BATTERY_OUT" \
  "$PYTHON" scripts/run_eval_battery.py 2>&1 | tail -30

# 8. Generate results.md with comparison to prior.
echo ""
echo "── 8. generating results.md (R${PRIOR} vs R${TARGET}) ──"
"$PYTHON" scripts/generate_harvest_results.py "$PRIOR" "$TARGET" --n-workers "$N_WORKERS"

# 9. Generate next-round dispatch prompt.
NEXT=$((TARGET + 10))
DISPATCH_OUT="docs/spork-chain-diverse-dispatch-r${NEXT}.md"
if [ -f scripts/generate_dispatch_prompt.py ]; then
  echo ""
  echo "── 9. generating dispatch prompt for R${TARGET}→R${NEXT} ──"
  "$PYTHON" scripts/generate_dispatch_prompt.py "$TARGET" "$NEXT" --n-workers "$N_WORKERS" \
    --out "$DISPATCH_OUT"
else
  echo "  (skipping — scripts/generate_dispatch_prompt.py not present yet)"
fi

# 10. Commit + push.
if [ "$PUSH" = "true" ]; then
  echo ""
  echo "── 10. committing + pushing to ${DISPATCHER_BRANCH} ──"
  git add scripts/ workers/dispatcher/ docs/ "$MANIFEST_FILE" 2>/dev/null || true
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
