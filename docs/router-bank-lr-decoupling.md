# Router vs bank — differential learning rates

A follow-up to `parallelization-and-bank-sizing.md`. The thesis here
is about WHEN to update each component, not HOW MUCH compute to put
behind it.

## The router-vs-expert framing

The hard-split three-tier architecture has a clean conceptual split:

| Component | Role | Implementation |
|---|---|---|
| **Router** | Decides which bank entries to retrieve for each query | Q/K projections, especially the long-tier `q_proj_l`, plus `K_a` and `K_b` sub-key matrices |
| **Bank V** | Holds the semantic content the router retrieves | `nn.Embedding` of `sqrt_n²` rows × `q_dim`, sparse-grad |
| **Downstream** | Mixes retrieved bank rows + KV cache outputs into the residual stream | Output projection, FFN, RMSNorm — the "consume what the router fetched" half |

In MoE / RAG language, the router is the gate; the bank is the
expert pool; the downstream is the consumer. In our PKM-bank
architecture all three are learned end-to-end via gradient descent
through the same forward pass.

## The problem co-trained routers + experts run into

If the router keeps moving (q-proj weights shift, K_a/K_b shift),
then which bank rows are retrieved for a given query keeps
changing. The bank rows that USED to fire for a pattern now don't,
and the new rows that fire have stale-relative-to-the-current-router
content. The bank effectively has to re-learn its content as the
router's notion of "similar" drifts.

The reverse is also true: if the bank's content shifts a lot, the
router has to re-learn which queries should land where. Co-training
both at full lr in late training is wasteful — every step the
router moves perturbs the bank's effective content, every step the
bank moves perturbs what the router should retrieve.

This shows up in MoE literature as "expert assignment instability"
and is mitigated by load-balancing losses + reduced gate lr after
warmup. It hasn't been studied as carefully for PKM banks
specifically, but the same dynamic applies — the q-proj is a
content-addressed retrieval gate, and once it's "locked in" on
good content-→-row mappings, further perturbing it costs more
than it gains.

## The hypothesis (johnmn3, 2026-05-09)

> "Once the model learns the tool calling and how to route for the
> bank, then most of the training should shift to the bank, so that
> we don't keep regressing the router."

In numbers: cool the dense (router) lr after ~10-20B tokens, cool
the bank lr toward 100B. Phrased as multipliers on the peak lr:

| phase     | tokens   | dense_lr_mult | bank_lr_mult | what the run is doing |
|----------:|---------:|--------------:|-------------:|---|
| early     |   0-9B   |          1.0  |         1.0  | joint co-training; format anchor + bank simultaneously |
| transition| 9-12B    |          0.7  |         1.0  | format anchor stable; let bank keep absorbing while router cools |
| mid-late  | 12-15B   |          0.4  |         1.0  | router locked in; bank fills in semantic detail |
| late      | 15-18B   |          0.2  |         0.7  | router frozen-ish; bank starts consolidating |
| end       | 18-20B   |          0.1  |         0.3  | end-state lock-in for v3's 20B scope |
| beyond    | →100B    |         0.05  |         0.1  | bank slowly winds down too |

This is a smooth differential decay overlaid on top of the existing
linear-warmup + cosine schedule. The product of (cosine schedule)
× (component multiplier) is the actual lr each optimizer sees.

## Current code (what's wired)

`modal_app.py::train_with_bank` exposes a single `--lr` flag. From
`mmllm/core.lpy:118`:

> "default 3e-3). Applied to BOTH AdamW (dense) and SparseAdam (V)."

Two optimizers are constructed in `train-corpus`:

```clojure
opt-dense (optim/AdamW   (python/list (parameters m)) :lr (pick-lr))
opt-bank  (vbopt/CPUOffloadSparseAdam ...            :lr (pick-lr))
```

Both call `pick-lr`, which reads `MMLLM_LR` env var → single scalar
applied identically. The `lr_warmup` schedule applies the same
linear-warmup-cosine-decay curve to both via `set-lr` calls.

There's currently no way to express "dense at 0.7 × peak while bank
at 1.0 × peak" — both move together.

## What needs to change

Three small edits in `mmllm/core.lpy`, plus two CLI/env passthroughs
in `modal_app.py`:

### 1. New env vars + CLI args

`modal_app.py::train_with_bank`:

```python
def train_with_bank(
    ...
    lr: float = 1.4e-3,            # peak (the unified default)
    lr_dense_mult: float = 1.0,    # multiplier on AdamW lr
    lr_bank_mult:  float = 1.0,    # multiplier on SparseAdam lr
    ...):
```

Pass `MMLLM_LR_DENSE_MULT` and `MMLLM_LR_BANK_MULT` env vars.

### 2. `pick-lr` becomes `pick-lr-dense` + `pick-lr-bank`

In `mmllm/core.lpy` around line 118-148:

```clojure
(defn pick-lr-dense []
  (* (pick-lr) (-> "MMLLM_LR_DENSE_MULT" (os/getenv "1.0") python/float)))

(defn pick-lr-bank []
  (* (pick-lr) (-> "MMLLM_LR_BANK_MULT"  (os/getenv "1.0") python/float)))
```

Call sites at line 711 and 1153 swap `:lr (pick-lr)` →
`:lr (pick-lr-dense)` for the AdamW and `:lr (pick-lr-bank)` for
the SparseAdam.

### 3. `set-lr` cosine-decay updates per-optimizer

The cosine schedule should still be unified (one schedule shape),
but applied via separate per-optimizer multipliers. Around line
186-193:

```clojure
(defn set-lr-dense [opt new-lr]
  (let [eff-lr (* new-lr (-> "MMLLM_LR_DENSE_MULT" ...))]
    (doseq [pg (.- opt param_groups)]
      (python/setattr pg "lr" eff-lr))))

(defn set-lr-bank [opt new-lr]
  (let [eff-lr (* new-lr (-> "MMLLM_LR_BANK_MULT" ...))]
    (doseq [pg (.- opt param_groups)]
      (python/setattr pg "lr" eff-lr))))
```

The training loop's lr-update call site (somewhere in the warmup +
cosine code around line 1162) becomes two calls instead of one.

## Empirical test before adopting

We don't have direct evidence yet that decoupling lr improves
trajectories on this specific architecture. Before committing the
implementation as a phase-by-phase ratchet, run a side-by-side at
the 10-11B mark (after Gate B):

**Branch A (control)** — main v3 run continues with `lr_dense_mult=1.0`,
`lr_bank_mult=1.0`.

**Branch B (cooled router)** — fork of the same ckpt with
`lr_dense_mult=0.5`, `lr_bank_mult=1.0`. Same 1B-token mix as
Phase 11. Costs ~$5.

**Compare at end of branch (~12B)**:

1. **Ablation Δ trajectory** — if the cooled-router branch's Δ
   keeps climbing or climbs faster, the bank is taking over the
   learning successfully. If Δ flattens, the dense-modules' partial
   freeze is starving the architecture of routing capacity.
2. **`format_validity` stability** — the format anchor is the most
   route-dependent capability we measure. If cooled-router holds
   `format_validity` >= main run, evidence the router was already
   well-saturated and didn't need more updates.
3. **BPC on held-out** (cosmopedia, fineweb-edu, aesop) — has
   general capability degraded? Tighter routing should
   theoretically not hurt prediction quality if the router was
   adequate to begin with.

If branch B wins or matches on all three, adopt the differential
schedule from Phase 13 onward (per the table above). If branch B
loses on any, hold the unified lr longer and re-test at 14-15B.

## Open questions

- **Per-module group, not just dense vs bank?** The "router" is
  arguably narrower than "all dense modules." Q/K projections are
  router-specific; FFN and output projections are downstream
  consumers. A finer split might decay the q-proj + K_a/K_b
  multipliers separately from FFN multipliers. Left for future
  work — the dense-vs-bank cut is the highest-impact lever.
- **What about KV cache contributions?** Long-tier episodic KV is
  not learned via gradient descent (it's just activations cached
  per-conversation), so it's outside this lr discussion. Short-tier
  KV likewise.
- **Bank Δ flatline at 0.7× lr_bank?** If we cool the bank at 18-20B
  and Δ flatlines, that's the saturation signal Gate C looks for —
  pivot to v3.1 with bigger bank. This schedule may make the bank
  appear saturated earlier than it is; need to disambiguate.

## Status

- Theory: documented (this file).
- Implementation: queued for "before Phase 10" (i.e. when we're
  past Gate A and need to be ready to try the differential
  schedule at 10-12B).
- Empirical test: penciled in for Phase 11-12 fork.
- Adoption: contingent on the test's outcome.

If Phase 5 (Gate A) shows format_validity is climbing as expected,
the routing-stability hypothesis is well-positioned to be tested.
If format_validity is stuck near zero like v2, the differential-lr
question is moot — we have a bigger problem.
