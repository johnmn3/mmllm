# Spork

**Spork** is the small-scale variant of [mmllm](../README.md) — a
3-tier memory-hierarchy LM tuned for *spoonfuls of data* trained in a
continuous, federated way across many forks.

Current version: **0.9**. Versions move up as architecture changes
land, similar to Gemma/Qwen numbering.

## Why "spork"?

A spork is small: each training session sees a spoonful of data
(currently 7 steps × ~16k tokens per round, ~10 rounds per bird) and
*sparks* (sparse-delta encodes) its contribution onto the chain. The
chain accumulates many such spoonfuls into a community model that
exceeds what any individual contributor could train.

## Architecture (spork 0.9)

```
                 ┌─────────────────────────────────┐
   dense router  │  routes each token to a Local   │
                 │  bank (a "router" of 16)         │
                 └────────────┬────────────────────┘
                              │
                              ▼
   ┌──────────────────────────────────────────────────┐
   │  24 Local Banks  (sym24: layers 0–23)            │
   │  [L0][L1][L2] … [L21][L22][L23]                  │  the fast
   │  16 routers × 1 MB each per bank                 │  hill climber
   └──────────────────┬───────────────────────────────┘
                      │ logitkd output-KD (last ~30% of training)
                      ▼
   ┌──────────────────────────────────────────────────┐
   │  Net Bank  (1 GB, durable cortex)                │
   │  net-only STUDENT distilled to reproduce the     │
   │  local-only TEACHER (KL on softened logits)      │
   └──────────────────────────────────────────────────┘
```

> **Config note (sym24, current).** The production chain is **sym24**: a
> **24-symmetric** Local-Bank layout (`MMLLM_LOCAL_BANK_LAYERS=0…23`), defined in
> the genesis `chain_meta.json` and enforced by `train.sh` / `extend_chain.sh`.
> The older asymmetric **8-layer** layout `[0,1,2,12,20,29,30,31]` is the cpu-mini
> *default* but is NOT the chain — a bird built on it produces an off-shape dense
> the harvest drops. Distillation is **logitkd** (real output-KD: net-only student
> reproduces the local-only teacher), NOT the older feature-MSE.

**Tiers:**

| tier      | size       | role                              | lifetime          |
|-----------|-----------:|-----------------------------------|-------------------|
| Dense router | small    | per-token routing                 | trained always    |
| Local Bank   | 100 MB ×24 | fast hill-climber (sym24 layers 0–23) | reset each round |
| Net Bank     | 1 GB     | durable cortex / community memory | carries forward   |

## Training rhythm

Each spork training run is split into two **phases**, transitioning at
~70% through the round:

1. **Wake / hill-climbing (steps 0 → ~70% of round).**
   Local-bank LR is at its wake plateau (~30× the base LR), Net LR is
   essentially zero, KD coefficient is at floor. The 24 Local Banks
   hill-climb on the day's data. `MMLLM_LR_LAYER_MULTS=7,3,1,0.5,0.3,0.7,2,5`
   is an 8-value per-layer LR pattern **tiled (modulo) across the 24 layers**
   — a leftover shape from the old 8-bank era, applied uniformly to all birds.
   Δ_local is the signal here; Δ_net is expected ≈ 0.

2. **Sleep / distill (steps ~70% → 100%).**
   Local-bank LR cosines down to 0.001×; Net LR ramps to 5.0×. The
   KD coefficient rises toward its end value. Whatever Local accumulated in
   phase 1 flows into Net via **logitkd output distillation** — a net-only
   STUDENT forward is trained (KL on softened logits, T=2) to reproduce a
   local-only TEACHER forward, with the gradient frozen to the NetBank (trunk
   detached, `MMLLM_KD_FREEZE=trunk`). This is real Hinton output-KD, NOT the
   older feature-MSE on intermediate vectors. **Δ_net is the signal now**, with
   Δ_net rising toward Δ_local
   by end-of-run. This is the "potentially continuous" property — Net
   carries the chain's collective memory across rounds and across
   sporks.

## Federated chain

Many sporks train independently on top of the same chain head. Each
publishes a sparse-delta of V_net (encoded against the chain's genesis
anchor — `harvest-0way-r0_<prefix>/round-0` for prefixed chains like sym24,
the legacy r10 anchor for the original chain — for
git-friendly transit, ~50-100 MB per spork instead of the 1 GB full
state). The **harvest** workflow row-aware-FedAvg-merges every spork
at a given round and advances the chain head.

Forks of `johnmn3/mmllm` participate automatically — the harvest
workflow on upstream enumerates public forks, fetches their
`claude/train-*` branches, and includes any bird at the target round.

## Versioning + artifact

Each harvested round publishes a manifest:

```
workers/dispatcher/harvest-<N>way-r<round>/
├── spork-0.9-r<round>.json     ← the spork manifest (this file)
├── harvest_meta.json
├── results.md
└── round-<round>/
    ├── delta-sparse-net.{0..31}.pt
    ├── delta-sparse-net.meta.pt
    └── dense.pt
```

The `spork-<version>-r<round>.json` manifest is the canonical entry
point: it carries the spork version, the cumulative training-step
count across the full ancestry, and pointers to the netbank components.

## Trivia

Project shorthand from `CLAUDE.md`:
- **spork** = a 100-step training run at the cpu-tiny recipe (or
  shared-trunk recipe variant)
- **chain** = N sporks back-to-back; V_local zero-init each round,
  V_net + dense carried forward
- **harvest** = FedAvg merge across multiple sporks at the same round
