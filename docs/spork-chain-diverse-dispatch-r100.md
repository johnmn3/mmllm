# Chain-diverse dispatch (rounds 91 → 100, 9-corpus mix, off R90 harvest)

You are extending the chain by 10 more rounds (round 91 → round 100)
**off the harvested round-90 state** with the same 9-corpus diverse
training mix that produced the previous wave's harvest.

R80 harvest → R90 harvest (5-way FedAvg of last wave, all 7 OOD datasets):

| dataset            | R80 harvest | R90 harvest | Δ bpc   | Δ %     |
|--------------------|------------:|------------:|--------:|--------:|
| glaive-fim-val     |      1.2368 | **1.1958**  | -0.041  |  -3.3%  |
| cosmopedia         |      2.1394 | **2.0884**  | -0.051  |  -2.4%  |
| fineweb-edu        |      2.4306 | **2.3978**  | -0.033  |  -1.3%  |
| magicoder          |      2.3244 | **2.2820**  | -0.042  |  -1.8%  |
| hermes-funcall     |      2.2148 | **2.1616**  | -0.053  |  -2.4%  |
| toolace            |      2.0901 | **2.0328**  | -0.057  |  -2.7%  |
| tiny-stories       |      2.1565 | **2.0879**  | -0.069  |  -3.2%  |
| aesop-fables       |      1.3123 | **1.2483**  | -0.064  |  -4.9%  |
| open-web-math      |      2.5225 | **2.4809**  | -0.042  |  -1.6%  |

Every dataset improved including Glaive. You're stacking another 10 rounds on top.

Read `CLAUDE.md` first; it defines spork / chain / Δ_local / Δ_net,
lists conduct rules ("don't delete or overwrite files I didn't put
there" applies — your archive at `/tmp/mmllm-cpu/chain-diverse/` is
yours; everything in `workers/dispatcher/` is not), and documents the
stack-3e-2-5.0 + mag-coef-on recipe (which `extend_chain.sh` defaults
to — don't override).

## Setup (one fetch, then go)

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/
pip install -e . --quiet
```

Confirm the starting state and runner are present:

```bash
ls workers/dispatcher/harvest-25way-r90/round-90/  # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt
ls scripts/run_chain_diverse.sh                   # the runner (auto-discovers highest round)
ls scripts/extend_chain.sh                        # which run_chain_diverse.sh hands off to
ls scripts/prep_chain_diverse_corpora.sh          # idempotent corpus prep
ls scripts/stage_chain_diverse.sh                # generic stager (takes round arg)
```

## Pre-flight: corpora

Same 9-corpus mix as the previous wave (corpora byte-identical to prior).

```bash
bash scripts/prep_chain_diverse_corpora.sh
```

First-time cost: 20–40 min (most is HF downloads). Idempotent — skips any step whose output exists.

## Stage the harvested round-90 state

```bash
bash scripts/stage_chain_diverse.sh 90
```

Copies `workers/dispatcher/harvest-25way-r90/round-90/` → `/tmp/mmllm-cpu/chain-diverse/round-90/`.
32 V_net layers + dense.pt + opt-sparse-net.pt, 15 MB total. V_net + dense are the 25-way FedAvg;
opt-state is the best individual worker's (lowest R{current} ctrl_bpc) for optimizer warmth.

## Run (rounds 91–100)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` auto-discovers the highest existing round, sets `MMLLM_MIX` for the
9-corpus weighted sampler, and hands off to `extend_chain.sh` for 10 more rounds at 100 steps each.
Total wall: ~30–50 min at cpu-mini scale.

DO NOT pass env overrides. The mix weights, recipe, and ablation cap are baked in.

## Watch for

- Round 91's `ctrl_bpc` on Glaive should sit near ~1.20 (the harvest's Glaive val bpc).
  Don't abort if it sits in [1.05, 1.35]. **Abort only if it climbs above 2.0 or `Δ_net`
  collapses to ≤+0.02 across multiple rounds.**
- Per-round wall ≈ 150–230s. If a round takes >500s, check `df -h /tmp` and `free -g`.
- Each round prints an ablation summary with `control bpc`, `Δ_local`, `Δ_net`, `Δ_both`, `synergy`.
  Δ_net should stay in roughly +0.10–0.25 across rounds. The OOD bpc gains are NOT in the per-round prints —
  those come from the post-chain eval battery the dispatcher will run.

If round 91's ctrl_bpc is dramatically HIGHER than 1.55 or Δ_net goes to zero immediately,
something failed to inherit — abort and dump the train logs into the chat.

## Publish your result

After round 100 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-diverse-100"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# Final V_net + dense + opt-state for the next harvest
cp "$ARCHIVE"/round-100/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-100/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-100/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round training logs (rounds 91–100)
for r in $(seq 91 100); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done

cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16",
  "recipe": "stack-3e-2-5.0+mag-coef-on",
  "mix": "9-corpus diverse (glaive:25 cosmopedia:10 fineweb-edu:10 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 open-web-math:10 tiny-stories:5)",
  "n_rounds_extended": 10,
  "n_rounds_total": 100,
  "extended_from": "workers/dispatcher/harvest-25way-r90/round-90 (25-way FedAvg; Glaive-val=1.1958)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (the remote here requires the `claude/*` namespace):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r100" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r100"
git add "$DEST"
git commit -m "chain-diverse rounds 91-100 from harvested-r90 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r100"
```

If the remote 413/502s on a large push, split into 2–3 commits (V_net.0-15, V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round per-round table for rounds 91–100 (wall_s, ctrl_bpc on Glaive val,
   Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/chaindiverse-<HANDLE>-r100`.

The dispatcher will harvest all returning workers via `bash scripts/harvest_chain.sh 100` —
you don't need to run the battery yourself.

## Hard rules

- DO NOT change the mix weights or recipe. The defaults in `run_chain_diverse.sh` and
  `extend_chain.sh` are the documented winners.
- DO NOT start over with `run_chain_stack.sh` or any Glaive-only runner.
- DO publish even on partial failure — a few completed rounds + logs is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`. That's the dispatcher's read-only published starting state.
