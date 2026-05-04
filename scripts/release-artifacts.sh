#!/usr/bin/env bash
# Publish the inference artifact bundle as a GitHub Release.
#
# Run this from any machine that has the artifacts cached locally
# (e.g., after pulling them from Modal volume into /tmp/local-bench).
# Requires `gh` CLI (https://cli.github.com) authenticated to the
# target repo.
#
# Usage:
#   scripts/release-artifacts.sh <tag> <artifact-dir>
#
# Example:
#   scripts/release-artifacts.sh v0.1-bench /tmp/local-bench
#
# After release lands, laptop clients run:
#   mmllm fetch-artifacts ./mmllm-artifacts \
#     https://github.com/<owner>/<repo>/releases/download/v0.1-bench
# (or set MMLLM_ARTIFACTS_URL and skip the second arg)

set -euo pipefail

TAG="${1:-v0.1-bench}"
SRC="${2:-/tmp/local-bench}"
REPO_OWNER="${REPO_OWNER:-johnmn3}"
REPO_NAME="${REPO_NAME:-mmllm}"

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: gh CLI not found. Install from https://cli.github.com" >&2
  exit 1
fi

DENSE="${SRC}/pile-github.bin.ckpts/step-305000/dense.pt"
BANK_FILES=(
  "${SRC}/pile-bank-3tier-int8.0.int8.bin"
  "${SRC}/pile-bank-3tier-int8.1.int8.bin"
  "${SRC}/pile-bank-3tier-int8.2.int8.bin"
  "${SRC}/pile-bank-3tier-int8.3.int8.bin"
  "${SRC}/pile-bank-3tier-int8.4.int8.bin"
)

# Verify everything exists at sane sizes before uploading.
echo "verifying source artifacts at ${SRC}/..."
[[ -f "${DENSE}" ]] || { echo "  missing: ${DENSE}" >&2; exit 1; }
for f in "${BANK_FILES[@]}"; do
  [[ -f "$f" ]] || { echo "  missing: ${f}" >&2; exit 1; }
  size=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f")
  if [[ $size -lt 100000000 ]]; then
    echo "  suspicious size for $f: $size bytes" >&2
    exit 1
  fi
done
echo "  all 6 files present"

# `gh release create` accepts files inline; relabel to drop SRC prefix
# so the release-side filenames are clean.
RELABELED=()
RELABELED+=("${DENSE}#dense.pt")
for f in "${BANK_FILES[@]}"; do
  name=$(basename "$f")
  RELABELED+=("${f}#${name}")
done

echo
echo "creating release ${TAG} on ${REPO_OWNER}/${REPO_NAME}..."
gh release create "${TAG}" \
  --repo "${REPO_OWNER}/${REPO_NAME}" \
  --title "mmllm 5B-plain inference bundle (${TAG})" \
  --notes "Trained mmLLM checkpoint + int8-quantized bank for inference benches.

  - Dense weights: 47 MB (fp32, 10M params)
  - Bank V int8: 5 × 905 MB = ~4.5 GB total
  - Quality: BPC=1.273 on Pile-Github val, ablation Δ=+4.77

  Fetch: \`mmllm fetch-artifacts ./mmllm-artifacts\`
  (set MMLLM_ARTIFACTS_URL or pass URL as second arg to override default)" \
  "${RELABELED[@]}"

echo
echo "release published. Laptop client can now run:"
echo "  mmllm fetch-artifacts ./mmllm-artifacts \\"
echo "    https://github.com/${REPO_OWNER}/${REPO_NAME}/releases/download/${TAG}"
