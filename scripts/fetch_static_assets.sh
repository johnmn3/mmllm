#!/usr/bin/env bash
# fetch_static_assets.sh <bundle>
#
# Download + extract a STATIC asset bundle from its GitHub Release on the
# upstream repo. These large, never-changing files (training corpora, dependency
# wheels, the round-6 warm-start baseline) used to be committed into the git tree
# — ~3.5 GB of it — which made the tree 5.2 GB. Every shallow-clone bird push
# then shipped a fat pack (the in-tree blobs the remote couldn't confirm it had)
# and tripped GitHub's HTTP-500 large-pack wall. Moving them to release tarballs
# fetched on demand keeps the tree (and every push pack) tiny.
#
#   bundle ∈ { corpora | wheels | baseline-round6 }
#
# Idempotent: a bundle whose target dir already holds the extracted marker is
# skipped (local clones / warm runners don't re-download). Forks read the
# UPSTREAM repo's releases (override with MMLLM_ASSETS_REPO).
set -euo pipefail

BUNDLE="${1:?usage: fetch_static_assets.sh <corpora|wheels|baseline-round6>}"
REPO="${MMLLM_ASSETS_REPO:-johnmn3/mmllm}"
ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)

case "$BUNDLE" in
  corpora)         TAG="assets-corpora-v1";   DEST="$ROOT/workers/dispatcher/corpora" ;;
  wheels)          TAG="assets-wheels-v1";     DEST="$ROOT/workers/dispatcher/deps/wheels" ;;
  baseline-round6) TAG="assets-baseline-round6-v1"; DEST="$ROOT/core/round-6" ;;
  *) echo "fetch_static_assets: unknown bundle '$BUNDLE'" >&2; exit 2 ;;
esac

MARKER="$DEST/.asset-$TAG.ok"
if [ -f "$MARKER" ]; then
  echo "▶ static bundle '$BUNDLE' already present ($MARKER) — skip"
  exit 0
fi

TARNAME="$BUNDLE.tar"
echo "▶ fetching static bundle '$BUNDLE' from release $TAG ($REPO) → $DEST"
mkdir -p "$DEST"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Download tar + its sha256 sidecar; verify before extracting.
gh release download "$TAG" --repo "$REPO" --pattern "$TARNAME" --pattern "$TARNAME.sha256" \
  --dir "$TMP" --clobber
if [ ! -f "$TMP/$TARNAME" ]; then
  echo "fetch_static_assets: $TARNAME not found in release $TAG" >&2
  exit 1
fi
if [ -f "$TMP/$TARNAME.sha256" ]; then
  want=$(cut -d' ' -f1 < "$TMP/$TARNAME.sha256")
  got=$(shasum -a 256 "$TMP/$TARNAME" 2>/dev/null | cut -d' ' -f1 || sha256sum "$TMP/$TARNAME" | cut -d' ' -f1)
  if [ "$want" != "$got" ]; then
    echo "fetch_static_assets: sha256 mismatch for $TARNAME ($got != $want)" >&2
    exit 1
  fi
fi

tar -xf "$TMP/$TARNAME" -C "$DEST"
touch "$MARKER"
echo "  extracted $(find "$DEST" -type f ! -name '.asset-*.ok' | wc -l | tr -d ' ') file(s) into $DEST"
