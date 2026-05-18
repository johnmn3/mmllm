# Chain-diverse dispatch (rounds 41 → 50, 8-corpus mix, off R40 harvest)

You are extending the chain by 10 more rounds (round 41 → round 50)
**off the harvested round-40 state** with the same 8-corpus diverse
training mix that produced the previous wave's harvest.

R30 harvest → R40 harvest (5-way FedAvg of last wave, all 7 OOD datasets):

| dataset            | R30 harvest | R40 harvest | Δ bpc   | Δ %     |
|--------------------|------------:|------------:|--------:|--------:|
| glaive-fim-val     |      1.4375 | **1.3572**  | -0.080  |  -5.6%  |
| cosmopedia         |      2.4669 | **2.2900**  | -0.177  |  -7.2%  |
| fineweb-edu        |      2.6896 | **2.5637**  | -0.126  |  -4.7%  |
| magicoder          |      2.7118 | **2.5471**  | -0.165  |  -6.1%  |
| hermes-funcall     |      2.5486 | **2.3914**  | -0.157  |  -6.2%  |
| toolace            |      2.5010 | **2.3081**  | -0.193  |  -7.7%  |
| tiny-stories       |      2.4807 | **2.3052**  | -0.175  |  -7.1%  |
| aesop-fables       |      1.8283 | **1.5233**  | -0.305  | -16.7%  |

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
ls workers/dispatcher/harvest-5way-r40/round-40/  # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt
ls scripts/run_chain_diverse.sh                   # the runner (auto-discovers highest round)
ls scripts/extend_chain.sh                        # which run_chain_diverse.sh hands off to
ls scripts/prep_chain_diverse_corpora.sh          # idempotent corpus prep
ls scripts/stage_chain_diverse_round40.sh  # idempotent stager for round-40
```

## Pre-flight: corpora

Same 8-corpus mix as the previous wave (corpora byte-identical to prior).

```bash
bash scripts/prep_chain_diverse_corpora.sh
```

First-time cost: 20–40 min (most is HF downloads). Idempotent — skips any step whose output exists.

## Stage the harvested round-40 state

```bash
bash scripts/stage_chain_diverse_round40.sh
```

Copies `workers/dispatcher/harvest-5way-r40/round-40/` → `/tmp/mmllm-cpu/chain-diverse/round-40/`.
32 V_net layers + dense.pt + opt-sparse-net.pt, 15 MB total. V_net + dense are the 5-way FedAvg;
opt-state is the best individual worker's (lowest R{current} ctrl_bpc) for optimizer warmth.

## Run (rounds 41–50)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` auto-discovers the highest existing round, sets `MMLLM_MIX` for the
8-corpus weighted sampler, and hands off to `extend_chain.sh` for 10 more rounds at 100 steps each.
Total wall: ~30–50 min at cpu-mini scale.

DO NOT pass env overrides. The mix weights, recipe, and ablation cap are baked in.

## Watch for

- Round 41's `ctrl_bpc` on Glaive should sit near ~1.36 (the harvest's Glaive val bpc).
  Don't abort if it sits in [1.21, 1.51]. **Abort only if it climbs above 2.0 or `Δ_net`
  collapses to ≤+0.02 across multiple rounds.**
- Per-round wall ≈ 150–230s. If a round takes >500s, check `df -h /tmp` and `free -g`.
- Each round prints an ablation summary with `control bpc`, `Δ_local`, `Δ_net`, `Δ_both`, `synergy`.
  Δ_net should stay in roughly +0.10–0.25 across rounds. The OOD bpc gains are NOT in the per-round prints —
  those come from the post-chain eval battery the dispatcher will run.

If round 41's ctrl_bpc is dramatically HIGHER than 1.71 or Δ_net goes to zero immediately,
something failed to inherit — abort and dump the train logs into the chat.

## Publish your result

After round 50 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-diverse-50"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# Final V_net + dense + opt-state for the next harvest
cp "$ARCHIVE"/round-50/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-50/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-50/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round training logs (rounds 41–50)
for r in $(seq 41 50); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done

cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16",
  "recipe": "stack-3e-2-5.0+mag-coef-on",
  "mix": "8-corpus diverse (glaive:25 cosmopedia:15 fineweb-edu:15 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 tiny-stories:5)",
  "n_rounds_extended": 10,
  "n_rounds_total": 50,
  "extended_from": "workers/dispatcher/harvest-5way-r40/round-40 (5-way FedAvg; Glaive-val=1.3572)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (the remote here requires the `claude/*` namespace):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r50" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r50"
git add "$DEST"
git commit -m "chain-diverse rounds 41-50 from harvested-r40 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r50"
```

If the remote 413/502s on a large push, split into 2–3 commits (V_net.0-15, V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round per-round table for rounds 41–50 (wall_s, ctrl_bpc on Glaive val,
   Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/chaindiverse-<HANDLE>-r50`.

The dispatcher will harvest all returning workers via `bash scripts/harvest_chain.sh 50` —
you don't need to run the battery yourself.

## Hard rules

- DO NOT change the mix weights or recipe. The defaults in `run_chain_diverse.sh` and
  `extend_chain.sh` are the documented winners.
- DO NOT start over with `run_chain_stack.sh` or any Glaive-only runner.
- DO publish even on partial failure — a few completed rounds + logs is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`. That's the dispatcher's read-only published starting state.
