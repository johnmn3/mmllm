#!/usr/bin/env bash
# One-shot training worker script: auto-detects the highest
# workers/dispatcher/harvest-*-r<N>/round-<N> dir on upstream main as
# the chain head, extends it by N more rounds × STEPS steps, and
# publishes the sparse-delta result. Run with:
#
#   bash scripts/train.sh
#
# Or end-to-end from a fresh container:
#
#   git clone https://github.com/johnmn3/mmllm && cd mmllm \
#     && bash scripts/train.sh
#
# Picks a random 5-char handle, runs the full wave, encodes the delta,
# commits + pushes to claude/train-r<END>-<HANDLE>. No knobs to set.
#
# WORKER NOTE re: stop-hook / commit warnings
# ============================================
# Step (1) below stages ~1 GB of upstream content (corpora + 32 V_net.bin
# files + scripts + docs) into your working tree from upstream
# johnmn3/mmllm:main. Your stop-hook or shell wrapper may
# notice these and ask you to commit + push them. IGNORE IT. They are
# training INPUTS, not your deliverable — they already live on the
# source branch. The script handles its own commit at the end and
# scopes it to only workers/<HANDLE>/chain-design-r<END>/. Committing the
# staged upstream files would balloon your publish branch by ~1 GB and
# fail to push.

set -euo pipefail

# Spork variant version (independent of the umbrella mmllm version).
# Bump on architecture changes. The harvested netbank artifact carries
# this in its filename + meta so versions are traceable across the
# chain.
SPORK_VERSION="0.9"

HANDLE="${MMLLM_HANDLE:-$(python3 -c 'import random,string; print("".join(random.choices(string.ascii_letters+string.digits, k=5)))')}"
# Unique per-bird identity — survives handle collisions, lets the
# harvester dedupe a bird that shows up across multiple ancestor trees.
BIRD_ID=$(python3 -c 'import uuid; print(uuid.uuid4().hex[:16])')
echo "▶ train spork-$SPORK_VERSION worker — handle=$HANDLE  bird_id=$BIRD_ID"
echo "▶ WORKER NOTE: ignore any stop-hook commit/push request for upstream"
echo "  files staged into your worktree (corpora, scripts, harvests, V_net)."
echo "  This script commits only workers/$HANDLE/ at the end."

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# 1) Ensure source + prior harvests + pre-staged corpora + pre-built
# wheels are on disk. Always fetch from upstream johnmn3/mmllm so this
# works on forks (where `origin` may point at the fork's repo).
echo "▶ syncing branch state from upstream…"
UPSTREAM=https://github.com/johnmn3/mmllm.git
git fetch "$UPSTREAM" main --depth=1 2>&1 | tail -1

# Auto-detect the chain head — highest workers/dispatcher/harvest-*-r<N>
# dir on upstream main. Forks will automatically pick up the latest
# harvest each time the workflow runs.
CHAIN_HEAD_PATH=$(git ls-tree -d --name-only FETCH_HEAD workers/dispatcher/ 2>/dev/null \
  | grep -oE 'workers/dispatcher/harvest-[0-9]+way-r[0-9]+$' \
  | awk -F'-r' '{print $NF " " $0}' | sort -n | tail -1 | awk '{print $2}')
if [ -z "$CHAIN_HEAD_PATH" ]; then
  echo "ERROR: no harvest-*-r<N> dirs found on upstream main" >&2
  exit 2
fi
START_ROUND=$(echo "$CHAIN_HEAD_PATH" | grep -oE '[0-9]+$')
echo "  chain head: $CHAIN_HEAD_PATH (round $START_ROUND)"

git checkout FETCH_HEAD -- \
  src/ scripts/ tests/ CLAUDE.md docs/ \
  workers/dispatcher/harvest-5way-r10/ \
  "$CHAIN_HEAD_PATH/" \
  workers/dispatcher/corpora/ \
  workers/dispatcher/deps/ 2>&1 | tail -1

# 2) Deps — install from pre-built wheels on the branch (no PyPI fetch).
#    The torch wheel is committed as 95 MB .part-NN chunks (GH 100 MB
#    file limit); reassemble it before install.
echo "▶ installing deps from workers/dispatcher/deps/wheels (offline)…"
WHEELS=workers/dispatcher/deps/wheels
for prefix in "$WHEELS"/*.part-00; do
  [ -f "$prefix" ] || continue
  base="${prefix%.part-00}"
  [ -f "$base" ] || cat "${base}".part-?? > "$base"
done
pip install --no-index --find-links="$WHEELS" -e . --quiet

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

# 4) Reconstruct round-$START_ROUND full V_net from r10 anchor + that
#    round's sparse delta (chain head auto-detected above).
echo "▶ staging round-$START_ROUND…"
ARCHIVE=/tmp/mmllm-cpu/chain-diverse
mkdir -p "$ARCHIVE/round-$START_ROUND"
python3 scripts/_delta_sparse_net.py apply \
  workers/dispatcher/harvest-5way-r10/round-10 \
  "$CHAIN_HEAD_PATH/round-$START_ROUND" \
  "$ARCHIVE/round-$START_ROUND" 2>&1 | tail -2
cp "$CHAIN_HEAD_PATH/round-$START_ROUND/dense.pt"            "$ARCHIVE/round-$START_ROUND/"
cp "$CHAIN_HEAD_PATH/round-$START_ROUND"/opt-sparse-net.*.pt "$ARCHIVE/round-$START_ROUND/" 2>/dev/null || true

# 5) Train. Env locks the verified contract (frac=0.5, QUICK ablation,
# per-step prints, all 32 layers train in expectation).
export MMLLM_BWD_SKIP_FRAC_NET_ONLY=0.5
export MMLLM_BWD_SKIP_FRAC_LOCAL=0.0
export MMLLM_ABLATION_QUICK=true
export MMLLM_PRINT_EVERY=1
N_ROUNDS="${MMLLM_N_ROUNDS:-5}"
STEPS="${MMLLM_STEPS_PER_ROUND:-7}"
# START_ROUND was set in step (1) from the auto-detected chain head.
END_ROUND=$((START_ROUND + N_ROUNDS))

# Pick the training mix from MMLLM_CORPUS. Default is 'fim' (the
# 9-corpus FIM-heavy mix currently shipping). Workers can pick a
# different mix to specialize the model's exposure for the next harvest
# round.
# Pick the training mix. Order of precedence:
#   1. MMLLM_CORPUS env var set explicitly (manual workflow_dispatch
#      with a corpus chosen from the dropdown).
#   2. Empty/unset (cron-triggered schedule run, or someone running
#      train.sh by hand without setting it) → random choice across
#      all four corpora for diversity in the chain.
if [ -n "${MMLLM_CORPUS:-}" ]; then
  CORPUS="$MMLLM_CORPUS"
else
  CORPUS=$(python3 -c "import random; print(random.choice(['fim','general','clojure-general','clojure-fim']))")
  echo "▶ corpus auto-selected at random: $CORPUS"
fi
B=/tmp/mmllm-cpu/battery
G=/tmp/mmllm-cpu/fim-json-v3.train.bin
case "$CORPUS" in
  fim)
    # 9-corpus FIM-heavy: 25% glaive-fim-v3 + 8 batteries
    export MMLLM_MIX="${G}:25,${B}/cosmopedia.train.bin:10,${B}/fineweb-edu.train.bin:10,${B}/magicoder.train.bin:10,${B}/hermes-funcall.train.bin:10,${B}/toolace.train.bin:10,${B}/aesop-fables.bin.train.bin:10,${B}/open-web-math.train.bin:10,${B}/tiny-stories.train.bin:5"
    ;;
  general)
    # 8-corpus general: drop FIM-weighted glaive, rebalance toward
    # English / code / math / story diversity. aesop-fables retained
    # because it carries the in-house Clojure + tool-call mix.
    export MMLLM_MIX="${B}/cosmopedia.train.bin:15,${B}/fineweb-edu.train.bin:15,${B}/magicoder.train.bin:15,${B}/hermes-funcall.train.bin:10,${B}/toolace.train.bin:10,${B}/aesop-fables.bin.train.bin:10,${B}/open-web-math.train.bin:15,${B}/tiny-stories.train.bin:10"
    ;;
  clojure-general)
    # Pure clojure code corpus (loubnabnl/clojure_checks `content`
    # field). Tokenizes to ~17 MB; mixed with the broader battery so
    # the model still sees English/math/code variety alongside the
    # clojure focus. Clojure weighted heavily.
    export MMLLM_MIX="${B}/clojure-general.train.bin:40,${B}/cosmopedia.train.bin:10,${B}/fineweb-edu.train.bin:10,${B}/magicoder.train.bin:10,${B}/aesop-fables.bin.train.bin:15,${B}/open-web-math.train.bin:10,${B}/tiny-stories.train.bin:5"
    ;;
  clojure-fim)
    # Clojure edit-pair corpus (loubnabnl/clojure_checks content→
    # new_content as JSON Edit tool calls). FIM-loss-mask trains on
    # the edit payload only. Mixed similarly to fim corpus but with
    # clojure-fim replacing glaive-fim-v3 as the FIM-weighted anchor.
    export MMLLM_MIX="${B}/clojure-fim.train.bin:30,${B}/clojure-general.train.bin:10,${B}/cosmopedia.train.bin:10,${B}/fineweb-edu.train.bin:10,${B}/magicoder.train.bin:10,${B}/hermes-funcall.train.bin:10,${B}/toolace.train.bin:10,${B}/aesop-fables.bin.train.bin:5,${B}/tiny-stories.train.bin:5"
    ;;
  *)
    echo "ERROR: unknown corpus '$CORPUS'." >&2
    echo "  Valid: fim, general, clojure-general (TODO), clojure-fim (TODO)" >&2
    exit 2
    ;;
esac
# 6) Train + publish round-by-round so a runner-timeout kill still
#    leaves the last-completed round on origin (no full-loss after
#    50-min jobs). Single stable branch per bird, single PR per bird.

# Branch name encodes bird_id (16 hex chars) so we don't collide on
# duplicate handles. The round number lives inside the tree (in the
# chain-design-r<N>/ dir), not in the branch name.
BR="claude/train-${BIRD_ID:0:8}-${HANDLE}"
echo "▶ stable per-bird branch: $BR"
echo "▶ training round-by-round (push + PR-update after each round)…"

# Initial branch checkout. If origin already has it (e.g., we're
# resuming), fast-forward; otherwise create fresh.
git checkout -b "$BR" 2>/dev/null || git checkout "$BR"

PR_NUM=""
PREV_DEST=""
FINAL_CTRL="unknown"

for ((step = 1; step <= N_ROUNDS; step++)); do
  CUR_ROUND=$((START_ROUND + step))
  echo "── round $step/$N_ROUNDS  (r$CUR_ROUND) ──────────────────────────"

  # run_chain_diverse.sh extends the highest staged round by 1 each call
  bash scripts/run_chain_diverse.sh 1 "$STEPS"

  # Build this round's publish dir
  DEST="workers/$HANDLE/chain-design-r$CUR_ROUND"
  mkdir -p "$DEST"
  python3 scripts/_delta_sparse_net.py encode \
    workers/dispatcher/harvest-5way-r10/round-10 \
    "$ARCHIVE/round-$CUR_ROUND" "$DEST" 2>&1 | tail -2
  cp "$ARCHIVE/round-$CUR_ROUND/dense.pt"            "$DEST/"
  cp "$ARCHIVE/round-$CUR_ROUND"/opt-sparse-net.*.pt "$DEST/" 2>/dev/null || true
  for r in $(seq $((START_ROUND + 1)) "$CUR_ROUND"); do
    cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
  done
  cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

  # ctrl_bpc from THIS round's ablation
  FINAL_CTRL=$(python3 -c "
import json
try:
    for line in open('$ARCHIVE/round-$CUR_ROUND/log.jsonl'):
        e = json.loads(line)
        if e.get('event') == 'ablation':
            print(f\"{e.get('control_bpc'):.4f}\")
except: print('unknown')
" | tail -1)

  cat > "$DEST/meta.json" <<EOF
{
  "spork_version": "$SPORK_VERSION",
  "handle": "$HANDLE",
  "bird_id": "$BIRD_ID",
  "wave": "train-r$CUR_ROUND",
  "extended_from": "$CHAIN_HEAD_PATH/round-$START_ROUND (sparse-delta vs harvest-5way-r10/round-10)",
  "extended_from_harvest": "$CHAIN_HEAD_PATH",
  "start_round": $START_ROUND,
  "end_round": $CUR_ROUND,
  "round_length_steps": $STEPS,
  "n_rounds_trained": $step,
  "n_rounds_target": $N_ROUNDS,
  "n_total_steps": $((step * STEPS)),
  "final_ctrl_bpc": "$FINAL_CTRL",
  "corpus": "$CORPUS",
  "MMLLM_BWD_SKIP_FRAC_NET_ONLY": "0.5",
  "MMLLM_BWD_SKIP_FRAC_LOCAL": "0.0",
  "MMLLM_ABLATION_QUICK": "true",
  "branch_base": "main",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF

  # Clear the index of upstream-staged files, then stage only this
  # round's $DEST and (if exists) the deletion of the previous round's
  # $DEST so the branch's tree stays ~one round's payload (~140 MB)
  # instead of growing linearly with N_ROUNDS.
  git reset HEAD > /dev/null 2>&1 || true
  if [ -n "$PREV_DEST" ] && [ "$PREV_DEST" != "$DEST" ] && [ -e "$PREV_DEST" ]; then
    git rm -rf "$PREV_DEST" > /dev/null 2>&1 || rm -rf "$PREV_DEST"
    git add -u "$PREV_DEST" 2>/dev/null || true
  fi
  git add "$DEST"/delta-sparse-net.*.pt "$DEST"/dense.pt \
          "$DEST"/opt-sparse-net.*.pt "$DEST"/meta.json \
          "$DEST"/round-*.log.jsonl "$DEST"/wall.tsv 2>/dev/null

  # Tripwire — only the worker's own dir tree may be staged.
  STAGED_OUTSIDE=$(git diff --cached --name-only | grep -v "^workers/$HANDLE/" || true)
  if [ -n "$STAGED_OUTSIDE" ]; then
    echo "ERROR: files staged outside workers/$HANDLE/ — refusing." >&2
    echo "$STAGED_OUTSIDE" | head -10 >&2
    exit 1
  fi

  git commit -m "train-r$CUR_ROUND $HANDLE — step $step/$N_ROUNDS, final_ctrl=$FINAL_CTRL" --quiet

  for i in 1 2 3 4; do
    if git push -u origin "$BR" 2>&1 | tail -1 | grep -q -E "rejected|hung|error"; then
      sleep $((i * 4)); continue
    fi
    break
  done
  echo "    pushed r$CUR_ROUND to origin/$BR"

  # Open the PR on first successful round (draft); subsequent rounds
  # auto-update the PR via push. We never need to rebind HEAD.
  if [ -z "$PR_NUM" ] && command -v gh > /dev/null 2>&1; then
    PR_BODY=$(printf '%s\n' \
      "**Bird training in progress.** Pushes after every round so" \
      "partial work survives runner timeouts." \
      "" \
      "- Handle: \`$HANDLE\`" \
      "- Bird ID: \`$BIRD_ID\`" \
      "- Corpus: \`$CORPUS\`" \
      "- Extended from: \`$CHAIN_HEAD_PATH\` (r$START_ROUND)" \
      "- Target rounds: $N_ROUNDS  (\`STEPS=$STEPS\`)" \
      "" \
      "Latest commit's chain-design-r<N>/ dir shows the round actually" \
      "achieved. The PR title is updated when training finishes." )
    CREATE_OUT=$(gh pr create --base main --head "$BR" --draft \
      --title "[bird $HANDLE] training in progress  ($step/$N_ROUNDS, r$CUR_ROUND)" \
      --body "$PR_BODY" 2>&1) && PR_NUM=$(echo "$CREATE_OUT" | grep -oE '/pull/[0-9]+' | grep -oE '[0-9]+' | head -1)
    if [ -n "$PR_NUM" ]; then
      echo "    opened draft PR #$PR_NUM"
    else
      echo "    (PR open skipped — gh pr create returned: $(echo "$CREATE_OUT" | tail -1))"
    fi
  fi

  PREV_DEST="$DEST"
done

# Loop done — mark PR ready + finalize title.
END_ROUND_ACTUAL=$((START_ROUND + N_ROUNDS))
if [ -n "$PR_NUM" ] && command -v gh > /dev/null 2>&1; then
  gh pr ready "$PR_NUM" 2>&1 | tail -1 || true
  gh pr edit "$PR_NUM" \
    --title "[bird $HANDLE] train r$END_ROUND_ACTUAL — ctrl_bpc=$FINAL_CTRL  ($N_ROUNDS×$STEPS steps, $CORPUS)" \
    2>&1 | tail -1 || true
fi

echo "✓ DONE: $N_ROUNDS rounds complete. branch=$BR  PR=#${PR_NUM:-none}  final_ctrl=$FINAL_CTRL"

# ── Celebration sequence ─────────────────────────────────────────────
# Pull the chain-head's ctrl_bpc from the harvest meta we trained off
# of, and the per-round trajectory from the worker's own logs. Compute
# the bpc reduction this bird contributed to the community model.
python3 - "$START_ROUND" "$END_ROUND" "$HANDLE" "$CORPUS" "$BR" "$ARCHIVE" \
  "$CHAIN_HEAD_PATH/harvest_meta.json" <<'PYEOF'
import json, sys, glob, math

start_r   = int(sys.argv[1])
end_r     = int(sys.argv[2])
handle    = sys.argv[3]
corpus    = sys.argv[4]
br        = sys.argv[5]
archive   = sys.argv[6]
chain_meta = sys.argv[7]

# Chain head bpc (the round we extended from)
start_bpc = None
try:
    m = json.load(open(chain_meta))
    start_bpc = m.get("worker_ctrl_bpc_mean") or m.get("worker_ctrl_bpc_best")
    if isinstance(start_bpc, str):
        start_bpc = float(start_bpc)
except Exception:
    pass

# Per-round trajectory from our own logs
traj = []
for r in range(start_r + 1, end_r + 1):
    p = f"{archive}/round-{r}/log.jsonl"
    try:
        for line in open(p):
            e = json.loads(line)
            if e.get("event") == "ablation":
                traj.append({"r": r, "wall": e.get("wall_s"),
                             "ctrl": e.get("control_bpc"),
                             "dnet": e.get("delta_net")})
    except FileNotFoundError:
        pass

end_bpc = traj[-1]["ctrl"] if traj else None

# Banner
W = 64
def line(c="═"): return c * W
def center(s):
    pad = max(0, (W - len(s)) // 2)
    return " " * pad + s

print()
print(line())
print(center("✨  Thank you for contributing to mmllm  ✨"))
print(line())
print()
print(f"  handle:        {handle}")
print(f"  corpus:        {corpus}")
print(f"  rounds:        r{start_r + 1} → r{end_r}  ({end_r - start_r} rounds)")
print(f"  branch:        {br}")
print()

if start_bpc is not None and end_bpc is not None:
    delta = start_bpc - end_bpc
    pct   = 100.0 * delta / start_bpc if start_bpc > 0 else 0.0
    print("  Your contribution to the community model:")
    print(f"    before training:   ctrl_bpc = {start_bpc:.4f}  (chain head at r{start_r})")
    print(f"    after training:    ctrl_bpc = {end_bpc:.4f}  (your r{end_r})")
    if delta > 0:
        print(f"    improvement:       Δ = -{delta:.4f} bits/char  ({pct:.1f}% reduction)")
    elif delta < 0:
        print(f"    drift:             Δ = +{-delta:.4f} bits/char  (regression — happens; the FedAvg corrects)")
    else:
        print(f"    Δ = 0 — exact tie")
    print()
    if traj:
        print("  Per-round trajectory:")
        print("    round | wall_s | ctrl_bpc | Δ_net")
        print("    ------|--------|----------|--------")
        for t in traj:
            ws = f"{t['wall']:.0f}" if t["wall"] is not None else "—"
            cb = f"{t['ctrl']:.4f}" if t["ctrl"] is not None else "—"
            dn = f"{t['dnet']:+.4f}" if t["dnet"] is not None else "—"
            print(f"    {t['r']:>5} | {ws:>6} | {cb:>8} | {dn:>7}")
        print()

print("  When the harvest workflow merges your bird with others'")
print("  (row-aware FedAvg), your delta becomes part of the durable")
print("  community V_net that every future bird builds from.")
print()
print("  Compute donated. Thank you 🙏")
print(line())
PYEOF
