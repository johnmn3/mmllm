# Chain-diverse dispatch (rounds 92 → 101, design-sized banks)

You are extending the chain by 10 more rounds (round 92 → round 101)
**off the cooked round-91 state**, which is the architecture's first
round at the originally-designed bank sizes:

```
NetBank (V_net):  1 GB total   (was 4 MB stub for R20-R90)
Local Bank:       128 MB total (was 416 MB for R20-R90)
Router LR:        bank_lr × 0.05 (was bank_lr × 1.0 for R71-R90)
```

R20-R90 ran with V_net silently shrunk 256× per layer from your design
(committed in `extend_chain.sh@c1dac9f9` and never caught) and router
LR silently jacked up from 0.05× to 1.0× by `run_chain_diverse.sh:70`
(since dc0ae05). Every "distill into Net", "Δ_net up", "Net consolidates
features" claim from those waves was measured on top of that stub.

This wave is the first wave at the actual designed architecture.

## What changed in the scripts

- `scripts/extend_chain.sh`:
  ```
  MMLLM_SQRT_N=128           # Local Bank: per-router 1 MB, 16 routers/bank,
                             # 8 banks → 128 MB ≈ design
  MMLLM_NET_SQRT_N=1024      # NetBank: per-layer 33.5 MB, 32 layers → 1.07 GB
  MMLLM_NET_C_NET=8          # (unchanged; c_net stays 8)
  SQRT_LOCAL=128             # inline V_local Gaussian init shape
  SQRT_NET=1024              # inline V_net file shape for round publish
  ```
- `scripts/run_chain_diverse.sh`: removed the `MMLLM_LR_LOCAL_MULT:=1.0`
  override. optim.py's default of 0.05 now applies.
- `scripts/harvest_chain.py`: `SQRT_NET, C_NET = 1024, 8` (was 64, 8).
- `scripts/run_eval_battery.py`: env-var defaults match.

## Starting state

Cooked round-91 (1 round trained at design sizes from R90 dense + fresh
V_local + fresh V_net Gaussian):

```
ctrl_bpc 1.0536  (improved 0.14 over R90 harvest's 1.1958)
Δ_local +0.0000
Δ_net   -0.0012  (near-neutral — fresh V_net Gaussian hasn't been
                  populated by distillation yet; expected at round 1
                  of a freshly-resized chain)
```

Δ_net will read negative or near-zero for the first few rounds while
the new 1 GB NetBank is empty. Distillation needs many rounds to
populate it. **Do not interpret "Δ_net negative" as failure** — at
this scale of bank, that's the consolidation cold-start.

## Setup

```bash
git fetch origin claude/fim-training-cycle-T3giJ
git checkout origin/claude/fim-training-cycle-T3giJ -- \
  src/ scripts/ tests/ CLAUDE.md docs/ workers/dispatcher/
pip install -e . --quiet

ls workers/dispatcher/harvest-cooked-r91/round-91/  # 34 files: 32× V_net (32 MB each)
                                                    # + dense.pt + opt-sparse-net.pt
ls scripts/run_chain_diverse.sh
ls scripts/extend_chain.sh
ls scripts/prep_chain_diverse_corpora.sh
```

## Pre-flight: corpora

```bash
bash scripts/prep_chain_diverse_corpora.sh
```

Same 9-corpus mix as prior waves. Idempotent — skips anything already
on disk.

## Disk note

Each round writes ~1.3 GB to `/tmp/mmllm-cpu/chain-diverse/round-N/`
(was ~15 MB at the stub V_net). 10 rounds = ~13 GB. Watch
`df -h /tmp`. If tight, you can `rm -rf round-{N-1}/` after each
round provided you keep the latest two.

## Stage the cooked round-91 state

```bash
ARCHIVE=/tmp/mmllm-cpu/chain-diverse
mkdir -p "$ARCHIVE/round-91"
cp workers/dispatcher/harvest-cooked-r91/round-91/* "$ARCHIVE/round-91/"
ls "$ARCHIVE/round-91/" | wc -l   # 34
du -sh "$ARCHIVE/round-91/"        # ~1.3 GB
```

## Run (rounds 92–101)

```bash
bash scripts/run_chain_diverse.sh 10 100
```

`run_chain_diverse.sh` exports MMLLM_MIX + MMLLM_LR_LAYER_MULTS +
MMLLM_DISTILL_GATE_*, then hands off to `extend_chain.sh` for 10
rounds at 100 steps each. With design-sized banks, expect per-round
wall ≈ 200-300s (vs 150-230s at the stub size). Total wall: 40-60 min.

## Watch for

- Round 92's `ctrl_bpc` on Glaive should sit near ~1.05 (cooked state).
  Don't abort if it sits in [0.9, 1.3]. **Abort only if it climbs above
  2.0 or training NaNs.**
- **Δ_net is expected to be negative or near-zero for several rounds**
  while V_net populates. By round 95-97 it should turn positive. By
  round 101 it should be in the +0.05-0.15 range (less than the stub-
  Net's +0.15-0.25, because the big Net has more rows to spread signal
  across — expected and healthy).
- Each round writes ~1.3 GB. Watch `df -h /tmp`.

## Publish your result

After round 101 completes:

```bash
HANDLE="<your-handle>"     # lowercase, no spaces
DEST="workers/$HANDLE/chain-design-r101"
mkdir -p "$DEST"
ARCHIVE=/tmp/mmllm-cpu/chain-diverse

cp "$ARCHIVE"/round-101/V_net.*.bin       "$DEST/"
cp "$ARCHIVE"/round-101/dense.pt          "$DEST/"
cp "$ARCHIVE"/round-101/opt-sparse-net.pt "$DEST/" 2>/dev/null || true

for r in $(seq 92 101); do
  cp "$ARCHIVE/round-$r/log.jsonl" "$DEST/round-$r.log.jsonl" 2>/dev/null || true
done
cp "$ARCHIVE/wall.tsv" "$DEST/" 2>/dev/null || true

cat > "$DEST/meta.json" <<EOF
{
  "handle": "$HANDLE",
  "config": "cpu-mini-N16 — DESIGN SIZES",
  "recipe": "stack-3e-2-5.0+mag-coef-on+asym-V+movement-gate+design-banks",
  "mix": "9-corpus diverse (glaive:25 cosmopedia:10 fineweb-edu:10 magicoder:10 hermes-funcall:10 toolace:10 aesop:10 open-web-math:10 tiny-stories:5)",
  "layer_lr_mults": "7.0,3.0,1.0,0.5,0.3,0.7,2.0,5.0",
  "local_mult": "0.05 (router low LR)",
  "netbank_size": "1 GB (sqrt_n=1024 c_net=8)",
  "local_size":  "128 MB (sqrt_n=128 q_dim=16 n_trunks=16)",
  "n_rounds_extended": 10,
  "n_rounds_total": 101,
  "extended_from": "workers/dispatcher/harvest-cooked-r91/round-91 (single-round cook at design sizes)",
  "branch_base": "claude/fim-training-cycle-T3giJ",
  "git_sha": "$(git rev-parse HEAD)"
}
EOF
```

Push (the V_net.bin files are now 32 MB each × 32 = 1 GB. Chunk if
needed):

```bash
git checkout -b "claude/chaindiverse-${HANDLE}-r101" 2>/dev/null \
  || git checkout "claude/chaindiverse-${HANDLE}-r101"
git add "$DEST"
git commit -m "chain-design rounds 92-101 (design-sized banks) — final_ctrl=<...>"

# If push fails on size limit, chunk:
#   git rm --cached "$DEST"/V_net.{16..31}.bin "$DEST"/opt-sparse-net.pt
#   git commit --amend --no-edit
#   git push -u origin "claude/chaindiverse-${HANDLE}-r101"
#   git add "$DEST"/V_net.{16..31}.bin
#   git commit -m "...part2"
#   git push
#   git add "$DEST"/opt-sparse-net.pt
#   git commit -m "...part3"
#   git push
git push -u origin "claude/chaindiverse-${HANDLE}-r101"
```

## What to report back

1. Per-round table: wall_s, ctrl_bpc, Δ_local, Δ_net, Δ_both, synergy.
2. Gate probe output at step 70 of EACH round (movement signal).
3. Branch name `claude/chaindiverse-<HANDLE>-r101`.

Dispatcher will harvest via `bash scripts/harvest_chain.sh 101`.

## Hard rules

- DO NOT override the recipe (mix, mults, gate, bank sizes). The
  fixed sizes ARE the test — anything that deviates contaminates
  the comparison against the prior 90 rounds.
- DO publish even on partial failure.
- DO NOT touch `workers/dispatcher/`.
