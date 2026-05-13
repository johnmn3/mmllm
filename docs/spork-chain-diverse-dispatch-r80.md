# Chain-diverse dispatch (rounds 71 → 80, 9-corpus mix, off R70 harvest)

You are extending the chain by 10 more rounds (round 71 → round 80)
**off the harvested round-70 state** with the same 9-corpus diverse
training mix that produced the previous wave's harvest.

R60 harvest → R70 harvest (5-way FedAvg of last wave, all 7 OOD datasets):

| dataset            | R60 harvest | R70 harvest | Δ bpc   | Δ %     |
|--------------------|------------:|------------:|--------:|--------:|
| glaive-fim-val     |      1.2542 | **1.2125**  | -0.042  |  -3.3%  |
| cosmopedia         |      2.1584 | **2.1081**  | -0.050  |  -2.3%  |
| fineweb-edu        |      2.4471 | **2.4038**  | -0.043  |  -1.8%  |
| magicoder          |      2.3694 | **2.3140**  | -0.055  |  -2.3%  |
| hermes-funcall     |      2.2431 | **2.1900**  | -0.053  |  -2.4%  |
| toolace            |      2.1336 | **2.0566**  | -0.077  |  -3.6%  |
| tiny-stories       |      2.1448 | **2.1255**  | -0.019  |  -0.9%  |
| aesop-fables       |      1.3294 | **1.2913**  | -0.038  |  -2.9%  |
| open-web-math      |      2.5666 | **2.5122**  | -0.054  |  -2.1%  |

Every dataset improved including Glaive. You're stacking another 10 rounds on top.

## New this wave: V-shape per-layer V_local LR

A 6-arm 1-round sweep off R70 (uniform, ramps, V-shapes, monotonic) found
that staggered per-layer LRs on V_local — with **edge layers hot, middle
layer cold** — push Net consolidation harder without breaking ctrl_bpc.
The winning config (Arm G) is now the default in `run_chain_diverse.sh`:

```
MMLLM_LR_LOCAL_MULT=1.0
MMLLM_LR_LAYER_MULTS=7.0,5.0,3.0,2.0,1.0,3.0,5.0,7.0
```

(Layer 0 + layer 7 at 7×, layer 4 trough at 1×; deep V.)

Spike result vs uniform-LR baseline (R70 → R71, 1 round):

| arm | mults                              | ctrl_bpc | Δ_net    | synergy  |
|-----|------------------------------------|----------|----------|----------|
| A   | uniform 1.0 (baseline)             | 1.0643   | +0.1123  | +0.0001  |
| G   | **7,5,3,2,1,3,5,7 (V-shape)**      | **1.0651** | **+0.1556** | **+0.0002** |

ctrl_bpc within noise of baseline (+0.0008); Δ_net **+0.044 higher**; first
**positive synergy** of the sweep. Architectural reading: edge layers (0, 7)
see raw input / near-output features with strong gradient signal — they
benefit from hot LR. Middle layers carry stable consolidating representations
and should evolve slowly.

You don't need to set these env vars; `run_chain_diverse.sh` exports them
automatically. To override (e.g. fall back to uniform LR for comparison),
set MMLLM_LR_LAYER_MULTS yourself before launching.

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
ls workers/dispatcher/harvest-15way-r70/round-70/  # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt
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

## Stage the harvested round-70 state

```bash
bash scripts/stage_chain_diverse.sh 70
```

Copies `workers/dispatcher/harvest-15way-r70/round-70/` → `/tmp/mmllm-cpu/chain-diverse/round-70/`.
32 V_net layers + dense.pt + opt-sparse-net.pt, 15 MB total. V_net + dense are the 15-way FedAvg;
opt-state is the best individual worker's (lowest R{current} ctrl_bpc) for optimizer warmth.

## Run (rounds 71–80)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` auto-discovers the highest existing round, sets `MMLLM_MIX` for the
9-corpus weighted sampler, and hands off to `extend_chain.sh` for 10 more rounds at 100 steps each.
Total wall: ~30–50 min at cpu-mini scale.

DO NOT pass env overrides. The mix weights, recipe, and ablation cap are baked in.

## Watch for

- Round 71's `ctrl_bpc` on Glaive should sit near ~1.21 (the harvest's Glaive val bpc).
  Don't abort if it sits in [1.06, 1.36]. **Abort only if it climbs above 2.0 or `Δ_net`
  collapses to ≤+0.02 across multiple rounds.**
- Per-round wall ≈ 150–230s. If a round takes >500s, check `df -h /tmp` and `free -g`.
- Each round prints an ablation summary with `control bpc`, `Δ_local`, `Δ_net`, `Δ_both`, `synergy`.
  Δ_net should stay in roughly +0.10–0.25 across rounds. The OOD bpc gains are NOT in the per-round prints —
  those come from the post-chain eval battery the dispatcher will run.

If round 71's ctrl_bpc is dramatically HIGHER than 1.56 or Δ_net goes to zero immediately,
something failed to inherit — abort and dump the train logs into the chat.

## Publish your result

After round 80 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-diverse-80"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# Final V_net + dense + opt-state for the next harvest
cp "$ARCHIVE"/round-80/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-80/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-80/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round training logs (rounds 71–80)
for r in $(seq 71 80); do
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
  "n_rounds_total": 80,
  "extended_from": "workers/dispatcher/harvest-15way-r70/round-70 (15-way FedAvg; Glaive-val=1.2125)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (the remote here requires the `claude/*` namespace):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r80" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r80"
git add "$DEST"
git commit -m "chain-diverse rounds 71-80 from harvested-r70 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r80"
```

If the remote 413/502s on a large push, split into 2–3 commits (V_net.0-15, V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round per-round table for rounds 71–80 (wall_s, ctrl_bpc on Glaive val,
   Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/chaindiverse-<HANDLE>-r80`.

The dispatcher will harvest all returning workers via `bash scripts/harvest_chain.sh 80` —
you don't need to run the battery yourself.

## Hard rules

- DO NOT change the mix weights or recipe. The defaults in `run_chain_diverse.sh` and
  `extend_chain.sh` are the documented winners.
- DO NOT start over with `run_chain_stack.sh` or any Glaive-only runner.
- DO publish even on partial failure — a few completed rounds + logs is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`. That's the dispatcher's read-only published starting state.
