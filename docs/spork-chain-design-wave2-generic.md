# Chain-design wave-2 dispatch — generic / 9-corpus diverse mix

You are extending the chain by 10 more rounds (wave-2 rounds 1 → 10)
**off the harvested round-10 state** (`workers/dispatcher/harvest-5way-r10/round-10`),
using the same 9-corpus diverse training mix the prior wave used.

The just-completed wave-1 produced a 5-way FedAvg merge of two FIM
specialists + three generalists. Mean ctrl bpc 0.8973 (best
0.8220, fim-cQUhK). This wave continues from that merged state.

Read `CLAUDE.md` first — it defines spork / chain / Δ_local / Δ_net,
documents the wake/sleep schedule, and lists the conduct rules
("don't delete or overwrite files I didn't put there" applies — your
archive at `/tmp/mmllm-cpu/chain-diverse/` is yours; everything in
`workers/dispatcher/` is not).

## What's new vs prior waves (and what got reverted)

The recent scale-up commit (`7e45963`) intended to widen retrieval
bandwidth 8×. It accidentally also reshuffled `n-heads 4→16` in
cpu-mini, which silently broke checkpoint loading (saved dense.pt
has K/V proj shape `(8, 32)`; the reshuffled model expected `(2, 32)`
→ 240/618 dense tensors silently re-init from scratch per resume).

**The first wave-2 attempt produced three failure reports — none
trained.** The reshuffle has been reverted; cpu-mini is back at
`n-heads=4, head-dim=8` and the saved dense.pt now loads cleanly
(618/618 shapes match).

Defaults baked into `scripts/extend_chain.sh` (these CAN be overridden
via env; see "Memory budget" below):

```
MMLLM_SQRT_N=128            # Local Bank per-router 1 MB × 16 routers × 8 banks = 128 MB
MMLLM_NET_SQRT_N=1024       # NetBank 33.5 MB × 32 layers = 1.07 GB
MMLLM_NET_C_NET=8
MMLLM_MEMORY_TOP_K=128      # Local retrieval bandwidth
MMLLM_MEMORY_SUB_TOP_K=128
MMLLM_NET_TOP_K=512         # Net retrieval bandwidth
MMLLM_NET_SUB_TOP_K=64
MMLLM_N_TRUNKS=16           # 16 ROUTERS per Local Bank (env var is misnamed;
                            # CLAUDE.md: "16 routers per local bank, not trunks").
                            # There is ONE shared trunk (the dense backbone).
MMLLM_BATCH=1               # PER-ROUTER batch. Effective training batch =
                            # MMLLM_N_TRUNKS × MMLLM_BATCH = 16. Wave-2's old
                            # MMLLM_BATCH=16 was a misunderstanding — it
                            # produced effective batch 256 (16× over wave-1).
MMLLM_GRAD_CHECKPOINT=true  # Per-block gradient checkpointing. Drops each
                            # block's intermediates after the block returns
                            # and recomputes during backward. ~30% wall hit,
                            # ~10× lower peak RAM. Required for the wave-2
                            # bandwidth recipe to fit common containers.
rope-theta=500000           # Llama-3 base for long-context extensibility
seq-len=1024  max-pos=8192
n-heads=4 (head-dim=8)      # REVERTED from the broken n-heads=16
```

## Memory budget

The wave-2 bandwidth recipe needs **24+ GB** to run comfortably (full
forward + backward at effective batch 16). 32+ GB containers can scale
MMLLM_BATCH up to 2-4 for higher throughput.

Knobs explained:

- **`MMLLM_BATCH`** is per-ROUTER; effective batch = `MMLLM_N_TRUNKS × MMLLM_BATCH`.
  Default = 1 → effective 16. Set to 2 for effective 32 (32 GB containers),
  4 for effective 64 (48+ GB).
- **`MMLLM_GRAD_CHECKPOINT=true`** (default) cuts peak forward RAM ~10×
  by dropping each block's `combined_scores / latent / SDPA scratch`
  after the block returns and recomputing during backward. Pure compute
  trade-off (~30% wall hit). Set to `false` only on 64+ GB containers
  where the wall savings matter more than the headroom.
- **TOP_K** values (`MMLLM_MEMORY_TOP_K=128`, `MMLLM_NET_TOP_K=512`)
  are the bandwidth contract — keep them at default unless your
  container can't hold the per-block forward at all.

### Recommended tier table

| container RAM | MMLLM_BATCH | MMLLM_NET_TOP_K | MMLLM_NET_SUB_TOP_K | MMLLM_MEMORY_TOP_K | MMLLM_MEMORY_SUB_TOP_K | MMLLM_GRAD_CHECKPOINT | distill |
|--------------:|:-----------:|:---------------:|:-------------------:|:------------------:|:----------------------:|:---------------------:|:-------:|
| **15-16 GB**  | 1 (default) | **64** (wave-1) | 8                   | **16** (wave-1)    | 16                     | **false**             | on      |
| **24 GB**     | 1 (default) | 512 (default)   | 64 (default)        | 128 (default)      | 128 (default)          | true (default)        | off     |
| **32+ GB**    | 2           | 512 (default)   | 64 (default)        | 128 (default)      | 128 (default)          | false                 | on      |

Verified on a 15 GB box at e8c0907 fix: the 15-16 GB row's wave-1-bandwidth
recipe ran a full 100-step round + 4 ablation evals in 1127s wall, producing
ctrl bpc=0.7835, Δ_net=+0.0116 (NetBank is contributing). The full wave-2
bandwidth (NET_TOP_K=512) doesn't fit 15 GB even with grad-checkpointing
because the carried-forward `opt-sparse-net.pt` deserializes to ~1-3 GB of
Python-dict overhead (sparse Adam's `row_to_buf` is a `{int → int}` dict
that grows per touched row), and the per-step row-touch rate at NET_TOP_K=512
grows that footprint another ~5-7 GB through the round. The 15-16 GB tier
uses wave-1 bandwidth knobs (NET_TOP_K=64, MEMORY_TOP_K=16, sub=8/16) where
the row-touch rate is 4-8× slower, leaving headroom for the optimizer state
to grow within budget. Grad-checkpointing is OFF at this tier — at wave-1
bandwidth the activation snapshot is already small, and the ~2× wall hit
from CPU-side recompute isn't worth it.

Note: the 15-16 GB row is a recipe variant, not the wave-2 contract —
bandwidth is wave-1's (3 Gemma heads' worth → 1 Gemma head's worth).
Birds running it should report the tier they used.

Pass overrides via env BEFORE invoking the script:

```bash
# 32 GB container — increase effective batch to 32 for higher throughput
MMLLM_BATCH=2 \
  bash scripts/run_chain_diverse.sh 10 20
```

The script uses `: ${VAR:=default}` so env-passed values win.

## Setup

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/
pip install -e . --quiet

ls workers/dispatcher/harvest-5way-r10/round-10/ | wc -l   # 66 files:
#   32× V_net.{0..31}.bin       (32 MB each, 1 GB total)
#    1  dense.pt
#   32× opt-sparse-net.{0..31}.pt   (chunked Adam state, 2-13 MB each)
#    1  opt-sparse-net.meta.pt   (param_groups + pid list)
ls scripts/run_chain_diverse.sh
ls scripts/extend_chain.sh
ls scripts/prep_chain_diverse_corpora.sh
```

### If `git fetch` times out

The branch HEAD carries ~1.3 GB of binary bank artifacts. If your
proxy can't handle the pack, do a partial fetch and pull the binary
blobs separately:

```bash
git fetch origin claude/fim-training-cycle-T3giJ \
  --filter=blob:limit=20M --depth=1
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/

# Now pull the dispatcher harvest's binaries one at a time:
mkdir -p workers/dispatcher/harvest-5way-r10/round-10
for i in $(seq 0 31); do
  git cat-file -p "origin/claude/fim-training-cycle-T3giJ:workers/dispatcher/harvest-5way-r10/round-10/V_net.${i}.bin" \
    > "workers/dispatcher/harvest-5way-r10/round-10/V_net.${i}.bin"
done
# Repeat for opt-sparse-net.*.pt, dense.pt, opt-sparse-net.meta.pt.
```

## Pre-flight: free disk

Each round writes ~1.3 GB to `/tmp/mmllm-cpu/chain-diverse/round-N/`.
Per-round prune in `extend_chain.sh` (commit `52a238f`) keeps live
state at ~3 GB by dropping round-(N-2) after round-N starts.

```bash
df -h /tmp                                  # want >=20 GB free
rm -rf /tmp/mmllm-cpu/chain-diverse
rm -rf /tmp/mmllm-cpu/fim-chain-stack.ckpts
rm -f  /tmp/mmllm-cpu/harvested-r*.bank*.bin
rm -f  /tmp/mmllm-cpu/harvested-r*.dense.pt
df -h /tmp
```

## Pre-flight: corpora

```bash
bash scripts/prep_chain_diverse_corpora.sh
```

Idempotent. First-time cost ~20-40 min (HF downloads). Builds the
9-corpus mix: glaive-fim-v3, cosmopedia, fineweb-edu, magicoder,
hermes-funcall, toolace, aesop-fables, open-web-math, tiny-stories.

## Stage the harvested round-10 state

```bash
ARCHIVE=/tmp/mmllm-cpu/chain-diverse
mkdir -p "$ARCHIVE/round-10"
cp workers/dispatcher/harvest-5way-r10/round-10/* "$ARCHIVE/round-10/"
ls "$ARCHIVE/round-10/" | wc -l   # 66
du -sh "$ARCHIVE/round-10/"        # ~1.3 GB
```

## Run (rounds 11 → 20)

```bash
# Pass any RAM-tuning env vars BEFORE the script. On 15 GB containers:
MMLLM_BATCH=4 MMLLM_MEMORY_SUB_TOP_K=32 MMLLM_NET_SUB_TOP_K=32 \
  bash scripts/run_chain_diverse.sh 10 20

# On 32+ GB containers, just:
bash scripts/run_chain_diverse.sh 10 20
```

`run_chain_diverse.sh` exports MMLLM_MIX + MMLLM_LR_LAYER_MULTS +
MMLLM_DISTILL_GATE_*, then hands off to `extend_chain.sh` for 10
rounds at 100 steps each.

Per-round wall depends on (B × T × layers × banks):
- 15 GB + B=4: expect ~600-900s/round, ~2 hr total
- 32 GB + B=16: expect ~200-300s/round, ~40-60 min total

## Live reporting (don't go silent for an hour)

Per CLAUDE.md's "Reporting discipline" section. Arm a Monitor over
the training log — every signal line is one short chat update:

```bash
tail -F /tmp/mmllm-cpu/chain-diverse/round-*.train.log \
  | grep --line-buffered -E \
    "step|eval|ablation|control|Δ_local|Δ_net|training complete|wall|Traceback|RuntimeError|AssertionError|ZeroDivisionError|Killed|OOM|FAILED|WARN|NaN"
```

For each notification fire one short message back:
- **Round header**: "starting round N off prev_dense"
- **Step prints** (every ~20 steps): "round N step S: loss=L lr=R"
- **Ablation summary** (post step 70): ctrl_bpc, Δ_local, Δ_net,
  Δ_both, synergy in one line
- **Round complete**: wall_s + 1-line digest
- **Any failure mode**: traceback excerpt + abort

If a round NaNs or `ctrl_bpc` climbs above 2.0, abort the remaining
rounds and publish what you have — partial results beat zero.

**If your first round OOMs**, don't keep iterating silently. Stop,
report the OOM with the alloc size, and either drop one tier on the
recommended table or ask the dispatcher.

## Watch for

- The first WARN line on resume should say
  `0/618 param tensors skipped due to shape mismatch` (or no warn at
  all). If it says 240/618, the head-dim revert didn't make it into
  your checkout — `git pull` again before running.
- Round 11's `ctrl_bpc` should sit in roughly [0.85, 1.10]
  (continuing from harvest mean 0.8973).
- **Δ_net should be positive across most rounds** at this wave —
  V_net was populated by the prior wave, so distillation has
  somewhere to go.

## Publish your result

After round 20 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-design-r2-10"
mkdir -p "$DEST"
ARCHIVE=/tmp/mmllm-cpu/chain-diverse

cp "$ARCHIVE"/round-20/V_net.*.bin            "$DEST/"
cp "$ARCHIVE"/round-20/dense.pt               "$DEST/"
cp "$ARCHIVE"/round-20/opt-sparse-net.*.pt    "$DEST/" 2>/dev/null || true

for r in $(seq 11 20); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16 design banks, sparse-delta publish, wave-2 (n-heads=4 reverted)",
  "recipe": "stack-3e-2-5.0+mag-coef-on+asym-V+movement-gate+design-banks+wide-retrieval",
  "mix": "9-corpus diverse (glaive:25 cosmopedia:10 fineweb-edu:10 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 open-web-math:10 tiny-stories:5)",
  "wave_kind": "generalist",
  "n_rounds_trained": 10,
  "container_ram_gb": <fill-in>,
  "MMLLM_BATCH": <fill-in>,
  "MMLLM_MEMORY_SUB_TOP_K": <fill-in>,
  "MMLLM_NET_SUB_TOP_K": <fill-in>,
  "extended_from": "workers/dispatcher/harvest-5way-r10/round-10 (5-way FedAvg; wave-1 ctrl_bpc mean 0.8973)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r2-10" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r2-10"

git add "$DEST"
git commit -m "chain-design wave-2 rounds 11-20 from harvested-r10 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r2-10"
```

If the push 413/502s, split V_net into 2 commits.

## What to report back

1. Per-round table: wall_s, ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy.
2. Gate probe output at step 70 of each round.
3. Branch name `claude/chaindiverse-<HANDLE>-r2-10`.
4. The B / SUB_TOP_K values you ran at, and container RAM.

Dispatcher will harvest via `bash scripts/harvest_chain.sh 2-10`.

## Hard rules (these are real)

- DO NOT change MMLLM_MIX (the corpus weights), MMLLM_LR_LAYER_MULTS,
  MMLLM_DISTILL_GATE_*, bank sizes, n-heads, head-dim, or n-routers
  (MMLLM_N_TRUNKS is misnamed — it controls routers, not trunks;
  there's only one trunk, the dense backbone).
  Those ARE the architecture / recipe contract.
- B and SUB_TOP_K ARE tunable to fit RAM. Document what you ran at.
- DO publish on partial failure — a few completed rounds + logs
  is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/` or anyone else's `workers/<h>/`.
- If your first OOM is unrecoverable, publish a meta.json with
  `status: failed` and `n_rounds_trained: 0` so the dispatcher knows.
