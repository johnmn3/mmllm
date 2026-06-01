"""Detect divergent leaf heads (tips) of a chain.

Option-3 federation policy: when a fast bird (e.g. a 13x MLX bird doing 10 rounds)
extends a base further than the ~1-round fork birds, the chain forks into multiple
tips off a common base (e.g. r130 from 3 fork birds and r139 from one MLX bird,
both off r129). "Highest-round-wins" would orphan the lower tip and strand those
contributors' compute. Instead we AVERAGE divergent tips (we only DROP a lower
head when a corpus-comparable eval can name a winner — which cross-corpus birds
don't have).

A tip = a harvest dir whose round is not the `previous_harvest.round` of any other
harvest of the same chain. >1 tip off the same base = a divergence to merge.

Usage:
  python3 scripts/detect_divergent_heads.py <chain>          # human report
  python3 scripts/detect_divergent_heads.py <chain> --dirs   # one round-N dir per
                                                              # line for the LARGEST
                                                              # divergent set (for
                                                              # the merge script);
                                                              # empty if no divergence
"""
import os
import sys
import json
import glob
from collections import defaultdict

ROOT = "workers/dispatcher"


def _round(d):
    try:
        return int(d.rsplit("-r", 1)[-1].split("_")[0])
    except Exception:
        return -1


def divergent_sets(chain):
    """Return {base_round: [harvest_dir, ...]} for each set of >1 tip sharing a base."""
    dirs = [d for d in glob.glob(f"{ROOT}/harvest-*-r*_{chain}") if os.path.isdir(d)]
    info = {}
    referenced = set()        # rounds that some other harvest builds on / consumed
    for d in dirs:
        base = None
        merged_from = []
        mp = os.path.join(d, "harvest_meta.json")
        if os.path.exists(mp):
            try:
                m = json.load(open(mp))
                base = (m.get("previous_harvest") or {}).get("round")
                # a merge head records the rounds it consumed; those are no longer
                # tips (else the merged head + a consumed tip re-trigger forever).
                merged_from = m.get("merged_from") or []
            except Exception:
                pass
        info[_round(d)] = {"dir": d, "base": base}
        if base is not None:
            referenced.add(base)
        referenced.update(int(x) for x in merged_from)
    bases = {v["base"] for v in info.values() if v["base"] is not None}
    tips = [r for r in info if r not in referenced]       # not extended/consumed by any other
    byb = defaultdict(list)
    for r in tips:
        byb[info[r]["base"]].append(r)
    out = {}
    for b, rs in byb.items():
        if b is not None and len(rs) > 1:                 # genuine divergence (skip genesis)
            out[b] = [info[r]["dir"] for r in sorted(rs)]
    return out, info


def main():
    chain = sys.argv[1] if len(sys.argv) > 1 else "sym24"
    dirs_mode = "--dirs" in sys.argv[2:]
    sets, info = divergent_sets(chain)
    if dirs_mode:
        if not sets:
            return
        # emit the round-N dirs of the largest divergent set (most tips to average)
        base = max(sets, key=lambda b: len(sets[b]))
        for d in sets[base]:
            r = _round(d)
            print(os.path.join(d, f"round-{r}"))
        return
    print(f"chain={chain}  rounds={sorted(info)}")
    if not sets:
        print("  no divergent tips — chain is linear, nothing to merge")
        return
    for b, ds in sorted(sets.items()):
        print(f"  DIVERGENT off r{b}: average these {len(ds)} heads ->")
        for d in ds:
            print(f"      {d}")


if __name__ == "__main__":
    main()
