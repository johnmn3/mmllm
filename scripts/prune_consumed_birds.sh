#!/usr/bin/env bash
# prune_consumed_birds.sh — delete THIS repo's (origin's) consumed bird branches.
#
# A stable per-bird branch (claude/train-<tag>-<id>-<HANDLE>) is force-updated
# each round its bird runs. Once the chain head advances past a branch's latest
# round, that branch is consumed (its delta was folded) or permanently
# un-foldable — its tip just pins ~130 MB of delta. Delete branches whose latest
# round < the chain head. SAFE: never deletes a branch at/after the head (still
# foldable), matching scripts/harvest_action.sh's prune_consumed_bird_branches.
#
# Runs where a write-capable token actually exists for the target repo:
#   - harvest path → prunes UPSTREAM (harvest_action.sh, inline)
#   - bird path (train.sh) → prunes its own FORK, which the upstream harvest has
#     no perms to touch and the schedule-only branch-janitor never reaches (cron
#     workflows don't fire on forks).
#
# Env: PCB_TRAIN_PREFIX (e.g. "claude/train-sym24-"), PCB_HEAD_ROUND (int),
#      PCB_REPO (default $GITHUB_REPOSITORY), PCB_DRY_RUN (true = preview only).
set -uo pipefail

PREFIX="${PCB_TRAIN_PREFIX:?prune_consumed_birds: PCB_TRAIN_PREFIX required}"
HEAD_ROUND="${PCB_HEAD_ROUND:?prune_consumed_birds: PCB_HEAD_ROUND required}"
REPO="${PCB_REPO:-${GITHUB_REPOSITORY:-}}"
DRY="${PCB_DRY_RUN:-false}"

[ -n "$REPO" ] || { echo "prune_consumed_birds: no repo — skip"; exit 0; }
command -v gh >/dev/null 2>&1 || { echo "prune_consumed_birds: no gh — skip"; exit 0; }
case "$HEAD_ROUND" in ''|*[!0-9]*) echo "prune_consumed_birds: bad head round '$HEAD_ROUND' — skip"; exit 0;; esac

# Rounds present in a bird branch's OWN payload dir (workers/<HANDLE>/...).
# blob:none keeps the per-branch fetch to ~1-5 MB (trees only, no payload).
_rounds_in_branch() {
  local br="$1"
  git fetch origin "$br" --depth=1 --filter=blob:none >/dev/null 2>&1 || return 0
  local _h="${br#"$PREFIX"}"; _h="${_h#*-}"   # strip "<prefix>" then "<id>-"
  git ls-tree -r --name-only "origin/$br" 2>/dev/null \
    | sed -nE "s|^workers/${_h}/chain-design-r([0-9]+)/.*|\1|p" | sort -un
}

echo "+ pruning consumed bird branches on $REPO (latest round < head r${HEAD_ROUND})$([ "$DRY" = true ] && echo ' [DRY RUN]')..."
n=0
while IFS= read -r br; do
  [ -z "$br" ] && continue
  maxr=$(_rounds_in_branch "$br" | sort -n | tail -1)
  [ -z "$maxr" ] && continue
  if [ "$maxr" -lt "$HEAD_ROUND" ]; then
    if [ "$DRY" = "true" ]; then
      echo "    would delete (r${maxr} < r${HEAD_ROUND}): ${br}"; n=$((n + 1))
    elif gh api -X DELETE "repos/${REPO}/git/refs/heads/${br}" >/dev/null 2>&1; then
      echo "    deleted (r${maxr} < r${HEAD_ROUND}): ${br}"; n=$((n + 1))
    fi
  fi
done < <(git ls-remote origin "refs/heads/${PREFIX}*" 2>/dev/null | awk '{print $2}' | sed 's|^refs/heads/||')
[ "$DRY" = "true" ] && echo "    would prune ${n} consumed bird branch(es)" || echo "    pruned ${n} consumed bird branch(es)"
