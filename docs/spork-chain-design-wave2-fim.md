# Chain-design wave-2 dispatch — FIM specialist (in-domain Glaive JSON)

You are an **FIM specialist** extending the chain by 10 more rounds
(wave-2 rounds 1 → 10) **off the harvested round-10 state**
(`workers/dispatcher/harvest-5way-r10/round-10`), training on the
**FIM-only mix** (`/tmp/mmllm-cpu/fim-json-v3.train.bin` —
Glaive function-calling, JSON-value-boundary-split FIM corpus).

The just-completed wave-1's 2 FIM specialists (ZniT6, cQUhK) hit
ctrl bpc 0.8249 / 0.8220 — the best birds of the wave. This prompt
continues that specialization. The harvester picks up your branch
alongside generalist branches and the FedAvg merge produces the
next wave's reference state.

Read `CLAUDE.md` first — defines spork / chain / Δ_local / Δ_net,
wake/sleep schedule, conduct rules.

## What's new vs prior waves

The chain just got scaled up (`commit 7e45963`) — retrieval bandwidth
widened 8× and RoPE base widened 50× for 1M-context prep. Defaults
baked into `scripts/extend_chain.sh`:

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

DO NOT override these.

## Setup

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/
pip install -e . --quiet

ls workers/dispatcher/harvest-5way-r10/round-10/ | wc -l   # 66 files
ls scripts/extend_chain.sh
ls scripts/build_glaive_fim_corpus.sh
```

## Pre-flight: free disk

Each round writes ~1.3 GB. Per-round prune (commit `52a238f`)
keeps live state at ~3 GB, but you still need headroom for the
corpus (~150 MB) and the publish output (~250 MB sparse-delta).

```bash
df -h /tmp                                    # want >=15 GB free
rm -rf /tmp/mmllm-cpu/chain-diverse           # any prior wave's archive
rm -rf /tmp/mmllm-cpu/fim-chain-stack.ckpts
rm -f  /tmp/mmllm-cpu/harvested-r*.bank*.bin
rm -f  /tmp/mmllm-cpu/harvested-r*.dense.pt
df -h /tmp
```

## Pre-flight: corpus

Only the FIM corpus is needed:

```bash
bash scripts/build_glaive_fim_corpus.sh
```

Idempotent — skips any step whose output exists. ~5-15 min if
fully cold (HF download + unpack + tokenize). Outputs:

```
/tmp/mmllm-cpu/fim-json-v3.train.bin   (~110 MB)
/tmp/mmllm-cpu/fim-json-v3.val.bin     (~10 MB)
/tmp/mmllm-cpu/fim-json-v3.test.bin    (~10 MB)
```

## Stage the harvested round-10 state

```bash
ARCHIVE=/tmp/mmllm-cpu/chain-diverse
mkdir -p "$ARCHIVE/round-10"
cp workers/dispatcher/harvest-5way-r10/round-10/* "$ARCHIVE/round-10/"
ls "$ARCHIVE/round-10/" | wc -l   # 66
```

## Run (rounds 11 → 20) — FIM-only mix

For an FIM specialist we bypass `run_chain_diverse.sh` (which sets
the 9-corpus mix) and invoke `extend_chain.sh` directly with
`MMLLM_MIX` overridden to FIM-only:

```bash
export MMLLM_MIX="/tmp/mmllm-cpu/fim-json-v3.train.bin:100"
# Layer-LR mults: same as the 9-corpus runner (V-shape — hot endpoints).
# These are the documented winners from the bandwidth-knob sweep; don't
# change them.
export MMLLM_LR_LAYER_MULTS="7.0,3.0,1.0,0.5,0.3,0.7,2.0,5.0"
export MMLLM_DISTILL_GATE_MIN=0.05
export MMLLM_DISTILL_GATE_MAX=1.0
export MMLLM_DISTILL_GATE_TEMP=0.5

bash scripts/extend_chain.sh 10 20
```

`extend_chain.sh 10 20` means "extend from round-10 up to and
including round-20" — picks up the staged round-10 state, trains
rounds 11..20 at 100 steps each. Expected per-round wall ≈ 200-300s,
total 40-60 min.

DO NOT pass any other env overrides (LR, recipe, bank size). The
defaults in `extend_chain.sh` are the recipe.

## Live reporting

Arm a Monitor over the training log:

```bash
tail -F /tmp/mmllm-cpu/chain-diverse/round-*.train.log \
  | grep --line-buffered -E \
    "step|eval|ablation|control|Δ_local|Δ_net|training complete|wall|Traceback|RuntimeError|AssertionError|ZeroDivisionError|Killed|OOM|FAILED|WARN|NaN"
```

One short chat message per signal line:
- **Round header**: "starting round N off prev_dense"
- **Step prints** (~every 20 steps): "round N step S: loss=L lr=R"
- **Ablation summary** (post step 70): ctrl_bpc, Δ_local, Δ_net,
  Δ_both, synergy
- **Round complete**: wall_s + 1-line digest
- **Any failure mode**: traceback excerpt + abort

If a round NaNs or `ctrl_bpc` climbs above 1.5, abort and publish
what you have — partial results beat zero.

## Watch for

- Round 11's `ctrl_bpc` on FIM should sit near ~0.82 (wave-1 FIM
  specialists' end-of-train). Don't abort if it sits in [0.7, 1.0].
- **Δ_net should rise across the wave** — V_net was populated by
  the prior wave at the scaled-up bandwidth, distillation has
  somewhere to go.
- FIM-only is a NARROWER mix than the 9-corpus generalist. Δ_local
  will be larger than the generalist case (the bank specializes
  on Glaive JSON syntax). Expected and intended.

## Publish your result (sparse-delta)

After round 20 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-design-r2-10"
mkdir -p "$DEST"
ARCHIVE=/tmp/mmllm-cpu/chain-diverse

# extend_chain.sh writes sparse-delta + meta into round-20/ at end-of-train.
# Copy those instead of the full V_net (much smaller push, recommended).
cp "$ARCHIVE"/round-20/delta-sparse-net.*.pt   "$DEST/"
cp "$ARCHIVE"/round-20/dense.pt                "$DEST/"
cp "$ARCHIVE"/round-20/opt-sparse-net.*.pt     "$DEST/" 2>/dev/null || true

for r in $(seq 11 20); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16 design banks, sparse-delta publish, wave-2 scaled",
  "recipe": "stack-3e-2-5.0+mag-coef-on+asym-V+movement-gate+design-banks+wide-retrieval",
  "mix": "FIM-only (fim-json-v3 / Glaive in-domain JSON tool-calls)",
  "wave_kind": "fim-specialist",
  "n_rounds_trained": 10,
  "extended_from": "workers/dispatcher/harvest-5way-r10/round-10 (5-way FedAvg; wave-1 ctrl_bpc mean 0.8973)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Use the **`fim-` branch prefix** so the dispatcher can identify your
wave kind from the branch name alone (separate from the in-meta
`wave_kind` field — both are checked):

```bash
git checkout -b "claude/chaindiverse-fim-${HANDLE}-r2-10" 2>/dev/null \
  || git checkout "claude/chaindiverse-fim-${HANDLE}-r2-10"

git add "$DEST"
git commit -m "chain-design wave-2 FIM rounds 11-20 from harvested-r10 — final_ctrl=<...>"
git push -u origin "claude/chaindiverse-fim-${HANDLE}-r2-10"
```

If the push 413/502s, split into 2-3 commits.

## What to report back

1. Per-round table: wall_s, ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy.
2. Gate probe output at step 70 of each round.
3. Branch name `claude/chaindiverse-fim-<HANDLE>-r2-10`.

Dispatcher will harvest via `bash scripts/harvest_chain.sh 2-10`.

## Hard rules

- DO NOT override the recipe (mults, gate, bank sizes). The scaled
  defaults ARE the contract.
- DO NOT add other corpora — FIM-only is the specialization point
  of this prompt. If you want a generalist, take the other prompt.
- DO publish on partial failure.
- DO NOT touch `workers/dispatcher/` or anyone else's `workers/<h>/`.
