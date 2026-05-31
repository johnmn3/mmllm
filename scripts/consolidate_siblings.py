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

    python3 scripts/consolidate_siblings.py raw-birds <round> [--out OUT] [--extra-ref REF ...]
        Auto-discover every origin/claude/train-* branch with a
        chain-design-r<round>/ bird payload, fetch + extract each, and
        fold them into one harvest dir. Honors the quarantine list at
        workers/dispatcher/.bird_exclude.json (bird_ids listed there
        are skipped). --extra-ref accepts additional refs (e.g. fork
        branches fetched separately) and includes them in the fold.
        This is the operational pattern that replaces "cron picks 3
        birds and leaves the rest stranded" — every published bird at
        the round gets folded in.

Round-gap policy: gap > 1 across inputs is rejected for the `merge`
mode. The lower-round arm's delta references a V_net one round behind
the higher-round arm's; row-aware FedAvg of the two is approximate at
gap=1 (matches scripts/harvest_action.sh's tolerance for birds with
divergent extended_from_harvest) but degrades fast beyond that.
"""

import datetime
import glob
import json
import os
import re
import shutil
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


def _way_count(name):
    """harvest-3way-r36 -> 3; harvest-fold17way-r36 -> 17; otherwise 0.

    Used as a tiebreak when picking a "previous harvest" among multiple
    candidates at the same round — prefer the one with more bird
    contributions folded in.
    """
    m = re.search(r"(\d+)way-r", name)
    return int(m.group(1)) if m else 0


def _picker_key(d):
    """Sort key for picking the best 'previous harvest' candidate at a round.

    Tuple (round, is_fold, way_count). Higher wins in reverse sort:
      - higher round first
      - among equal rounds, fold harvests beat raw harvests
      - among equal-round folds, the one with more birds wins
    """
    return (_round_of(d),
            1 if "/harvest-fold" in d else 0,
            _way_count(d))


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


def _load_quarantine():
    """Return set of bird_ids listed in workers/dispatcher/.bird_exclude.json.

    Empty set if the file doesn't exist or can't be parsed. JSON shape:
        {"excluded_bird_ids": [
            {"bird_id": "...", "reason": "...", "added_at": "ISO8601"}
        ]}
    """
    p = Path(DISPATCHER_DIR) / ".bird_exclude.json"
    if not p.exists():
        return set()
    try:
        data = json.loads(p.read_text())
        return {entry["bird_id"] for entry in data.get("excluded_bird_ids", [])
                if entry.get("bird_id")}
    except Exception as e:
        print(f"  WARN: couldn't parse {p}: {e}", file=sys.stderr)
        return set()


def _discover_fork_branches_at_round(round_n, upstream="johnmn3/mmllm"):
    """Return [(handle, local_ref_name)] for fork train-* branches with payload
    at round_n. Requires `gh` CLI in PATH (available in harvest_action.sh's
    GH Actions runner; absent on most developer machines). Returns [] when
    gh isn't available or auth fails.

    Each matching fork branch is fetched into a `fork-<safe>` local ref
    with --filter=blob:none so the rest of fold_raw_birds() can treat it
    like any other extra-ref. Full blobs come later in _fetch_and_extract_bird.

    Mirrors harvest_action.sh's `_list_fork_branches` helper so the cron
    runner can discover the same fork birds the legacy path uses, instead
    of leaving them stranded.
    """
    import shutil as _shutil
    if not _shutil.which("gh"):
        return []
    try:
        forks_out = subprocess.check_output(
            ["gh", "api", f"repos/{upstream}/forks?per_page=100",
             "--jq", ".[].full_name"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return []
    if not forks_out:
        return []

    result = []
    for fork in forks_out.split("\n"):
        if not fork:
            continue
        try:
            branches_out = subprocess.check_output(
                ["gh", "api", f"repos/{fork}/branches?per_page=100",
                 "--jq", '.[] | select(.name | startswith("claude/train-")) | .name'],
                text=True, stderr=subprocess.DEVNULL,
            ).strip()
        except subprocess.CalledProcessError:
            continue
        if not branches_out:
            continue
        for br in branches_out.split("\n"):
            if not br:
                continue
            m = re.match(r"claude/train-[a-f0-9]+-(\w+)$", br)
            if not m:
                continue
            handle = m.group(1)
            safe = re.sub(r"[^a-zA-Z0-9-]", "-", f"{fork}-{br}")[:60]
            local_ref = f"fork-{safe}"
            try:
                subprocess.run(
                    ["git", "fetch", f"https://github.com/{fork}.git",
                     f"{br}:refs/heads/{local_ref}",
                     "--depth=1", "--filter=blob:none", "-q"],
                    check=True, stderr=subprocess.DEVNULL,
                )
                ls = subprocess.check_output(
                    ["git", "ls-tree", "-r", "--name-only", local_ref],
                    text=True, stderr=subprocess.DEVNULL,
                )
            except subprocess.CalledProcessError:
                continue
            target = f"workers/{handle}/chain-design-r{round_n}/dense.pt"
            if target in ls:
                result.append((handle, local_ref))
    return result


def _discover_origin_branches_at_round(round_n):
    """Return [(handle, branch_name)] for origin/claude/train-* branches that
    contain workers/<handle>/chain-design-r<round_n>/dense.pt.

    Probes with --filter=blob:none to keep fetches cheap (~1-5 MB per branch).
    The full blobs come later, only for selected branches.
    """
    result = []
    try:
        out = subprocess.check_output(
            ["git", "ls-remote", "origin", "claude/train-*"],
            text=True, stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return result

    for line in out.strip().split("\n"):
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        ref = parts[1].replace("refs/heads/", "")
        m = re.match(r"claude/train-[a-f0-9]+-(\w+)$", ref)
        if not m:
            continue
        handle = m.group(1)
        # Probe trees (filter=blob:none keeps it small)
        try:
            subprocess.run(
                ["git", "fetch", "origin", ref,
                 "--depth=1", "--filter=blob:none", "-q"],
                check=True, stderr=subprocess.DEVNULL,
            )
            ls = subprocess.check_output(
                ["git", "ls-tree", "-r", "--name-only", f"origin/{ref}"],
                text=True, stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            continue
        target = f"workers/{handle}/chain-design-r{round_n}/dense.pt"
        if target in ls:
            result.append((handle, ref))
    return result


def _fetch_and_extract_bird(branch_ref, handle, round_n, dst_root, full_remote=None):
    """git archive | tar the bird's chain-design-r<round>/ tree to dst_root/handle/.

    branch_ref is the origin/<branch> form OR a local ref name for fork branches
    fetched separately. If full_remote is provided we fetch with blobs first.
    Returns (dst_path, n_files) or (None, 0) on failure.
    """
    dst = Path(dst_root) / handle
    dst.mkdir(parents=True, exist_ok=True)
    archive_src = branch_ref
    if branch_ref.startswith("origin/"):
        # Re-fetch with blobs this time so git archive has the .pt contents
        try:
            subprocess.run(
                ["git", "fetch", "origin",
                 branch_ref.replace("origin/", ""), "--depth=1", "-q"],
                check=True, stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            shutil.rmtree(dst, ignore_errors=True)
            return None, 0
    try:
        archive = subprocess.Popen(
            ["git", "archive", archive_src,
             f"workers/{handle}/chain-design-r{round_n}/"],
            stdout=subprocess.PIPE,
        )
        tar = subprocess.Popen(
            ["tar", "-x", "-C", str(dst),
             "--strip-components=3", "--exclude=opt-sparse-net.*"],
            stdin=archive.stdout,
        )
        archive.stdout.close()
        tar.communicate()
        archive.wait()
    except Exception as e:
        print(f"  WARN extract failed for {handle}: {e}", file=sys.stderr)
        shutil.rmtree(dst, ignore_errors=True)
        return None, 0
    n_files = len(list(dst.iterdir()))
    if n_files == 0:
        shutil.rmtree(dst, ignore_errors=True)
        return None, 0
    return dst, n_files


def fold_raw_birds(round_n, out_dir=None, extra_refs=()):
    """Discover + fold every train-* branch's r<round_n> bird payload.

    extra_refs: additional refs to include (already fetched into the local
    repo with blobs available — e.g. fork branches fetched manually).
    Each extra_ref is given as the branch/ref name; handle is inferred from
    the chain-design-r<round_n>/ tree path.

    Output dir defaults to workers/dispatcher/harvest-fold<N>way-r<round_n>/
    where N is the count of birds that actually got folded in.
    """
    quarantine = _load_quarantine()
    print(f"▶ raw-birds fold for round r{round_n}")
    if quarantine:
        print(f"  quarantine: {len(quarantine)} bird_id(s) excluded")

    work_root = Path(f"/tmp/birds-r{round_n}")
    if work_root.exists():
        shutil.rmtree(work_root)
    work_root.mkdir(parents=True)

    print(f"▶ scanning origin/claude/train-* for r{round_n} payloads…")
    branches = _discover_origin_branches_at_round(round_n)
    print(f"  found {len(branches)} branch(es) on origin")

    # Also add extra_refs (fork branches the caller pre-fetched).
    bird_specs = [(handle, f"origin/{br}") for handle, br in branches]

    # Auto-discover fork branches via gh CLI (CI-side path). When gh isn't
    # available (most dev machines), this returns [] and only origin
    # branches + caller-provided --extra-refs get folded. The harvest
    # cron runner has gh installed and authenticated by the workflow.
    print(f"▶ scanning fork branches via gh for r{round_n} payloads…")
    fork_birds = _discover_fork_branches_at_round(round_n)
    print(f"  found {len(fork_birds)} branch(es) on forks (via gh)")
    bird_specs.extend(fork_birds)

    for ref in extra_refs:
        try:
            ls = subprocess.check_output(
                ["git", "ls-tree", "-r", "--name-only", ref],
                text=True, stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            print(f"  WARN: extra-ref {ref} not fetchable", file=sys.stderr)
            continue
        for line in ls.split("\n"):
            m = re.match(rf"workers/(\w+)/chain-design-r{round_n}/dense\.pt$", line)
            if m:
                bird_specs.append((m.group(1), ref))
                break

    # Deduplicate by handle: forks of johnmn3/mmllm inherit upstream branches,
    # so a train branch like claude/train-c1a4337b-rMAbc appears on BOTH
    # origin (johnmn3) AND every fork that's synced. Without dedup we'd
    # extract the same bird N times (overwriting the same dst dir but
    # appending N copies to bird_specs → fedavg over-weights that bird).
    # Keep first occurrence (origin wins over fork; gh-discovered after).
    seen_handles = set()
    deduped_specs = []
    n_dup = 0
    for handle, ref in bird_specs:
        if handle in seen_handles:
            n_dup += 1
            continue
        seen_handles.add(handle)
        deduped_specs.append((handle, ref))
    if n_dup:
        print(f"  deduplicated {n_dup} bird spec(s) (same handle across origin+fork)")
    bird_specs = deduped_specs

    bird_dirs = []
    direct_contribs = []
    excluded_log = []
    for handle, ref in bird_specs:
        dst, n = _fetch_and_extract_bird(ref, handle, round_n, work_root)
        if dst is None:
            continue
        meta_p = dst / "meta.json"
        if not meta_p.exists():
            print(f"  skip {handle}: no meta.json")
            shutil.rmtree(dst)
            continue
        try:
            m = json.loads(meta_p.read_text())
        except Exception as e:
            print(f"  skip {handle}: meta parse failed: {e}")
            shutil.rmtree(dst)
            continue
        bid = m.get("bird_id") or f"legacy:{ref}"
        if bid in quarantine:
            print(f"  EXCLUDE {handle} (bird_id={bid[:8]}…) — quarantined")
            excluded_log.append({"handle": handle, "bird_id": bid})
            shutil.rmtree(dst)
            continue
        n_steps = m.get("n_total_steps")
        if n_steps is None:
            nr = m.get("n_rounds_trained")
            rs = m.get("round_length_steps")
            if isinstance(nr, (int, float)) and isinstance(rs, (int, float)):
                n_steps = int(nr) * int(rs)
        ctrl = m.get("final_ctrl_bpc")
        direct_contribs.append({
            "bird_id": bid, "handle": handle, "branch": ref,
            "n_steps": n_steps,
            "ctrl_bpc": float(ctrl) if ctrl is not None else None,
        })
        bird_dirs.append(dst)
        print(f"  + {handle}  bid={bid[:8]}  ctrl={ctrl}  n_steps={n_steps}")

    if not bird_dirs:
        print(f"no foldable birds at r{round_n}")
        shutil.rmtree(work_root)
        return None

    N = len(bird_dirs)

    # Skip-if-not-bigger: if there's already a harvest dir at this round
    # that captured at least N direct contributors, this fold wouldn't
    # add new content. Avoids bloat from idempotent catchup loops (cron
    # firing raw-birds against past rounds where nothing's changed).
    existing_max = 0
    for hp in glob.glob(f"{DISPATCHER_DIR}/harvest-*-r{round_n}/harvest_meta.json"):
        em = _try_load_meta(Path(hp).parent)
        if em is None:
            continue
        existing_max = max(existing_max, len(em.get("direct_contributions") or []))
    if N <= existing_max:
        print(f"  skip: existing harvest at r{round_n} already has "
              f"{existing_max} direct contributor(s) ≥ {N} discovered; "
              f"no new fold needed")
        shutil.rmtree(work_root)
        return None
    if existing_max > 0:
        print(f"  ▶ existing max contributors at r{round_n} = {existing_max}; "
              f"this fold has {N} → producing new fold dir")

    if out_dir is None:
        out_dir = Path(DISPATCHER_DIR) / f"{FOLD_PREFIX}{N}way-r{round_n}"
        if out_dir.exists():
            i = 2
            while Path(f"{out_dir}-v{i}").exists():
                i += 1
            out_dir = Path(f"{out_dir}-v{i}")
    else:
        out_dir = Path(out_dir)
    if out_dir.exists():
        raise SystemExit(f"refuse to overwrite existing {out_dir}")
    out_round = out_dir / f"round-{round_n}"
    out_round.mkdir(parents=True, exist_ok=False)

    # Row-aware FedAvg of delta-sparse-net.
    cmd = ["python3", "scripts/_delta_sparse_net.py", "fedavg", str(out_round)]
    cmd.extend(str(d) for d in bird_dirs)
    print(f"▶ row-aware FedAvg of {N} bird deltas")
    subprocess.run(cmd, check=True)

    # Per-element mean of dense.pt.
    print(f"▶ averaging dense.pt across {N} birds")
    denses = []
    for d in bird_dirs:
        p = d / "dense.pt"
        if p.exists():
            denses.append(torch.load(p, map_location="cpu", weights_only=False))
    if not denses:
        raise SystemExit("no dense.pt across inputs")
    nten = len(denses[0])
    if not all(len(dd) == nten for dd in denses):
        raise SystemExit(f"dense.pt length mismatch: {[len(dd) for dd in denses]}")
    avg = []
    for i in range(nten):
        vals = [dd[i] for dd in denses]
        if isinstance(vals[0], torch.Tensor):
            avg.append((sum(v.float() for v in vals) / len(vals)).to(vals[0].dtype))
        else:
            avg.append(vals[0])
    torch.save(avg, out_round / "dense.pt")
    print(f"  dense.pt → {out_round/'dense.pt'} "
          f"({(out_round/'dense.pt').stat().st_size/1e6:.1f} MB)")

    # ctrl_bpc summary from input birds.
    bpcs = [c["ctrl_bpc"] for c in direct_contribs if c.get("ctrl_bpc") is not None]
    mean_b = round(sum(bpcs)/len(bpcs), 4) if bpcs else None
    best_b = round(min(bpcs), 4) if bpcs else None
    own_ids = {c["bird_id"] for c in direct_contribs}
    own_steps = sum((c.get("n_steps") or 0) for c in direct_contribs)

    # Pick the previous mega-fold (or any harvest) at round < round_n as
    # the lineage anchor. The picker on the existing harvester will use this.
    prev_anc = None
    for d in sorted(glob.glob(f"{DISPATCHER_DIR}/harvest-*-r*"),
                    key=_picker_key, reverse=True):
        r = _round_of(d)
        if r < 0 or r >= round_n:
            continue
        if _try_load_meta(d) is None:
            continue
        prev_anc = d
        break

    ancestor_starts = [prev_anc] if prev_anc else []
    anc_ids, anc_steps = _walk_ancestor_steps(ancestor_starts, own_ids)

    workers_list = [{"handle": c["handle"], "branch": c["branch"],
                     "ctrl_bpc": c.get("ctrl_bpc")} for c in direct_contribs]
    meta_out = {
        "spork_version": "0.9",
        "target_round": round_n,
        "n_workers": N,
        "wave": f"fold-r{round_n}-rawbirds",
        "workers": workers_list,
        "worker_ctrl_bpc_mean": mean_b,
        "worker_ctrl_bpc_best": best_b,
        "previous_harvest": ({"round": _round_of(prev_anc), "dir": prev_anc}
                             if prev_anc else None),
        "direct_contributions": direct_contribs,
        "ancestor_harvests": ancestor_starts,
        "cumulative_total_steps": own_steps + anc_steps,
        "cumulative_unique_birds": len(own_ids) + len(anc_ids),
        "harvested_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "harvester": "scripts/consolidate_siblings.py raw-birds (inclusive fold)",
        "note": (
            "Inclusive raw-bird fold: every origin/claude/train-* branch with "
            f"chain-design-r{round_n}/ payload was discovered, fetched, and "
            "FedAvg'd in. Replaces the cron's MAX_BIRDS=3-capped selection. "
            "Honors workers/dispatcher/.bird_exclude.json quarantine list."
        ),
        "quarantine_excluded": excluded_log,
    }
    (out_dir / "harvest_meta.json").write_text(json.dumps(meta_out, indent=2))

    lines = []
    lines.append(f"# {out_dir.name} — raw-birds fold at round r{round_n}\n")
    lines.append("## Folded birds\n")
    lines.append("| handle | ctrl_bpc | n_steps | bird_id |")
    lines.append("|--------|---------:|--------:|---------|")
    for c in sorted(direct_contribs, key=lambda x: (x["ctrl_bpc"] is None, x["ctrl_bpc"])):
        bpc = f"{c['ctrl_bpc']:.4f}" if c["ctrl_bpc"] is not None else "—"
        lines.append(f"| {c['handle']} | {bpc} | "
                     f"{c['n_steps'] if c['n_steps'] is not None else '—'} | "
                     f"`{c['bird_id'][:16]}` |")
    if mean_b is not None:
        lines.append(f"| **mean** |  **{mean_b}**  | | |")
        lines.append(f"| **best** |  **{best_b}**  | | |")
    if excluded_log:
        lines.append(f"\n## Quarantine-excluded\n")
        for e in excluded_log:
            lines.append(f"- {e['handle']} (`{e['bird_id'][:16]}`)")
    lines.append(f"\n## Cumulative\n")
    lines.append(f"- Birds folded here:  **{N}**")
    lines.append(f"- Cumulative unique birds across full ancestry: "
                 f"**{meta_out['cumulative_unique_birds']}**")
    lines.append(f"- Cumulative steps: **{meta_out['cumulative_total_steps']}**")
    if prev_anc:
        lines.append(f"- Previous harvest: `{prev_anc}` (round {_round_of(prev_anc)})")
    (out_dir / "results.md").write_text("\n".join(lines) + "\n")

    # Spork manifest
    manifest = {
        "spork_version": "0.9", "round": round_n,
        "harvested_at": meta_out["harvested_at"],
        "n_workers": N,
        "worker_ctrl_bpc_mean": mean_b,
        "worker_ctrl_bpc_best": best_b,
        "cumulative_total_steps": meta_out["cumulative_total_steps"],
        "cumulative_unique_birds": meta_out["cumulative_unique_birds"],
        "netbank_files": {
            "dense": f"round-{round_n}/dense.pt",
            "delta_sparse_net": [f"round-{round_n}/delta-sparse-net.{i}.pt"
                                 for i in range(32)],
            "delta_sparse_net_meta": f"round-{round_n}/delta-sparse-net.meta.pt",
            "reference_anchor": f"{DISPATCHER_DIR}/harvest-5way-r10/round-10",
        },
        "ancestor_harvests": meta_out["ancestor_harvests"],
        "harvester": meta_out["harvester"],
    }
    (out_dir / f"spork-0.9-r{round_n}.json").write_text(json.dumps(manifest, indent=2))

    # Clean up working dir.
    shutil.rmtree(work_root)

    print()
    print("=" * 60)
    print(f"  RAW-BIRDS FOLD — {out_dir.name}")
    print("=" * 60)
    print(f"  birds folded:        {N}")
    print(f"  cum_unique_birds:    {meta_out['cumulative_unique_birds']}")
    print(f"  cum_total_steps:     {meta_out['cumulative_total_steps']}")
    print(f"  ctrl_bpc mean/best:  {mean_b} / {best_b}")
    if prev_anc:
        print(f"  previous harvest:    {prev_anc}")
    if excluded_log:
        print(f"  quarantine excluded: {len(excluded_log)}")
    print("=" * 60)
    return out_dir


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
    elif cmd == "raw-birds" and len(sys.argv) >= 3:
        try:
            round_n = int(sys.argv[2])
        except ValueError:
            raise SystemExit(f"raw-birds: <round> must be an int, got {sys.argv[2]!r}")
        args = sys.argv[3:]
        out_dir = None
        extra_refs = []
        i = 0
        while i < len(args):
            a = args[i]
            if a == "--out" and i + 1 < len(args):
                out_dir = args[i + 1]; i += 2
            elif a == "--extra-ref" and i + 1 < len(args):
                extra_refs.append(args[i + 1]); i += 2
            else:
                raise SystemExit(f"raw-birds: unknown arg {a!r}")
        fold_raw_birds(round_n, out_dir=out_dir, extra_refs=extra_refs)
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
