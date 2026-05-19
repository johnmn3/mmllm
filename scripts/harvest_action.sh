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
python3 - "$TARGET_ROUND" "$N" "$HARVEST_DIR" "$WORK" "${HANDLES[@]}" :: "${BIRD_REFS[@]}" <<'PYEOF'
import json, os, sys, glob, datetime

target = int(sys.argv[1])
n_workers = int(sys.argv[2])
harvest_dir = sys.argv[3]
work = sys.argv[4]

# Split remaining args at "::" sentinel into handles + branches
rest = sys.argv[5:]
sep = rest.index("::")
handles = rest[:sep]
branches = rest[sep+1:]
assert len(handles) == len(branches) == n_workers

def safe_float(x):
    try: return float(x)
    except: return None

# Per-bird ctrl_bpc from each meta.json
birds = []
for h, br in zip(handles, branches):
    meta_path = f"{work}/{h}/meta.json"
    bpc = None
    try:
        m = json.load(open(meta_path))
        bpc = safe_float(m.get("final_ctrl_bpc"))
    except Exception:
        pass
    birds.append({"handle": h, "branch": br, "ctrl_bpc": bpc})

valid_bpcs = [b["ctrl_bpc"] for b in birds if b["ctrl_bpc"] is not None]
mean_bpc = sum(valid_bpcs) / len(valid_bpcs) if valid_bpcs else None
best_bpc = min(valid_bpcs) if valid_bpcs else None

# Find the previous harvest (highest harvest-*-r<N> with N < target)
prev = None
for d in sorted(glob.glob("workers/dispatcher/harvest-*-r*"), reverse=True):
    n = d.rsplit("-r", 1)[-1]
    try: n = int(n)
    except: continue
    if n >= target: continue
    meta = f"{d}/harvest_meta.json"
    if not os.path.exists(meta): continue
    try:
        prev_meta = json.load(open(meta))
    except: continue
    prev = {
        "round": n,
        "dir": d,
        "mean": safe_float(prev_meta.get("worker_ctrl_bpc_mean")),
        "best": safe_float(prev_meta.get("worker_ctrl_bpc_best")),
    }
    break

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
    "target_round": target,
    "n_workers": n_workers,
    "wave": f"smoke-r{target}",
    "workers": birds,
    "worker_ctrl_bpc_mean": round(mean_bpc, 4) if mean_bpc is not None else None,
    "worker_ctrl_bpc_best": round(best_bpc, 4) if best_bpc is not None else None,
    "previous_harvest": prev,
    "harvested_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "harvester": "scripts/harvest_action.sh (GH Action)",
    "note": "Lean harvest — sparse deltas + averaged dense only, no opt-state.",
}
with open(f"{harvest_dir}/harvest_meta.json", "w") as f:
    json.dump(meta_out, f, indent=2)

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
print("═" * 60)
PYEOF

echo "▶ harvest done:"
echo "  dir: $HARVEST_DIR"
echo "  files: $(ls "$OUT" | wc -l)"
echo "  size: $(du -sh "$HARVEST_DIR" | cut -f1)"

# Clean up working dir to free runner disk
rm -rf "$WORK"

echo "✓ DONE"
