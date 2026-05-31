#!/usr/bin/env bash
set -euo pipefail
# Branch janitor — auto-prune stale claude/* branches so the repo does not
# re-accumulate the hundreds of bird-harvest + session branches that bloated it
# to 64 GB (the Stage-1 sweep on 2026-05-27 deleted 325 of them by hand).
#
# Safe by construction:
#   - only ever touches refs under claude/ (never main, never *-curriculum*)
#   - skips any branch that currently backs an open PR
#   - only deletes a branch whose TIP COMMIT is older than a retention window
#     (claude/train-* bird branches: short — they are folded into main hourly;
#      other claude/* session branches: longer)
#   - JANITOR_DRY_RUN=true prints what it would delete and changes nothing
#
# Requires gh with GH_TOKEN/GITHUB_TOKEN (contents:write to delete refs).

REPO="${GITHUB_REPOSITORY:-johnmn3/mmllm}"
DRY_RUN="${JANITOR_DRY_RUN:-false}"
TRAIN_RETENTION_DAYS="${JANITOR_TRAIN_RETENTION_DAYS:-1}"
OTHER_RETENTION_DAYS="${JANITOR_OTHER_RETENTION_DAYS:-7}"
NOW=$(date -u +%s)

echo "branch-janitor on $REPO (dry_run=$DRY_RUN train_retention=${TRAIN_RETENTION_DAYS}d other_retention=${OTHER_RETENTION_DAYS}d)"

# Branches that currently back an open PR — never delete these.
gh api --paginate "/repos/$REPO/pulls?state=open&per_page=100" \
  --jq '.[].head.ref' 2>/dev/null | sort -u > /tmp/janitor-openpr.txt || true
gh api --paginate "/repos/$REPO/branches?per_page=100" \
  --jq '.[].name' > /tmp/janitor-branches.txt

deleted=0; kept=0; skipped_pr=0
while IFS= read -r br; do
  # Defensive: only ever manage claude/* (main / *-curriculum* fall through to keep).
  case "$br" in
    claude/*) : ;;
    *) kept=$((kept + 1)); continue ;;
  esac
  if grep -qxF "$br" /tmp/janitor-openpr.txt; then
    echo "  skip (open PR): $br"; skipped_pr=$((skipped_pr + 1)); continue
  fi
  case "$br" in
    claude/train-*) ret="$TRAIN_RETENTION_DAYS" ;;
    *)              ret="$OTHER_RETENTION_DAYS" ;;
  esac
  ts=$(gh api "/repos/$REPO/commits/$br" --jq '.commit.committer.date' 2>/dev/null || true)
  if [ -z "$ts" ]; then echo "  skip (no commit date): $br"; kept=$((kept + 1)); continue; fi
  age=$(( (NOW - $(date -u -d "$ts" +%s)) / 86400 ))
  if [ "$age" -ge "$ret" ]; then
    if [ "$DRY_RUN" = "true" ]; then
      echo "  [dry-run] would delete $br (age ${age}d >= ${ret}d)"
    elif gh api -X DELETE "/repos/$REPO/git/refs/heads/$br" >/dev/null 2>&1; then
      echo "  deleted $br (age ${age}d)"
    else
      echo "  FAILED to delete $br"; kept=$((kept + 1)); continue
    fi
    deleted=$((deleted + 1))
  else
    kept=$((kept + 1))
  fi
done < /tmp/janitor-branches.txt

echo "branch-janitor done: deleted=$deleted kept=$kept skipped_open_pr=$skipped_pr dry_run=$DRY_RUN"
