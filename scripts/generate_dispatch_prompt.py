"""Generate the next-round dispatch prompt from the harvest's results.md
+ eval_battery.jsonl.

Inputs:
  current_target    e.g. 30 (the harvest just completed)
  next_target       e.g. 40 (the wave we're now dispatching for)
  --n-workers N     (used to find the right harvest-${N}way-r${current} dir)
  --out PATH        where to write the dispatch markdown

The prompt template embeds the prior-harvest battery numbers (so agents
see what trajectory they're extending) and the path to the just-staged
starting state.

Usage:
  python3 scripts/generate_dispatch_prompt.py 30 40 --n-workers 5 \\
    --out docs/spork-chain-diverse-dispatch-r40.md
"""
import argparse, json, sys
from pathlib import Path

DATASETS = ["glaive-fim-val", "cosmopedia", "fineweb-edu", "magicoder",
            "hermes-funcall", "toolace", "tiny-stories", "aesop-fables"]

def load_jsonl(p):
    out = {}
    if not p or not p.exists(): return out
    for line in p.read_text().splitlines():
        try: ev = json.loads(line)
        except: continue
        out[ev["dataset"]] = (float(ev["bpc"]), float(ev["ppl"]))
    return out

def discover_harvest_dir(round_n):
    root = Path("workers/dispatcher")
    for c in sorted(root.glob(f"harvest-*way-r{round_n}")):
        if (c / "eval_battery.jsonl").exists():
            return c
    legacy = root / "harvest-5way"
    if round_n == 20 and legacy.exists():
        return legacy
    return None

def write_prompt(current, next_n, n_workers, out_path, harvest_dir, prior_dir):
    cur = load_jsonl(harvest_dir / "eval_battery.jsonl")
    prior = load_jsonl(prior_dir / "eval_battery.jsonl") if prior_dir else {}

    lines = []
    lines.append(f"# Chain-diverse dispatch (rounds {current + 1} → {next_n}, 8-corpus mix, off R{current} harvest)")
    lines.append("")
    lines.append(f"You are extending the chain by 10 more rounds (round {current + 1} → round {next_n})")
    lines.append(f"**off the harvested round-{current} state** with the same 8-corpus diverse")
    lines.append("training mix that produced the previous wave's harvest.")
    lines.append("")

    prior_round = current - 10
    if prior:
        lines.append(f"R{prior_round} harvest → R{current} harvest (5-way FedAvg of last wave, all 7 OOD datasets):")
        lines.append("")
        lines.append(f"| dataset            | R{prior_round} harvest | R{current} harvest | Δ bpc   | Δ %     |")
        lines.append("|--------------------|------------:|------------:|--------:|--------:|")
        for ds in DATASETS:
            if ds not in cur: continue
            new_bpc, _ = cur[ds]
            old_bpc = prior.get(ds, (None, None))[0]
            if old_bpc is not None:
                dbpc = new_bpc - old_bpc
                dpct = 100 * dbpc / old_bpc
                lines.append(f"| {ds:<18} | {old_bpc:11.4f} | **{new_bpc:.4f}**  | {dbpc:+.3f}  | {dpct:+5.1f}%  |")
        lines.append("")
        lines.append("Every dataset improved including Glaive. You're stacking another 10 rounds on top.")
    else:
        lines.append(f"Starting R{current} harvest battery (no prior R{prior_round} for comparison):")
        lines.append("")
        lines.append(f"| dataset            | R{current} harvest |")
        lines.append("|--------------------|------------:|")
        for ds in DATASETS:
            if ds not in cur: continue
            new_bpc, _ = cur[ds]
            lines.append(f"| {ds:<18} | **{new_bpc:.4f}**  |")
    lines.append("")

    lines.append("Read `CLAUDE.md` first; it defines spork / chain / Δ_local / Δ_net,")
    lines.append("lists conduct rules (\"don't delete or overwrite files I didn't put")
    lines.append("there\" applies — your archive at `/tmp/mmllm-cpu/chain-diverse/` is")
    lines.append("yours; everything in `workers/dispatcher/` is not), and documents the")
    lines.append("stack-3e-2-5.0 + mag-coef-on recipe (which `extend_chain.sh` defaults")
    lines.append("to — don't override).")
    lines.append("")

    lines.append("## Setup (one fetch, then go)")
    lines.append("")
    lines.append("```bash")
    lines.append("git fetch origin claude/fim-training-cycle-T3giJ")
    lines.append("git checkout origin/claude/fim-training-cycle-T3giJ -- \\")
    lines.append("  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/")
    lines.append("pip install -e . --quiet")
    lines.append("```")
    lines.append("")
    lines.append("Confirm the starting state and runner are present:")
    lines.append("")
    lines.append("```bash")
    lines.append(f"ls {harvest_dir}/round-{current}/  # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt")
    lines.append("ls scripts/run_chain_diverse.sh                   # the runner (auto-discovers highest round)")
    lines.append("ls scripts/extend_chain.sh                        # which run_chain_diverse.sh hands off to")
    lines.append("ls scripts/prep_chain_diverse_corpora.sh          # idempotent corpus prep")
    lines.append(f"ls scripts/stage_chain_diverse_round{current}.sh  # idempotent stager for round-{current}")
    lines.append("```")
    lines.append("")

    lines.append("## Pre-flight: corpora")
    lines.append("")
    lines.append("Same 8-corpus mix as the previous wave (corpora byte-identical to prior).")
    lines.append("")
    lines.append("```bash")
    lines.append("bash scripts/prep_chain_diverse_corpora.sh")
    lines.append("```")
    lines.append("")
    lines.append("First-time cost: 20–40 min (most is HF downloads). Idempotent — skips any step whose output exists.")
    lines.append("")

    lines.append(f"## Stage the harvested round-{current} state")
    lines.append("")
    lines.append("```bash")
    lines.append(f"bash scripts/stage_chain_diverse_round{current}.sh")
    lines.append("```")
    lines.append("")
    lines.append(f"Copies `{harvest_dir}/round-{current}/` → `/tmp/mmllm-cpu/chain-diverse/round-{current}/`.")
    lines.append(f"32 V_net layers + dense.pt + opt-sparse-net.pt, 15 MB total. V_net + dense are the {n_workers}-way FedAvg;")
    lines.append("opt-state is the best individual worker's (lowest R{current} ctrl_bpc) for optimizer warmth.")
    lines.append("")

    lines.append(f"## Run (rounds {current + 1}–{next_n})")
    lines.append("")
    lines.append("```bash")
    lines.append("bash scripts/run_chain_diverse.sh 10 100")
    lines.append("```")
    lines.append("")
    lines.append("`run_chain_diverse.sh` auto-discovers the highest existing round, sets `MMLLM_MIX` for the")
    lines.append("8-corpus weighted sampler, and hands off to `extend_chain.sh` for 10 more rounds at 100 steps each.")
    lines.append("Total wall: ~30–50 min at cpu-mini scale.")
    lines.append("")
    lines.append("DO NOT pass env overrides. The mix weights, recipe, and ablation cap are baked in.")
    lines.append("")

    # Pick a sensible "expected ctrl_bpc" hint
    glaive_bpc = cur.get("glaive-fim-val", (None, None))[0]
    if glaive_bpc:
        low_b = glaive_bpc - 0.15
        high_b = glaive_bpc + 0.15
        hint = f"~{glaive_bpc:.2f}"
    else:
        low_b, high_b, hint = 1.20, 1.50, "~1.30"

    lines.append("## Watch for")
    lines.append("")
    lines.append(f"- Round {current + 1}'s `ctrl_bpc` on Glaive should sit near {hint} (the harvest's Glaive val bpc).")
    lines.append(f"  Don't abort if it sits in [{low_b:.2f}, {high_b:.2f}]. **Abort only if it climbs above 2.0 or `Δ_net`")
    lines.append("  collapses to ≤+0.02 across multiple rounds.**")
    lines.append("- Per-round wall ≈ 150–230s. If a round takes >500s, check `df -h /tmp` and `free -g`.")
    lines.append("- Each round prints an ablation summary with `control bpc`, `Δ_local`, `Δ_net`, `Δ_both`, `synergy`.")
    lines.append("  Δ_net should stay in roughly +0.10–0.25 across rounds. The OOD bpc gains are NOT in the per-round prints —")
    lines.append("  those come from the post-chain eval battery the dispatcher will run.")
    lines.append("")
    lines.append(f"If round {current + 1}'s ctrl_bpc is dramatically HIGHER than {high_b + 0.2:.2f} or Δ_net goes to zero immediately,")
    lines.append("something failed to inherit — abort and dump the train logs into the chat.")
    lines.append("")

    lines.append("## Publish your result")
    lines.append("")
    lines.append(f"After round {next_n} completes:")
    lines.append("")
    lines.append("```bash")
    lines.append("HANDLE=\"<your-handle>\"     # lowercase, no spaces")
    lines.append(f"DEST=\"workers/$HANDLE/chain-diverse-{next_n}\"")
    lines.append("mkdir -p \"$DEST\"")
    lines.append("")
    lines.append("ARCHIVE=/tmp/mmllm-cpu/chain-diverse")
    lines.append("")
    lines.append("# Final V_net + dense + opt-state for the next harvest")
    lines.append(f"cp \"$ARCHIVE\"/round-{next_n}/V_net.*.bin       \"$DEST/\"")
    lines.append(f"cp \"$ARCHIVE\"/round-{next_n}/dense.pt          \"$DEST/\"")
    lines.append(f"cp \"$ARCHIVE\"/round-{next_n}/opt-sparse-net.pt \"$DEST/\" 2>/dev/null || true")
    lines.append("")
    lines.append(f"# Per-round training logs (rounds {current + 1}–{next_n})")
    lines.append(f"for r in $(seq {current + 1} {next_n}); do")
    lines.append("  cp \"$ARCHIVE/round-$r/log.jsonl\" \"$DEST/round-$r.log.jsonl\" 2>/dev/null || true")
    lines.append("done")
    lines.append("")
    lines.append(f"cp \"$ARCHIVE/wall.tsv\" \"$DEST/\" 2>/dev/null || true")
    lines.append("")
    lines.append("cat > \"$DEST/meta.json\" <<EOF")
    lines.append("{")
    lines.append("  \"handle\": \"$HANDLE\",")
    lines.append("  \"config\": \"cpu-mini-N16\",")
    lines.append("  \"recipe\": \"stack-3e-2-5.0+mag-coef-on\",")
    lines.append("  \"mix\": \"8-corpus diverse (glaive:25 cosmopedia:15 fineweb-edu:15 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 tiny-stories:5)\",")
    lines.append("  \"n_rounds_extended\": 10,")
    lines.append(f"  \"n_rounds_total\": {next_n},")
    if glaive_bpc:
        lines.append(f"  \"extended_from\": \"{harvest_dir}/round-{current} ({n_workers}-way FedAvg; Glaive-val={glaive_bpc:.4f})\",")
    else:
        lines.append(f"  \"extended_from\": \"{harvest_dir}/round-{current} ({n_workers}-way FedAvg)\",")
    lines.append("  \"branch_base\": \"claude/fim-training-cycle-T3giJ\",")
    lines.append("  \"git_sha\": \"$(git rev-parse HEAD)\"")
    lines.append("}")
    lines.append("EOF")
    lines.append("```")
    lines.append("")
    lines.append("Push to your own branch (the remote here requires the `claude/*` namespace):")
    lines.append("")
    lines.append("```bash")
    lines.append(f"git checkout -b \"claude/chaindiverse-${{HANDLE}}-r{next_n}\" 2>/dev/null \\")
    lines.append(f"  || git checkout \"claude/chaindiverse-${{HANDLE}}-r{next_n}\"")
    lines.append("git add \"$DEST\"")
    lines.append(f"git commit -m \"chain-diverse rounds {current + 1}-{next_n} from harvested-r{current} — final_ctrl=<...>\"")
    lines.append(f"git push -u origin \"claude/chaindiverse-${{HANDLE}}-r{next_n}\"")
    lines.append("```")
    lines.append("")
    lines.append("If the remote 413/502s on a large push, split into 2–3 commits (V_net.0-15, V_net.16-31, then dense+opt-state).")
    lines.append("")

    lines.append("## What to report back")
    lines.append("")
    lines.append(f"1. The 10-round per-round table for rounds {current + 1}–{next_n} (wall_s, ctrl_bpc on Glaive val,")
    lines.append("   Δ_local, Δ_net, Δ_both, synergy).")
    lines.append(f"2. The branch name `claude/chaindiverse-<HANDLE>-r{next_n}`.")
    lines.append("")
    lines.append(f"The dispatcher will harvest all returning workers via `bash scripts/harvest_chain.sh {next_n}` —")
    lines.append("you don't need to run the battery yourself.")
    lines.append("")

    lines.append("## Hard rules")
    lines.append("")
    lines.append("- DO NOT change the mix weights or recipe. The defaults in `run_chain_diverse.sh` and")
    lines.append("  `extend_chain.sh` are the documented winners.")
    lines.append("- DO NOT start over with `run_chain_stack.sh` or any Glaive-only runner.")
    lines.append("- DO publish even on partial failure — a few completed rounds + logs is more valuable than a missing run.")
    lines.append("- DO NOT touch `workers/dispatcher/`. That's the dispatcher's read-only published starting state.")

    out_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out_path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("current_target", type=int)
    ap.add_argument("next_target", type=int)
    ap.add_argument("--n-workers", type=int, default=5)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    harvest_dir = discover_harvest_dir(args.current_target)
    if not harvest_dir:
        print(f"ERROR: no harvest dir for round {args.current_target}", file=sys.stderr)
        sys.exit(2)
    prior_dir = discover_harvest_dir(args.current_target - 10)

    write_prompt(args.current_target, args.next_target, args.n_workers,
                 args.out, harvest_dir, prior_dir)

if __name__ == "__main__":
    main()
