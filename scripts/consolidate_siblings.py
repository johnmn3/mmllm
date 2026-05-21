#!/usr/bin/env python3
"""Fold sibling harvest dirs into one consolidated harvest.

scripts/harvest_action.sh picks the single highest-round prior harvest
as the base for each new round's bird-deltas. When two harvest runs
land at adjacent rounds, or when birds extend from sibling arms of the
chain tree, the two arms never merge — the "losing" arm's bird-deltas
stay stranded in their own dir and never contribute to subsequent
rounds' tensors.

This script does the cross-arm fold: row-aware FedAvg of the
delta-sparse-net chunks across sibling harvest dirs (reusing
scripts/_delta_sparse_net.py fedavg, same code path the bird-level
harvester trusts), per-element mean of dense.pt, and a merged
harvest_meta.json that records the inputs as ancestor_harvests. Output
is labeled harvest-fold{N}way-r{R}/, where R is the highest round
across the inputs and N is the cumulative unique bird count.

Usage:
    python3 scripts/consolidate_siblings.py auto [--dry-run]
        Auto-detect: find leaf harvest dirs (not yet an ancestor of any
        other harvest) within one round of the highest round, fold them.
        Exits 0 quietly when nothing's foldable.

    python3 scripts/consolidate_siblings.py merge <out_dir> <h1> <h2> [<h3> ...]
        Explicit: merge listed harvest dirs into out_dir. Each input
        must have round-R/{dense.pt, delta-sparse-net.{0..31}.pt,
        delta-sparse-net.meta.pt} + harvest_meta.json. out_dir must not
        already exist.

Round-gap policy: gap > 1 across inputs is rejected. The lower-round
arm's delta references a V_net one round behind the higher-round
arm's; row-aware FedAvg of the two is approximate at gap=1 (matches
scripts/harvest_action.sh's tolerance for birds with divergent
extended_from_harvest) but degrades fast beyond that.
"""

import datetime
import glob
import json
import os
import subprocess
import sys
from pathlib import Path

import torch


DISPATCHER_DIR = "workers/dispatcher"
FOLD_PREFIX = "harvest-fold"


def _round_of(name):
    """harvest-3way-r36 -> 36; harvest-fold7way-r36 -> 36; otherwise -1."""
    try:
        return int(name.rsplit("-r", 1)[-1])
    except Exception:
        return -1


def _load_meta(harvest_dir):
    p = Path(harvest_dir) / "harvest_meta.json"
    if not p.exists():
        raise SystemExit(f"missing {p}")
    return json.loads(p.read_text())


def _try_load_meta(harvest_dir):
    p = Path(harvest_dir) / "harvest_meta.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except Exception:
        return None


def _find_leaves():
    """Return harvest dirs not referenced as an ancestor by any other.

    A "leaf" is a tip of the lineage tree — no downstream harvest has
    folded it in via ancestor_harvests or previous_harvest.dir. We can
    only fold leaves; folding an interior node would duplicate
    contributions that a downstream harvest already absorbed.
    """
    all_dirs = sorted(
        glob.glob(f"{DISPATCHER_DIR}/harvest-*-r*"),
        key=_round_of,
        reverse=True,
    )
    all_dirs = [d for d in all_dirs if _round_of(d) > 0]
    # Drop dirs missing harvest_meta.json — we can't fold them (no
    # ancestor info, no direct_contributions) and they shouldn't gate
    # newer harvests as "potential parents" we'd want to merge.
    all_dirs = [d for d in all_dirs if _try_load_meta(d) is not None]
    referenced = set()
    for d in all_dirs:
        m = _try_load_meta(d)
        if m is None:
            continue
        for a in (m.get("ancestor_harvests") or []):
            referenced.add(a)
        ph = m.get("previous_harvest")
        if isinstance(ph, dict) and ph.get("dir"):
            referenced.add(ph["dir"])
    return [d for d in all_dirs if d not in referenced]


def _walk_ancestor_steps(start_dirs, own_bird_ids):
    """BFS over ancestor_harvests, accumulate per-bird steps deduped by
    bird_id, EXCLUDING ids that already appear in own_bird_ids.

    Matches the dedup convention in scripts/harvest_action.sh:497-501.
    """
    visited_ids = set()
    cum_steps = 0
    seen_dirs = set()
    queue = list(start_dirs)
    while queue:
        d = queue.pop()
        ds = str(d)
        if ds in seen_dirs:
            continue
        seen_dirs.add(ds)
        try:
            m = _load_meta(ds)
        except Exception:
            continue
        for c in m.get("direct_contributions", []):
            bid = c.get("bird_id")
            steps = c.get("n_steps")
            if not bid or steps is None:
                continue
            if bid in own_bird_ids or bid in visited_ids:
                continue
            visited_ids.add(bid)
            cum_steps += int(steps)
        ancs = m.get("ancestor_harvests")
        if not ancs:
            ph = m.get("previous_harvest")
            if isinstance(ph, dict) and ph.get("dir"):
                ancs = [ph["dir"]]
        for a in (ancs or []):
            queue.append(a)
    return visited_ids, cum_steps


def fold(out_dir, harvest_dirs):
    out_dir = Path(out_dir)
    if out_dir.exists():
        raise SystemExit(f"refuse to overwrite existing {out_dir}")
    harvest_dirs = [Path(d) for d in harvest_dirs]
    if len(harvest_dirs) < 2:
        raise SystemExit("fold needs at least 2 harvest dirs")

    metas = [_load_meta(d) for d in harvest_dirs]
    rounds = [int(m["target_round"]) for m in metas]
    target_round = max(rounds)
    gap = target_round - min(rounds)
    if gap > 1:
        raise SystemExit(
            f"round gap {gap} > 1 across inputs ({rounds}) — refusing to fold"
        )

    data_dirs = []
    for d, m in zip(harvest_dirs, metas):
        r = int(m["target_round"])
        rd = d / f"round-{r}"
        if not rd.exists():
            raise SystemExit(f"missing {rd}")
        data_dirs.append(rd)

    out_round = out_dir / f"round-{target_round}"
    out_round.mkdir(parents=True, exist_ok=False)

    cmd = ["python3", "scripts/_delta_sparse_net.py", "fedavg", str(out_round)]
    cmd.extend(str(p) for p in data_dirs)
    print(f"▶ row-aware FedAvg of delta-sparse-net across {len(data_dirs)} arms")
    subprocess.run(cmd, check=True)

    print(f"▶ averaging dense.pt across {len(data_dirs)} arms")
    denses = []
    for rd in data_dirs:
        p = rd / "dense.pt"
        if p.exists():
            denses.append(torch.load(p, map_location="cpu", weights_only=False))
    if not denses:
        raise SystemExit("no dense.pt across inputs — refusing to write empty fold")
    n = len(denses[0])
    if not all(len(d) == n for d in denses):
        raise SystemExit(f"dense.pt length mismatch: {[len(d) for d in denses]}")
    avg = []
    for i in range(n):
        vals = [d[i] for d in denses]
        if isinstance(vals[0], torch.Tensor):
            avg.append((sum(v.float() for v in vals) / len(vals)).to(vals[0].dtype))
        else:
            avg.append(vals[0])
    torch.save(avg, out_round / "dense.pt")
    sz = (out_round / "dense.pt").stat().st_size / 1e6
    print(f"  dense.pt averaged from {len(denses)}/{len(data_dirs)} arms → "
          f"{out_round/'dense.pt'} ({sz:.1f} MB)")

    own_birds = {}
    workers_concat = []
    bpcs = []
    for m in metas:
        for w in m.get("workers", []):
            workers_concat.append(w)
            if w.get("ctrl_bpc") is not None:
                bpcs.append(w["ctrl_bpc"])
        for c in m.get("direct_contributions", []):
            bid = c.get("bird_id")
            if not bid:
                continue
            if bid in own_birds:
                continue
            own_birds[bid] = c

    own_steps = sum((c.get("n_steps") or 0) for c in own_birds.values())
    own_ids_set = set(own_birds.keys())

    ancestor_starts = []
    for m in metas:
        for a in (m.get("ancestor_harvests") or []):
            ancestor_starts.append(a)
    anc_ids, anc_steps = _walk_ancestor_steps(ancestor_starts, own_ids_set)
    cum_steps = own_steps + anc_steps
    cum_unique = len(own_birds) + len(anc_ids)

    mean_bpc = round(sum(bpcs) / len(bpcs), 4) if bpcs else None
    best_bpc = round(min(bpcs), 4) if bpcs else None

    meta_out = {
        "spork_version": metas[0].get("spork_version", "0.9"),
        "target_round": target_round,
        "n_workers": len(workers_concat),
        "wave": f"fold-r{target_round}",
        "workers": workers_concat,
        "worker_ctrl_bpc_mean": mean_bpc,
        "worker_ctrl_bpc_best": best_bpc,
        "previous_harvest": None,
        "direct_contributions": list(own_birds.values()),
        "ancestor_harvests": sorted(str(d) for d in harvest_dirs),
        "cumulative_total_steps": cum_steps,
        "cumulative_unique_birds": cum_unique,
        "harvested_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "harvester": "scripts/consolidate_siblings.py (cross-arm fold)",
        "note": (
            "Cross-arm fold of sibling harvest dirs. delta-sparse-net is "
            "row-aware FedAvg-merged across input arms; dense.pt is "
            "per-element mean. ctrl_bpc reflects the input arms' birds; "
            "this fold did no fresh training of its own."
        ),
        "consolidation_of": sorted(str(d) for d in harvest_dirs),
        "round_gap_across_inputs": gap,
    }
    (out_dir / "harvest_meta.json").write_text(json.dumps(meta_out, indent=2))

    lines = []
    lines.append(f"# {out_dir.name} — fold of {len(harvest_dirs)} sibling harvest(s)\n")
    lines.append("## Folded inputs\n")
    lines.append("| harvest | round | direct birds | best ctrl_bpc | mean ctrl_bpc |")
    lines.append("|---------|------:|-------------:|--------------:|--------------:|")
    for d, m in zip(harvest_dirs, metas):
        best = m.get("worker_ctrl_bpc_best")
        mean = m.get("worker_ctrl_bpc_mean")
        lines.append(
            f"| `{d.name}` | {m['target_round']} | {m.get('n_workers', '—')} | "
            f"{best if best is not None else '—'} | "
            f"{mean if mean is not None else '—'} |"
        )
    lines.append("")
    lines.append("## Cumulative across full ancestry (deduped by bird_id)\n")
    lines.append(f"- Unique birds:   **{cum_unique}**")
    lines.append(f"- Total steps:    **{cum_steps}**")
    lines.append(f"- Target round:   **{target_round}**  "
                 f"(input round gap: {gap})")
    if mean_bpc is not None:
        lines.append(f"- ctrl_bpc mean: **{mean_bpc}**")
        lines.append(f"- ctrl_bpc best: **{best_bpc}**")
    lines.append("")
    lines.append("## Output\n")
    lines.append(f"`{out_round}/`:")
    lines.append(f"- `delta-sparse-net.{{0..31}}.pt` (row-aware FedAvg of {len(data_dirs)} arms)")
    lines.append(f"- `dense.pt` (per-element mean of {len(data_dirs)} arms)")
    lines.append("")
    (out_dir / "results.md").write_text("\n".join(lines) + "\n")

    spork_v = meta_out["spork_version"]
    manifest = {
        "spork_version": spork_v,
        "round": target_round,
        "harvested_at": meta_out["harvested_at"],
        "n_workers": meta_out["n_workers"],
        "worker_ctrl_bpc_mean": mean_bpc,
        "worker_ctrl_bpc_best": best_bpc,
        "cumulative_total_steps": cum_steps,
        "cumulative_unique_birds": cum_unique,
        "netbank_files": {
            "dense":  f"round-{target_round}/dense.pt",
            "delta_sparse_net": [
                f"round-{target_round}/delta-sparse-net.{i}.pt"
                for i in range(32)
            ],
            "delta_sparse_net_meta": f"round-{target_round}/delta-sparse-net.meta.pt",
            "reference_anchor": f"{DISPATCHER_DIR}/harvest-5way-r10/round-10",
        },
        "ancestor_harvests": meta_out["ancestor_harvests"],
        "harvester": meta_out["harvester"],
        "consolidation_of": meta_out["consolidation_of"],
    }
    (out_dir / f"spork-{spork_v}-r{target_round}.json").write_text(
        json.dumps(manifest, indent=2)
    )

    print()
    print("=" * 60)
    print(f"  FOLD SUMMARY — {out_dir.name}")
    print("=" * 60)
    print(f"  inputs:              {len(harvest_dirs)} sibling harvest(s)")
    for d in harvest_dirs:
        print(f"                       {d}")
    print(f"  cum unique birds:    {cum_unique}")
    print(f"  cum total steps:     {cum_steps}")
    print(f"  target_round:        {target_round}  (gap {gap})")
    if mean_bpc is not None:
        print(f"  ctrl_bpc mean/best:  {mean_bpc} / {best_bpc}")
    print("=" * 60)


def auto(dry_run=False):
    leaves = _find_leaves()
    if len(leaves) <= 1:
        print("no sibling harvests to fold (≤1 leaf in the tree)")
        return 0

    top = max(_round_of(d) for d in leaves)
    close = [d for d in leaves if top - _round_of(d) <= 1]
    if len(close) <= 1:
        print(f"only 1 leaf within 1 round of top (r{top}); "
              f"other leaves too divergent to fold")
        return 0

    metas = [_load_meta(d) for d in close]
    own_bird_ids = set()
    for m in metas:
        for c in m.get("direct_contributions", []):
            bid = c.get("bird_id")
            if bid:
                own_bird_ids.add(bid)
    ancestor_starts = []
    for m in metas:
        for a in (m.get("ancestor_harvests") or []):
            ancestor_starts.append(a)
    anc_ids, _ = _walk_ancestor_steps(ancestor_starts, own_bird_ids)
    cum_unique = len(own_bird_ids) + len(anc_ids)

    out_name = f"{FOLD_PREFIX}{cum_unique}way-r{top}"
    out_dir = f"{DISPATCHER_DIR}/{out_name}"
    if Path(out_dir).exists():
        i = 2
        while Path(f"{out_dir}-v{i}").exists():
            i += 1
        out_dir = f"{out_dir}-v{i}"

    print(f"▶ {len(close)} sibling leaf harvest(s) to fold:")
    for d in close:
        print(f"    {d}  (round {_round_of(d)})")
    print(f"  → {out_dir}")
    if dry_run:
        print("  (--dry-run; not folding)")
        return 0
    fold(out_dir, close)
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "auto":
        dry = "--dry-run" in sys.argv[2:]
        sys.exit(auto(dry_run=dry))
    elif cmd == "merge" and len(sys.argv) >= 5:
        fold(sys.argv[2], sys.argv[3:])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
