# Chain-diverse dispatch (rounds 31 → 40, 8-corpus mix, off R30 harvest)

You are extending the chain by 10 more rounds (round 31 → round 40)
**off the harvested round-30 state** with the same 8-corpus diverse
training mix that produced the round-30 result.

Why another wave: the chain through round 20 was Glaive-only and weak
OOD (3.0–3.4 bpc across English / code / function-calls / stories).
The first chain-diverse wave (rounds 21–30, harvested 5-way) dropped
OOD mean by 22% and improved Glaive in-domain by 3% — diverse training
acted as regularization, not specialty cost. You're stacking another
10 rounds on top.

R20 harvest → R30 harvest (5-way FedAvg of last wave, all 7 OOD datasets):

| dataset            | R20 harvest | R30 harvest | Δ bpc   | Δ %     |
|--------------------|------------:|------------:|--------:|--------:|
| glaive-fim-val     | 1.4813      | **1.4375**  | -0.044  |  -3.0%  |
| cosmopedia         | 2.9881      | **2.4669**  | -0.521  | -17.4%  |
| fineweb-edu        | 3.1916      | **2.6896**  | -0.502  | -15.7%  |
| magicoder          | 3.2055      | **2.7118**  | -0.494  | -15.4%  |
| hermes-funcall     | 3.0996      | **2.5486**  | -0.551  | -17.8%  |
| toolace            | 3.0647      | **2.5010**  | -0.564  | -18.4%  |
| tiny-stories       | 3.1028      | **2.4807**  | -0.622  | -20.1%  |
| aesop-fables       | 3.3550      | **1.8283**  | -1.527  | -45.5%  |

Every dataset improved including Glaive. Workers in the previous wave
ended at individual ctrl_bpc in [1.249, 1.333] on Glaive train slice;
the 5-way FedAvg landed at 1.4375 on Glaive val and beat every
individual worker on the OOD battery.

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
ls workers/dispatcher/harvest-5way-r30/round-30/  # 34 files: 32× V_net + dense.pt + opt-sparse-net.pt
ls scripts/run_chain_diverse.sh                   # the runner (auto-discovers highest round)
ls scripts/extend_chain.sh                        # which run_chain_diverse.sh hands off to
ls scripts/prep_chain_diverse_corpora.sh          # idempotent corpus prep (same 8 corpora)
ls scripts/stage_chain_diverse_round30.sh         # idempotent stager for round-30
```

## Pre-flight: corpora

Same 8-corpus mix as the previous wave. If a worker comes with
`/tmp/mmllm-cpu/` warm from the prior chain, every step skips
(corpora are byte-identical to what produced the R30 harvest).

```bash
bash scripts/prep_chain_diverse_corpora.sh
```

First-time cost: 20–40 min total (most is Glaive + cosmopedia +
fineweb-edu HF downloads). Idempotent — every step skips if its output
exists at non-zero size.

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

## Stage the harvested round-30 state

```bash
bash scripts/stage_chain_diverse_round30.sh
```

Copies `workers/dispatcher/harvest-5way-r30/round-30/` →
`/tmp/mmllm-cpu/chain-diverse/round-30/`. 32 V_net layers + dense.pt +
opt-sparse-net.pt, 15 MB total. The opt state is `opus47`'s (best
individual worker in the prior wave at R30 ctrl_bpc 1.2492); V_net and
dense are the 5-way FedAvg.

If your `/tmp/mmllm-cpu/chain-diverse/` is warm from a prior session
and you have a round-30 from your own run, the stager will skip and
you'd continue from your local state. If you want a clean run, `rm -rf
/tmp/mmllm-cpu/chain-diverse/round-30` first, then stage.

## Run (rounds 31–40)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` auto-discovers the highest existing round in
`/tmp/mmllm-cpu/chain-diverse/` (your freshly-staged round-30), sets
the `MMLLM_MIX` env var (8-corpus weighted sampler), and hands off to
`extend_chain.sh` for N=10 more rounds (31–40) at 100 steps each.
Total wall time: ~30–50 min at cpu-mini scale (the prior wave's
workers landed at 149–223s per round depending on disk/CPU contention).

DO NOT pass env overrides. The mix weights, recipe, and ablation cap
are all baked in.

## Watch for

- Round 31's `ctrl_bpc` on Glaive will be close to ~1.32 (the prior
  wave's R30 mean was 1.28, harvest was 1.44). Don't abort if it sits
  in the 1.25–1.45 band. **Abort only if it climbs above 2.0 or
  `Δ_net` collapses to ≤+0.02 across multiple rounds.**
- Per-round wall ≈ 150–230s. If a round takes >500s, check `df -h /tmp`
  (need ~10 GB) and `free -g` (need ~15 GB peak).
- Each round prints an ablation summary like:

  ```
  ── round 31 ablation summary (wall 175s) ──
  ════ ablation summary ════
    control  bpc=1.3x ppl=2.5x
    Δ_local: +0.0xxx
    Δ_net:   +0.1xxx
    Δ_both:  +0.1xxx  (synergy: +0.00xx)
  ```

  Glaive ctrl_bpc should oscillate in a 1.25–1.40 band; Δ_net should
  stay in roughly +0.10–0.25. The interesting numbers (OOD bpc gains)
  won't show up in per-round prints — those come from the post-chain
  eval battery the dispatcher will run.

If round 31's `ctrl_bpc` is dramatically HIGHER than 1.70 or `Δ_net`
goes to zero immediately, something failed to inherit — abort and
dump the train logs into the chat.

## Publish your result

After round 40 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-diverse-40"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# Final V_net + dense + opt-state for the next extender / harvest
cp "$ARCHIVE"/round-40/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-40/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-40/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round training logs (rounds 31–40)
for r in $(seq 31 40); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done

# Wall.tsv (now covers rounds 1–40)
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16",
  "recipe": "stack-3e-2-5.0+mag-coef-on",
  "mix": "8-corpus diverse (glaive:25 cosmopedia:15 fineweb-edu:15 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 tiny-stories:5)",
  "n_rounds_extended": 10,
  "n_rounds_total": 40,
  "extended_from": "workers/dispatcher/harvest-5way-r30/round-30 (5-way FedAvg of chain-diverse-30 wave; Glaive-val=1.4375, OOD mean=2.46)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (the remote here requires the `claude/*`
namespace):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r40" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r40"
git add "$DEST"
git commit -m "chain-diverse rounds 31-40 from harvested-r30 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r40"
```

If the remote 413/502s on a large push, split into 2–3 commits
(V_net.0-15, V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round per-round table for rounds 31–40 (wall_s, ctrl_bpc on
   Glaive val, Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/chaindiverse-<HANDLE>-r40`.

The dispatcher will run the 7-dataset OOD eval battery on the 5-way
FedAvg of all workers' final R40 states — you don't need to run the
battery yourself.

## Hard rules

- DO NOT change the mix weights or recipe. The defaults in
  `run_chain_diverse.sh` and `extend_chain.sh` are the documented
  winners (stack-3e-2-5.0 + mag-coef-on; mix unchanged from the wave
  that produced the R30 harvest).
- DO NOT start over with `run_chain_stack.sh` or any Glaive-only
  runner. You want `run_chain_diverse.sh` so MMLLM_MIX gets set before
  the handoff to `extend_chain.sh`.
- DO publish even on partial failure — a few completed rounds + logs
  is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`. That's the dispatcher's
  read-only published starting state.
