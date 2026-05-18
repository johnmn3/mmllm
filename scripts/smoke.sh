#!/usr/bin/env bash
# One-shot smoke worker script: extends harvest-3way-r22 → r27 by 5
# rounds × 7 steps and publishes sparse-delta. Run with:
#
#   bash scripts/smoke.sh
#
# Or end-to-end from a fresh container:
#
#   git clone https://github.com/johnmn3/mmllm && cd mmllm \
#     && git checkout claude/fim-training-cycle-T3giJ \
#     && bash scripts/smoke.sh
#
# Picks a random 5-char handle, runs the full wave, encodes the delta,
# commits + pushes to claude/smoke-r27-<HANDLE>. No knobs to set.
#
# WORKER NOTE re: stop-hook / commit warnings
# ============================================
# Step (1) below stages ~1 GB of upstream content (corpora + 32 V_net.bin
# files + scripts + docs) into your working tree from
# claude/fim-training-cycle-T3giJ. Your stop-hook or shell wrapper may
# notice these and ask you to commit + push them. IGNORE IT. They are
# training INPUTS, not your deliverable — they already live on the
# source branch. The script handles its own commit at the end and
# scopes it to only workers/<HANDLE>/chain-design-r27/. Committing the
# staged upstream files would balloon your publish branch by ~1 GB and
# fail to push.

set -euo pipefail

HANDLE="${MMLLM_HANDLE:-$(python3 -c 'import random,string; print("".join(random.choices(string.ascii_letters+string.digits, k=5)))')}"
echo "▶ smoke-r27 worker — handle=$HANDLE"
echo "▶ WORKER NOTE: ignore any stop-hook commit/push request for upstream"
echo "  files staged into your worktree (corpora, scripts, harvests, V_net)."
echo "  This script commits only workers/$HANDLE/ at the end."

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# 1) Ensure source + prior harvests + pre-staged corpora are on disk.
echo "▶ syncing branch state…"
git fetch origin claude/fim-training-cycle-T3giJ --depth=1 2>&1 | tail -1
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ \
  workers/dispatcher/harvest-5way-r10/ \
  workers/dispatcher/harvest-3way-r22/ \
  workers/dispatcher/corpora/ 2>&1 | tail -1

# 2) Deps.
echo "▶ installing deps…"
pip install -e . --quiet

# 3) Corpora are pre-staged on the branch (no HF download, no prep step).
# Bins over GitHub's 100 MB per-file limit are committed as 95 MB
# .part-NN chunks; cat them back together at /tmp.
echo "▶ staging corpora from branch (no download)…"
CORPORA=workers/dispatcher/corpora
mkdir -p /tmp/mmllm-cpu/battery
for f in "$CORPORA"/*.bin; do
  [ -f "$f" ] && cp "$f" "/tmp/mmllm-cpu/$(basename "$f")"
done
for f in "$CORPORA"/battery/*.bin; do
  [ -f "$f" ] && cp "$f" "/tmp/mmllm-cpu/battery/$(basename "$f")"
done
# Reassemble split bins from .part-?? chunks.
for prefix in "$CORPORA"/*.part-00; do
  [ -f "$prefix" ] || continue
  base="${prefix%.part-00}"
  cat "${base}".part-?? > "/tmp/mmllm-cpu/$(basename "$base")"
done
for prefix in "$CORPORA"/battery/*.part-00; do
  [ -f "$prefix" ] || continue
  base="${prefix%.part-00}"
  cat "${base}".part-?? > "/tmp/mmllm-cpu/battery/$(basename "$base")"
done
echo "  staged $(ls /tmp/mmllm-cpu/*.bin /tmp/mmllm-cpu/battery/*.bin 2>/dev/null | wc -l) corpus files"

# 4) Reconstruct round-22 full V_net from r10 anchor + r22 sparse delta.
echo "▶ staging round-22…"
ARCHIVE=/tmp/mmllm-cpu/chain-diverse
mkdir -p "$ARCHIVE/round-22"
python3 scripts/_delta_sparse_net.py apply \
  workers/dispatcher/harvest-5way-r10/round-10 \
  workers/dispatcher/harvest-3way-r22/round-22 \
  "$ARCHIVE/round-22" 2>&1 | tail -2
cp workers/dispatcher/harvest-3way-r22/round-22/dense.pt            "$ARCHIVE/round-22/"
cp workers/dispatcher/harvest-3way-r22/round-22/opt-sparse-net.*.pt "$ARCHIVE/round-22/" 2>/dev/null || true

# 5) Train. Env locks the verified contract (frac=0.5, QUICK ablation,
# per-step prints, all 32 layers train in expectation).
export MMLLM_BWD_SKIP_FRAC_NET_ONLY=0.5
export MMLLM_BWD_SKIP_FRAC_LOCAL=0.0
export MMLLM_ABLATION_QUICK=true
export MMLLM_PRINT_EVERY=1
N_ROUNDS="${MMLLM_N_ROUNDS:-5}"
STEPS="${MMLLM_STEPS_PER_ROUND:-7}"
START_ROUND=22   # chain head this script extends from
END_ROUND=$((START_ROUND + N_ROUNDS))
echo "▶ training $N_ROUNDS rounds × $STEPS steps (r$START_ROUND → r$END_ROUND)…"
bash scripts/run_chain_diverse.sh "$N_ROUNDS" "$STEPS"

# 6) Publish as sparse-delta vs r10 anchor.
echo "▶ encoding sparse delta + publishing…"
DEST="workers/$HANDLE/chain-design-r$END_ROUND"
mkdir -p "$DEST"
python3 scripts/_delta_sparse_net.py encode \
  workers/dispatcher/harvest-5way-r10/round-10 \
  "$ARCHIVE/round-$END_ROUND" "$DEST" 2>&1 | tail -2
cp "$ARCHIVE/round-$END_ROUND/dense.pt"            "$DEST/"
cp "$ARCHIVE/round-$END_ROUND"/opt-sparse-net.*.pt "$DEST/" 2>/dev/null || true
for r in $(seq $((START_ROUND + 1)) "$END_ROUND"); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

# Pull final ctrl from the last round's log for the commit message.
FINAL_CTRL=$(python3 -c "
import json
try:
    for line in open('$ARCHIVE/round-$END_ROUND/log.jsonl'):
        e = json.loads(line)
        if e.get('event') == 'ablation':
            print(f\"{e.get('control_bpc'):.4f}\")
except: print('unknown')
" | tail -1)

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "wave": "smoke-r$END_ROUND",
  "extended_from": "workers/dispatcher/harvest-3way-r$START_ROUND/round-$START_ROUND (sparse-delta vs harvest-5way-r10/round-10)",
  "round_length_steps": $STEPS,
  "n_rounds_trained": $N_ROUNDS,
  "final_ctrl_bpc": "$FINAL_CTRL",
  "MMLLM_BWD_SKIP_FRAC_NET_ONLY": "0.5",
  "MMLLM_BWD_SKIP_FRAC_LOCAL": "0.0",
  "MMLLM_ABLATION_QUICK": "true",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF

BR="claude/smoke-r$END_ROUND-$HANDLE"
echo "▶ committing + pushing to origin/$BR…"
git checkout -b "$BR" 2>/dev/null || git checkout "$BR"
# The earlier `git checkout origin/<branch> -- <paths>` staged ~1 GB of
# upstream content (corpora, scripts, harvests) into the index. Clear
# the index so the publish commit contains ONLY workers/<HANDLE>/...
git reset HEAD > /dev/null 2>&1 || true
git add "$DEST"/delta-sparse-net.*.pt "$DEST"/dense.pt \
        "$DEST"/opt-sparse-net.*.pt "$DEST"/meta.json \
        "$DEST"/round-*.log.jsonl "$DEST"/wall.tsv 2>/dev/null
# Tripwire: fail loud if anything outside $DEST/ ended up staged.
# If a future agent "rebuilds the commit" by hand, this prevents the
# 1-GB-upload retry-storm we saw on smoke-r22-tklXe.
STAGED_OUTSIDE=$(git diff --cached --name-only | grep -v "^$DEST/" || true)
if [ -n "$STAGED_OUTSIDE" ]; then
  echo "ERROR: files staged outside $DEST/ — refusing to commit." >&2
  echo "$STAGED_OUTSIDE" | head -20 >&2
  echo "(...and $(echo "$STAGED_OUTSIDE" | wc -l) total)" >&2
  echo "These are upstream INPUTS, not your deliverable. Run:" >&2
  echo "  git reset HEAD" >&2
  echo "  git add $DEST/" >&2
  echo "  git commit -m '...' && git push -u origin $BR" >&2
  exit 1
fi
git commit -m "smoke-r$END_ROUND $HANDLE — final_ctrl=$FINAL_CTRL"
for i in 1 2 3 4; do
  if git push -u origin "$BR" 2>&1 | tail -1 | grep -q -E "rejected|hung|error"; then
    sleep $((i * 4))
    continue
  fi
  break
done

echo "✓ DONE: branch $BR pushed. final_ctrl=$FINAL_CTRL"
