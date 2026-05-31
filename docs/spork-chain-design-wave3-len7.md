# Chain-design wave-3 dispatch — round-length-7 spork chain

Extend the chain by **10 rounds of 7 steps each** (= 70 training
steps total) off the harvested round-10 state
(`workers/dispatcher/harvest-5way-r10/round-10`), continuing the
9-corpus diverse mix.

Round-length-7 was selected as the CPU sweep optimum at a fixed
compute budget — length-7 (4 rounds, 28 steps) beat length-6 (5
rounds, 30 steps) and length-10 (3 rounds, 30 steps) on ctrl:

| round-length | rounds | steps | ctrl  | Δ_net |
|--------------|-------:|------:|------:|------:|
| 6            | 5      | 30    | 10.63 | +0.59 |
| **7**        | 4      | 28    | **10.28** | +0.82 |
| 10           | 3      | 30    | 11.38 | +0.40 |

Long enough rounds for V_local to learn, frequent enough resets to
inject diversity. Wave-3 confirms the recipe carries to the
production 9-corpus mix.

Read `CLAUDE.md` first — defines spork / chain / Δ_local / Δ_net,
wake/sleep, conduct rules.

> **Worker note — stop-hook / commit warnings.** The setup step below
> stages ~1 GB of upstream content (corpora + 32 V_net.bin files +
> scripts + docs + harvests) into your working tree, checked out from
> `claude/fim-training-cycle-T3giJ`. Your stop-hook or shell wrapper
> may notice these and ask you to commit + push them. **IGNORE IT.**
> They are training INPUTS, not your deliverable — they already live
> on the source branch. Your publish branch contains ONLY
> `workers/<HANDLE>/chain-design-r20/`. Committing the staged upstream
> files would balloon your publish branch by ~1 GB and fail to push.

## What's new since wave-2

Three code changes landed:

1. **Stochastic-depth-in-backward** (`MMLLM_BWD_SKIP_FRAC_NET_ONLY`).
   Net-only blocks (24 of the 32) run their forward inside
   `torch.no_grad()` so backward never traverses their internals.
   Default for this wave: **1.0** (every net-only block skips its
   backward each step). Verified to drop per-step wall ~33% with
   Δ_net signal preserved.
2. **Round-relative warmup ramp**. `extend_chain.sh` already resets
   the step counter to 1 each round, so the existing
   `MMLLM_LR_WARMUP=$((STEPS * 70 / 100))` logic now produces a
   real linear ramp across the first ⌊7 × 0.7⌋ = 4 steps of each
   round, then cosine decay for the remaining 3. Falls out of the
   round reset; no new env var to set.
3. **Tolerant `load_state_dict`** in `mmllm.optim`. Fixes a
   `row_to_buf` dtype-drift bug that crashed round-2+ of any chained
   resume. Required to survive the chain.

Recipe / contract is otherwise unchanged from wave-2.

## Defaults

Inherited from `scripts/extend_chain.sh`:

```
MMLLM_SQRT_N=128
MMLLM_NET_SQRT_N=1024
MMLLM_NET_C_NET=8
MMLLM_MEMORY_TOP_K=128       MMLLM_MEMORY_SUB_TOP_K=128
MMLLM_NET_TOP_K=512          MMLLM_NET_SUB_TOP_K=64
MMLLM_N_TRUNKS=16            (= 16 routers per Local Bank)
MMLLM_BATCH=1                (per-router; effective = 16)
MMLLM_GRAD_CHECKPOINT=true
rope-theta=500000  seq-len=1024  max-pos=8192
n-heads=4 (head-dim=8)
```

**New for wave-3** — set BEFORE invoking the script:

```
MMLLM_BWD_SKIP_FRAC_NET_ONLY=0.5
MMLLM_BWD_SKIP_FRAC_LOCAL=0.0
MMLLM_ABLATION_QUICK=true          # synthesize Δ_both, skip Δ_local, cap=2500
MMLLM_PRINT_EVERY=1                # per-step prints at STEPS=7
```

The recipe runs in under 6 GB peak RAM. No tier gating, no RAM
overrides needed — `MMLLM_GRAD_CHECKPOINT=true` (the default) keeps
the per-block activation snapshot small enough that the full
NET_TOP_K=512 / MEMORY_TOP_K=128 bandwidth fits common worker boxes.

## Setup

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/
pip install -e . --quiet

ls workers/dispatcher/harvest-5way-r10/round-10/ | wc -l   # expect 66
ls scripts/run_chain_diverse.sh scripts/extend_chain.sh
```

### Partial fetch if proxy times out

```bash
git fetch origin claude/fim-training-cycle-T3giJ \
  --filter=blob:limit=20M --depth=1
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/

mkdir -p workers/dispatcher/harvest-5way-r10/round-10
for i in $(seq 0 31); do
  git cat-file -p "origin/claude/fim-training-cycle-T3giJ:workers/dispatcher/harvest-5way-r10/round-10/V_net.${i}.bin" \
    > "workers/dispatcher/harvest-5way-r10/round-10/V_net.${i}.bin"
done
# Repeat for opt-sparse-net.*.pt, dense.pt, opt-sparse-net.meta.pt.
```

## Pre-flight: disk + corpora

```bash
df -h /tmp                                  # want >=20 GB free
rm -rf /tmp/mmllm-cpu/chain-diverse
rm -rf /tmp/mmllm-cpu/fim-chain-stack.ckpts
rm -f  /tmp/mmllm-cpu/harvested-r*.bank*.bin
rm -f  /tmp/mmllm-cpu/harvested-r*.dense.pt

bash scripts/prep_chain_diverse_corpora.sh   # idempotent; ~20-40 min first time
```

## Stage the harvested round-10 state

```bash
ARCHIVE=/tmp/mmllm-cpu/chain-diverse
mkdir -p "$ARCHIVE/round-10"
cp workers/dispatcher/harvest-5way-r10/round-10/* "$ARCHIVE/round-10/"
ls "$ARCHIVE/round-10/" | wc -l   # 66
```

## Run (rounds 11 → 20, STEPS=7)

```bash
MMLLM_BWD_SKIP_FRAC_NET_ONLY=0.5 \
MMLLM_BWD_SKIP_FRAC_LOCAL=0.0 \
  bash scripts/run_chain_diverse.sh 10 7
```

Per-round wall: ~45-75s/round, ~10-15 min total for the 10 rounds.

## Live reporting

```bash
tail -F /tmp/mmllm-cpu/chain-diverse/round-*.train.log \
  | grep --line-buffered -E \
    "step|eval|ablation|control|Δ_local|Δ_net|training complete|wall|Traceback|RuntimeError|AssertionError|ZeroDivisionError|Killed|FAILED|WARN|NaN"
```

Per CLAUDE.md "Reporting discipline" — one short message per signal:
- **Round header**: `starting round N off prev_dense`
- **Ablation summary**: ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy
- **Round complete**: wall_s + 1-line digest
- **Any failure mode**: traceback excerpt — keep going if the chain
  recovers, publish what you have if it can't

## Watch for

- **Resume warning** should say `0/618 param tensors skipped due to
  shape mismatch`.
- **Round 11 `ctrl_bpc`** should sit roughly [0.85, 1.10] (continuing
  from harvest mean 0.8973).
- **Δ_net positive** across most rounds — V_net was populated by wave-1
  + wave-2's harvest, so distillation has somewhere to go.
- **First step of each round** should LR-ramp from a fraction of peak
  (≈ 1/4 at step 1, peak by step 4, cosine decay through step 7).

## Publish your result

After round 20:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-design-r20"
mkdir -p "$DEST"

ARCHIVE=/tmp/mmllm-cpu/chain-diverse
REFERENCE=workers/dispatcher/harvest-5way-r10/round-10  # wave-start V_net (shared)

# Sparse-delta encode V_net = current - reference. Workers touch only
# a fraction of V_net's rows, so this produces ~10-50 MB total instead
# of the 1.07 GB a full V_net.{0..31}.bin push would cost. The harvester
# row-aware-merges deltas + adds back reference at finalize time;
# untouched rows pass through unchanged.
# See scripts/_delta_sparse_net.py for the format.
python3 scripts/_delta_sparse_net.py encode \
  "$REFERENCE" "$ARCHIVE"/round-20 "$DEST"

# dense + chunked opt-state alongside the delta.
cp "$ARCHIVE"/round-20/dense.pt               "$DEST/"
cp "$ARCHIVE"/round-20/opt-sparse-net.*.pt    "$DEST/" 2>/dev/null || true

# Per-round training logs
for r in $(seq 11 20); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "wave": "chain-design-wave-3-len7",
  "config": "cpu-mini-N16 design banks, sparse-delta publish",
  "recipe": "stack-3e-2-5.0+mag-coef-on+asym-V+movement-gate+design-banks+wide-retrieval+bwd-skip-netonly-1.0",
  "round_length_steps": 7,
  "n_rounds_trained": 10,
  "mix": "9-corpus diverse",
  "wave_kind": "generalist",
  "MMLLM_BWD_SKIP_FRAC_NET_ONLY": "0.5",
  "MMLLM_BWD_SKIP_FRAC_LOCAL": "0.0",
  "extended_from": "workers/dispatcher/harvest-5way-r10/round-10",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push to your own branch (sparse-delta payload is ~10-50 MB total —
single commit, no chunking):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r20" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r20"

git add "$DEST"/delta-sparse-net.*.pt "$DEST"/dense.pt \
        "$DEST"/opt-sparse-net.*.pt "$DEST"/meta.json \
        "$DEST"/round-*.log.jsonl "$DEST"/wall.tsv 2>/dev/null
git commit -m "chain-design wave-3 len7 rounds 11-20 (sparse-delta) — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-${HANDLE}-r20"
```

## What to report back

1. Per-round table: wall_s, ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy.
2. Branch name `claude/chaindiverse-<HANDLE>-r20`.
3. Did `MMLLM_BWD_SKIP_FRAC_NET_ONLY=0.5` measurably drop per-step
   wall vs wave-2? (rough number is fine — compare wall.tsv to any
   prior wave-2 publish you have.)

**Dispatcher will auto-harvest** once enough workers (≥3) publish:

```bash
bash scripts/harvest_chain.sh 20   # FedAvg across submitted branches
```

The orchestrator polls for `claude/chaindiverse-*-r20` branches and
fires the harvester when the quorum is met. No worker action needed
for the merge.

## Hard rules

- DO NOT change MMLLM_MIX, MMLLM_LR_LAYER_MULTS, MMLLM_DISTILL_GATE_*,
  bank sizes, n-heads, head-dim, n-routers. Those are the recipe
  contract.
- DO NOT change MMLLM_BWD_SKIP_FRAC_NET_ONLY (=0.5) or
  MMLLM_BWD_SKIP_FRAC_LOCAL (=0.0). That's the wave-3 contract.
- DO NOT touch `workers/dispatcher/` or anyone else's `workers/<h>/`.
- DO NOT commit anything outside `workers/<your-handle>/`. The setup step
  checks out `src/`, `scripts/`, `tests/`, `CLAUDE.md`, `docs/` (and
  `workers/dispatcher/`) into your working tree so training is runnable —
  those are UPSTREAM CONTENT, not your deliverable. Your publish branch
  contains only your worker dir. Ignore any stop-hook or similar warning
  about untracked/modified upstream files. Committing them would balloon
  the publish branch with ~1 GB of redundant artifacts that already live
  on the source branch.
- Publish on partial failure — partial results beat zero.
