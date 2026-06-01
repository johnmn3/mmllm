#!/usr/bin/env bash
# merge_divergent_heads.sh — option-3 federation policy: AVERAGE divergent leaf
# heads of a chain into one unified head, instead of highest-round-wins orphaning
# the lower tip (which strands contributors' compute — e.g. a fast MLX bird's r139
# superseding 3 fork birds' r130, both off r129).
#
# We only DROP a lower head when a corpus-comparable eval can pick a winner; absent
# that (cross-corpus birds), we average. Reuses the exact FedAvg the per-round
# harvest uses (scripts/_delta_sparse_net.py fedavg for V_net deltas + dense mean),
# so the merge math is the production-proven path; only the *input selection*
# (divergent tips instead of same-round birds) is new.
#
# Usage:  bash scripts/merge_divergent_heads.sh [chain]      # default sym24
#         MMLLM_REPO=owner/name  (default johnmn3/mmllm)
#         MMLLM_MERGE_PUBLISH=true   to publish+commit (default: dry-run, FedAvg
#                                    locally + print, do NOT mutate the chain)
set -euo pipefail
export LC_ALL=C
CHAIN="${1:-sym24}"
REPO="${MMLLM_REPO:-johnmn3/mmllm}"
PUBLISH="${MMLLM_MERGE_PUBLISH:-false}"
ROOT=$(git rev-parse --show-toplevel); cd "$ROOT"

# 1) detect divergent tips (round-N dirs of the largest divergent set)
mapfile -t TIPS < <(python3 scripts/detect_divergent_heads.py "$CHAIN" --dirs)
if [ "${#TIPS[@]}" -lt 2 ]; then
  echo "▶ no divergent tips for chain '$CHAIN' — chain is linear, nothing to merge."
  exit 0
fi
echo "▶ divergent tips to AVERAGE (${#TIPS[@]}):"
for t in "${TIPS[@]}"; do echo "    $t"; done

# 2) fetch each tip's Release assets (dense.pt + delta-sparse-net.*.pt) in-place
for t in "${TIPS[@]}"; do
  echo "▶ fetching assets for $t …"
  python3 scripts/chain_assets.py fetch "$t" --repo "$REPO"
done

# 3) target round = max tip round + 1 (the merged head supersedes all tips)
MAXR=0
for t in "${TIPS[@]}"; do
  r=$(echo "$t" | sed -E 's#.*-r([0-9]+)_.*#\1#'); [ "$r" -gt "$MAXR" ] && MAXR=$r
done
TARGET=$((MAXR + 1))
WAYS="${#TIPS[@]}way-merge"
OUT="workers/dispatcher/harvest-${WAYS}-r${TARGET}_${CHAIN}/round-${TARGET}"
mkdir -p "$OUT"
echo "▶ merging ${#TIPS[@]} heads → harvest-${WAYS}-r${TARGET}_${CHAIN}"

# 4) FedAvg V_net deltas (row-aware, the production fedavg) + mean the dense
python3 scripts/_delta_sparse_net.py fedavg "$OUT" "${TIPS[@]}" 2>&1 | tail -3
python3 - "$OUT" "${TIPS[@]}" <<'PYEOF'
import torch, os, sys
out, tips = sys.argv[1], sys.argv[2:]
ds = [torch.load(f"{t}/dense.pt", map_location="cpu", weights_only=False)
      for t in tips if os.path.exists(f"{t}/dense.pt")]
assert ds and all(len(d) == len(ds[0]) for d in ds), "dense.pt missing/len-mismatch across tips"
avg = [(sum(d[i].float() for d in ds) / len(ds)).to(ds[0][i].dtype)
       if isinstance(ds[0][i], torch.Tensor) else ds[0][i] for i in range(len(ds[0]))]
torch.save(avg, f"{out}/dense.pt")
print(f"  dense.pt = mean of {len(ds)} heads → {out}/dense.pt ({os.path.getsize(out+'/dense.pt')/1e6:.1f} MB)")
PYEOF

# 4b) harvest_meta.json — record the merge so the chain recognizes r<TARGET> as a
#     proper head and future divergence-detection sees both inputs consumed
#     (merged_from) and the common base (previous_harvest). Without merged_from the
#     consumed tips would re-trigger as divergent forever.
HDIR="workers/dispatcher/harvest-${WAYS}-r${TARGET}_${CHAIN}"
python3 - "$HDIR" "$TARGET" "$CHAIN" "${TIPS[@]}" <<'PYEOF'
import json, os, sys, datetime
hdir, target, chain = sys.argv[1], int(sys.argv[2]), sys.argv[3]
tips = sys.argv[4:]
workers, merged_from, ctrls = [], [], []
base = None
for t in tips:
    hm = os.path.join(os.path.dirname(t), "harvest_meta.json")
    r = int(t.rstrip("/").rsplit("-r", 1)[-1].split("_")[0].split("/")[0])
    best = mean = None; ways = "?"
    try:
        m = json.load(open(hm))
        best = m.get("worker_ctrl_bpc_best"); mean = m.get("worker_ctrl_bpc_mean")
        base = base if base is not None else (m.get("previous_harvest") or {}).get("round")
        ways = m.get("n_workers")
    except Exception: pass
    merged_from.append(r)
    if best is not None: ctrls.append(best)
    workers.append({"handle": f"r{r}-head", "branch": os.path.dirname(t),
                    "ctrl_bpc": best, "n_workers": ways})
meta = {
    "spork_version": "0.9", "target_round": target, "n_workers": len(tips),
    "wave": f"merge-r{target}", "merge": True,
    "merged_from": sorted(merged_from),
    "workers": workers,
    "worker_ctrl_bpc_mean": (sum(ctrls)/len(ctrls)) if ctrls else None,
    "worker_ctrl_bpc_best": (min(ctrls)) if ctrls else None,
    "previous_harvest": {"round": base},
    "harvested_at": datetime.datetime.utcnow().isoformat() + "Z",
    "harvester": "scripts/merge_divergent_heads.sh (option-3: average divergent tips)",
    "note": ("Divergent-head merge: FedAvg of the listed tips (V_net row-aware + "
             "dense mean) into one head, so no contributor's compute is orphaned. "
             "Tips averaged (not dropped) — no corpus-comparable eval to pick a winner."),
}
os.makedirs(hdir, exist_ok=True)
json.dump(meta, open(os.path.join(hdir, "harvest_meta.json"), "w"), indent=2)
print(f"  harvest_meta.json written: r{target} merged_from={sorted(merged_from)} "
      f"base=r{base} ctrl_best={meta['worker_ctrl_bpc_best']}")
PYEOF

# 5) publish — gated. Dry-run by default so this never mutates the live chain
#    without an explicit opt-in (verify the FedAvg output first, then re-run with
#    MMLLM_MERGE_PUBLISH=true, or wire this into the harvest cron once trusted).
if [ "$PUBLISH" = "true" ]; then
  echo "▶ publishing merged head r${TARGET} as Release assets on $REPO …"
  python3 scripts/chain_assets.py publish "$OUT" --round "$TARGET" --chain "$CHAIN" --repo "$REPO"
  echo "▶ merged head built + published. Commit the manifest/meta to land it as the chain tip."
else
  echo "▶ DRY-RUN: merged head FedAvg'd locally at $OUT (not published)."
  echo "  Re-run with MMLLM_MERGE_PUBLISH=true to publish + land it as r${TARGET}."
fi
