#!/usr/bin/env bash
# migrate_lean.sh — ONE-TIME migration to the lean repo.
#
# Moves every large blob currently committed in main's tree out to GitHub
# Release assets, then rewrites main to a single orphan commit of the resulting
# lean tree. After this, the git tree is ~tens of MB, so shallow-clone bird
# pushes carry only their own small objects (no more ~1 GB packs / HTTP-500s),
# and per-round growth is gone (harvests commit manifest-only).
#
# What moves where:
#   - corpora        → release assets-corpora-v1        (tarball)
#   - wheels         → release assets-wheels-v1         (tarball)
#   - core/round-6   → release assets-baseline-round6-v1 (tarball)
#   - chain V_net/dense (genesis + every harvest head) → per-round releases
#     via scripts/chain_assets.py (manifest.json stays committed)
#
# SQUASH_DRY_RUN=true (default): do the uploads + local index changes + report
# the projected lean tree size, but DO NOT force-push. Uploads are idempotent
# (--clobber), so a dry run then a real run is safe.
set -euo pipefail

DRY="${SQUASH_DRY_RUN:-true}"
REPO="${GITHUB_REPOSITORY:-johnmn3/mmllm}"
CHAIN="${MMLLM_CHAIN_PREFIX:-sym24}"
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

sha256_of() { shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1 || sha256sum "$1" | cut -d' ' -f1; }
tree_mb()   { git ls-tree -r -l "$1" | awk '{s+=$4} END {printf "%d", s/1048576}'; }

echo "▶ lean-migrate on $REPO  chain=$CHAIN  dry_run=$DRY"
echo "  main tree now: $(tree_mb HEAD) MB committed"

# --- 1) Static bundles → release tarballs (idempotent) --------------------- #
publish_static() {  # bundle  srcdir  tag
  local bundle="$1" dir="$2" tag="$3"
  if [ ! -d "$dir" ] || [ -z "$(ls -A "$dir" 2>/dev/null)" ]; then
    echo "  • $bundle: $dir absent/empty — skip"; return 0
  fi
  local tar="/tmp/$bundle.tar"
  tar -cf "$tar" -C "$dir" .
  sha256_of "$tar" > "$tar.sha256"
  gh release view "$tag" --repo "$REPO" >/dev/null 2>&1 \
    || gh release create "$tag" --repo "$REPO" --target main --title "$tag" \
         --notes "Static asset bundle '$bundle' (kept out of git history)."
  gh release upload "$tag" "$tar" "$tar.sha256" --repo "$REPO" --clobber
  echo "  • $bundle: uploaded $(du -h "$tar" | cut -f1) → $tag"
  rm -f "$tar" "$tar.sha256"   # free runner disk before the next bundle
}
publish_static corpora         workers/dispatcher/corpora        assets-corpora-v1
publish_static wheels          workers/dispatcher/deps/wheels    assets-wheels-v1
publish_static baseline-round6 core/round-6                      assets-baseline-round6-v1

# --- 2) Chain blobs → per-round releases (genesis + every harvest head) ---- #
GENESIS="workers/dispatcher/harvest-0way-r0_${CHAIN}/round-0"
echo "▶ publishing chain blobs (genesis + harvest heads) via chain_assets.py…"
while IFS=$'\t' read -r d rnd; do
  [ -z "$d" ] && continue
  if [ "$rnd" = "0" ]; then
    python3 scripts/chain_assets.py publish "$d" --round 0 --chain "$CHAIN" --repo "$REPO"
  else
    python3 scripts/chain_assets.py publish "$d" --round "$rnd" --chain "$CHAIN" \
      --repo "$REPO" --reference-anchor "$GENESIS" --reference-round 0
  fi
done < <(python3 - "$CHAIN" <<'PYEOF'
import glob, os, re, sys
chain = sys.argv[1]
for d in sorted(glob.glob(f"workers/dispatcher/harvest-*-r*_{chain}/round-*")):
    m = re.search(rf"harvest-(?:fold)?\d+way-r(\d+)_{re.escape(chain)}/round-(\d+)$", d)
    if not m:
        continue
    print(f"{d}\t{int(m.group(2))}")
PYEOF
)

# --- 3) Untrack the static big files (now in release tarballs) ------------- #
mapfile -t BIG < <(git ls-files | grep -E \
  '^(workers/dispatcher/corpora/.*\.(bin|part-[0-9]+)|workers/dispatcher/deps/wheels/.*\.(whl|part-[0-9]+)|core/round-6/.*\.(bin|pt))$' || true)
if [ "${#BIG[@]}" -gt 0 ]; then
  git rm --cached -q "${BIG[@]}"
  echo "  untracked ${#BIG[@]} static big file(s)"
fi

# --- 4) Stage manifests + deletions ---------------------------------------- #
git add -A
echo "▶ projected lean tree: $(tree_mb $(git write-tree)) MB"

if [ "$DRY" = "true" ]; then
  echo "✓ DRY RUN — assets uploaded (idempotent); NOT committing or force-pushing."
  echo "  re-run with dry_run=false to rewrite main to the lean tree."
  exit 0
fi

# --- 5) Commit the lean tree, then orphan-squash + force-push -------------- #
git -c user.name="lean-migrate" -c user.email="lean@github-actions.local" \
    commit -q -m "lean-migrate: statics + chain blobs → release assets" || echo "  (nothing new to commit)"

# Safety: genesis manifest + chain manifests must exist in the new tree.
test -f "$GENESIS/manifest.json" || { echo "ABORT: genesis manifest missing — refusing to squash" >&2; exit 1; }

NEWTREE=$(git write-tree)
STAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
ORPHAN=$(git commit-tree "$NEWTREE" -m "lean repo (assets in releases) — migrated $STAMP")
echo "▶ force-pushing orphan-squashed lean main ($ORPHAN, tree $(tree_mb "$NEWTREE") MB)…"
git push --force origin "$ORPHAN:main"
echo "✓ lean-migrate done — repo shrinks after GitHub GC; forks self-resync; birds push thin."
