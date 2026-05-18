# mmllm v3 — triune-brain architecture

This document maps mmllm v3's three-tier memory + routing architecture
onto a coarse-grained triune-brain mental model, then walks through
every architectural decision that supports it. The goal is not a literal
neuroscience claim but a useful operational metaphor — one that explains
why each mechanism is shaped the way it is and how they compose.

## TL;DR

```
                      ┌──────────────────────────────┐
                      │     working memory (KV)      │   ← forebrain
                      │     (short + long caches)    │
                      └────────────┬─────────────────┘
                                   │
                  ┌────────────────┴────────────────┐
                  │                                 │
        ┌─────────▼──────────┐         ┌────────────▼─────────────┐
        │  Local Bank (PKM)  │         │   NetBank (off-machine)  │
        │       cortex       │         │        cerebellum        │
        │ ─────────────────  │ ◄────── │ ──────────────────────── │
        │ fast hill-climber  │  consol-│  slow accumulator        │
        │ high LR, plastic   │  idation│  predicts cortex's calls │
        │ short retrieval    │  via    │  long-term terrain map   │
        │ working slots      │  distill│  WAN-resident, latent    │
        └─────────▲──────────┘         └────────────▲─────────────┘
                  │                                 │
                  └─────────────┬───────────────────┘
                                │
                      ┌─────────▼──────────┐
                      │   dense router     │  ← brain stem
                      │  (in-mem trunk)    │     mid-brain
                      │  routing, gating,  │     basal ganglia
                      │  context-switch,   │
                      │  multi-timescale   │
                      │  EMAs, focal/IH    │
                      └────────────────────┘
```

- **Cortex** = Local Bank. In-memory PKM, high learning rate, fast hill
  climber on the current task distribution. Working slots get touched
  often, learn fast.
- **Cerebellum** = NetBank. Off-machine (or GPU-resident with simulated
  WAN delay), 2× the size of cortex but with a c_net=64 bottleneck.
  Receives consolidated patterns from cortex; eventually predicts
  cortex's retrievals so cortex can be freed up for novel patterns.
- **Brain stem / mid-brain / basal ganglia** = dense router. The 5-layer
  transformer trunk. Decides per-position which tier to consult, how
  much compute to apply, when to hand off.
- **Forebrain / working memory** = KV caches (short window + long
  window) plus the per-block carry's multi-timescale EMAs.

The dynamic we want to drive: **cortex hill-climbs novel patterns; once
mastered, cerebellum picks them up via consolidation; cortex frees that
slot for the next novel pattern**.

---

## Forward pass — per-block anatomy

A single transformer block runs the trunk attention against four
parallel sources:

```
                           input x  (B, T, d_model)
                              │
                       ┌──────┼──────┐
                       │      │      │
                    norm1   norm2  bank_query(x)
                       │      │      │
                  ┌────┴───┐  │      │   (W_ctx · x; ctx-add)
                  │ q,k,v  │  │      │
                  │ proj   │  │      │
                  └───┬────┘  │      │
                      │       │      │
        ┌─────────────┼───────┼──────┤
        │             │       │      │
        │             │       │      │
    ┌───▼───┐    ┌────▼────┐ ┌▼──────▼───┐  ┌────────────────┐
    │ short │    │ long    │ │ Local Bank │  │   NetBank       │
    │  SDPA │    │  SDPA   │ │  (cortex) │  │  (cerebellum)   │
    │       │    │         │ │            │  │                 │
    │ RoPE+ │    │ no RoPE │ │ K_a, K_b  │  │  K_a, K_b       │
    │ window│    │ episodic│ │ V         │  │  V (c_net dim)  │
    └───┬───┘    └────┬────┘ └─────┬─────┘  │  expander → q   │
        │             │            │        └────────┬────────┘
        │             │            │                 │
        │             │            │ (iterate Nx)    │ (sim WAN delay)
        │             │            │                 │
        │             └─┬──────────┴────────────────┘
        │               │
        │               ▼
        │     ┌────────────────────┐
        │     │   3-way SwitchGate │   (sdpa, local, net)
        │     │ softmax over heads │
        │     │ × α_net on net path│
        │     └────────┬───────────┘
        │              │
        └──────┬───────┘
               │
        attn_concat → o_proj
               │
               + residual    ──── carry(x) ──── residual ────►  block_out
                                  (4 EMAs)
```

### Tier responsibilities

| Tier | Latency model | Capacity | Plasticity | Target patterns |
|---|---|---|---|---|
| **Short SDPA** | Cache only (KV) | T=128 window | None (KV is just state) | Recent context |
| **Long SDPA** | Cache only | T=4096 window | None | Episodic, no RoPE |
| **Local Bank** | In-memory PKM | sqrt_n²=2048² entries × q_dim=224 | High (lr_bank_mult ≥ 10×) | Skill working set |
| **NetBank** | 1-10 ms simulated WAN | sqrt_n²=4096² entries × c_net=64 (+ expander) | Lower (lr_net_mult ≤ 5×) | Consolidated terrain |

The two SDPA tiers are stateless attention against the KV cache — they
are "working memory," analogous to forebrain running activations. The
two PKM tiers are the persistent stores: cortex (Local) and cerebellum
(NetBank).

### Why the tiers are split this way

1. **Short SDPA** (RoPE'd) handles local context — recent few tokens.
   Brain stem reads these for "what just happened."
2. **Long SDPA** (no RoPE, set-style) handles episodic context — bag
   of recent positions without ordering. Mid-brain reads these for
   "what's been going on."
3. **Local Bank** (PKM, in-mem) handles task-specific patterns the
   model is currently learning. Cortex's working set.
4. **NetBank** (PKM with bottleneck, simulated off-machine) holds the
   long-term, slow-drifting terrain map. Cerebellum's predictions.

The brain-stem analog (the dense router + SwitchGate) decides which of
the four to consult per position.

---

## Learning dynamics — different tiers, different rates

Every parameter group has its own learning rate multiplier on the global
peak `lr`:

```
       MMLLM_LR_DENSE_MULT  → AdamW(d_model trunk) lr
                            ─── round-9 v3: 0.05 → 0.005 (cosine)
       MMLLM_LR_KAB_MULT    → AdamW(K_a, K_b) lr  (#3 spike)
                            ─── default = LR_DENSE_MULT (single group)
       MMLLM_LR_BANK_MULT   → SparseAdam(Local V) lr
                            ─── round-9 v3: 10.0 → 0.001 (cosine — cools off)
       MMLLM_LR_NET_MULT    → SparseAdam(NetBank V) lr
                            ─── round-9 v3: 0.001 → 1.0 (cosine — ramps up)

       Each multiplier supports cosine scheduling via *_END:
         round-9 v3 schedule (wake → consolidate):
           lr_bank_mult  cosine 10    → 0.001    (cortex cools to off)
           lr_net_mult   cosine  0.001 → 1.0     (cerebellum frozen → plastic)
           lr_dense_mult cosine  0.05  → 0.005   (trunk barely moves, decays)
```

The SCHEDULE encodes the central consolidation hypothesis: cortex hill-
climbs hard throughout the run; cerebellum is a slow receiver early
(when there's nothing for Local to transfer yet) and a fast consolidator
late (when distill has accumulated content to absorb). The trunk barely
moves so it doesn't absorb work the banks should be doing.

Per-tier reasoning:

- **Cortex (Local) cosine 10 → 0.001.** High during wake (Local hill-
  climbs the current task distribution), cools to effectively-frozen by
  end. The cooling drives the consolidation handoff: once Local stops
  accumulating, distill has time to copy what Local has into Net, and
  the gate can shift routing toward Net for those patterns. The prior
  round-9 redo kept Local flat at 10× and saw Δ_local / Δ_net converge
  to parity rather than the wake→consolidate sequential transfer.
- **Cerebellum (Net) cosine 0.001 → 1.0.** Near-zero start prevents Net's
  V from drifting while distill's target ≈ −sdpa (Local≈0 at init).
  Symmetric ramp-up vs Local's cool-down. Lower peak (1.0 not 5.0) since
  direction-only residual distill drives Net's *direction* explicitly —
  Net doesn't need a large LR to chase unbounded residual magnitudes.
- **Trunk cosine 0.05 → 0.005.** Round-9 redo worker 1's diagnosis:
  the residual `(local − sdpa)` shrinks across the run because the dense
  trunk absorbs whatever Local adds. Pinning the trunk LR very low (and
  decaying it further) preserves the residual signal for Net to learn
  from. Trunk weights are ~1% the size of the banks; high LR there would
  absorb work the banks should carry.

---

## Consolidation mechanisms

The schedule alone is not enough — cortex and cerebellum train on the
same loss but don't directly teach each other. We added five active
mechanisms to drive transfer.

### 1. Net→Local distillation (P2')

```
  per block forward:
     mem_out  ← Local Bank lookup (cortex output)
     net_out  ← NetBank lookup    (cerebellum output)
                                                    ┐
     gate(q) decides routing weights    ───────────►│ main forward
     attn_l  = w0·sdpa + w1·mem_out + w2·net_out   ─┘

                                                    ┐
     aux loss (target='residual', default):         │ distillation
     coef · |net_out − (mem_out − sdpa_out).detach()|²── path
                                                    ┘
```

Cerebellum learns the **unique contribution** Local adds beyond the
always-on attention path. The sdpa baseline is subtracted from Local's
output before MSE so Net can't twin Local by replicating what sdpa
already provides. Without that subtraction (target='local', legacy),
when Local's output is mostly sdpa + ε, Net learns sdpa, becomes
Local's twin, and `Δ_net` collapses — the round-5 / round-8 redundancy
basin. Worker 2's diagnosis from round-9 reports; the round-10
architectural fix.

Both Local and sdpa are detached so the gradient only modifies Net.
As Local hill-climbs new content, distill copies the *Local-unique*
part into Net — the actual transfer mechanism.

Knobs:
- `MMLLM_DISTILL_COEF` — overall scale (default 0.0 = off). Round-5
  used 0.1; round-8 evidence (`distill_loss ~ 5e-4` floor → ~5e-5
  effective gradient on Net, three orders below the main loss) drove
  a round-9 raise to 1.0. Also schedulable: `MMLLM_DISTILL_COEF_END`
  sets the end-of-run target value and the coefficient is
  cosine-interpolated across training. Round-9 re-run uses 0.0 → 1.0
  so the coefficient stays near-zero during the wake window when
  Local≈0 makes the target ≈ −sdpa (anti-sdpa basin risk), and
  engages only after Local has accumulated real content.
- `MMLLM_DISTILL_TARGET` — `'residual'` (default) or `'local'`. See
  above; residual subtracts sdpa so Net learns Local's unique add.
- `MMLLM_DISTILL_DIRECTION_ONLY` — when true, target and net are
  RMS-normalized before MSE so Net learns the target's *direction*
  only. Stacks with the target choice (direction of the residual is
  the direction Local adds beyond sdpa). **Recommended `true` when
  using `target=residual`**: bounds Net's V magnitude. Round-9 re-run
  data showed magnitude-aware residual distill destabilized training
  around step 3000-3500 in some workers (Net's V grew unbounded to
  match the unbounded-magnitude residual; ctrl_bpc spiked when small
  routing perturbations swung net_out's large magnitude wildly).
  Direction-only keeps the unique-add signal but caps Net's response
  magnitude — handled instead by `alpha_net` × gate weight (bounded).

### 1b. Net-default Bernoulli gate (round-9)

Round-8 evidence: in the 3-way softmax gate, `w_local` collapses from
~0.15 to ~0.01 within the first cycle. The optimizer routes around
Local; distill's target shrinks with it; Net's gradient starves on a
vanishing input.

When `MMLLM_GATE_NET_DEFAULT=true`, SwitchGate switches to a hybrid:
- Net + sdpa run unconditionally and always feed the next layer.
- Local fires per (B, H, T) Bernoulli decision computed from `q_long`.
  Sigmoid init bias = -2.0 so ~12% of queries invoke Local at step 0.
- Training: straight-through Bernoulli (forward = hard 0/1, backward
  = sigmoid grad); inference: deterministic threshold at 0.5.
- The 3-way softmax weights are renormalized over the surviving tiers
  when Local is skipped, so the routing mass always sums to 1.

There is no `w_local` for the optimizer to collapse — Local is invoked
explicitly when the gate decides this query needs it, otherwise it
contributes zero. The recurrent feedback between Net's output and the
gate's routing decision (the original motivation for the 3-way mixer)
is preserved because Net always runs.

### 2. α_net per-head scale on Net's path (#C)

NetBank's V has a c_net=64 bottleneck and small expander init, so even
when the gate routes 49% to Net, the actual contribution is small in
magnitude. `α_net` is a learnable per-head scalar (init 1.0) that
amplifies Net's path:

```
  attn_l = w0·sdpa  +  w1·mem_out  +  w2·(α_net · net_out)
                                          ↑
                              learnable per-head scale
                              compensates magnitude asymmetry
```

### 3. Replay buffer (P3)

```
   each train step:                   every replay-every steps:
   ┌─────────────────────┐           ┌──────────────────────────────┐
   │ run forward+back    │           │ sample one batch from buffer │
   │ if loss < threshold │           │ run forward+back             │
   │   push (x,y) to buf │ ────────► │ ZERO Local V's gradients     │
   │ (buf is a CPU FIFO  │           │ optimizer.step()             │
   │  of "mastered"      │           │ → only Net + dense + carry   │
   │  batches)           │           │   update on this batch       │
   └─────────────────────┘           └──────────────────────────────┘
```

Cerebellum trains directly on patterns cortex already mastered. Cortex
stays put on those patterns (its V is frozen during the replay step).

### 4. Multi-timescale carry (router-smarts)

Per-block residual:

```
  x' = block(x)
  emas = [EMA_decay₀(x'), EMA_decay₁(x'), EMA_decay₂(x'), EMA_decay₃(x')]
       (decays = 0.5, 0.875, 0.96875, 0.992 → half-lives 1, 5, 22, 86 tokens)
  carry = RMSNorm( gate(x') · emas )    (norm-bounded magnitude)
  x_out = x' + carry                    (residual; norm.weight zero-init → identity)
```

Mid-brain "many clocks" — the router gets implicit access to multiple
time scales at every block. The carry is identity at init, so adding it
to a trained ckpt is non-disruptive; it differentiates over training.

### 5. Cold-row gradient boost (#1 spike)

Per-row Adam approximation: each row of Local V gets a touch counter.
Cold rows (rarely touched) get their gradient scaled up:

```
  for each row i in V_local:
      touch_count[i] += 1   (only for touched rows)
      boost = 1 + cold_boost / (eps + touch_count[i])
      grad[i] *= boost      (cold rows get max boost)
```

Counters the issue that Adam's global step count over-dampens the LR
for slots touched only a few times per epoch.

---

## Structural-learning mechanisms

Format synthesis (JSON tool calls) was the unbroken wall throughout
the early phases. Every following mechanism targets it specifically.

### 1. Focal CE (router-smarts)

```
  per_pos_ce = (1 − p_correct)^γ · (− log p_correct)
                            ↑
                   γ=2.0 → easy bytes get ~0,
                   hard bytes get full CE
```

Up-weights bytes the model gets wrong. No hardcoding of any byte scheme.
Numerical guard: `log p_true ≥ -50` to prevent `0 · -∞ = NaN` in backward.

### 2. Importance head v2

Per-position Linear(d_model, 1) + softplus. Output is **detached** when
multiplied with `per_pos_ce` (no grad from main loss into IH); IH is
trained by a SEPARATE aux MSE that regresses IH onto the actual
per-byte CE. This avoids the v1 sign bug where IH learned to suppress
hard bytes.

### 3. JSON-delimiter aux head (#4)

A dedicated 1-bit head over the final hidden state, BCE-trained against
"is the next byte in `{}[]:,"\n`?":

```
  delim_logits = Linear(d_model, 1)( norm_final(x) )
  delim_target = is_in_DELIM_BYTES(y)
  aux_loss     = BCEWithLogits(delim_logits, delim_target) · coef
```

Forces the trunk's hidden state to encode JSON parser-state position.

### 4. Schema-mask teacher forcing (#5)

Approximates parser-mask training without a real grammar:

```
  per_pos_ce[t] *= (w  if  x[t-1] ∈ DELIM_BYTES  else  1.0)
                       ↑
                  MMLLM_SCHEMA_MASK_WEIGHT (default 1.0 = disabled)
```

Position right after a structural delim ("commit" position) gets w×
weight on its CE. The model learns "after `:`, you have to commit
correctly" via gradient pressure.

### 5. Pause-byte injection (#9)

Training-time augmentation:

```
  with probability p:
     x[:, :n] = pause_byte_value         (overwrite first N bytes)
     y unchanged                          (target sequence stays)
```

Trains the model to handle pause-byte prefixes. At inference, prepend
N pause bytes before structural commit positions to give Local Bank
extra forward passes to deliberate.

### 6. Local Bank iterative refinement (#7+8)

```
  bank_q = q_long_flat + bank_query(x)
  mem_out = Local_Bank.lookup(bank_q)         iter 1
  for _ in range(N - 1):
      bank_q  = bank_q + α · mem_out           feedback
      mem_out = Local_Bank.lookup(bank_q)      iter 2..N
```

Cortex re-queries itself with previous output as residual. "Deliberation"
loop. Cost: ~+1 PKM lookup per extra iteration.

---

## Visibility surface — what we measure

The architectural mental model only works if we can observe each
mechanism's effect. Every spike emits at least one diagnostic to
`<base>.log.jsonl`:

```
event=eval                  → val_bpc, val_ppl  (every 2500 steps)
event=ablation_intermediate → Δ_local, Δ_net, Δ_both, synergy,
                              consolidation_idx, baseline_delta_local
                              (every 5000 steps)
event=slot_usage            → dead_a/b, entropy_a/b per layer per tier
                              (every 250-2500 steps)
event=row_touch_dist        → per-Local-V touch-count distribution
                              (mean, std, max, p95, pct_nonzero)
event=param_norms           → L∞ + L2 per named tensor
                              (catches drift; eg blk*-mem-V vs blk*-net-V)
event=gate_dist             → per-layer (sdpa, local, net) softmax fractions
event=router_metrics        → distill_loss, replay_loss, replay_buf_n, delim_loss
event=manifest              → snapshot of all MMLLM_* env vars, phase_label
```

### How each mechanism's signal looks in the data

```
Mechanism          Direct signal                       File line / event
─────────────────────────────────────────────────────────────────────────
Distillation       distill_loss ↓ over training        router_metrics
α_net              alpha_net L∞ growth                 param_norms (blkN-α)
Replay buffer      replay_loss ↓; buf_n→cap            router_metrics
Carry              norm.weight grows from zero         param_norms
Cold-row boost     row_touch_dist std ↓, pct_nz ↑      row_touch_dist
K_a/K_b separate   blk*-mem-Ka/Kb L∞ vs blk*-mem-V     param_norms
Focal CE           train CE on hard bytes ↑ then ↓     by-corpus EMA
IH (importance)    ih-proj-w L∞ growth                 param_norms
Delim aux head     delim_loss → small over training    router_metrics
Schema-mask        per-corpus EMA on agent corpora ↓   by-corpus EMA
Pause bytes        train loss with prefix similar to                
                   without — model robust to pauses    by-corpus EMA
Iter refinement    TPS ↓ ~50% with N=2; gate_dist
                   shifts toward Local                 step prints, gate_dist
─────────────────────────────────────────────────────────────────────────
THE TARGET METRIC: format_validity at agent-eval       eval-watcher
```

`format_validity` has been the unbroken wall — 0.000 across every
ckpt evaluated to date. Every architectural mechanism above is in
service of cracking that single metric without sacrificing val_bpc.

---

## Composition — how mechanisms compose

Three tiers of mechanisms, each layered on top of the previous:

```
┌──────────────────────────────────────────────────────────────┐
│  Tier 0 — substrate                                          │
│   • short + long SDPA + Local Bank PKM + NetBank PKM         │
│   • 3-way SwitchGate per layer                               │
│   • differential lr (10× cortex, 5× cerebellum, 1× trunk)    │
│   • ckpt persistence + tolerant load                         │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  Tier 1 — router smarts (focal CE, IH, multi-timescale carry)│
│  + grad clip + nan guard + plain-CE printer                  │
│   Goal: trunk learns to up-weight hard bytes,                │
│         carry exposes multi-scale time context               │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  Tier 2 — consolidation (P1 lr schedules, P2' distillation,  │
│          P3 replay buffer, α_net, dir-only distill)          │
│   Goal: cerebellum learns cortex's contribution,             │
│         cortex's role contracts, gate shifts toward Net      │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│  Tier 3 — structural learning (cold-row boost, K_a/K_b LR,   │
│          delim aux, schema-mask, pause-bytes, iter refine)   │
│   Goal: cortex learns structural addressing fast;            │
│         trunk encodes JSON parser state explicitly;          │
│         crack format_validity                                │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ format_validity │
                     │      > 0.0      │   ← the wall
                     └─────────────────┘
```

Each tier is env-gated; defaults preserve backward compat. A production
run typically composes Tier 0 (always on) + Tier 1 + Tier 2 + selected
mechanisms from Tier 3.

---

## Information flow per training step

```
   (x_input, y_target) batch
              │
              │  optional: pause-byte prefix injection (#9)
              │
              ▼
   ┌─────────────────────────────────────┐
   │    forward through 5 blocks         │
   │  (each with 4-tier attention,       │
   │   carry residual, FFN, norm)        │
   │  → final_x, logits, aux_logits      │
   │                                     │
   │  Each block stashes:                │
   │   long_gate.last_local_out          │
   │   long_gate.last_net_out            │
   │   long_gate.last_gate_dist          │
   │  ← used by distill loss + visibility│
   └────────────────┬────────────────────┘
                    │
                    ▼
   ┌─────────────────────────────────────────────────────┐
   │ loss = focal_CE(logits, y, γ=2)                     │
   │      · IH(final_x).detach() / mean(IH)         (if IH on)
   │      · schema_mask(x, w)                       (if mask on)
   │      + ih_aux_loss   (regress IH → per_pos_ce)
   │      + z_loss        (PKM query stability)
   │      + mtp_aux_loss  (t+2 prediction)
   │      + distill_loss  (Net direction → Local detached)
   │      + delim_loss    (BCE on delim head vs y∈DELIMS)
   └────────────────┬────────────────────────────────────┘
                    │
                    ▼
   ┌──────────────────────────────────────────────┐
   │ loss.backward()                              │
   │ cold-row boost on Local V grads (if on)      │
   │ freeze-local? zero Local grads (replay step) │
   │ grad_clip on dense param group               │
   │ opt-dense.step()                             │
   │ opt-sparse.step()       (Local V — sparse)   │
   │ opt-sparse-net.step()   (NetBank V — sparse) │
   └────────────────┬─────────────────────────────┘
                    │
                    ▼
   ┌──────────────────────────────────────────────┐
   │ if plain_ce < replay_threshold:              │
   │    replay_buf.push((x.cpu, y.cpu))           │
   │ if step % replay_every == 0:                 │
   │    sample buf, run frozen-Local replay step  │
   └──────────────────────────────────────────────┘
                    │
                    ▼
              next step ...
```

---

## Inference flow

At inference, only the forward path runs (no backward, no replay,
no aux losses). The same routing mechanisms apply:

```
  prompt → encode → (B, T_p) byte ids
                        │
                        ▼
              ┌──────────────────┐
              │  prefix forward  │  (process prompt; warm KV caches)
              └────────┬─────────┘
                       │
                       ▼
                  greedy / sampled byte
                       │
                       │  (optional: prepend pause bytes #9)
                       ▼
              ┌──────────────────┐
              │ token-by-token   │  (1 byte at a time;
              │  forward via KV  │   uses 4 tiers, gate routes,
              │   cache update   │   carry updates per token)
              └────────┬─────────┘
                       │
                       ▼
                generated bytes ► decode → utf-8
```

---

## References

The following SOTA papers shaped the architecture (cited where they
informed a specific decision):

- **AdaLomo** (arxiv:2310.10195) — per-row optimizer state for sparse memory
- **PonderNet** (arxiv:2107.05407) — adaptive halting (deferred)
- **Mixture-of-Recursions** (arxiv:2507.10524) — depth-routed iterative attn
- **Universal Transformers** (arxiv:1807.03819) — weight-tied iter attention
- **Focal Loss** (Lin et al 2017) — hard-byte up-weighting
- **PEER** (arxiv:2403.04432) — PKM training tricks (q_norm, dead-slot reinit, z-loss)
- **DualNet** (arxiv:2110.00175) — fast/slow consolidation template
- **FSC-Net** (arxiv:2511.11707) — within-run distillation+replay
- **StableMoE** (arxiv:2204.08396) — distill-then-freeze gate handoff
- **Routing Absorption** (arxiv:2603.02227) — co-trained gate failure mode
- **Read-ME** (NeurIPS 2024) — router-distillation loss design
- **Token Order Prediction** (arxiv:2508.19228) — auxiliary structural heads
- **Generative Replay** (arxiv:2007.07308) — hippocampal-cortical analogue

---

## Appendix — checkpoint compatibility

Adding new parameters to the model would, by default, shift positional
ckpt-load alignment. Every mechanism above that adds new params puts
them at the **end** of `(parameters m)`:

```
  position-stable params (old ckpts always align):
    1. tok-emb
    2. per-block core (norm, q/k/v/o/FFN, bank-query, bank-feedback, K_a, K_b)
    3. norm-final

  position-EXTENDED params (loaded if present, else fresh init):
    4. mtp-head             (added when MTP_COEF > 0)
    5. memory q-norm        (PEER addition)
    6. SwitchGate gate_proj + gate_proj_3
    7. NetBank dense (K_a, K_b, expander, q_norm)
    8. importance-head      (router-smarts)
    9. carry per block      (router-smarts)
   10. SwitchGate alpha_net (only when MMLLM_ALPHA_NET=true)
   11. delim-head           (only when MMLLM_DELIM_AUX_COEF > 0)
```

The tolerant `load-checkpoint!` handles `len(model_params) > len(saved)`
gracefully — extras stay at fresh init. This means any combination of
mechanism flags can be activated on a resume without needing to retrain
from scratch.
