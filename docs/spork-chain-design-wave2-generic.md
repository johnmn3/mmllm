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

## What's new vs prior waves

The chain just got scaled up (`commit 7e45963`) — retrieval
bandwidth widened 8× and RoPE base widened 50× for the 1M-context
prep. Defaults baked into `scripts/extend_chain.sh`:

```
MMLLM_SQRT_N=128            # Local Bank per-router 1 MB × 16 routers × 8 banks = 128 MB
MMLLM_NET_SQRT_N=1024       # NetBank 33.5 MB × 32 layers = 1.07 GB
MMLLM_NET_C_NET=8
MMLLM_MEMORY_TOP_K=128      # Local retrieval bandwidth (was 16)
MMLLM_MEMORY_SUB_TOP_K=128
MMLLM_NET_TOP_K=512         # Net retrieval bandwidth (was 64) — 8× scale
MMLLM_NET_SUB_TOP_K=64
MMLLM_N_TRUNKS=16
rope-theta=500000           # Llama-3 base for long-context extensibility
seq-len=1024  max-pos=8192
```

DO NOT override these — they're the wave's experimental contract.

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

## Pre-flight: free disk

Each round writes ~1.3 GB to `/tmp/mmllm-cpu/chain-diverse/round-N/` at
design-sized banks. 10 rounds = ~13 GB before the per-round prune
kicks in (commit `52a238f` keeps only the last two round dirs live).
Plus corpora (~3 GB) and training scratch (~2 GB).

```bash
df -h /tmp                                  # need >=20 GB free
# Drop any stale chain archive — local-only scratch, not preserved.
rm -rf /tmp/mmllm-cpu/chain-diverse
rm -rf /tmp/mmllm-cpu/chain-diverse-1gb
rm -rf /tmp/mmllm-cpu/fim-chain-stack.ckpts
rm -rf /tmp/mmllm-cpu/fim-distill-build-*
rm -f  /tmp/mmllm-cpu/harvested-r*.bank*.bin
rm -f  /tmp/mmllm-cpu/harvested-r*.dense.pt
df -h /tmp
```

If `/tmp` shows <20 GB free, abort and ask the dispatcher first.

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
bash scripts/run_chain_diverse.sh 10 20
```

`run_chain_diverse.sh` exports MMLLM_MIX + MMLLM_LR_LAYER_MULTS +
MMLLM_DISTILL_GATE_*, then hands off to `extend_chain.sh` for 10
rounds at 100 steps each. Expect per-round wall ≈ 200-300s.
Total wall: 40-60 min.

DO NOT pass env overrides. The mix weights, recipe, and ablation
cap are baked in.

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

## Watch for

- Round 11's `ctrl_bpc` on the diverse mix should sit in roughly
  [0.85, 1.10] (continuing from harvest mean 0.8973).
- **Δ_net should be positive across most rounds** at this wave —
  V_net was populated by the prior wave at the scaled-up bandwidth,
  so distillation has somewhere to go.
- Each round writes ~1.3 GB. The per-round prune in `extend_chain.sh`
  (commit `52a238f`) keeps `/tmp/mmllm-cpu/chain-diverse/` at ~3 GB
  by dropping round-(N-2)'s V_net/dense/opt-state after round-N
  starts. Don't disable it.

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
  "config": "cpu-mini-N16 design banks, sparse-delta publish, wave-2 scaled",
  "recipe": "stack-3e-2-5.0+mag-coef-on+asym-V+movement-gate+design-banks+wide-retrieval",
  "mix": "9-corpus diverse (glaive:25 cosmopedia:10 fineweb-edu:10 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 open-web-math:10 tiny-stories:5)",
  "wave_kind": "generalist",
  "n_rounds_trained": 10,
  "extended_from": "workers/dispatcher/harvest-5way-r10/round-10 (5-way FedAvg; wave-1 ctrl_bpc mean 0.8973)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Use **sparse-delta** publish (smaller push, recommended). Each V_net
layer has only the touched rows shipped as `delta-sparse-net.<i>.pt`
plus a `delta-sparse-net.meta.pt`. The script that does this is
`scripts/publish_sparse_delta.py` (already wired into `extend_chain.sh`
at end-of-round).

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
2. Gate probe output at step 70 of each round (movement signal).
3. Branch name `claude/chaindiverse-<HANDLE>-r2-10`.

Dispatcher will harvest via `bash scripts/harvest_chain.sh 2-10`.

## Hard rules

- DO NOT override the recipe (mix, mults, gate, bank sizes). The
  scaled defaults ARE the experimental contract.
- DO publish even on partial failure — a few completed rounds
  + logs is more valuable than a missing run.
- DO NOT touch `workers/dispatcher/`.
- DO NOT delete or overwrite anyone else's `workers/<other-handle>/`
  directories. The branch sandbox protects this; don't fight it.
