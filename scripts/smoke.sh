#!/usr/bin/env bash
# One-shot smoke worker script: extends harvest-4way-r19 → r22 by 3
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
# commits + pushes to claude/smoke-r22-<HANDLE>. No knobs to set.

set -euo pipefail

HANDLE="${MMLLM_HANDLE:-$(python3 -c 'import random,string; print("".join(random.choices(string.ascii_letters+string.digits, k=5)))')}"
echo "▶ smoke-r22 worker — handle=$HANDLE"

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# 1) Ensure source + prior harvests are on disk.
echo "▶ syncing branch state…"
git fetch origin claude/fim-training-cycle-T3giJ --depth=1 2>&1 | tail -1
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ \
  workers/dispatcher/harvest-5way-r10/ \
  workers/dispatcher/harvest-4way-r19/ 2>&1 | tail -1

# 2) Deps.
echo "▶ installing deps…"
pip install -e . --quiet
pip install datasets --quiet   # not in pyproject yet

# 3) Corpora (idempotent; ~2-3 min cold).
echo "▶ preparing corpora…"
bash scripts/prep_chain_diverse_corpora.sh

# 4) Reconstruct round-19 full V_net from r10 anchor + r19 sparse delta.
echo "▶ staging round-19…"
ARCHIVE=/tmp/mmllm-cpu/chain-diverse
mkdir -p "$ARCHIVE/round-19"
python3 scripts/_delta_sparse_net.py apply \
  workers/dispatcher/harvest-5way-r10/round-10 \
  workers/dispatcher/harvest-4way-r19/round-19 \
  "$ARCHIVE/round-19" 2>&1 | tail -2
cp workers/dispatcher/harvest-4way-r19/round-19/dense.pt            "$ARCHIVE/round-19/"
cp workers/dispatcher/harvest-4way-r19/round-19/opt-sparse-net.*.pt "$ARCHIVE/round-19/" 2>/dev/null || true

# 5) Train. Env locks the verified contract (frac=0.5, QUICK ablation,
# per-step prints, all 32 layers train in expectation).
export MMLLM_BWD_SKIP_FRAC_NET_ONLY=0.5
export MMLLM_BWD_SKIP_FRAC_LOCAL=0.0
export MMLLM_ABLATION_QUICK=true
export MMLLM_PRINT_EVERY=1
echo "▶ training 3 rounds × 7 steps (~22 min wall)…"
bash scripts/run_chain_diverse.sh 3 7

# 6) Publish as sparse-delta vs r10 anchor.
echo "▶ encoding sparse delta + publishing…"
DEST="workers/$HANDLE/chain-design-r22"
mkdir -p "$DEST"
python3 scripts/_delta_sparse_net.py encode \
  workers/dispatcher/harvest-5way-r10/round-10 \
  "$ARCHIVE/round-22" "$DEST" 2>&1 | tail -2
cp "$ARCHIVE"/round-22/dense.pt            "$DEST/"
cp "$ARCHIVE"/round-22/opt-sparse-net.*.pt "$DEST/" 2>/dev/null || true
for r in 20 21 22; do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

# Pull final ctrl from the last round's log for the commit message.
FINAL_CTRL=$(python3 -c "
import json
try:
    for line in open('$ARCHIVE/round-22/log.jsonl'):
        e = json.loads(line)
        if e.get('event') == 'ablation':
            print(f\"{e.get('control_bpc'):.4f}\")
except: print('unknown')
" | tail -1)

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "wave": "smoke-r22",
  "extended_from": "workers/dispatcher/harvest-4way-r19/round-19 (sparse-delta vs harvest-5way-r10/round-10)",
  "round_length_steps": 7,
  "n_rounds_trained": 3,
  "final_ctrl_bpc": "$FINAL_CTRL",
  "MMLLM_BWD_SKIP_FRAC_NET_ONLY": "0.5",
  "MMLLM_BWD_SKIP_FRAC_LOCAL": "0.0",
  "MMLLM_ABLATION_QUICK": "true",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF

BR="claude/smoke-r22-$HANDLE"
echo "▶ committing + pushing to origin/$BR…"
git checkout -b "$BR" 2>/dev/null || git checkout "$BR"
git add "$DEST"/delta-sparse-net.*.pt "$DEST"/dense.pt \
        "$DEST"/opt-sparse-net.*.pt "$DEST"/meta.json \
        "$DEST"/round-*.log.jsonl "$DEST"/wall.tsv 2>/dev/null
git commit -m "smoke-r22 $HANDLE — final_ctrl=$FINAL_CTRL"
for i in 1 2 3 4; do
  if git push -u origin "$BR" 2>&1 | tail -1 | grep -q -E "rejected|hung|error"; then
    sleep $((i * 4))
    continue
  fi
  break
done

echo "✓ DONE: branch $BR pushed. final_ctrl=$FINAL_CTRL"
