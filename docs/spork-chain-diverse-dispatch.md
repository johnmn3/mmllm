# Chain-diverse dispatch (rounds 21 → 30, 8-corpus mix)

You are extending the chain by 10 more rounds (round 21 → round 30)
**off the harvested round-20 state** with an 8-corpus diverse training
mix (instead of the previous Glaive-only training).

Why diverse mix: the chain through round 20 was trained on Glaive
function-call JSON only. The end-state is sharp on Glaive
(in-domain bpc=1.48) but weak everywhere else (OOD bpc 3.0–3.4 across
English / code / function-calls / stories). A 1-round trial (R20 → R21)
with the 8-corpus mix produced:

| dataset            | R20 (Glaive-only) | R21 (1× diverse mix) | Δ bpc   |
|--------------------|------------------:|---------------------:|--------:|
| glaive-fim-val     | 1.4813            | 1.6358               | +0.155  |
| cosmopedia         | 2.9881            | 2.8581               | -0.130  |
| fineweb-edu        | 3.1916            | 3.0038               | -0.188  |
| magicoder          | 3.2055            | 3.0597               | -0.146  |
| hermes-funcall     | 3.0996            | 2.9171               | -0.183  |
| toolace            | 3.0647            | 2.9373               | -0.127  |
| tiny-stories       | 3.1028            | 2.9232               | -0.180  |
| aesop-fables       | 3.3550            | 2.6849               | -0.670  |

Every OOD dataset moved down by 4–6% in a single 100-step round
(aesop-fables by 20%), at a +10% cost to Glaive specialty. Δ_net at
R21 was +0.128. You're extending this trajectory by 9 more rounds.

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
ls workers/dispatcher/chain-diverse/round-20/   # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt
ls scripts/run_chain_diverse.sh                 # the runner
ls scripts/extend_chain.sh                      # which run_chain_diverse.sh hands off to
ls scripts/prep_chain_diverse_corpora.sh        # idempotent corpus prep
ls scripts/stage_chain_diverse_round20.sh       # idempotent state stager
```

## Pre-flight: corpora

The 8-corpus mix needs all eight corpora prepped. The script is
idempotent (every step skips if its output exists at non-zero size),
so you can rerun safely.

```bash
bash scripts/prep_chain_diverse_corpora.sh
```

First-time cost: 20–40 min total (most is Glaive + cosmopedia +
fineweb-edu HF downloads). If a worker comes with `/tmp/mmllm-cpu/`
warm from a prior chain, most steps will skip.

Expected final summary (8 train.bin paths shown — these are the eight
the mix string in `run_chain_diverse.sh` references):

```
  Glaive:
    106M  /tmp/mmllm-cpu/fim-json-v3.train.bin
  Battery train.bin's used by MMLLM_MIX:
    101M  /tmp/mmllm-cpu/battery/cosmopedia.train.bin
    101M  /tmp/mmllm-cpu/battery/fineweb-edu.train.bin
    101M  /tmp/mmllm-cpu/battery/magicoder.train.bin
     10M  /tmp/mmllm-cpu/battery/hermes-funcall.train.bin
    3.3M  /tmp/mmllm-cpu/battery/toolace.train.bin
     17M  /tmp/mmllm-cpu/battery/tiny-stories.train.bin
    2.0M  /tmp/mmllm-cpu/battery/aesop-fables.bin.train.bin
```

## Stage the harvested round-20 state

```bash
bash scripts/stage_chain_diverse_round20.sh
```

Copies `workers/dispatcher/chain-diverse/round-20/` → `/tmp/mmllm-cpu/chain-diverse/round-20/`.
The harvested state is the 5-way FedAvg of 4 first-wave workers'
round-20 endpoints (ctrl_bpc=1.1764, the best model state through
round 20). 32 V_net layers + dense.pt + opt-sparse-net.pt, 15 MB total.

## Run (rounds 21–30)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` sets the `MMLLM_MIX` env var (8-corpus weighted
sampler) and hands off to `extend_chain.sh`. extend_chain.sh reads the
latest existing round in `/tmp/mmllm-cpu/chain-diverse/` (round-20 you
just staged), then runs N=10 more rounds (21–30) at 100 steps each.
Total wall time: ~38–50 min at cpu-mini scale (each round 230–300s
with mixed-corpus sampling).

DO NOT pass env overrides. The mix weights, recipe, and ablation cap
are all baked in.

## Watch for

- Round 21's `ctrl_bpc` on Glaive will be HIGHER than 1.18 — that's
  the cost of diluting from 100% Glaive to 25%. The trial showed R21
  Glaive bpc≈1.35. Don't abort on this; abort only if it climbs above
  2.0 or `Δ_net` collapses to ≤+0.02.
- Per-round wall ≈ 230–320s. If a round takes >500s, check `df -h /tmp`
  (need ~10 GB) and `free -g` (need ~15 GB peak).
- Each round prints an ablation summary like:

  ```
  ── round 21 ablation summary (wall 240s) ──
  ════ ablation summary ════
    control  bpc=1.3x ppl=2.5x
    Δ_local: +0.0xxx
    Δ_net:   +0.1xxx
    Δ_both:  +0.1xxx  (synergy: +0.00xx)
  ```

  Glaive ctrl_bpc on the val should drift slightly upward then stabilize
  as Net consolidates broad features; Δ_net should stay in the
  +0.10–0.20 band across rounds 22–30. The interesting numbers
  (OOD bpc gains) won't show up in per-round prints — those come from
  the post-chain eval battery the dispatcher will run.

If round 21's `ctrl_bpc` is dramatically HIGHER than 1.60 or `Δ_net`
goes to zero immediately, something failed to inherit — abort and
dump the train logs into the chat.

## Publish your result

After round 30 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-diverse-30"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# Final V_net + dense + opt-state for the next extender / harvest
cp "$ARCHIVE"/round-30/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-30/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-30/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round training logs (rounds 21–30)
for r in $(seq 21 30); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done

# Wall.tsv (now covers rounds 1–30)
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16",
  "recipe": "stack-3e-2-5.0+mag-coef-on",
  "mix": "8-corpus diverse (glaive:25 cosmopedia:15 fineweb-edu:15 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 tiny-stories:5)",
  "n_rounds_extended": 10,
  "n_rounds_total": 30,
  "extended_from": "workers/dispatcher/chain-diverse/round-20 (5-way FedAvg harvest, ctrl_bpc=1.1764)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (the remote here requires the `claude/*`
namespace):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r30" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r30"
git add "$DEST"
git commit -m "chain-diverse rounds 21-30 from harvested-r20 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r30"
```

If the remote 413/502s on a large push, split into 2-3 commits
(V_net.0-15, V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round per-round table for rounds 21–30 (wall_s, ctrl_bpc on
   Glaive val, Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/chaindiverse-<HANDLE>-r30`.

The dispatcher will run a multi-dataset eval battery on your final
state to measure OOD bpc gains — you don't need to run the battery
yourself.

## Hard rules

- DO NOT change the mix weights or recipe. The defaults in
  `run_chain_diverse.sh` and `extend_chain.sh` are the documented
  winners (stack-3e-2-5.0 + mag-coef-on; mix shaped by the R21 trial).
- DO NOT start over with `run_chain_stack.sh` or any Glaive-only
  runner. You want `run_chain_diverse.sh` so MMLLM_MIX gets set before
  the handoff.
- DO publish even on partial failure — a few completed rounds + logs is
  more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`. That's the dispatcher's
  read-only starting state.
