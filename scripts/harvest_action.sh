#!/usr/bin/env bash
# Harvest a train-r<N> wave: row-aware FedAvg merge of all bird deltas
# + dense average. Output to workers/dispatcher/harvest-<W>way-r<N>/.
#
# Usage:
#   bash scripts/harvest_action.sh [target_round] [extra_ref ...]
#
# If target_round is empty, auto-detects the latest unharvested round:
# the highest N with origin/claude/{train,smoke}-r<N>-* branches but no
# corresponding workers/dispatcher/harvest-*-r<N>/ dir on this branch.
#
# extra_ref args are passed as additional refs to harvest from (e.g.,
# "pr-12" for a fetched fork PR ref). They must contain a bird payload
# at workers/<HANDLE>/chain-design-r<TARGET>/ with the same layout as
# a train.sh publish.
#
# Output is intentionally lean — sparse deltas + averaged dense only,
# no opt-state. Bird branches retain opt-state if anyone needs it for
# warmstarting. Total harvest size: ~135 MB regardless of bird count.

set -euo pipefail

# Spork variant version — should match train.sh's SPORK_VERSION. The
# harvested netbank artifact carries this in a `spork-<ver>-r<round>.json`
# manifest at the top of each harvest dir.
SPORK_VERSION="0.9"

ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

TARGET_ROUND="${1:-}"
shift || true
EXTRA_REFS=("$@")

# Helper: peek at a remote branch tree (fetches if not local) and emit
# every chain-design-r<N>/ round number present at the
# workers/<HANDLE>/chain-design-r<N>/ canonical bird-payload path.
# Used by both auto-detect (round → ?) and discovery (round → branches).
_rounds_in_branch() {
  local br="$1"
  git fetch origin "$br" --depth=1 >/dev/null 2>&1 || return 0
  git ls-tree -r --name-only "origin/$br" 2>/dev/null \
    | sed -nE 's|^workers/[^/]+/chain-design-r([0-9]+)/.*|\1|p' \
    | sort -un
}

# Helper: list (fork/full_name, branch_name) pairs across forks of the
# upstream repo, filtered to claude/train-* branches. Requires gh CLI
# (preinstalled on GH-hosted runners; auto-uses GITHUB_TOKEN). Emits
# one line per (fork, branch) as "fork|branch".
UPSTREAM_REPO="${MMLLM_UPSTREAM_REPO:-johnmn3/mmllm}"
_list_fork_branches() {
  echo "  [_list_fork_branches] starting…" >&2
  if ! command -v gh > /dev/null 2>&1; then
    echo "  [_list_fork_branches] gh CLI not available — skipping fork scan" >&2
    return 0
  fi
  echo "  [_list_fork_branches] gh CLI present; calling forks API…" >&2
  local forks_out=""
  # Wrap the substitution in 'if ! ...; then' so set -e doesn't kill us
  # silently when gh exits non-zero (auth fail, rate limit, etc).
  if ! forks_out=$(gh api "repos/${UPSTREAM_REPO}/forks?per_page=100" --jq '.[].full_name' 2>&1); then
    echo "  [_list_fork_branches] gh api forks FAILED:" >&2
    echo "  $forks_out" | head -5 >&2
    return 0
  fi
  local n_forks=0
  for fork in $forks_out; do
    n_forks=$((n_forks + 1))
    local br_out=""
    if ! br_out=$(gh api "repos/${fork}/branches?per_page=100" --jq '.[] | select(.name | startswith("claude/train-")) | .name' 2>&1); then
      echo "  [_list_fork_branches] gh api branches FAILED for $fork:" >&2
      echo "  $br_out" | head -3 >&2
      continue
    fi
    local n_branches=0
    for br in $br_out; do
      n_branches=$((n_branches + 1))
      echo "${fork}|${br}"
    done
    echo "  [_list_fork_branches] $fork → $n_branches claude/train-* branches" >&2
  done
  echo "  [_list_fork_branches] enumerated $n_forks fork(s) of $UPSTREAM_REPO" >&2
}

# Helper: fetch (fork, branch) into a local ref so the rest of the
# script can treat it like any other ref. Echoes the local-ref name on
# success, returns non-zero on failure.
_fetch_fork_branch() {
  local fork="$1"
  local br="$2"
  local safe
  safe=$(echo "${fork}/${br}" | tr '/. ' '-' | tr -cd 'a-zA-Z0-9-' | cut -c1-60)
  local local_ref="fork-${safe}"
  if git fetch "https://github.com/${fork}.git" "${br}:refs/heads/${local_ref}" --depth=1 >/dev/null 2>&1; then
    echo "$local_ref"
    return 0
  fi
  return 1
}

# --- 1) Auto-detect target round if not specified --------------------
# Branch flavors we accept:
#   claude/smoke-r<N>-*           legacy, round in name
#   claude/train-r<N>-*           interim, round in name
#   claude/train-<bird_id>-<H>    current stable per-bird, round in tree
if [ -z "$TARGET_ROUND" ]; then
  echo "▶ auto-detecting latest unharvested round…"
  ROUNDS_FROM_NAME=$( ( git ls-remote origin 'refs/heads/claude/smoke-r*' 2>/dev/null
                        git ls-remote origin 'refs/heads/claude/train-r*' 2>/dev/null ) \
    | grep -oE '(smoke|train)-r[0-9]+' | sed -E 's/^(smoke|train)-r//' || true)
  # Stable per-bird branches: claude/train-* that ISN'T the interim
  # claude/train-r<N>-* form. Peek into each tree for chain-design-r<N>.
  # Cap to MMLLM_MAX_BIRDS_PER_HARVEST branches — each _rounds_in_branch
  # does a `git fetch --depth=1` (~1 GB pack) and 15+ accumulated stable
  # branches × 1 GB was OOMing the runner before bird extraction even
  # started. The fork-scan below also contributes rounds, so we don't
  # need every origin branch to find the latest unharvested round.
  STABLE_BRANCH_SAMPLE="${MMLLM_MAX_BIRDS_PER_HARVEST:-3}"
  STABLE_BRANCHES=$( ( git ls-remote origin 'refs/heads/claude/train-*' 2>/dev/null \
    | awk '{print $2}' | sed 's|^refs/heads/||' \
    | grep -vE '^claude/train-r[0-9]+-' \
    | head -"$STABLE_BRANCH_SAMPLE" ) || true)
  ROUNDS_FROM_TREE=""
  for br in $STABLE_BRANCHES; do
    rs=$(_rounds_in_branch "$br")
    [ -n "$rs" ] && ROUNDS_FROM_TREE="$ROUNDS_FROM_TREE $rs"
  done
  # Same scan across forks of upstream
  ROUNDS_FROM_FORKS=""
  echo "  scanning forks of $UPSTREAM_REPO…"
  while IFS='|' read -r fork br; do
    [ -z "$fork" ] && continue
    local_ref=$(_fetch_fork_branch "$fork" "$br") || continue
    # Strict: only count rounds at the canonical bird-payload path
    # workers/<HANDLE>/chain-design-r<N>/ so auto-detect agrees with
    # step-2 discovery.
    rs=$(git ls-tree -r --name-only "$local_ref" 2>/dev/null \
      | sed -nE 's|^workers/[^/]+/chain-design-r([0-9]+)/.*|\1|p' \
      | sort -un)
    if [ -n "$rs" ]; then
      ROUNDS_FROM_FORKS="$ROUNDS_FROM_FORKS $rs"
      echo "  [fork-scan] $fork/$br → rounds: $(echo "$rs" | tr '\n' ' ')"
    fi
  done < <(_list_fork_branches)
  ALL_ROUNDS=$( ( ( echo "$ROUNDS_FROM_NAME"
                    echo "$ROUNDS_FROM_TREE"
                    echo "$ROUNDS_FROM_FORKS" ) \
    | tr ' ' '\n' | grep -E '^[0-9]+$' | sort -un ) || true)
  echo "  rounds visible (origin + forks): $(echo "$ALL_ROUNDS" | tr '\n' ' ')"
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
# Four sources:
#   (a) claude/smoke-r<T>-*  legacy branches whose name encodes T
#   (b) claude/train-r<T>-*  interim branches whose name encodes T
#   (c) claude/train-<id>-*  stable per-bird branches on origin whose
#                            latest commit has chain-design-r<T>/
#   (d) claude/train-*       on FORKS of $UPSTREAM_REPO whose latest
#                            commit has chain-design-r<T>/
BIRD_REFS=()
while read -r line; do
  ref=$(echo "$line" | awk '{print $2}' | sed 's|^refs/heads/|origin/|')
  [ -n "$ref" ] && BIRD_REFS+=("$ref")
done < <( git ls-remote origin "refs/heads/claude/smoke-r${TARGET_ROUND}-*" 2>/dev/null
          git ls-remote origin "refs/heads/claude/train-r${TARGET_ROUND}-*" 2>/dev/null )
# Stable per-bird branches on origin — same cap as step 1 so we
# inspect at most MMLLM_MAX_BIRDS_PER_HARVEST branches total. If step
# 1 ran auto-detect, these are the same branches it already fetched
# (so this loop's _rounds_in_branch fetches are no-ops). If
# TARGET_ROUND was passed manually (step 1 skipped), these are fresh
# fetches but still bounded.
STABLE_BRANCH_SAMPLE="${MMLLM_MAX_BIRDS_PER_HARVEST:-3}"
STABLE_BRANCHES=$( ( git ls-remote origin 'refs/heads/claude/train-*' 2>/dev/null \
  | awk '{print $2}' | sed 's|^refs/heads/||' \
  | grep -vE '^claude/train-r[0-9]+-' \
  | head -"$STABLE_BRANCH_SAMPLE" ) || true)
for br in $STABLE_BRANCHES; do
  rs=$(_rounds_in_branch "$br")
  if echo "$rs" | grep -qx "$TARGET_ROUND"; then
    BIRD_REFS+=("origin/$br")
  fi
done

# Fork branches: scan every public fork of $UPSTREAM_REPO for train
# branches and include any whose tree has chain-design-r<TARGET>/.
echo "▶ scanning forks of $UPSTREAM_REPO for round-$TARGET_ROUND birds…"
while IFS='|' read -r fork br; do
  [ -z "$fork" ] && continue
  echo "  checking $fork/$br…"
  if ! local_ref=$(_fetch_fork_branch "$fork" "$br"); then
    echo "    skip — _fetch_fork_branch failed"
    continue
  fi
  # Use sed (same code path as auto-detect, known to work) to extract
  # all rounds present at canonical workers/<H>/chain-design-r<N>/
  # paths; then check whether TARGET_ROUND is in that set.
  canonical_rounds=$(git ls-tree -r --name-only "$local_ref" 2>/dev/null \
    | sed -nE 's|^workers/[^/]+/chain-design-r([0-9]+)/.*|\1|p' \
    | sort -un || true)
  if echo "$canonical_rounds" | grep -qx "$TARGET_ROUND"; then
    BIRD_REFS+=("$local_ref")
    echo "    ✓ fork bird (canonical rounds: $(echo "$canonical_rounds" | tr '\n' ' '))"
  else
    echo "    skip — TARGET_ROUND=$TARGET_ROUND not in canonical rounds: $(echo "$canonical_rounds" | tr '\n' ' '|| echo none)"
  fi
done < <(_list_fork_branches)

for ref in "${EXTRA_REFS[@]}"; do
  BIRD_REFS+=("$ref")
done

N=${#BIRD_REFS[@]}
if [ $N -eq 0 ]; then
  echo "ERROR: no birds found for round $TARGET_ROUND" >&2
  exit 1
fi

# Cap N birds per harvest run. Without a cap, each accumulated origin
# bird branch triggers a ~1 GB pack fetch via _rounds_in_branch and
# the runner OOMs. The MAX_BIRDS=3 setting matches the historical
# 3-way harvests (r20, r22) that pushed clean. Override via
# MMLLM_MAX_BIRDS_PER_HARVEST. Unharvested birds at the same round
# are picked up on a subsequent run (cron retries hourly).
MAX_BIRDS="${MMLLM_MAX_BIRDS_PER_HARVEST:-3}"
if [ $N -gt $MAX_BIRDS ]; then
  echo "▶ found $N birds — capping at $MAX_BIRDS for this run"
  echo "  keeping:"
  for i in $(seq 0 $((MAX_BIRDS - 1))); do echo "    - ${BIRD_REFS[$i]}"; done
  echo "  skipping (re-run harvest to pick these up):"
  for i in $(seq $MAX_BIRDS $((N - 1))); do echo "    - ${BIRD_REFS[$i]}"; done
  BIRD_REFS=("${BIRD_REFS[@]:0:$MAX_BIRDS}")
  N=$MAX_BIRDS
else
  echo "▶ found $N birds:"
  for ref in "${BIRD_REFS[@]}"; do echo "  - $ref"; done
fi

# --- 3) Fetch each bird, extract chain-design-r<N> dir ---------------
WORK=/tmp/harvest-r${TARGET_ROUND}
rm -rf "$WORK"
mkdir -p "$WORK"

HANDLES=()
BIRD_DIRS=()
KEPT_REFS=()
for ref in "${BIRD_REFS[@]}"; do
  echo "▶ processing $ref…"
  case "$ref" in
    origin/claude/*)
      BRANCH="${ref#origin/}"
      echo "    fetching $BRANCH…"
      git fetch origin "$BRANCH" --depth=1 2>&1 | tail -1 || true
      ;;
  esac
  # Resolve ref → tree. If ls-tree fails (PR fetch went sideways,
  # malformed ref, etc.) skip with a visible error instead of dying.
  TREE=""
  if ! TREE=$(git ls-tree -r --name-only "$ref" 2>&1); then
    echo "  WARN: git ls-tree failed for $ref:" >&2
    echo "  $TREE" >&2
    echo "  skipping" >&2
    continue
  fi
  # Find the bird's handle. Pipeline wrapped in '|| true' so a no-match
  # (empty HANDLE) doesn't trigger set -e via pipefail.
  HANDLE=$(echo "$TREE" \
    | grep -oE "^workers/[^/]+/chain-design-r${TARGET_ROUND}/" \
    | head -1 | sed 's|^workers/||;s|/.*||' || true)
  if [ -z "$HANDLE" ]; then
    echo "  WARN: $ref has no workers/<HANDLE>/chain-design-r${TARGET_ROUND}/ — skipping"
    continue
  fi
  echo "  handle: $HANDLE"
  mkdir -p "$WORK/$HANDLE"
  # Errors visible; if archive can't read the tree (shallow fetch
  # missing blobs, etc.) we want to know which bird and why.
  if ! git archive "$ref" "workers/$HANDLE/chain-design-r${TARGET_ROUND}/" \
       | tar -x -C "$WORK/$HANDLE/" --strip-components=3; then
    echo "  WARN: git archive | tar failed for $ref — skipping" >&2
    rm -rf "$WORK/$HANDLE"
    continue
  fi
  N_FILES=$(ls "$WORK/$HANDLE/" 2>/dev/null | wc -l)
  if [ "$N_FILES" -eq 0 ]; then
    echo "  WARN: extracted 0 files for $ref — skipping" >&2
    rm -rf "$WORK/$HANDLE"
    continue
  fi
  echo "    extracted $N_FILES files"
  HANDLES+=("$HANDLE")
  BIRD_DIRS+=("$WORK/$HANDLE")
  KEPT_REFS+=("$ref")
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

# --- 5) Harvest meta + results.md -----------------------------------
HARVEST_DIR="workers/dispatcher/harvest-${WAYS}-r${TARGET_ROUND}"

# Build meta + results.md via Python: pull each bird's ctrl_bpc + the
# previous harvest's ctrl_bpc, compute mean/best/Δ, print + write.
python3 - "$SPORK_VERSION" "$TARGET_ROUND" "$N" "$HARVEST_DIR" "$WORK" "${HANDLES[@]}" :: "${KEPT_REFS[@]}" <<'PYEOF'
import json, os, sys, glob, datetime

spork_version = sys.argv[1]
target = int(sys.argv[2])
n_workers = int(sys.argv[3])
harvest_dir = sys.argv[4]
work = sys.argv[5]

# Split remaining args at "::" sentinel into handles + branches
rest = sys.argv[6:]
sep = rest.index("::")
handles = rest[:sep]
branches = rest[sep+1:]
assert len(handles) == len(branches) == n_workers

def safe_float(x):
    try: return float(x)
    except: return None

# Per-bird ctrl_bpc + identity + step count from each meta.json
birds = []
direct_contributions = []
ancestor_set = set()
for h, br in zip(handles, branches):
    meta_path = f"{work}/{h}/meta.json"
    bpc = None
    bird_id = None
    n_steps = None
    extended_from = None
    try:
        m = json.load(open(meta_path))
        bpc = safe_float(m.get("final_ctrl_bpc"))
        bird_id = m.get("bird_id")
        n_steps = m.get("n_total_steps")
        if n_steps is None:
            # Older meta — derive from n_rounds_trained × round_length_steps
            nr = m.get("n_rounds_trained")
            rs = m.get("round_length_steps")
            if isinstance(nr, (int, float)) and isinstance(rs, (int, float)):
                n_steps = int(nr) * int(rs)
        extended_from = m.get("extended_from_harvest")
    except Exception:
        pass
    birds.append({"handle": h, "branch": br, "ctrl_bpc": bpc})
    # Fall back to (handle, branch) as identity if no bird_id was set
    # (legacy birds). That's still unique enough for dedupe across runs.
    direct_contributions.append({
        "bird_id": bird_id or f"legacy:{br}",
        "handle":  h,
        "branch":  br,
        "n_steps": n_steps,
        "ctrl_bpc": bpc,
    })
    if extended_from:
        ancestor_set.add(extended_from)

valid_bpcs = [b["ctrl_bpc"] for b in birds if b["ctrl_bpc"] is not None]
mean_bpc = sum(valid_bpcs) / len(valid_bpcs) if valid_bpcs else None
best_bpc = min(valid_bpcs) if valid_bpcs else None

# Find the previous harvest (highest harvest-*-r<N> with N < target).
# Sort by extracted round number, not lexicographically — otherwise
# harvest-5way-r10 sorts before harvest-3way-r22 in string order.
def _round_of(d):
    try: return int(d.rsplit("-r", 1)[-1])
    except: return -1
prev = None
for d in sorted(glob.glob("workers/dispatcher/harvest-*-r*"),
                key=_round_of, reverse=True):
    n = _round_of(d)
    if n < 0 or n >= target: continue
    meta = f"{d}/harvest_meta.json"
    if not os.path.exists(meta): continue
    try:
        prev_meta = json.load(open(meta))
    except: continue
    mean = safe_float(prev_meta.get("worker_ctrl_bpc_mean"))
    best = safe_float(prev_meta.get("worker_ctrl_bpc_best"))
    # Skip older harvests that predate the worker_ctrl_bpc_mean field —
    # they have no comparable number for our delta.
    if mean is None and best is None: continue
    prev = {"round": n, "dir": d, "mean": mean, "best": best}
    break

# Walk ancestor harvest tree(s), deduping by bird_id, summing steps.
# Handles multi-tree merges (multiple ancestor_harvests per harvest)
# and legacy harvests (no direct_contributions field → 0 contribution
# from that level, but ancestor walk continues).
ancestor_harvests = sorted(ancestor_set)

def _walk_steps(start_dirs):
    visited_ids = set()
    visited_birds = []  # for transparency in meta
    queue = list(start_dirs)
    seen_dirs = set()
    while queue:
        d = queue.pop()
        if d in seen_dirs: continue
        seen_dirs.add(d)
        meta_p = f"{d}/harvest_meta.json"
        if not os.path.exists(meta_p): continue
        try: m = json.load(open(meta_p))
        except: continue
        for c in m.get("direct_contributions", []):
            bid = c.get("bird_id")
            steps = c.get("n_steps")
            if not bid or steps is None: continue
            if bid in visited_ids: continue
            visited_ids.add(bid)
            visited_birds.append({"bird_id": bid, "handle": c.get("handle"),
                                  "n_steps": steps, "from": d})
        # Follow ancestors (list-form). Legacy schema may have
        # 'previous_harvest.dir' as a single scalar — fall back.
        ancs = m.get("ancestor_harvests")
        if not ancs:
            ph = m.get("previous_harvest")
            if isinstance(ph, dict) and ph.get("dir"):
                ancs = [ph["dir"]]
        for a in (ancs or []):
            queue.append(a)
    return visited_ids, visited_birds

# Account for this harvest's own contributions first, then walk ancestors.
own_ids = {c["bird_id"]: c.get("n_steps") or 0 for c in direct_contributions}
own_steps = sum(s for s in own_ids.values())
anc_ids, anc_birds = _walk_steps(ancestor_harvests)
# Dedupe: remove from the ancestor sum any bird_id that also appears
# in this harvest's direct contributions (shouldn't happen normally,
# but defensive).
dedup_anc_steps = sum(b["n_steps"] for b in anc_birds
                      if b["bird_id"] not in own_ids)
cumulative_total_steps = own_steps + dedup_anc_steps
cumulative_unique_birds = len(own_ids) + sum(
    1 for b in anc_birds if b["bird_id"] not in own_ids)

# Per-round trajectory from the best bird's logs (lowest ctrl_bpc)
best_bird = min((b for b in birds if b["ctrl_bpc"] is not None),
                key=lambda b: b["ctrl_bpc"], default=None)
trajectory = []
if best_bird:
    log_files = sorted(glob.glob(f"{work}/{best_bird['handle']}/round-*.log.jsonl"))
    for lf in log_files:
        r = int(lf.rsplit("round-", 1)[-1].split(".")[0])
        wall, ctrl, dnet = None, None, None
        for line in open(lf):
            try: e = json.loads(line)
            except: continue
            if e.get("event") == "ablation":
                ctrl = e.get("control_bpc")
                dnet = e.get("delta_net")
                wall = e.get("wall_s")
        if ctrl is not None:
            trajectory.append({"round": r, "wall_s": wall, "ctrl_bpc": ctrl, "delta_net": dnet})

# Write harvest_meta.json
meta_out = {
    "spork_version": spork_version,
    "target_round": target,
    "n_workers": n_workers,
    "wave": f"train-r{target}",
    "workers": birds,
    "worker_ctrl_bpc_mean": round(mean_bpc, 4) if mean_bpc is not None else None,
    "worker_ctrl_bpc_best": round(best_bpc, 4) if best_bpc is not None else None,
    "previous_harvest": prev,
    "direct_contributions": direct_contributions,
    "ancestor_harvests": ancestor_harvests,
    "cumulative_total_steps": cumulative_total_steps,
    "cumulative_unique_birds": cumulative_unique_birds,
    "harvested_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "harvester": "scripts/harvest_action.sh (GH Action)",
    "note": "Lean harvest — sparse deltas + averaged dense only, no opt-state.",
}
with open(f"{harvest_dir}/harvest_meta.json", "w") as f:
    json.dump(meta_out, f, indent=2)

# Write the spork manifest file. Named with the spork version + target
# round so the artifact is identifiable on disk and in tarballs.
# Points at the netbank components inside this harvest dir.
spork_manifest = {
    "spork_version": spork_version,
    "round": target,
    "harvested_at": meta_out["harvested_at"],
    "n_workers": n_workers,
    "worker_ctrl_bpc_mean": meta_out.get("worker_ctrl_bpc_mean"),
    "worker_ctrl_bpc_best": meta_out.get("worker_ctrl_bpc_best"),
    "cumulative_total_steps": cumulative_total_steps,
    "cumulative_unique_birds": cumulative_unique_birds,
    "netbank_files": {
        "dense":  f"round-{target}/dense.pt",
        "delta_sparse_net": [f"round-{target}/delta-sparse-net.{i}.pt" for i in range(32)],
        "delta_sparse_net_meta": f"round-{target}/delta-sparse-net.meta.pt",
        "reference_anchor": "workers/dispatcher/harvest-5way-r10/round-10",
    },
    "ancestor_harvests": ancestor_harvests,
    "harvester": meta_out["harvester"],
}
manifest_name = f"spork-{spork_version}-r{target}.json"
with open(f"{harvest_dir}/{manifest_name}", "w") as f:
    json.dump(spork_manifest, f, indent=2)

# Write results.md
lines = []
lines.append(f"# harvest-{n_workers}way-r{target} — sparse-delta merge of {n_workers} birds\n")
lines.append("## Worker endpoints\n")
lines.append("| handle | branch | R{0} ctrl_bpc |".format(target))
lines.append("|--------|--------|--------------:|")
for b in sorted(birds, key=lambda x: (x["ctrl_bpc"] is None, x["ctrl_bpc"])):
    bpc_str = f"{b['ctrl_bpc']:.4f}" if b["ctrl_bpc"] is not None else "—"
    lines.append(f"| {b['handle']} | {b['branch']} | {bpc_str} |")
if mean_bpc is not None:
    lines.append(f"| **mean** | | **{mean_bpc:.4f}** |")
    lines.append(f"| **best** | | **{best_bpc:.4f}** |")

if prev and prev["mean"] is not None and mean_bpc is not None:
    delta_mean = mean_bpc - prev["mean"]
    delta_best = best_bpc - prev["best"] if (best_bpc and prev["best"]) else None
    lines.append(f"\n## Chain progression R{prev['round']} → R{target}\n")
    lines.append(f"Previous harvest: `{prev['dir']}`\n")
    lines.append("| metric         | prior          | this           | Δ        |")
    lines.append("|----------------|---------------:|---------------:|---------:|")
    lines.append(f"| ctrl_bpc mean  | {prev['mean']:.4f}         | {mean_bpc:.4f}         | {delta_mean:+.4f} |")
    if delta_best is not None:
        lines.append(f"| ctrl_bpc best  | {prev['best']:.4f}         | {best_bpc:.4f}         | {delta_best:+.4f} |")

if trajectory:
    lines.append(f"\n## Per-round trajectory (best bird: {best_bird['handle']})\n")
    lines.append("| round | wall_s | ctrl_bpc | Δ_net   |")
    lines.append("|-------|-------:|---------:|--------:|")
    for t in trajectory:
        ws = f"{t['wall_s']:.0f}" if t["wall_s"] is not None else "—"
        cb = f"{t['ctrl_bpc']:.4f}" if t["ctrl_bpc"] is not None else "—"
        dn = f"{t['delta_net']:+.4f}" if t["delta_net"] is not None else "—"
        lines.append(f"| {t['round']} | {ws} | {cb} | {dn} |")

lines.append(f"\n## Cumulative training contribution\n")
lines.append(f"- This harvest: **{own_steps} steps** from {len(own_ids)} bird(s)")
lines.append(f"- Across full ancestry (deduped by bird_id): "
             f"**{cumulative_total_steps} steps** from {cumulative_unique_birds} unique bird(s)")
if ancestor_harvests:
    lines.append("- Ancestor harvest(s):")
    for a in ancestor_harvests:
        lines.append(f"  - `{a}`")

lines.append(f"\n## Output\n")
lines.append(f"`{harvest_dir}/round-{target}/`:")
lines.append(f"- `delta-sparse-net.{{0..31}}.pt` (row-aware FedAvg merge of {n_workers} workers)")
lines.append(f"- `dense.pt` (averaged across {n_workers} birds)")
lines.append(f"- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`\n")

with open(f"{harvest_dir}/results.md", "w") as f:
    f.write("\n".join(lines) + "\n")

# Print summary to stdout for the workflow log
print()
print("═" * 60)
print(f"  HARVEST SUMMARY — r{target} ({n_workers} birds)")
print("═" * 60)
for b in sorted(birds, key=lambda x: (x["ctrl_bpc"] is None, x["ctrl_bpc"])):
    bpc_str = f"{b['ctrl_bpc']:.4f}" if b["ctrl_bpc"] is not None else "—"
    print(f"  {b['handle']:8s}  ctrl_bpc={bpc_str}  ({b['branch']})")
if mean_bpc is not None:
    print(f"  {'mean':8s}  ctrl_bpc={mean_bpc:.4f}")
    print(f"  {'best':8s}  ctrl_bpc={best_bpc:.4f}")
if prev and prev["mean"] is not None and mean_bpc is not None:
    print()
    print(f"  vs r{prev['round']} ({prev['dir']}):")
    print(f"    mean: {prev['mean']:.4f} → {mean_bpc:.4f}  (Δ {mean_bpc - prev['mean']:+.4f})")
    if best_bpc and prev["best"]:
        print(f"    best: {prev['best']:.4f} → {best_bpc:.4f}  (Δ {best_bpc - prev['best']:+.4f})")
print()
print(f"  this harvest contributed:    {own_steps:>6} steps from {len(own_ids)} bird(s)")
print(f"  cumulative across ancestry:  {cumulative_total_steps:>6} steps from {cumulative_unique_birds} unique bird(s)")
if ancestor_harvests:
    print(f"  ancestor harvest(s):         {', '.join(ancestor_harvests)}")
print("═" * 60)
PYEOF

echo "▶ harvest done:"
echo "  dir: $HARVEST_DIR"
echo "  files: $(ls "$OUT" | wc -l)"
echo "  size: $(du -sh "$HARVEST_DIR" | cut -f1)"

# Clean up working dir to free runner disk
rm -rf "$WORK"

echo "✓ DONE"
