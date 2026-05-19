#!/usr/bin/env bash
# Harvest a smoke-r<N> wave: row-aware FedAvg merge of all bird deltas
# + dense average. Output to workers/dispatcher/harvest-<W>way-r<N>/.
#
# Usage:
#   bash scripts/harvest_action.sh [target_round] [extra_ref ...]
#
# If target_round is empty, auto-detects the latest unharvested round:
# the highest N with origin/claude/smoke-r<N>-* branches but no
# corresponding workers/dispatcher/harvest-*-r<N>/ dir on this branch.
#
# extra_ref args are passed as additional refs to harvest from (e.g.,
# "pr-12" for a fetched fork PR ref). They must contain a bird payload
# at workers/<HANDLE>/chain-design-r<TARGET>/ with the same layout as
# a smoke.sh publish.
#
# Output is intentionally lean — sparse deltas + averaged dense only,
# no opt-state. Bird branches retain opt-state if anyone needs it for
# warmstarting. Total harvest size: ~135 MB regardless of bird count.

set -euo pipefail

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

TARGET_ROUND="${1:-}"
shift || true
EXTRA_REFS=("$@")

# --- 1) Auto-detect target round if not specified --------------------
if [ -z "$TARGET_ROUND" ]; then
  echo "▶ auto-detecting latest unharvested round…"
  ALL_ROUNDS=$(git ls-remote origin 'refs/heads/claude/smoke-r*' 2>/dev/null \
    | grep -oE 'smoke-r[0-9]+' | sed 's/smoke-r//' | sort -un)
  echo "  smoke-r rounds on origin: $(echo "$ALL_ROUNDS" | tr '\n' ' ')"
  for R in $(echo "$ALL_ROUNDS" | tac); do
    if ! compgen -G "workers/dispatcher/harvest-*-r${R}" > /dev/null 2>&1; then
      TARGET_ROUND=$R
      break
    fi
  done
  if [ -z "$TARGET_ROUND" ]; then
    echo "▶ no unharvested rounds found. Already-harvested dirs:"
    ls -d workers/dispatcher/harvest-*-r*/ 2>/dev/null | head -10
    exit 0
  fi
fi
echo "▶ target round: $TARGET_ROUND"

# --- 2) Discover bird branches for this round ------------------------
BIRD_REFS=()
while read -r line; do
  ref=$(echo "$line" | awk '{print $2}' | sed 's|^refs/heads/|origin/|')
  [ -n "$ref" ] && BIRD_REFS+=("$ref")
done < <(git ls-remote origin "refs/heads/claude/smoke-r${TARGET_ROUND}-*" 2>/dev/null)

for ref in "${EXTRA_REFS[@]}"; do
  BIRD_REFS+=("$ref")
done

N=${#BIRD_REFS[@]}
if [ $N -eq 0 ]; then
  echo "ERROR: no birds found for round $TARGET_ROUND" >&2
  exit 1
fi
echo "▶ found $N birds:"
for ref in "${BIRD_REFS[@]}"; do echo "  - $ref"; done

# --- 3) Fetch each bird, extract chain-design-r<N> dir ---------------
WORK=/tmp/harvest-r${TARGET_ROUND}
rm -rf "$WORK"
mkdir -p "$WORK"

HANDLES=()
BIRD_DIRS=()
for ref in "${BIRD_REFS[@]}"; do
  case "$ref" in
    origin/claude/*)
      BRANCH="${ref#origin/}"
      echo "▶ fetching $BRANCH…"
      git fetch origin "$BRANCH" --depth=1 2>&1 | tail -1
      ;;
  esac
  # Find the bird's handle by inspecting the tree
  HANDLE=$(git ls-tree -r --name-only "$ref" 2>/dev/null \
    | grep -oE "^workers/[^/]+/chain-design-r${TARGET_ROUND}/" \
    | head -1 | sed 's|^workers/||;s|/.*||')
  if [ -z "$HANDLE" ]; then
    echo "  WARN: $ref has no workers/<HANDLE>/chain-design-r${TARGET_ROUND}/ — skipping"
    continue
  fi
  echo "  handle: $HANDLE"
  mkdir -p "$WORK/$HANDLE"
  git archive "$ref" "workers/$HANDLE/chain-design-r${TARGET_ROUND}/" 2>/dev/null \
    | tar -x -C "$WORK/$HANDLE/" --strip-components=3
  HANDLES+=("$HANDLE")
  BIRD_DIRS+=("$WORK/$HANDLE")
done

N=${#BIRD_DIRS[@]}
if [ $N -eq 0 ]; then
  echo "ERROR: extracted 0 bird payloads" >&2
  exit 1
fi

# --- 4) FedAvg merge -------------------------------------------------
WAYS="${N}way"
OUT="workers/dispatcher/harvest-${WAYS}-r${TARGET_ROUND}/round-${TARGET_ROUND}"
mkdir -p "$OUT"

echo "▶ FedAvg merging delta-sparse-net across $N birds…"
python3 scripts/_delta_sparse_net.py fedavg "$OUT" "${BIRD_DIRS[@]}" 2>&1 | tail -3

echo "▶ averaging dense.pt across $N birds…"
python3 - "$OUT" "${BIRD_DIRS[@]}" <<'PYEOF'
import torch, os, sys
out = sys.argv[1]
birds = sys.argv[2:]

denses = []
for b in birds:
    p = f"{b}/dense.pt"
    if os.path.exists(p):
        denses.append(torch.load(p, map_location="cpu", weights_only=False))
if not denses:
    print("  WARN: no dense.pt found across birds")
    sys.exit(0)

n = len(denses[0])
assert all(len(d) == n for d in denses), f"len mismatch: {[len(d) for d in denses]}"
avg = []
for i in range(n):
    vals = [d[i] for d in denses]
    if isinstance(vals[0], torch.Tensor):
        avg.append((sum(v.float() for v in vals) / len(vals)).to(vals[0].dtype))
    else:
        avg.append(vals[0])
torch.save(avg, f"{out}/dense.pt")
print(f"  dense.pt averaged from {len(denses)}/{len(birds)} birds → {out}/dense.pt ({os.path.getsize(out+'/dense.pt')/1e6:.1f} MB)")
PYEOF

# --- 5) Harvest meta -------------------------------------------------
HARVEST_DIR="workers/dispatcher/harvest-${WAYS}-r${TARGET_ROUND}"

# Pull each bird's ctrl_bpc + branch from its meta.json
BIRDS_JSON="["
for i in "${!HANDLES[@]}"; do
  h="${HANDLES[$i]}"
  br="${BIRD_REFS[$i]}"
  ctrl=$(python3 -c "
import json
try:
    print(json.load(open('$WORK/$h/meta.json')).get('final_ctrl_bpc', 'unknown'))
except: print('unknown')
" 2>/dev/null)
  [ $i -gt 0 ] && BIRDS_JSON+=","
  BIRDS_JSON+="
    {\"handle\": \"$h\", \"branch\": \"$br\", \"ctrl_bpc\": \"$ctrl\"}"
done
BIRDS_JSON+="
  ]"

cat > "$HARVEST_DIR/harvest_meta.json" <<EOF
{
  "target_round": $TARGET_ROUND,
  "n_workers": $N,
  "wave": "smoke-r${TARGET_ROUND}",
  "workers": $BIRDS_JSON,
  "harvested_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "harvester": "scripts/harvest_action.sh (GH Action)",
  "note": "Lean harvest — sparse deltas + averaged dense only, no opt-state. Bird branches retain opt-state if needed for warmstart."
}
EOF

echo "▶ harvest done:"
echo "  dir: $HARVEST_DIR"
echo "  files: $(ls "$OUT" | wc -l)"
echo "  size: $(du -sh "$HARVEST_DIR" | cut -f1)"

# Clean up working dir to free runner disk
rm -rf "$WORK"

echo "✓ DONE"
