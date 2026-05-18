# Spork-chain dogfood prompt v2 (extend, don't restart)

**v1 was wrong.** v1 (`docs/spork-chain-dogfood.md`) told the worker to
run a 10-round chain from scratch with a different seed and then FedAvg
the two parallel endpoints. That ran a wasted 40-min compute arm — the
right design is to **EXTEND** the dispatcher's chain by 10 more rounds,
carrying the dispatcher's V_net + dense + opt-state forward as the seed.

If you previously ran v1 and are reading this, **sorry — that was on me,
not you.** The task is actually trivial: 1 fetch, 1 stage, 1 command. v1
asked you to repeat work I had already done. v2 has you build on top.

---

You are extending the dispatcher's 10-round spork chain by an additional
N rounds (default 10 → end state will be round 20 of the same chain).

The dispatcher's chain end-state is already published on the branch at
`workers/dispatcher/spork-chain-10/round-10/`:

  V_net.{0..31}.bin   — 32 layers × 64²×8 fp32, 4 MB total (the seed)
  dense.pt            — shared 2.4 MB router
  opt-sparse-net.pt   — Adam moments for V_net (so extend resumes cleanly)

Final-round metrics from the dispatcher's chain (sanity check):

  ctrl_bpc = 1.5991  ppl = 3.03   Δ_net = +0.2205   Δ_both = +0.2201

Read `CLAUDE.md` first; it defines "spork" / "chain" / "Δ_local" /
"Δ_net" and lists conduct rules. Read "Winning bank-engagement recipes"
for the stack-3e-2-5.0 + mag-coef-on recipe — it's the default in the
scripts, don't override.

## Setup (one fetch, then go)

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/
pip install -e . --quiet
```

Confirm:

```bash
ls workers/dispatcher/spork-chain-10/round-10/   # V_net.*.bin + dense.pt + opt-sparse-net.pt
ls scripts/extend_chain.sh                       # the runner you'll use
```

## Pre-flight: corpus

If `/tmp/mmllm-cpu/fim-json-v3.train.bin` doesn't exist:

```bash
bash scripts/build_glaive_fim_corpus.sh   # ~5-10 min first time
```

## Stage the dispatcher's end-state as an archive `extend_chain.sh` can resume

```bash
ARCHIVE=/tmp/mmllm-cpu/chain-extended
rm -rf "$ARCHIVE"
mkdir -p "$ARCHIVE/round-10"
cp workers/dispatcher/spork-chain-10/round-10/V_net.*.bin "$ARCHIVE/round-10/"
cp workers/dispatcher/spork-chain-10/round-10/dense.pt    "$ARCHIVE/round-10/"
cp workers/dispatcher/spork-chain-10/round-10/opt-sparse-net.pt "$ARCHIVE/round-10/"
cp workers/dispatcher/spork-chain-10/wall.tsv             "$ARCHIVE/"
```

## Run (rounds 11–20)

```bash
bash scripts/extend_chain.sh "$ARCHIVE" 10 100
```

`extend_chain.sh` reads the latest existing round in `$ARCHIVE` (round-10
from the dispatcher), then runs N=10 more rounds (11 through 20) at 100
steps each. Total wall time: ~38 min at cpu-mini scale (each round
~230s with `MMLLM_ABLATION_EVAL_CAP=25000` baked in).

DO NOT pass any env overrides. The recipe is fixed in the script.

## Watch for

- Per-round wall ≈ 220-240s. If a round takes >400s, check `df -h /tmp`
  (need ~10 GB) and `free -g` (need ~15 GB peak).
- Each round prints an ablation summary like:

  ```
  ── round 11 ablation summary (wall 226s) ──
  ════ ablation summary ════
    control  bpc=1.5xxx ppl=2.9x
    Δ_local: +0.0000
    Δ_net:   +0.2xxx
    Δ_both:  +0.2xxx  (synergy: +0.00xx)
  ```

Expected trajectory: continued bpc descent from 1.60 (round 10) with
diminishing returns. Δ_net should stay in the +0.18-0.22 band across
rounds 11-20.

If round 11's ctrl_bpc is HIGHER than 1.60, something failed to
inherit — abort and dump the train logs into the chat. Most likely
cause: the staging copies didn't land correctly (compare bytes).

## Publish your result

After round 20 completes:

```bash
HANDLE="<your-handle>"    # lowercase, no spaces
DEST="workers/$HANDLE/spork-chain-20"
mkdir -p "$DEST"

# Final V_net + dense + opt for the next extender (and for any harvest)
cp "$ARCHIVE"/round-20/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-20/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-20/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

# Per-round logs (rounds 11-20 you just ran)
for r in $(seq 11 20); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done

# Updated wall.tsv (now covers rounds 1-20)
cp "$ARCHIVE/wall.tsv" "$DEST/"

# Meta — read final-round ablation from log.jsonl
cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16",
  "recipe": "stack-3e-2-5.0+mag-coef-on",
  "n_rounds_extended": 10,
  "n_rounds_total": 20,
  "extended_from": "workers/dispatcher/spork-chain-10",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (NOT the dispatcher's). The remote here requires
the `claude/*` namespace:

```bash
git checkout -b "claude/sporkchain-${HANDLE}-extend10" 2>/dev/null \
  || git checkout "claude/sporkchain-${HANDLE}-extend10"
git add "$DEST"
git commit -m "spork-chain extend rounds 11-20 from dispatcher — final_ctrl=<...>"
git push -u origin "claude/sporkchain-${HANDLE}-extend10"
```

If the remote 413/502s on a large push, split into 2-3 commits (V_net.0-15,
V_net.16-31, then dense+opt-state).

## What to report back

1. The 10-round ablation table for rounds 11-20 (wall_s, ctrl_bpc,
   Δ_local, Δ_net, Δ_both, synergy).
2. The branch name `claude/sporkchain-<HANDLE>-extend10`.

## Hard rules

- DO NOT change the recipe. The defaults in `extend_chain.sh` are the
  documented winners; overriding any will desynchronize from the
  dispatcher's trajectory and the resume-state won't behave consistently.
- DO NOT start over with `run_chain_stack.sh`. That's the runner for
  rounds 1-N from a fresh seed; you want `extend_chain.sh` which
  continues an existing archive.
- DO publish even on partial failure — a few completed rounds + logs is
  more valuable than a missing run.
