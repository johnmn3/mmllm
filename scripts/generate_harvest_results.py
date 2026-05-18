"""Generate a rich results.md for an N-way FedAvg harvest from the
harvest_meta.json + eval_battery.jsonl that harvest_chain.py writes.

Compares against the prior harvest's eval_battery.jsonl when available
to produce the R{N-10} → R{N} battery table.

Reads:
  workers/dispatcher/harvest-{N}way-r{target}/harvest_meta.json
  workers/dispatcher/harvest-{N}way-r{target}/eval_battery.jsonl
  workers/dispatcher/harvest-{M}way-r{prior}/eval_battery.jsonl   (prior)

Writes:
  workers/dispatcher/harvest-{N}way-r{target}/results.md

Usage:
  python3 scripts/generate_harvest_results.py <prior_round> <target_round> [--n-workers N]
"""
import argparse, json, sys
from pathlib import Path

DATASETS = ["glaive-fim-val", "cosmopedia", "fineweb-edu", "magicoder",
            "hermes-funcall", "toolace", "tiny-stories", "aesop-fables",
            "open-web-math"]
OOD_DATASETS = [d for d in DATASETS if d != "glaive-fim-val"]

def load_jsonl(p):
    out = {}
    if not p or not p.exists(): return out
    for line in p.read_text().splitlines():
        try: ev = json.loads(line)
        except: continue
        out[ev["dataset"]] = (float(ev["bpc"]), float(ev["ppl"]))
    return out

def discover_harvest_dir(round_n, prefer_n=None):
    root = Path("workers/dispatcher")
    candidates = sorted(root.glob(f"harvest-*way-r{round_n}"))
    legacy = root / "harvest-5way"
    if round_n == 20 and legacy.exists():
        candidates.append(legacy)
    for c in candidates:
        if (c / "eval_battery.jsonl").exists():
            if prefer_n is None or f"harvest-{prefer_n}way-" in c.name:
                return c
    if candidates: return candidates[-1]
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prior_round", type=int)
    ap.add_argument("target_round", type=int)
    ap.add_argument("--n-workers", type=int, default=None)
    args = ap.parse_args()

    prior_dir = discover_harvest_dir(args.prior_round)
    target_dir = discover_harvest_dir(args.target_round, prefer_n=args.n_workers)
    if not target_dir:
        print(f"ERROR: no harvest dir for round {args.target_round}", file=sys.stderr)
        sys.exit(2)

    prior = load_jsonl(prior_dir / "eval_battery.jsonl") if prior_dir else {}
    target = load_jsonl(target_dir / "eval_battery.jsonl")
    # Degraded mode: no eval battery data (corpora not built on this host).
    # Still emit a results.md based on harvest_meta.json's worker_ctrl_bpc
    # fields — at minimum the operator sees workers, mean/best ctrl, and
    # the chain ancestor.
    eval_degraded = not target

    meta = {}
    meta_path = target_dir / "harvest_meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text())

    target_n = meta.get("n_workers", args.n_workers or "?")
    prior_n = "?"
    if prior_dir:
        prior_meta = prior_dir / "harvest_meta.json"
        if prior_meta.exists():
            try: prior_n = json.loads(prior_meta.read_text()).get("n_workers", "?")
            except: pass

    out = []
    out.append(f"# {target_dir.name} — battery results")
    out.append("")
    out.append(f"FedAvg of {target_n} workers' round-{args.target_round} endpoints from the chain-diverse")
    out.append(f"extension wave (rounds {args.prior_round + 1}–{args.target_round}, 8-corpus mix).")
    out.append("")

    # Worker endpoints table
    if meta and meta.get("workers"):
        out.append(f"## Worker endpoints (individual round-{args.target_round} ctrl_bpc)")
        out.append("")
        out.append("| handle                       | branch                                                | R{} ctrl_bpc |".format(args.target_round))
        out.append("|------------------------------|-------------------------------------------------------|-------------:|")
        ws = sorted(meta["workers"], key=lambda w: (w.get("ctrl_bpc") is None,
                                                     w.get("ctrl_bpc") or 0))
        for w in ws:
            cb = w.get("ctrl_bpc")
            cb_s = f"{cb:.4f}" if cb is not None else "n/a"
            out.append(f"| {w['handle']:<28} | {w['branch']:<53} |       {cb_s} |")
        if meta.get("worker_ctrl_bpc_mean") is not None:
            out.append(f"| **mean**                     |                                                       |   **{meta['worker_ctrl_bpc_mean']:.4f}** |")
        out.append("")

    # State similarity
    if meta and meta.get("vnet_cos"):
        out.append(f"## State similarity (pairwise across the {meta.get('n_workers', '?')} workers)")
        out.append("")
        out.append("| component         | cos (pairwise mean) | range          |")
        out.append("|-------------------|--------------------:|---------------:|")
        if meta.get("dense_cos"):
            d = meta["dense_cos"]
            out.append(f"| dense.pt          | {d['mean']:.4f}              | {d['min']:.4f}–{d['max']:.4f} |")
        for layer in [0, 12, 31]:
            c = meta["vnet_cos"].get(str(layer)) or meta["vnet_cos"].get(layer)
            if c:
                out.append(f"| V_net layer {layer:<5} | {c['mean']:.4f}              | {c['min']:.4f}–{c['max']:.4f} |")
        out.append("")

    # Worker-ctrl-based before/after (always emitted; only field that's
    # available when the eval battery's corpora aren't built locally).
    if meta.get("worker_ctrl_bpc_mean") is not None:
        prior_meta = {}
        if prior_dir and (prior_dir / "harvest_meta.json").exists():
            try: prior_meta = json.loads((prior_dir / "harvest_meta.json").read_text())
            except: pass
        out.append(f"## Worker ctrl_bpc: R{args.prior_round} → R{args.target_round}")
        out.append("")
        out.append(f"Per-worker training-val ctrl_bpc (not a fixed eval — each worker's"
                   f" own training loop val data).")
        out.append("")
        prior_mean = prior_meta.get("worker_ctrl_bpc_mean")
        prior_best = prior_meta.get("worker_ctrl_bpc_best")
        target_mean = meta["worker_ctrl_bpc_mean"]
        target_best = meta.get("worker_ctrl_bpc_best")
        out.append("| metric        | prior (R{0:<3}) | this  (R{1:<3}) | Δ      |".format(args.prior_round, args.target_round))
        out.append("|---------------|---------------:|---------------:|-------:|")
        if prior_mean is not None:
            d = target_mean - prior_mean
            out.append(f"| ctrl_bpc mean | {prior_mean:>14.4f} | {target_mean:>14.4f} | {d:+.4f} |")
        else:
            out.append(f"| ctrl_bpc mean |             — | {target_mean:>14.4f} |     —  |")
        if prior_best is not None and target_best is not None:
            d = target_best - prior_best
            out.append(f"| ctrl_bpc best | {prior_best:>14.4f} | {target_best:>14.4f} | {d:+.4f} |")
        elif target_best is not None:
            out.append(f"| ctrl_bpc best |             — | {target_best:>14.4f} |     —  |")
        out.append("")

    if eval_degraded:
        out.append("## Battery eval: not run")
        out.append("")
        out.append("`eval_battery.jsonl` is missing — the harvester's step-7 eval")
        out.append("battery couldn't run (likely because the per-dataset val/test")
        out.append("corpora aren't built locally; run `bash scripts/prep_chain_diverse_corpora.sh`")
        out.append("to enable fixed-eval before/after comparisons across harvests).")
        out.append("")
        out.append(f"## Final state")
        out.append("")
        out.append(f"- `/tmp/mmllm-cpu/harvested-r{args.target_round}.bank-net.{{0..31}}.bin` — FedAvg V_net")
        out.append(f"- `/tmp/mmllm-cpu/harvested-r{args.target_round}.dense.pt` — FedAvg dense params")
        out.append(f"- `{target_dir}/round-{args.target_round}/` — published starting state for next dispatch wave")
        out.append("")
        out.append("Auto-generated by `scripts/generate_harvest_results.py` (degraded mode).")
        out_path = target_dir / "results.md"
        out_path.write_text("\n".join(out) + "\n")
        print(f"Wrote {out_path} (degraded — no battery)")
        return

    # Comparison table
    out.append(f"## R{args.prior_round} harvest vs R{args.target_round} harvest — full 7-dataset battery")
    out.append("")
    if prior:
        out.append(f"| dataset            | R{args.prior_round} harvest | R{args.target_round} harvest | Δ bpc   | Δ %      |")
        out.append("|--------------------|------------:|------------:|--------:|---------:|")
    else:
        out.append(f"| dataset            | R{args.target_round} harvest |")
        out.append("|--------------------|------------:|")
    ood_old, ood_new, all_old, all_new = [], [], [], []
    for ds in DATASETS:
        if ds not in target: continue
        new_bpc, _ = target[ds]
        all_new.append(new_bpc)
        if ds in OOD_DATASETS: ood_new.append(new_bpc)
        if prior and ds in prior:
            old_bpc, _ = prior[ds]
            all_old.append(old_bpc)
            if ds in OOD_DATASETS: ood_old.append(old_bpc)
            dbpc = new_bpc - old_bpc
            dpct = 100 * dbpc / old_bpc
            mark = "**" if new_bpc < old_bpc else ""
            out.append(f"| {ds:<18} |      {old_bpc:.4f} | {mark}{new_bpc:.4f}{mark}  | {dbpc:+.3f}  | {dpct:+5.1f}%  |")
        else:
            out.append(f"| {ds:<18} | **{new_bpc:.4f}**  |")
    if ood_old and ood_new:
        om, nm = sum(ood_old)/len(ood_old), sum(ood_new)/len(ood_new)
        out.append(f"| **OOD mean (7)**   |      {om:.4f} |  **{nm:.4f}** | {nm-om:+.3f}  | {100*(nm-om)/om:+5.1f}%  |")
        am, anm = sum(all_old)/len(all_old), sum(all_new)/len(all_new)
        out.append(f"| **ALL mean (8)**   |      {am:.4f} |  **{anm:.4f}** | {anm-am:+.3f}  | {100*(anm-am)/am:+5.1f}%  |")
    out.append("")

    # Headlines
    if prior and ood_old and ood_new:
        nm, om = sum(ood_new)/len(ood_new), sum(ood_old)/len(ood_old)
        ood_pct = 100 * (nm - om) / om
        glaive_dpct = 100 * (target["glaive-fim-val"][0] - prior["glaive-fim-val"][0]) / prior["glaive-fim-val"][0] if "glaive-fim-val" in prior else None
        out.append("## Headlines")
        out.append("")
        out.append(f"- **OOD mean dropped {abs(ood_pct):.1f}%** across {args.target_round - args.prior_round} rounds.")
        if glaive_dpct is not None:
            direction = "improved" if glaive_dpct < 0 else "regressed"
            out.append(f"- **Glaive in-domain {direction} by {abs(glaive_dpct):.1f}%** "
                      f"(diverse training acts as regularization)." if glaive_dpct < 0
                      else f"- **Glaive in-domain regressed by {glaive_dpct:.1f}%** (dilution cost).")
        if meta.get("best_worker"):
            out.append(f"- **Best individual worker**: `{meta['best_worker']}` "
                      f"({meta.get('worker_ctrl_bpc_best', 'n/a')} ctrl_bpc).")
            out.append(f"- **FedAvg state** harvested from {meta.get('n_workers', '?')} workers.")
        out.append("")

    out.append(f"## Final state")
    out.append("")
    out.append(f"- `/tmp/mmllm-cpu/harvested-r{args.target_round}.bank-net.{{0..31}}.bin` — FedAvg V_net (32 × 128 KB)")
    out.append(f"- `/tmp/mmllm-cpu/harvested-r{args.target_round}.dense.pt` — FedAvg dense params (~2.45 MB)")
    out.append(f"- `/tmp/mmllm-cpu/inf-spork-r{args.target_round}.{{fim,bank}}` — staged inf-spork format")
    out.append(f"- `{target_dir}/round-{args.target_round}/` — published starting state for next dispatch wave")
    out.append(f"- `{target_dir}/eval_battery.jsonl` — battery results")
    out.append("")
    out.append("Auto-generated by `scripts/generate_harvest_results.py`.")

    out_path = target_dir / "results.md"
    out_path.write_text("\n".join(out) + "\n")
    print(f"Wrote {out_path}")
    print()
    # Print just the comparison table to stdout for visibility
    in_table = False
    for line in out:
        if line.startswith("## R") and "harvest vs" in line: in_table = True
        if line.startswith("## ") and not line.startswith("## R") and in_table: break
        if in_table: print(line)

if __name__ == "__main__":
    main()
