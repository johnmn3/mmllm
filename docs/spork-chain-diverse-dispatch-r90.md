# Chain-diverse dispatch (rounds 81 → 90, 9-corpus mix, off R80 harvest)

You are extending the chain by 10 more rounds (round 81 → round 90)
**off the harvested round-80 state** with the same 9-corpus diverse
training mix that produced the previous wave's harvest.

R70 harvest → R80 harvest (14-way FedAvg of last wave, all 9 datasets):

| dataset            | R70 harvest | R80 harvest | Δ bpc   | Δ %     |
|--------------------|------------:|------------:|--------:|--------:|
| glaive-fim-val     |      1.2125 |   1.2368    | +0.024  |  +2.0%  |
| cosmopedia         |      2.1081 |   2.1394    | +0.031  |  +1.5%  |
| fineweb-edu        |      2.4038 |   2.4306    | +0.027  |  +1.1%  |
| magicoder          |      2.3140 |   2.3244    | +0.010  |  +0.4%  |
| hermes-funcall     |      2.1900 |   2.2148    | +0.025  |  +1.1%  |
| toolace            |      2.0566 |   2.0901    | +0.034  |  +1.6%  |
| tiny-stories       |      2.1255 |   2.1565    | +0.031  |  +1.5%  |
| aesop-fables       |      1.2913 |   1.3123    | +0.021  |  +1.6%  |
| open-web-math      |      2.5122 |   2.5225    | +0.010  |  +0.4%  |

**Every dataset REGRESSED.** This is the chain's first wave-level
regression after 6 consecutive improving waves (R20→R70 averaged -7%
OOD per wave). The R71-R80 wave used a symmetric V-shape per-layer
LR (`7,5,3,2,1,3,5,7`) that wasn't right for chain extension — the
high-LR edge layers diverged across workers (V_net layer-0 cos
dropped from 0.97 to 0.85), and FedAvg of divergent worker basins
underperformed the prior consensus state.

## What's new for R81–R90

Two recipe changes baked into `run_chain_diverse.sh` defaults:

1. **Asymmetric V mults**: `7,3,1,0.5,0.3,0.7,2,5` (mean 2.44, span
   0.3×–7×) — sharper trough than the symmetric V, less heat on the
   tail layers. At 1-round comparison this produces a clean per-layer
   movement footprint (mean|V_local| ranges 0.0160-0.0228 vs Gaussian
   baseline 0.0160) without the symmetric V's hot-edge divergence.

2. **Movement-signal distill gate**:
   `MMLLM_DISTILL_GATE_BY_ABLATION=true`,
   `MMLLM_DISTILL_GATE_SIGNAL=movement`.
   At step 70 the gate computes per-layer mean|V_local|. With
   threshold default 0.016 (Gaussian E[|X|]), all layers above
   baseline are gated in. Probe wall: ~0.1s (vs 100s+ for ablation
   gate). 1-round comparison on the asymmetric mults:
   ```
   gate OFF: ctrl_bpc 1.0879  Δ_net +0.1375
   gate ON:  ctrl_bpc 1.0769  Δ_net +0.1484
   ```
   +0.011 Δ_net direction-consistent across runs (single-round noise
   ±0.025). This wave tests whether that compounds over 10 rounds.

You don't need to set these env vars — `run_chain_diverse.sh` exports
them automatically. Operators can override either via shell env.

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
ls workers/dispatcher/harvest-14way-r80/round-80/  # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt
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

## Stage the harvested round-80 state

```bash
bash scripts/stage_chain_diverse.sh 80
```

Copies `workers/dispatcher/harvest-14way-r80/round-80/` → `/tmp/mmllm-cpu/chain-diverse/round-80/`.
32 V_net layers + dense.pt + opt-sparse-net.pt, 15 MB total. V_net + dense are the 14-way FedAvg;
opt-state is the best individual worker's (lowest R{current} ctrl_bpc) for optimizer warmth.

## Run (rounds 81–90)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` auto-discovers the highest existing round, sets `MMLLM_MIX` for the
9-corpus weighted sampler, and hands off to `extend_chain.sh` for 10 more rounds at 100 steps each.
Total wall: ~30–50 min at cpu-mini scale.

DO NOT pass env overrides. The mix weights, recipe, and ablation cap are baked in.

## Watch for

- Round 81's `ctrl_bpc` on Glaive should sit near ~1.24 (the harvest's Glaive val bpc).
  Don't abort if it sits in [1.09, 1.39]. **Abort only if it climbs above 2.0 or `Δ_net`
  collapses to ≤+0.02 across multiple rounds.**
- Per-round wall ≈ 150–230s. If a round takes >500s, check `df -h /tmp` and `free -g`.
- Each round prints an ablation summary with `control bpc`, `Δ_local`, `Δ_net`, `Δ_both`, `synergy`.
  Δ_net should stay in roughly +0.10–0.25 across rounds. The OOD bpc gains are NOT in the per-round prints —
  those come from the post-chain eval battery the dispatcher will run.

If round 81's ctrl_bpc is dramatically HIGHER than 1.59 or Δ_net goes to zero immediately,
something failed to inherit — abort and dump the train logs into the chat.

## Publish your result

After round 90 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-diverse-90"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# Final V_net + dense + opt-state for the next harvest
cp "$ARCHIVE"/round-90/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-90/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-90/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round training logs (rounds 81–90)
for r in $(seq 81 90); do
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
  "n_rounds_total": 90,
  "extended_from": "workers/dispatcher/harvest-14way-r80/round-80 (14-way FedAvg; Glaive-val=1.2368)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (the remote here requires the `claude/*` namespace):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r90" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r90"
git add "$DEST"
git commit -m "chain-diverse rounds 81-90 from harvested-r80 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r90"
```

If the remote 413/502s on a large push, split into 2–3 commits (V_net.0-15, V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round per-round table for rounds 81–90 (wall_s, ctrl_bpc on Glaive val,
   Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/chaindiverse-<HANDLE>-r90`.

The dispatcher will harvest all returning workers via `bash scripts/harvest_chain.sh 90` —
you don't need to run the battery yourself.

## Hard rules

- DO NOT change the mix weights or recipe. The defaults in `run_chain_diverse.sh` and
  `extend_chain.sh` are the documented winners.
- DO NOT start over with `run_chain_stack.sh` or any Glaive-only runner.
- DO publish even on partial failure — a few completed rounds + logs is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`. That's the dispatcher's read-only published starting state.
