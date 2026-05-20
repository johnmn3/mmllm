#!/usr/bin/env bash
# Commit + push a new harvest dir in size-bounded chunks.
#
# Why: a single push of the ~150 MB harvest dir hits GitHub's HTTP
# proxy sideband-disconnect threshold inconsistently. r31 (145 MB) got
# through; r36 (154 MB) hung with "send-pack: unexpected disconnect
# while reading sideband packet", and the retry loop then exhausted
# the 120-min job budget. The "Everything up-to-date" message on the
# second attempt is misleading — git's ref tracking saw the first
# attempt's local refs but origin/main never actually advanced.
#
# Fix: split the commit into ~5 size-bounded pieces (scaffolding +
# supersession deletions, then delta-sparse-net pids 0-7 / 8-15 /
# 16-23 / 24-31, then trailing). Each individual push is ~30-40 MB,
# well below where the disconnect starts happening. Partial progress
# is preserved on failure of a later chunk.
#
# Assumes harvest_action.sh has already:
#   - laid out the new harvest dir at $NEW_DIR/round-<R>/
#   - staged deletions of any superseded harvest-*-r<R>/ dirs via git rm -rf

set -euo pipefail

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Pick the new harvest dir. Accept as arg for testability; else auto-
# detect from the most recently mtime'd harvest-*-r*/ in the worktree.
NEW_DIR="${1:-}"
if [ -z "$NEW_DIR" ]; then
  NEW_DIR=$(ls -dt workers/dispatcher/harvest-*-r*/ 2>/dev/null \
    | head -1 | sed 's|/$||')
fi
if [ -z "$NEW_DIR" ] || [ ! -d "$NEW_DIR" ]; then
  echo "▶ harvest_push: no harvest dir to commit"
  exit 0
fi
echo "▶ harvest_push: chunking $NEW_DIR"

ROUND_DIR=$(ls -d "$NEW_DIR"/round-*/ 2>/dev/null | head -1 | sed 's|/$||')
if [ -z "$ROUND_DIR" ] || [ ! -d "$ROUND_DIR" ]; then
  echo "ERROR: $NEW_DIR has no round-*/ subdir" >&2
  exit 1
fi

# --- Helpers ---------------------------------------------------------

# Per-push retry. Uses PIPESTATUS to capture git's real exit code past
# the tee (the previous inline version had `if git push … | tee | tail`
# which always saw tail's exit code 0). Returns 0 on success.
push_with_retry() {
  local label="$1"
  local i out=/tmp/push.out
  for i in 1 2 3 4; do
    git push origin HEAD:main 2>&1 | tee "$out"
    local rc=${PIPESTATUS[0]}
    if [ $rc -eq 0 ] \
       && ! grep -qE 'rejected|hung up|408|disconnect|RPC failed|sideband' "$out"; then
      echo "✓ $label pushed (attempt $i)"
      return 0
    fi
    local wait=$((i * 8))
    echo "▶ $label push attempt $i failed (rc=$rc); retrying in ${wait}s…"
    sleep $wait
  done
  echo "ERROR: $label push failed after 4 attempts" >&2
  return 1
}

# Tripwire: nothing staged should be outside workers/dispatcher/harvest-*-r*/
# (e.g. reassembled wheel parts, accidental worktree pollution).
check_staged_scope() {
  local outside
  outside=$(git diff --cached --name-only \
    | grep -vE '^workers/dispatcher/harvest-[0-9]+way-r[0-9]+/' || true)
  if [ -n "$outside" ]; then
    echo "ERROR: $(echo "$outside" | wc -l) files staged outside harvest dirs:" >&2
    echo "$outside" | head -10 >&2
    exit 1
  fi
}

commit_and_push() {
  local label="$1"
  if git diff --cached --quiet; then
    echo "▶ $label: nothing staged, skipping"
    return 0
  fi
  check_staged_scope
  local n_files
  n_files=$(git diff --cached --name-only | wc -l)
  local bytes
  bytes=$(git diff --cached --name-only -z \
    | xargs -0 -I{} bash -c '[ -f "{}" ] && stat -c %s "{}" 2>/dev/null || echo 0' \
    | awk '{s+=$1} END {print s}')
  printf '  %s: %d files, %.1f MB\n' "$label" "$n_files" "$(echo "$bytes / 1048576" | bc -l)"
  git commit -m "$label" --quiet
  push_with_retry "$label"
}

# --- Stage in chunks -------------------------------------------------

# harvest_action.sh already staged deletions of superseded harvest dirs
# via `git rm -rf`. Reset what's currently staged so we can re-stage in
# controlled chunks (deletions are still reflected in worktree state).
git reset HEAD -- . >/dev/null 2>&1 || true

# Chunk 1 — supersession deletions + scaffolding (manifests, logs,
# wall.tsv, results.md, dense.pt, delta-sparse-net.meta.pt).
# EVERYTHING except the 32 large delta-sparse-net.{0..31}.pt files.
# Re-staging via `git add -A` on the parent picks up deletions; we
# then explicitly unstage the 32 numbered delta files so they go in
# later chunks. Iterating by index avoids shell-glob surprises if
# any happen to be missing.
echo "▶ chunk 1: scaffolding + supersessions"
git add -A workers/dispatcher/ 2>/dev/null || true
for i in $(seq 0 31); do
  f="$ROUND_DIR/delta-sparse-net.$i.pt"
  [ -f "$f" ] && git reset HEAD -- "$f" >/dev/null 2>&1 || true
done
commit_and_push "harvest: $NEW_DIR scaffolding + supersessions"

# Chunks 2..5 — delta-sparse-net.*.pt in groups of 8 (pids 0-7, 8-15,
# 16-23, 24-31). Each chunk is ~40 MB.
for start in 0 8 16 24; do
  end=$((start + 7))
  files=()
  for i in $(seq $start $end); do
    f="$ROUND_DIR/delta-sparse-net.$i.pt"
    [ -f "$f" ] && files+=("$f")
  done
  if [ ${#files[@]} -eq 0 ]; then
    echo "▶ chunk pids $start..$end: no files, skipping"
    continue
  fi
  git add "${files[@]}"
  commit_and_push "harvest: $NEW_DIR pids $start..$end"
done

# Chunk 6 — anything left (defensive; meta.pt, late additions, etc).
git add -A "$NEW_DIR/"
if ! git diff --cached --quiet; then
  commit_and_push "harvest: $NEW_DIR trailing"
fi

echo "✓ harvest pushed in chunks"
