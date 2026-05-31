#!/usr/bin/env bash
# squash_main.sh — reclaim main's history bloat by rewriting main to a single
# orphan commit of the CURRENT tree. The working tree is byte-identical; only
# the dead commit history (pruned per-round harvest deltas, ~290MB/round
# retained even after the HEAD-prune) is dropped, shrinking the repo + the
# shared fork-object pool. The orphan reuses existing blobs, so the push is
# tiny (commit+tree metadata only — no large-pack 500). Forks re-sync via
# train.sh's merge-upstream / force-reset / sidecar fallbacks (built for exactly
# this post-squash divergence). Threshold-gated so it only fires when bloated.
#
# Env: SQUASH_DRY_RUN (true=preview), SQUASH_THRESHOLD_GB (default 8).
set -euo pipefail
DRY="${SQUASH_DRY_RUN:-false}"
THRESH_GB="${SQUASH_THRESHOLD_GB:-8}"
REPO="${GITHUB_REPOSITORY:-johnmn3/mmllm}"

size_kb=$(gh api "repos/$REPO" --jq '.size' 2>/dev/null || echo 0)
size_gb=$(( size_kb / 1048576 ))
echo "▶ repo $REPO size: ${size_gb} GB (threshold ${THRESH_GB} GB)"
if [ "$size_gb" -lt "$THRESH_GB" ]; then
  echo "✓ under threshold — no squash needed"; exit 0
fi

# Safety: refuse to squash a broken/empty tree.
if [ ! -d workers/dispatcher ]; then
  echo "ERROR: workers/dispatcher missing — refusing to squash (bad checkout)" >&2; exit 1
fi
genesis=$(ls -d workers/dispatcher/harvest-0way-r0* 2>/dev/null | head -1 || true)
heads=$(ls -d workers/dispatcher/harvest-*way-r*_* 2>/dev/null | grep -cE 'r[0-9]+_' || echo 0)
if [ -z "$genesis" ] || [ "$heads" -lt 1 ]; then
  echo "ERROR: genesis ($genesis) or harvest heads ($heads) missing — refusing to squash" >&2; exit 1
fi
echo "  safety OK: genesis=$(basename "$genesis"), $heads harvest head(s)"

CUR=$(git rev-parse HEAD)
git config user.name  "history-squash"
git config user.email "squash@github-actions.local"

# Orphan commit = exact current tree (no parent → old history becomes unreachable).
git checkout --orphan _squash >/dev/null 2>&1
git add -A
git commit -q -m "Squash main history to current tree (reclaim storage) [auto]

Drops dead per-round harvest history retained only in main's commit history
and pinned in GitHub's shared fork-object pool. Working tree byte-identical to
$CUR. Forks re-sync via train.sh merge-upstream / force-reset / sidecar."
NEW=$(git rev-parse HEAD)

# HARD safety: the squashed tree MUST be byte-identical to the original.
if [ "$(git rev-parse "${CUR}^{tree}")" != "$(git rev-parse "${NEW}^{tree}")" ]; then
  echo "ERROR: squashed tree != original tree — refusing to force-push" >&2; exit 1
fi
echo "  squash $CUR -> $NEW (tree identical ✓)"

if [ "$DRY" = "true" ]; then
  echo "✓ DRY RUN — would force-push $NEW to main (not pushing)"; exit 0
fi
git push --force origin "_squash:main"
echo "✓ force-pushed squashed main ($NEW) — repo will shrink after GitHub GC; forks self-resync"
