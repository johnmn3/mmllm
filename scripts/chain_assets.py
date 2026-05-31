#!/usr/bin/env python3
"""chain_assets.py — keep the chain's large V_net/dense blobs OUT of git history.

The federated chain used to commit ~135 MB of delta-sparse-net.*.pt + dense.pt
to main every harvest round. git history retains every blob forever (the
working-tree prune only trims HEAD), so main ballooned ~135 MB/round → tens of
GB. This moves those binaries to per-round GitHub Release assets; git keeps only
a tiny manifest.json. History stays KB-scale; old releases prune cleanly without
any history rewrite.

Verbs
-----
publish <dir> --round N --chain sym24 --repo owner/name
    Upload the dir's big binaries as assets on release tag harvest-r<N>_<chain>
    (genesis r0 carries V_net.*.bin; later rounds carry delta-sparse-net.*.pt),
    write <dir>/manifest.json (round, chain, repo, tag, ref anchor, per-asset
    sha256+bytes), then drop the local big files so the commit is manifest-only.

fetch <dir> [--repo owner/name]
    Read <dir>/manifest.json and download its assets from the release into <dir>,
    verifying sha256. Repo comes from the manifest (forks fetch upstream's
    releases) unless --repo overrides. No-op if the files are already present and
    hash-match (local runs that still have the blobs on disk).

prune --chain sym24 --repo owner/name [--keep 5] [--hours 24]
    Delete harvest releases for the chain that are BOTH older than --hours AND
    beyond the newest --keep by round. Genesis (r0) is always kept. Deleting a
    release frees storage immediately (unlike git history).

All gh calls are best-effort-logged; publish/fetch fail loudly (a missing asset
must not pass silently), prune is non-fatal (cleanup should never break a run).
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

# Big-binary patterns that move to releases. Everything else in the harvest dir
# (manifest.json, meta.json, chain_meta.json, README.md, *.log.jsonl, wall.tsv)
# stays committed — it's small and useful for tooling/humans.
BIG_PATTERNS = ("delta-sparse-net.*.pt", "V_net.*.bin", "dense.pt", "opt-sparse-net.*.pt")


def log(msg):
    print(f"  [chain_assets] {msg}", flush=True)


def big_files(d):
    out = []
    for pat in BIG_PATTERNS:
        out.extend(sorted(glob.glob(os.path.join(d, pat))))
    # de-dup while preserving order (dense.pt etc. can't double-match, but be safe)
    seen = set()
    return [f for f in out if not (f in seen or seen.add(f))]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def gh(args, check=True, capture=False):
    """Run a gh command. capture=True returns stdout; else streams."""
    r = subprocess.run(["gh", *args], check=False,
                       stdout=subprocess.PIPE if capture else None,
                       stderr=subprocess.PIPE if capture else None,
                       text=True)
    if check and r.returncode != 0:
        err = (r.stderr or "").strip() if capture else ""
        raise RuntimeError(f"gh {' '.join(args)} failed (rc={r.returncode}) {err}")
    return (r.stdout or "") if capture else r.returncode


def tag_for(round_n, chain):
    return f"harvest-r{round_n}_{chain}" if chain else f"harvest-r{round_n}"


def release_exists(tag, repo):
    return subprocess.run(["gh", "release", "view", tag, "--repo", repo],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL).returncode == 0


# --------------------------------------------------------------------------- #
def cmd_publish(a):
    d = a.dir.rstrip("/")
    files = big_files(d)
    if not files:
        log(f"no big binaries in {d} — nothing to publish (manifest-only already?)")
        return 0
    tag = tag_for(a.round, a.chain)
    log(f"publish {len(files)} asset(s) → release {tag} on {a.repo}")

    # 1) Ensure the release exists (idempotent — re-runs/overlapping harvests).
    if not release_exists(tag, a.repo):
        notes = f"Chain {a.chain or '(default)'} round {a.round} — V_net/dense blobs (kept out of git history)."
        gh(["release", "create", tag, "--repo", a.repo, "--target", "main",
            "--title", tag, "--notes", notes], check=False, capture=True)
        log(f"created release {tag}")

    # 2) Upload assets (clobber so a re-aimed/overlapping run is safe).
    gh(["release", "upload", tag, *files, "--repo", a.repo, "--clobber"], capture=True)
    log("upload ok")

    # 3) Build manifest with per-asset sha256+bytes (verified on fetch).
    assets = {}
    for f in files:
        assets[os.path.basename(f)] = {"sha256": sha256(f), "bytes": os.path.getsize(f)}
    ref_round = a.reference_round
    manifest = {
        "schema": 1,
        "round": a.round,
        "chain": a.chain,
        "repo": a.repo,
        "release_tag": tag,
        "reference_anchor": a.reference_anchor or None,
        "reference_release_tag": tag_for(ref_round, a.chain) if ref_round is not None else None,
        "assets": assets,
    }
    mpath = os.path.join(d, "manifest.json")
    with open(mpath, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)
        f.write("\n")
    log(f"wrote {mpath} ({len(assets)} assets)")

    # 4) Drop the local big files so the commit is manifest-only. git rm if
    #    tracked (migration of already-committed dirs), plain rm otherwise
    #    (fresh harvest dir, never added).
    for f in files:
        rc = subprocess.run(["git", "rm", "-f", "--quiet", f],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
        if rc != 0 and os.path.exists(f):
            os.remove(f)
    log("removed local big files (commit will be manifest-only)")
    return 0


# --------------------------------------------------------------------------- #
def cmd_fetch(a):
    d = a.dir.rstrip("/")
    mpath = os.path.join(d, "manifest.json")
    if not os.path.exists(mpath):
        # Pre-migration dirs (or local genesis) still carry the blobs in-tree.
        if big_files(d):
            log(f"{d}: no manifest but blobs present in-tree — nothing to fetch")
            return 0
        raise RuntimeError(f"{d}: no manifest.json and no blobs — cannot materialize")
    m = json.load(open(mpath))
    repo = a.repo or m["repo"]
    tag = m["release_tag"]
    assets = m.get("assets", {})

    # Skip anything already present + hash-matching (local runs, retries).
    need = [n for n, meta in assets.items()
            if not (os.path.exists(os.path.join(d, n))
                    and sha256(os.path.join(d, n)) == meta["sha256"])]
    if not need:
        log(f"{d}: all {len(assets)} assets present + verified — skip download")
        return 0

    log(f"fetch {len(need)}/{len(assets)} asset(s) from release {tag} on {repo} → {d}")
    last = None
    for attempt in range(1, 5):
        gh(["release", "download", tag, "--repo", repo, "--dir", d, "--clobber",
            *sum((["--pattern", n] for n in need), [])], check=False, capture=True)
        bad = []
        for n in need:
            p = os.path.join(d, n)
            if not os.path.exists(p):
                bad.append((n, "missing")); continue
            got = sha256(p)
            if got != assets[n]["sha256"]:
                bad.append((n, f"sha256 {got[:12]}≠{assets[n]['sha256'][:12]}"))
        if not bad:
            log(f"verified {len(need)} asset(s)")
            return 0
        last = bad
        log(f"attempt {attempt}: {len(bad)} bad ({bad[0]}); retrying")
    raise RuntimeError(f"fetch failed for {tag}: {last}")


# --------------------------------------------------------------------------- #
def cmd_prune(a):
    out = gh(["release", "list", "--repo", a.repo, "--limit", "400",
              "--json", "tagName,createdAt"], check=False, capture=True)
    try:
        rels = json.loads(out or "[]")
    except json.JSONDecodeError:
        log("release list unparseable — skip prune (non-fatal)")
        return 0
    suffix = f"_{a.chain}" if a.chain else ""
    pat = re.compile(rf"^harvest-r(\d+){re.escape(suffix)}$")
    mine = []
    for r in rels:
        m = pat.match(r["tagName"])
        if m:
            mine.append((int(m.group(1)), r["tagName"], r.get("createdAt", "")))
    if not mine:
        log(f"no releases match chain '{a.chain}' — nothing to prune")
        return 0
    mine.sort()  # by round
    keep_recent = {t for _, t, _ in mine[-a.keep:]}        # last N by round
    now = datetime.now(timezone.utc)
    deleted = 0
    for rnd, tag, created in mine:
        if rnd == 0:
            continue                                       # genesis always kept
        if tag in keep_recent:
            continue                                       # within last --keep
        if created:
            try:
                age_h = (now - datetime.fromisoformat(created.replace("Z", "+00:00"))).total_seconds() / 3600
                if age_h < a.hours:
                    continue                               # younger than --hours
            except ValueError:
                continue                                   # unparseable date → keep
        gh(["release", "delete", tag, "--repo", a.repo, "--yes", "--cleanup-tag"],
           check=False, capture=True)
        deleted += 1
        log(f"pruned release {tag} (round {rnd})")
    log(f"prune: kept {len(mine) - deleted}, deleted {deleted} "
        f"(keep last {a.keep} + <{a.hours}h + genesis)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("publish")
    pp.add_argument("dir")
    pp.add_argument("--round", type=int, required=True)
    pp.add_argument("--chain", default="")
    pp.add_argument("--repo", required=True)
    pp.add_argument("--reference-anchor", default="")
    pp.add_argument("--reference-round", type=int, default=None)
    pp.set_defaults(func=cmd_publish)

    pf = sub.add_parser("fetch")
    pf.add_argument("dir")
    pf.add_argument("--repo", default="")
    pf.set_defaults(func=cmd_fetch)

    pr = sub.add_parser("prune")
    pr.add_argument("--chain", default="")
    pr.add_argument("--repo", required=True)
    pr.add_argument("--keep", type=int, default=5)
    pr.add_argument("--hours", type=float, default=24.0)
    pr.set_defaults(func=cmd_prune)

    a = p.parse_args()
    sys.exit(a.func(a))


if __name__ == "__main__":
    main()
