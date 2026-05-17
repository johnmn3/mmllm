# Chain-design wave-3 dispatch — round-length-7 spork chain

You are extending the chain by **10 rounds of 7 steps each** (= 70
training steps total) off the harvested round-10 state
(`workers/dispatcher/harvest-5way-r10/round-10`), continuing the
9-corpus diverse mix.

This wave is much lighter than wave-2 (10 rounds × **7** steps vs
wave-2's 10 × 100). Round-length-7 was selected as the CPU sweep
optimum at a fixed compute budget — length-7 (4 rounds, 28 steps)
beat length-6 (5 rounds, 30 steps) and length-10 (3 rounds, 30 steps)
on ctrl:

| round-length | rounds | steps | ctrl  | Δ_net |
|--------------|-------:|------:|------:|------:|
| 6            | 5      | 30    | 10.63 | +0.59 |
| **7**        | 4      | 28    | **10.28** | +0.82 |
| 10           | 3      | 30    | 11.38 | +0.40 |

The "longer always wins ctrl" trend from length=3-to-7 broke at
length-10: with only 3 rounds, V_local got 2 fewer diversity-
injection resets, and that cost overtook the per-round LB-hill-climb
gain. Length-7 sits at the sweet spot — long enough rounds for V_local
to learn, frequent enough resets to inject diversity. Wave-3's job is
to confirm the recipe carries to the production 9-corpus mix at the
full V_net design size.

Read `CLAUDE.md` first — it defines spork / chain / Δ_local / Δ_net,
wake/sleep, and the "don't touch other workers' dirs" rule.

## What's new vs wave-2

Three code changes landed since wave-2:

1. **Stochastic-depth-in-backward** (`MMLLM_BWD_SKIP_FRAC_NET_ONLY`).
   Net-only blocks (24 of the 32) run their forward inside
   `torch.no_grad()` so backward never traverses their internals.
   Default for this wave: **1.0** (every net-only block skips its
   backward each step). Verified to drop per-step wall ~33% with
   Δ_net signal preserved.
2. **Round-relative warmup ramp** (`MMLLM_LR_ROUND_BASE`).
   `extend_chain.sh` already resets the step counter to 1 each
   round, so the existing `MMLLM_LR_WARMUP=$((STEPS * 70 / 100))`
   logic now produces a real linear ramp across the first 4 steps
   of each round (= ⌊7 × 0.7⌋ = 4 at STEPS=7), then cosine decay
   for the remaining 3. No new env var to set — falls out of the
   round reset.
3. **Tolerant `load_state_dict`** in `mmllm.optim`. The chain's
   first-touched-row Adam allocator (`row_to_buf`) had a dtype-drift
   bug that crashed round 2 of a CPU smoke when `row_to_buf` was
   reloaded as float. The loader now coerces to (cpu, torch.long)
   and drops topology-mismatched `m_buf` / `v_buf`. If your worker
   trained on a wave-2 branch before, this fix is required for
   round 2 to survive resume.

Recipe / contract is otherwise unchanged from wave-2 (same
bandwidth, same corpora, same n-heads=4 head-dim=8).

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
MMLLM_BWD_SKIP_FRAC_NET_ONLY=1.0   # stochastic-depth bwd, net-only
MMLLM_BWD_SKIP_FRAC_LOCAL=0.0      # local layers always backward
```

## Memory budget

Same as wave-2; the 24+ GB tier is the contract for default bandwidth.
The bwd-skip knob frees ~33% step wall without changing peak RAM.

| container RAM | MMLLM_BATCH | MMLLM_NET_TOP_K | MMLLM_NET_SUB_TOP_K | MMLLM_MEMORY_TOP_K | MMLLM_MEMORY_SUB_TOP_K | MMLLM_GRAD_CHECKPOINT |
|--------------:|:-----------:|:---------------:|:-------------------:|:------------------:|:----------------------:|:---------------------:|
| **15-16 GB**  | 1           | 64 (wave-1)     | 8                   | 16 (wave-1)        | 16                     | false                 |
| **24 GB**     | 1 (default) | 512 (default)   | 64 (default)        | 128 (default)      | 128 (default)          | true (default)        |
| **32+ GB**    | 2           | 512 (default)   | 64 (default)        | 128 (default)      | 128 (default)          | false                 |

B and SUB_TOP_K are tunable to fit RAM. Document what you ran at.

## Setup

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/
pip install -e . --quiet

# Sanity: the new env vars should resolve through pick-bwd-skip-frac-*
python3 -c "
import basilisp.main; basilisp.main.init()
import mmllm.core as m
print('skip_net_only helper:', hasattr(m, 'pick_bwd_skip_frac_net_only'))
print('skip_local helper:',    hasattr(m, 'pick_bwd_skip_frac_local'))
"

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
# Wave-3 knobs in env, then 10 more rounds × 7 steps each.
MMLLM_BWD_SKIP_FRAC_NET_ONLY=1.0 \
MMLLM_BWD_SKIP_FRAC_LOCAL=0.0 \
  bash scripts/run_chain_diverse.sh 10 7
```

On a 15 GB container with reduced bandwidth:

```bash
MMLLM_BWD_SKIP_FRAC_NET_ONLY=1.0 MMLLM_BWD_SKIP_FRAC_LOCAL=0.0 \
MMLLM_BATCH=4 MMLLM_MEMORY_SUB_TOP_K=32 MMLLM_NET_SUB_TOP_K=32 \
MMLLM_NET_TOP_K=64 MMLLM_MEMORY_TOP_K=16 MMLLM_GRAD_CHECKPOINT=false \
  bash scripts/run_chain_diverse.sh 10 7
```

Per-round wall (7 steps each + ablation eval) — much faster than wave-2:
- 24 GB + default bandwidth: ~45-75s/round, ~10-15 min total
- 15 GB + wave-1 bandwidth: ~60-110s/round, ~15-20 min total

## Live reporting

```bash
tail -F /tmp/mmllm-cpu/chain-diverse/round-*.train.log \
  | grep --line-buffered -E \
    "step|eval|ablation|control|Δ_local|Δ_net|training complete|wall|Traceback|RuntimeError|AssertionError|ZeroDivisionError|Killed|OOM|FAILED|WARN|NaN"
```

Per CLAUDE.md "Reporting discipline" — one short message per signal:
- **Round header**: `starting round N off prev_dense`
- **Ablation summary**: ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy
- **Round complete**: wall_s + 1-line digest
- **Any failure mode**: traceback excerpt + abort

If a round NaNs or `ctrl_bpc` climbs above 2.0, abort the remaining
rounds and publish what you have.

## Watch for

- **Resume warning** should say `0/618 param tensors skipped due to
  shape mismatch`.
- **Round 11 `ctrl_bpc`** should sit roughly [0.85, 1.10] (continuing
  from harvest mean 0.8973).
- **Δ_net positive** across most rounds — V_net was populated by wave-1
  + wave-2's harvest, so distillation has somewhere to go.
- **First step of each round** should LR-ramp from a fraction of peak
  (≈ 1/4 at step 1, peak by step 4, cosine decay through step 7).
  If it looks flat at peak the whole round, your `extend_chain.sh`
  is older than the wave-3 cut — `git pull` and retry.

## Publish your result

After round 20:

```bash
HANDLE="<your-handle>"
DEST="workers/$HANDLE/chain-design-len7-r2-10"
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
  "wave": "chain-design-wave-3-len7",
  "config": "cpu-mini-N16 design banks, sparse-delta publish, wave-2 cont (n-heads=4)",
  "recipe": "stack-3e-2-5.0+mag-coef-on+asym-V+movement-gate+design-banks+wide-retrieval+bwd-skip-netonly-1.0",
  "round_length_steps": 7,
  "n_rounds_trained": 10,
  "mix": "9-corpus diverse",
  "wave_kind": "generalist",
  "MMLLM_BWD_SKIP_FRAC_NET_ONLY": "1.0",
  "MMLLM_BWD_SKIP_FRAC_LOCAL": "0.0",
  "container_ram_gb": <fill-in>,
  "MMLLM_BATCH": <fill-in>,
  "MMLLM_MEMORY_SUB_TOP_K": <fill-in>,
  "MMLLM_NET_SUB_TOP_K": <fill-in>,
  "extended_from": "workers/dispatcher/harvest-5way-r10/round-10",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF

git checkout -b "claude/chainlen7-${HANDLE}-r2-10" 2>/dev/null \
  || git checkout "claude/chainlen7-${HANDLE}-r2-10"

git add "$DEST"
git commit -m "chain-design wave-3 len7 rounds 11-20 — final_ctrl=<...>"
git push -u origin "claude/chainlen7-${HANDLE}-r2-10"
```

If push 413/502s, split V_net into 2 commits.

## What to report back

1. Per-round table: wall_s, ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy.
2. The B / SUB_TOP_K values you ran at, and container RAM.
3. Branch name `claude/chainlen7-<HANDLE>-r2-10`.
4. Did `MMLLM_BWD_SKIP_FRAC_NET_ONLY=1.0` measurably drop per-step
   wall vs wave-2? (rough number is fine — compare wall.tsv to any
   prior wave-2 publish you have.)

**Dispatcher will auto-harvest** once enough workers (≥3) publish:

```bash
bash scripts/harvest_chain.sh len7-r2-10   # FedAvg across submitted branches
```

The orchestrator polls for `claude/chainlen7-*-r2-10` branches and
fires the harvester when the quorum is met. No worker action needed
for the merge.

## Hard rules

- DO NOT change MMLLM_MIX, MMLLM_LR_LAYER_MULTS, MMLLM_DISTILL_GATE_*,
  bank sizes, n-heads, head-dim, n-routers. Those are the recipe
  contract.
- DO NOT change MMLLM_BWD_SKIP_FRAC_NET_ONLY (=1.0) or
  MMLLM_BWD_SKIP_FRAC_LOCAL (=0.0). That's the wave-3 contract.
- B and SUB_TOP_K ARE tunable to fit RAM. Document what you ran.
- DO publish on partial failure — partial results beat zero.
- DO NOT touch `workers/dispatcher/` or anyone else's `workers/<h>/`.
- If your first round OOMs unrecoverably, publish a meta.json with
  `status: failed` and `n_rounds_trained: 0` so the dispatcher knows.
