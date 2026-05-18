# Chain-diverse dispatch (rounds 61 → 70, 9-corpus mix, off R60 harvest)

You are extending the chain by 10 more rounds (round 61 → round 70)
**off the harvested round-60 state** with the same 9-corpus diverse
training mix that produced the previous wave's harvest.

R50 harvest → R60 harvest (5-way FedAvg of last wave, all 7 OOD datasets):

| dataset            | R50 harvest | R60 harvest | Δ bpc   | Δ %     |
|--------------------|------------:|------------:|--------:|--------:|
| glaive-fim-val     |      1.3115 | **1.2542**  | -0.057  |  -4.4%  |
| cosmopedia         |      2.2324 | **2.1584**  | -0.074  |  -3.3%  |
| fineweb-edu        |      2.5087 | **2.4471**  | -0.062  |  -2.5%  |
| magicoder          |      2.4517 | **2.3694**  | -0.082  |  -3.4%  |
| hermes-funcall     |      2.3278 | **2.2431**  | -0.085  |  -3.6%  |
| toolace            |      2.2366 | **2.1336**  | -0.103  |  -4.6%  |
| tiny-stories       |      2.2706 | **2.1448**  | -0.126  |  -5.5%  |
| aesop-fables       |      1.4187 | **1.3294**  | -0.089  |  -6.3%  |
| open-web-math      |      2.6563 | **2.5666**  | -0.090  |  -3.4%  |

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
ls workers/dispatcher/harvest-10way-r60/round-60/  # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt
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

## Stage the harvested round-60 state

```bash
bash scripts/stage_chain_diverse.sh 60
```

Copies `workers/dispatcher/harvest-10way-r60/round-60/` → `/tmp/mmllm-cpu/chain-diverse/round-60/`.
32 V_net layers + dense.pt + opt-sparse-net.pt, 15 MB total. V_net + dense are the 10-way FedAvg;
opt-state is the best individual worker's (lowest R{current} ctrl_bpc) for optimizer warmth.

## Run (rounds 61–70)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` auto-discovers the highest existing round, sets `MMLLM_MIX` for the
9-corpus weighted sampler, and hands off to `extend_chain.sh` for 10 more rounds at 100 steps each.
Total wall: ~30–50 min at cpu-mini scale.

DO NOT pass env overrides. The mix weights, recipe, and ablation cap are baked in.

## Watch for

- Round 61's `ctrl_bpc` on Glaive should sit near ~1.25 (the harvest's Glaive val bpc).
  Don't abort if it sits in [1.10, 1.40]. **Abort only if it climbs above 2.0 or `Δ_net`
  collapses to ≤+0.02 across multiple rounds.**
- Per-round wall ≈ 150–230s. If a round takes >500s, check `df -h /tmp` and `free -g`.
- Each round prints an ablation summary with `control bpc`, `Δ_local`, `Δ_net`, `Δ_both`, `synergy`.
  Δ_net should stay in roughly +0.10–0.25 across rounds. The OOD bpc gains are NOT in the per-round prints —
  those come from the post-chain eval battery the dispatcher will run.

If round 61's ctrl_bpc is dramatically HIGHER than 1.60 or Δ_net goes to zero immediately,
something failed to inherit — abort and dump the train logs into the chat.

## Publish your result

After round 70 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-diverse-70"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# Final V_net + dense + opt-state for the next harvest
cp "$ARCHIVE"/round-70/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-70/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-70/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round training logs (rounds 61–70)
for r in $(seq 61 70); do
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
  "n_rounds_total": 70,
  "extended_from": "workers/dispatcher/harvest-10way-r60/round-60 (10-way FedAvg; Glaive-val=1.2542)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (the remote here requires the `claude/*` namespace):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r70" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r70"
git add "$DEST"
git commit -m "chain-diverse rounds 61-70 from harvested-r60 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r70"
```

If the remote 413/502s on a large push, split into 2–3 commits (V_net.0-15, V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round per-round table for rounds 61–70 (wall_s, ctrl_bpc on Glaive val,
   Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/chaindiverse-<HANDLE>-r70`.

The dispatcher will harvest all returning workers via `bash scripts/harvest_chain.sh 70` —
you don't need to run the battery yourself.

## Hard rules

- DO NOT change the mix weights or recipe. The defaults in `run_chain_diverse.sh` and
  `extend_chain.sh` are the documented winners.
- DO NOT start over with `run_chain_stack.sh` or any Glaive-only runner.
- DO publish even on partial failure — a few completed rounds + logs is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`. That's the dispatcher's read-only published starting state.
