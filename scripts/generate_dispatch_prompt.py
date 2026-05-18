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
            "hermes-funcall", "toolace", "tiny-stories", "aesop-fables",
            "open-web-math"]

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
    lines.append(f"# Chain-diverse dispatch (rounds {current + 1} → {next_n}, 9-corpus mix, off R{current} harvest)")
    lines.append("")
    lines.append(f"You are extending the chain by 10 more rounds (round {current + 1} → round {next_n})")
    lines.append(f"**off the harvested round-{current} state** with the same 9-corpus diverse")
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
    lines.append(f"ls {harvest_dir}/round-{current}/ | wc -l   # 66 files: 32× V_net + dense.pt + 32× opt-sparse-net.<i>.pt + opt-sparse-net.meta.pt")
    lines.append("ls scripts/run_chain_diverse.sh                   # the runner (auto-discovers highest round)")
    lines.append("ls scripts/extend_chain.sh                        # which run_chain_diverse.sh hands off to")
    lines.append("ls scripts/prep_chain_diverse_corpora.sh          # idempotent corpus prep")
    lines.append(f"ls scripts/stage_chain_diverse.sh                # generic stager (takes round arg)")
    lines.append("```")
    lines.append("")

    lines.append("## Pre-flight: free disk")
    lines.append("")
    lines.append("Each round writes ~1.3 GB to `/tmp/mmllm-cpu/chain-diverse/round-N/` at")
    lines.append("design-sized banks. 10 rounds = ~13 GB plus corpora (~3 GB) and training")
    lines.append("scratch (~2 GB). Stale state from prior worker sessions can starve the wave.")
    lines.append("")
    lines.append("**Before starting, clean up any stale state:**")
    lines.append("")
    lines.append("```bash")
    lines.append("df -h /tmp                                    # baseline")
    lines.append("# Local-only scratch — published state under workers/dispatcher/ is untouched.")
    lines.append("rm -rf /tmp/mmllm-cpu/chain-diverse           # any prior wave's archive")
    lines.append("rm -rf /tmp/mmllm-cpu/chain-diverse-1gb       # earlier cook name")
    lines.append("rm -rf /tmp/mmllm-cpu/fim-chain-stack.ckpts   # last round's live ckpt")
    lines.append("rm -rf /tmp/mmllm-cpu/fim-distill-build-*     # any sweep scratch")
    lines.append("rm -f  /tmp/mmllm-cpu/harvested-r*.bank*.bin  # any prior harvest dump")
    lines.append("rm -f  /tmp/mmllm-cpu/harvested-r*.dense.pt")
    lines.append("df -h /tmp                                    # confirm cleared")
    lines.append("```")
    lines.append("")
    lines.append("If `/tmp` shows <20 GB free after this, abort and ask the dispatcher before")
    lines.append("continuing — a wave needs ~15 GB headroom.")
    lines.append("")

    lines.append("## Pre-flight: corpora")
    lines.append("")
    lines.append("Same 9-corpus mix as the previous wave (corpora byte-identical to prior).")
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
    lines.append(f"bash scripts/stage_chain_diverse.sh {current}")
    lines.append("```")
    lines.append("")
    lines.append(f"Copies `{harvest_dir}/round-{current}/` → `/tmp/mmllm-cpu/chain-diverse/round-{current}/`.")
    lines.append("Contents at design-sized banks:")
    lines.append("")
    lines.append("- 32× V_net.{0..31}.bin (32 MB each, 1 GB total — the N-way V_net FedAvg)")
    lines.append("- 1 dense.pt (the N-way dense FedAvg)")
    lines.append("- 32× opt-sparse-net.{0..31}.pt + opt-sparse-net.meta.pt — per-V_net-layer")
    lines.append("  Adam state chunks (2-13 MB each, ~242 MB total). Row-aware FedAvg of all")
    lines.append("  workers' chunks: rows touched by k workers get the mean over those k.")
    lines.append("  extend_chain.sh merges the chunks back at resume; you don't manage it.")
    lines.append("")

    lines.append(f"## Run (rounds {current + 1}–{next_n})")
    lines.append("")
    lines.append("```bash")
    lines.append("bash scripts/run_chain_diverse.sh 10 100")
    lines.append("```")
    lines.append("")
    lines.append("`run_chain_diverse.sh` auto-discovers the highest existing round, sets `MMLLM_MIX` for the")
    lines.append("9-corpus weighted sampler, and hands off to `extend_chain.sh` for 10 more rounds at 100 steps each.")
    lines.append("Total wall: ~30–50 min at cpu-mini scale.")
    lines.append("")
    lines.append("DO NOT pass env overrides. The mix weights, recipe, and ablation cap are baked in.")
    lines.append("")

    lines.append("## Live reporting (don't go silent for 40 min)")
    lines.append("")
    lines.append("Per CLAUDE.md's \"Reporting discipline\" section. Arm a Monitor over the")
    lines.append("training log filter — every signal line wakes you, and each one is one")
    lines.append("short chat message back:")
    lines.append("")
    lines.append("```bash")
    lines.append("# (run in background — Monitor wakes you when grep matches)")
    lines.append("tail -F /tmp/mmllm-cpu/chain-diverse/round-*.train.log \\")
    lines.append("  | grep --line-buffered -E \\")
    lines.append("    \"step|eval|ablation|control|Δ_local|Δ_net|training complete|wall|Traceback|RuntimeError|AssertionError|ZeroDivisionError|Killed|OOM|FAILED|WARN|NaN\"")
    lines.append("```")
    lines.append("")
    lines.append("For each notification fire one brief chat message:")
    lines.append("")
    lines.append("- **Per-round header** (`── ROUND N ──`): \"starting round N off prev_dense\"")
    lines.append("- **Step prints during training** (every ~20 steps): \"round N step S: loss=L lr=R\"")
    lines.append("- **Ablation summary** (post step 70): a line with ctrl_bpc, Δ_local,")
    lines.append("  Δ_net, Δ_both, synergy")
    lines.append("- **Round complete**: wall_s + 1-line digest")
    lines.append("- **Any failure mode**: full traceback excerpt + abort")
    lines.append("")
    lines.append("Don't batch. Don't wait for the end. The dispatcher reads these live")
    lines.append("to know whether to fold your run in.")
    lines.append("")
    lines.append("If a round's training NaNs or `ctrl_bpc` climbs above 2.0, abort the")
    lines.append("remaining rounds and publish what you have — partial results beat zero.")
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
    lines.append(f"REFERENCE={harvest_dir}/round-{current}    # the wave-start V_net (everyone shares this)")
    lines.append("")
    lines.append("# Sparse-delta encode V_net = current - reference. Workers that only touch")
    lines.append("# a fraction of V_net's rows produce ~10-50 MB total (vs 1.25 GB if we pushed")
    lines.append("# full V_net.{0..31}.bin). The harvester row-aware-merges deltas + adds back")
    lines.append("# reference at finalize time. Untouched rows pass through unchanged.")
    lines.append("# See scripts/_delta_sparse_net.py for the format.")
    lines.append(f"python3 scripts/_delta_sparse_net.py encode \\")
    lines.append(f"  \"$REFERENCE\" \"$ARCHIVE\"/round-{next_n} \"$DEST\"")
    lines.append("")
    lines.append("# dense + chunked opt-state alongside the delta.")
    lines.append(f"cp \"$ARCHIVE\"/round-{next_n}/dense.pt               \"$DEST/\"")
    lines.append(f"cp \"$ARCHIVE\"/round-{next_n}/opt-sparse-net.*.pt    \"$DEST/\" 2>/dev/null || true")
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
    lines.append("  \"mix\": \"9-corpus diverse (glaive:25 cosmopedia:10 fineweb-edu:10 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 open-web-math:10 tiny-stories:5)\",")
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
    lines.append("Push to your own branch (the remote here requires the `claude/*` namespace).")
    lines.append("Sparse-delta payload is ~10-50 MB total, well under GitHub's per-file and")
    lines.append("per-commit limits — single commit, no chunking:")
    lines.append("")
    lines.append("```bash")
    lines.append(f"git checkout -b \"claude/chaindiverse-${{HANDLE}}-r{next_n}\" 2>/dev/null \\")
    lines.append(f"  || git checkout \"claude/chaindiverse-${{HANDLE}}-r{next_n}\"")
    lines.append("")
    lines.append("git add \"$DEST\"/delta-sparse-net.*.pt \"$DEST\"/dense.pt \\")
    lines.append("        \"$DEST\"/opt-sparse-net.*.pt \"$DEST\"/meta.json \\")
    lines.append("        \"$DEST\"/round-*.log.jsonl \"$DEST\"/wall.tsv 2>/dev/null")
    lines.append(f"git commit -m \"chain-diverse rounds {current + 1}-{next_n} (sparse-delta) — final_ctrl=<...>\"")
    lines.append(f"git push -u origin \"claude/chaindiverse-${{HANDLE}}-r{next_n}\"")
    lines.append("```")
    lines.append("")

    lines.append("## What to report back")
    lines.append("")
    lines.append("Throughout the run (live, as each fires — don't batch):")
    lines.append("")
    lines.append("- Per-round starting header")
    lines.append("- Step prints (every ~20 steps)")
    lines.append("- Each round's ablation summary (ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy)")
    lines.append("- Each round's wall_s + completion 1-liner")
    lines.append("- Any traceback / NaN / OOM in full")
    lines.append("")
    lines.append("At the end:")
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
    lines.append("- DO NOT commit anything outside `workers/<your-handle>/`. The setup step checks out")
    lines.append("  `src/`, `scripts/`, `tests/`, `CLAUDE.md`, `docs/` (and possibly `workers/dispatcher/`)")
    lines.append("  into your working tree to make training runnable — those are UPSTREAM CONTENT, not your")
    lines.append("  deliverable. Your publish branch contains only your worker dir. If a stop hook or")
    lines.append("  similar tool warns about untracked or modified upstream files, ignore it. Committing")
    lines.append("  them would balloon the publish branch with ~1 GB of redundant artifacts that already")
    lines.append("  live on the source branch.")

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
