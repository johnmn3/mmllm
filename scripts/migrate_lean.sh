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
# Handles EVERY chain present in the tree, not just $CHAIN: sym24 (suffixed,
# anchor harvest-0way-r0_sym24) AND the legacy/orig chain (no suffix, anchor
# harvest-5way-r10). An anchor dir carries full V_net.*.bin → publish with no
# reference; a delta dir carries delta-sparse-net.*.pt → reference its chain's
# anchor. chain_assets.py git-rm's whatever it uploads.
echo "▶ publishing chain blobs (all chains: anchors + harvest heads) via chain_assets.py…"
while IFS=$'\t' read -r d rnd chain; do
  [ -z "$d" ] && continue
  if ls "$d"/V_net.*.bin >/dev/null 2>&1; then
    # anchor (full V_net) — no reference
    python3 scripts/chain_assets.py publish "$d" --round "$rnd" --chain "$chain" --repo "$REPO"
  else
    if [ -n "$chain" ]; then
      ANCHOR="workers/dispatcher/harvest-0way-r0_${chain}/round-0"; ANCHOR_R=0
    else
      ANCHOR="workers/dispatcher/harvest-5way-r10/round-10"; ANCHOR_R=10
    fi
    python3 scripts/chain_assets.py publish "$d" --round "$rnd" --chain "$chain" \
      --repo "$REPO" --reference-anchor "$ANCHOR" --reference-round "$ANCHOR_R"
  fi
done < <(python3 - <<'PYEOF'
import glob, re
for d in sorted(glob.glob("workers/dispatcher/harvest-*-r*/round-*")):
    m = re.search(r"harvest-(?:fold)?\d+way-r(\d+)(?:_([A-Za-z0-9]+))?/round-(\d+)$", d)
    if not m:
        continue
    rnd, chain = int(m.group(3)), (m.group(2) or "")
    print(f"{d}\t{rnd}\t{chain}")
PYEOF
)

# --- 3) Untrack the static big files (now in release tarballs) ------------- #
# corpora / wheels / round-6 baseline, PLUS a safety-net for any harvest blob
# the chain loop above didn't already git-rm (V_net / delta / opt under any
# harvest dir). manifest.json + small meta stay committed.
mapfile -t BIG < <(git ls-files | grep -E \
  '^(workers/dispatcher/corpora/.*\.(bin|part-[0-9]+)|workers/dispatcher/deps/wheels/.*\.(whl|part-[0-9]+)|core/round-6/.*\.(bin|pt)|workers/dispatcher/harvest-.*/(V_net\.[0-9]+\.bin|delta-sparse-net\..*\.pt|opt-sparse-net\..*\.pt|dense\.pt))$' || true)
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

# --- 5) Orphan-squash the staged lean tree + force-push -------------------- #
# git identity (the lean-migrate workflow configures none; commit-tree needs it).
git config user.email "lean@github-actions.local"
git config user.name  "lean-migrate"

# Safety: the production-chain genesis manifest must exist in the staged tree
# (proves chain_assets ran + wrote manifests before we drop the blobs).
GENESIS="workers/dispatcher/harvest-0way-r0_${CHAIN}/round-0"
test -f "$GENESIS/manifest.json" || { echo "ABORT: genesis manifest missing ($GENESIS) — refusing to squash" >&2; exit 1; }

# `git add -A` above already staged the manifests + blob removals. Orphan-commit
# that index tree (no parent → history dropped) and force-push it as main; no
# intermediate commit needed.
NEWTREE=$(git write-tree)
STAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
ORPHAN=$(git commit-tree "$NEWTREE" -m "lean repo (assets in releases) — migrated $STAMP")
echo "▶ force-pushing orphan-squashed lean main ($ORPHAN, tree $(tree_mb "$NEWTREE") MB)…"
git push --force origin "$ORPHAN:main"
echo "✓ lean-migrate done — repo shrinks after GitHub GC; forks self-resync; birds push thin."
