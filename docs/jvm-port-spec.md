# JVM Port Spec — hand-rolled Neanderthal training + inference

Status: DRAFT for review. Nothing in this document is implemented yet.

This specs the "option 3" port: reimplement mmLLM's **training and
inference** on the JVM in Clojure, hand-rolling the model math on
[Neanderthal](https://github.com/uncomplicate/neanderthal) (with
[Deep Diamond](https://github.com/uncomplicate/deep-diamond) tensor
descriptors where convenient), with hand-derived backward passes instead
of an autograd tape. The motivating win is **thread parallelism**: real
JVM threads driving the 16-router training step concurrently, hogwild
sparse bank updates, and no interpreter lock anywhere — the things the
Python/Basilisp stack structurally can't give us. diamond-onnxrt remains
the eventual *serving* tier (separate workstream); this spec is the
*training* engine.

The PyTorch/Basilisp implementation stays the **reference
implementation** and the production chain keeps running on it until the
JVM port passes every parity gate in §12. Nothing existing is modified
except additive bridge/dump tooling.

---

## 1. Ground rules

1. **Parity first, speed second.** Every module lands with a parity test
   against golden vectors dumped from the torch reference before any
   threading or optimization work on it starts. The MLX backend
   (`src/mmllm/mlx/`, esp. `parity.py`) is the precedent and template.
2. **The torch stack is not touched.** All new code lives under `jvm/`
   plus a small number of additive Python dump/bridge scripts under
   `scripts/`. No changes to `core.lpy`, `extend_chain.sh`, recipes, or
   CI training paths.
3. **Δ-ablation alone is not proof** (CLAUDE.md, 2026-05-13): the JVM
   trainer's acceptance tests MUST include the V-moved check
   (`moved% > 1%`, `cos(V, V_init) < 1.0`) in addition to Δ_local/Δ_net.
4. **Chain/harvest compatibility is a phase-3 concern.** The port first
   proves it can train a spoon standalone; only then do we wire it up as
   a bird. A JVM bird must be byte-compatible at the artifact level
   (dense.pt tensor count + order, V_net `.bin` layout) or the harvest
   drops it — see §4 and §13.
5. **Canonical config only.** The port targets the sym24 production
   arch as pinned by the genesis
   `workers/dispatcher/harvest-0way-r0_sym24/round-0/chain_meta.json`
   plus the `extend_chain.sh` recipe env. Every optional feature that
   the prod recipe leaves off (focal CE, importance head, schema mask,
   FIM loss mask, MTP head, delim head, bank repeat-N, feature-MSE
   distill) is **out of scope v1** — the parity harness runs with those
   envs unset on the torch side too.

## 2. Target configuration (what exactly we are porting)

From `chain_meta.json` (authoritative) + `default-config-cpu-mini`
(`core.lpy:911`) + `extend_chain.sh` forced env:

| knob | value | source |
|---|---|---|
| config | cpu-mini: d_model=32, n_layers=32, d_ff=128 | core.lpy:911 |
| heads | 4 = 2 short + 2 long; head_dim=8; 1 KV head/tier (GQA ×2) | core.lpy:938 |
| q_dim (bank query/value dim) | n_long_heads × head_dim = 16 | core.lpy:938 |
| seq_len / max_pos / rope_theta | 1024 / 8192 / 500000 | core.lpy:955 |
| vocab | 256 (bytes), weight-tied LM head | core.lpy |
| local bank layers | 0..23 (sym24) | chain_meta |
| local bank | sqrt_n=128, n_trunks=16 routers, top_k=128, sub_top_k=24, V fp32 | extend_chain.sh:97,118,128,145 |
| netbank | per-layer ×32 (NETBANK_SHARED=false), sqrt_n=1024, c_net=8, top_k=512, sub_top_k=24, expander Linear(8→16, no bias) | chain_meta + extend_chain.sh:129 |
| gate | SwitchGate 3-way + alpha_net=true + GATE_NET_DEFAULT=true (ST-Bernoulli local firing) | extend_chain.sh:157-158 |
| batch | B=1 per router × 16 routers = effective 16 | extend_chain.sh:145,154 |
| objective | CE + z-loss + logitkd KD (KD_TEMP=2, KD_COEF=1, KD_FREEZE=trunk, KD_EVERY=2) | extend_chain.sh:187-191 |
| LR | base 3e-3 (min 3e-3), warmup 70% of round steps; group mults cosine: net 0.001→5.0, bank 3.0→0.001, dense 0.05→0.005 | extend_chain.sh:192-233 |
| sparse opt | adam-cpu (touched-row SparseAdam), MMLLM_LR_LOCAL_MULT=0.05 | optim.py |

**M0 (below) extracts ground truth from a live chain-head checkpoint**
— exact dense tensor count (expected 698), every tensor's shape and
positional index, bank file sizes — and freezes them into a
`jvm/resources/arch-sym24.edn` schema file. Derived sizes in this table
are formulas, not stamps; M0's dump wins any discrepancy.

## 3. Stack and repo layout

- **JDK 22+** (final `java.lang.foreign` FFM API for mmap
  `MemorySegment`s; `Float.float16ToFloat`/`floatToFloat16` intrinsics
  for V_net fp16). Loom virtual threads available but the training pool
  uses platform threads (compute-bound).
- **Clojure 1.12**, `deps.edn` project rooted at `jvm/`.
- **Neanderthal ≥ 0.60.0** — CPU backend (MKL on x86, Accelerate on
  Apple Silicon: both local-bird targets). All matmuls, axpy, scal.
- **Deep Diamond ≥ 0.42.0** — optional convenience (tensor descriptors,
  softmax primitive). We do NOT use its layer/network API: our layers
  are custom and its blueprint abstraction doesn't fit hand-rolled
  backward. If it earns nothing beyond Neanderthal by M2, drop the dep.
- Java arrays / `MemorySegment` for banks and activations; no
  `nn.Module` analog — the model is a plain map of named float buffers
  (the same shape as `mlx/parity.py`'s param dict).

```
jvm/
  deps.edn
  src/mmllm/jvm/
    config.clj        ;; arch-sym24.edn loader + env-var recipe parsing (§2)
    params.clj        ;; param schema: name ↔ shape ↔ positional index (§4)
    bridge.clj        ;; npy/npz + raw .bin readers/writers (§4)
    tensor.clj        ;; thin helpers over Neanderthal (views, reshapes)
    rope.clj          ;; cos/sin cache + apply-rope fwd/bwd
    norm.clj          ;; RMSNorm fwd/bwd
    sdpa.clj          ;; causal/windowed SDPA fwd + recompute-bwd (§9)
    pkm.clj           ;; product-key retrieval fwd/bwd (Local + Net share it)
    gate.clj          ;; SwitchGate 3-way + alpha_net + ST-Bernoulli fwd/bwd
    block.clj         ;; pre-norm block fwd/bwd (attention + SwiGLU FFN)
    model.clj         ;; full forward: tok-emb → 32 blocks → norm-final → tied head
    loss.clj          ;; CE, z-loss, logitkd KD
    optim.clj         ;; AdamW (dense) + touched-row SparseAdam (banks)
    schedule.clj      ;; lr-at-step + per-group cosine mults
    bank_store.clj    ;; MemorySegment mmap banks, fp16<->fp32, hogwild writes
    data.clj          ;; corpus staging, byte batcher, batch-replay mode
    train.clj         ;; train-step + round loop + ckpt save/load
    evals.clj         ;; eval-bpc + Δ_local/Δ_net ablations + V-moved check
    parity.clj        ;; golden-vector comparison harness
  test/mmllm/jvm/     ;; per-module parity + finite-difference grad tests
scripts/
  jvm_bridge.py       ;; NEW (additive): dense.pt ↔ .npz + manifest.json
  dump_goldens.py     ;; NEW (additive): per-module golden I/O + grad dumps
```

## 4. Interop boundary (checkpoints, banks, goldens)

The torch side's serialization quirks are handled ONCE at the boundary;
no JVM code ever parses pickle.

- **`scripts/jvm_bridge.py`** (Python, torch env): converts a
  `dense.pt` (positional `list[Tensor]`, order defined by
  `(parameters m)` at `core.lpy:2181`) to a `.npz` plus
  `manifest.json` mapping `index → {name, shape, dtype}` — and back.
  The name schema comes from walking the same model build that
  produced the list, mirroring `mlx/parity.py:extract_params`. The
  reverse direction (npz → dense.pt) is what a future JVM bird uses to
  emit harvest-compatible checkpoints; getting the order right is the
  bridge's job, tested by round-tripping a real chain-head dense.pt to
  bit-identical bytes.
- **Bank files need no bridge**: Local V and V_net are headerless raw
  arrays (`memory.py:746`, `netbank.py:58`) — fp32 row-major
  `(n_trunks·sqrt_n², q_dim)` for Local, fp32/fp16 `(sqrt_n², c_net)`
  per layer for Net. `bank_store.clj` maps them directly with
  `FileChannel.map` → `MemorySegment` (read/write, shared). Same files,
  same bytes, zero conversion — the OS page cache is shared with any
  other reader, exactly the README's serving story.
- **`scripts/dump_goldens.py`**: for each module, dump input, output,
  and (input-grad, param-grads) under a fixed seed to `.npz`, running
  the torch reference in the prod-recipe env. Also dumps 3 full
  train-step traces (loss scalars per term, per-param grad norms,
  post-step param deltas) and a tokenized batch stream for §11's
  replay mode.

## 5. Parameter schema

`params.clj` materializes the model as `{name → Neanderthal matrix}`
plus a vector giving the canonical positional order. The order is the
back-compat-sensitive contract from `core.lpy:2181`:

1. `tok-emb.weight`
2. per-block core: norm1, norm2, q/k_s/v_s/k_l/v_l/o-proj, FFN
   gate/up/down, bank-query, bank-feedback, memory.K_a, memory.K_b
3. `norm-final.weight`
4. (end-appended, in order): per-block memory.q_norm; per-block
   long-gate (gate_proj, gate_proj_3); per-block netbank dense
   (K_a, K_b, q_norm, expander); per-block carry (if any);
   per-block alpha_net; per-block local_active_proj + local_active_bias

Sparse (non-dense.pt) params: per-block Local `V` and Net `V` — these
live in the mmap'd bank files, never in dense.pt.

M0 freezes this as data (`arch-sym24.edn`) generated by
`jvm_bridge.py`, not as code — so a count/order mismatch is a diff in a
checked-in file, caught at review time, instead of a silently dropped
bird at harvest time.

## 6. Forward spec

All fp32 except V_net storage (fp16 on disk in some chains; convert
per-row on gather). Shapes use B=batch-per-router, T=seq, D=d_model=32,
H_s/H_l=2/2, d_h=8, q_dim=16.

Reference implementations: `attention_kernel.py:198` (attention),
`:435` (block), `memory.py:908` (PKM), `netbank.py:295` (NetBank),
`gating.py:135` (SwitchGate), `core.lpy:2412` (model forward).

1. **Embedding**: row gather from `tok-emb (256, 32)`.
2. **RMSNorm** (norm1/norm2/norm-final/q_norm):
   `y = w ⊙ x / rms(x)`, `rms = sqrt(mean(x²) + eps)`.
3. **RoPE** (short tier only): precomputed cos/sin at `rope_theta=5e5`,
   `max_pos=8192` (`core.lpy:988`); `y = x·cos + rotate_half(x)·sin`,
   offset by the cache position.
4. **Three-tier attention** (per block):
   - Q proj `(D→D)`, split 2 short + 2 long heads.
   - Short: K_s/V_s proj `(D→d_h)` (1 KV head, GQA-repeat ×2), RoPE on
     Q+K, append to short KV cache, causal SDPA
     (`softmax(QKᵀ/√d_h)V`), optional sliding window.
   - Long-SDPA: K_l/V_l proj, **no RoPE**, unbounded long cache,
     causal SDPA.
   - Long-bank: `bank_q = flatten(q_long) (B,T,16)` (+ bank-query ctx
     mod if configured; prod default is none). Local PKM (5) and
     NetBank (6) both consume `bank_q`. SwitchGate (7) mixes the three
     long sources; short and long head outputs concat → O proj.
   - Training runs full-sequence (T=1024, caches start empty,
     `is_causal` masking); decode runs T=1 against persistent caches.
5. **Local PKM** (`pkm.clj`, math from `memory.py:942-1038`):
   `q_norm(q)` → split halves `(8,8)` → `s_a = q_a·K_aᵀ`,
   `s_b = q_b·K_bᵀ` (K_* are `(128, 8)`) → per-half top-`sub_top_k=24`
   → outer-sum of 24×24 candidate pairs → top-`top_k=128` scores +
   flat indices `i_a·128 + i_b` → per-router offset
   `+ trunk_id·128²` → gather V rows `(128, 16)` from the mmap →
   `out = Σ softmax(scores)_k · V_k`. Z-loss side-product:
   `zl = mean(logsumexp(s_a)²) + mean(logsumexp(s_b)²)`.
6. **NetBank**: same addressing at sqrt_n=1024, top_k=512, no trunks;
   gathered rows are `(512, 8)` latents;
   `out = expander( Σ softmax(scores)_k · latent_k )` (fold the
   softmax into the sum before the 8→16 matmul, as
   `netbank.py:397-402`). The 1–10 ms simulated WAN delay is
   training-only flavor — replicate it (config-gated) so step-time
   comparisons are honest.
7. **SwitchGate 3-way + prod extras** (`gating.py:169-260`):
   `w = softmax(einsum(q_long, gate_proj_3))` per (B,H,T);
   `net *= alpha_net[h]`; ST-Bernoulli local firing:
   `p = σ(einsum(q_long, local_active_proj) + bias)`; training samples
   hard 0/1 with straight-through gradient (`hard + p - detach(p)`),
   eval uses `p` directly; renormalize `(w_sdpa, w_local·fire, w_net)`
   to sum 1 (+1e-6); mix.
8. **FFN**: SwiGLU `down( silu(gate(x)) ⊙ up(x) )`, d_ff=128.
9. **Head**: `logits = x_final · tok_embᵀ` (weight-tied).

## 7. Backward spec

No tape. Each module's forward returns `[out ctx]`; `block.clj`
composes closures in a fixed reverse order. Per-module gradients (all
textbook; the finite-difference tests in §12 are the safety net):

- **RMSNorm**: `dx = w/rms ⊙ (dy - x · mean(dy⊙w⊙x)/rms²)`;
  `dw += Σ dy ⊙ x/rms`.
- **RoPE**: linear — `dx = dy·cos + rotate_half⁻¹(dy·sin)` where
  `rotate_half⁻¹ = -rotate_half`.
- **SDPA**: standard softmax-attention backward; recomputed
  block-wise, see §9.
- **GQA repeat**: sum grads across the repeated head groups back to
  the single KV head.
- **top-k / gather**: selection is piecewise-constant — grads route to
  the selected indices only (scatter-add), zero elsewhere. No gradient
  through the *choice* of indices (matches torch).
- **PKM**: given `w = softmax(top_scores)`, `V_sel (k, q_dim)`:
  `dV[row_j] += w_j · dout` (sparse scatter, per-router rows);
  `dw_j = dout · V_j`; softmax backward → `dscores`; scores decompose
  as `s_a[i_a] + s_b[i_b]` → scatter `dscores` into `ds_a`, `ds_b` at
  the selected sub-key indices; `dK_a += ds_aᵀ·q_a`,
  `dq_a = ds_a·K_a` (and b-side); q_norm backward; plus the z-loss
  branch (`d logsumexp = softmax`).
- **NetBank** adds: `d_expander`, `d_latent = ...·expanderᵀ`, then the
  same PKM scatter into V_net (fp16 rows: read-modify-write in fp32,
  store fp16).
- **SwitchGate**: product/softmax/sigmoid rules; ST-Bernoulli backward
  is the smooth `σ` gradient (that's the whole point of the ST trick);
  renormalization is a quotient rule over the +1e-6-stabilized sum.
- **SwiGLU / Linear / embedding / tied head**: standard; tied head
  means `d tok_emb` accumulates from both the input gather and the
  output matmul.
- **freeze-trunk (KD student pass)**: `_flin`/`_fnorm` with detached
  weights (`attention_kernel.py:110-119`) ≡ propagate `dx` through the
  op but skip the parameter-gradient accumulation for dense trunk
  params. In `block.clj` this is a per-pass boolean checked at each
  accumulation site.

## 8. Losses and train-step

Per `core.lpy:2622` with prod-recipe env (focal γ=0, no IH/schema/FIM/
MTP/delim ⇒ those terms vanish):

```
loss = CE(logits, y)
     + z_coef · Σ_layers z_loss                      (z_coef ~1e-5)
     + [step % KD_EVERY == 0] · KD_COEF · T² · KL(teacher_T ‖ student_T)
```

The KD term costs two extra forwards: **teacher** = local-only
(NetBank off) under no-grad; **student** = net-only (Local off) with
freeze-trunk. KL at temperature T=2 over the byte softmax,
`mean over positions of Σ_v p_t (log p_t − log p_s)`. Stash
`kd_local_net`, `teacher_bpc`, `student_bpc` for the step printer —
the reporting discipline in CLAUDE.md expects them.

Backward runs on (CE + z) through the main forward, and on the KD term
through the student forward only. Router batching: the 16 routers each
run B=1; §10 makes those 16 forward/backward pairs the unit of thread
parallelism.

## 9. Activation memory plan

At B=16(eff)×T=1024, materialized SDPA attention weights are
`(B,H,T,T)` ≈ 8 MB/call and torch needed grad-checkpointing to fit CI
(`attention_kernel.py:287-306`, `MMLLM_GRAD_CHECKPOINT=true`). The JVM
port does NOT replicate torch checkpointing; instead:

- **SDPA backward recomputes attention row-blocks** (flash-style CPU
  loop, block size ~64 rows): keep only Q/K/V and the output; never
  hold `(T,T)` for backward. This is cheaper than torch's
  checkpoint-everything (which recomputes the whole block forward and
  cost ~20× wall on CPU per the comment at `attention_kernel.py:300`).
- Everything else at cpu-mini is small (D=32): per-block saved ctx is
  a few MB; per-router totals stay well under the 16-thread × RAM
  budget. `train.clj` asserts a computed activation budget at startup
  against a `MMLLM_JVM_MAX_RSS` knob and refuses configs that don't fit.

## 10. Threading architecture (the payoff)

Parallelism levels, all with MKL/Accelerate pinned to 1 intra-op thread
(at D=32 the matrices are far too small for intra-op threading; outer
parallelism owns the cores):

1. **Per-router step parallelism (primary).** 16 platform threads,
   each running the full forward+backward for its router at B=1 over
   the same shared read-only dense params. Dense grads accumulate into
   per-thread buffers, reduced tree-wise once per step (~500 k dense
   params ⇒ microseconds). Local-bank V grads are hogwild: each
   router's rows live in ITS OWN trunk slice (`trunk_id·128²` offset)
   — disjoint by construction, so scatter-writes need no locks at all.
   V_net rows CAN collide across routers; apply V_net updates through
   the sparse optimizer's single-threaded apply phase (per-step
   reduce), or per-row striped locks if profiling demands. This is the
   step-level speedup Python cannot express: today the 16 routers ride
   through torch ops as one batched B=16 tensor where bank gathers,
   optimizer scatter and all Python orchestration serialize.
2. **KD overlap.** The teacher forward is no-grad and independent of
   the main forward's backward — run it on spare threads concurrently.
3. **Pipeline threads**: data batcher, checkpoint writer, and the
   periodic ablation eval run off the training threads.
4. **Determinism switch.** `MMLLM_JVM_DETERMINISTIC=true` forces
   fixed-order reductions and a fixed per-router RNG stream — required
   for parity runs and CI; free-order reductions otherwise.

Benchmark deliverable (M6): steps/s and tokens/J vs the torch reference
on the same box at 1, 4, 8, 16 threads, plus a scaling curve. The port
justifies itself here or not at all.

## 11. Data pipeline

- Corpora: reuse the release-tarball staging
  (`scripts/fetch_static_assets.sh corpora`); `data.clj` reads the same
  staged files. Byte-level "tokenization" is `unsigned byte → int`.
- **Batch-replay parity mode**: `dump_goldens.py` records the exact
  (x, y) batch stream the torch reference consumed for N steps; the JVM
  trainer replays it so loss curves are comparable point-by-point
  without reproducing Python RNG.
- Native sampling mode (post-parity): port the 9-corpus mix weights
  from `datasets.py`; document any sampler difference as a recipe
  deviation, not silently.

## 12. Parity and verification gates

Golden-vector tolerances (fp32 CPU vs fp32 CPU): per-module forward
max-abs-err ≤ 1e-5 relative; grads ≤ 1e-4 relative vs torch autograd
dumps AND central-difference checks on the JVM side alone. RNG is
never reproduced across runtimes — all stochastic inputs (init,
Bernoulli draws, batch order) come from dumps in parity mode.

| gate | test |
|---|---|
| G1 module fwd | every module in §6 matches goldens |
| G2 module bwd | every gradient in §7 matches autograd dumps + finite diff |
| G3 full fwd | end-to-end logits on a chain-head ckpt match torch ≤ 1e-4; bpc matches to 4 decimals (mirrors `mlx/parity.py:run`) |
| G4 step | 3 replayed train-steps: every loss term and per-param grad norm matches; post-step param deltas match (AdamW + sparse Adam semantics incl. LOCAL_MULT rules from `optim.py:98-106`) |
| G5 spoon | 100-step replayed run: loss curve within noise band of a torch seed-pair spread; Δ_local > 0; **V_local moved% > 1% and cos < 1** (the 2026-05-13 lesson — mandatory) |
| G6 threads | 16-thread run ≡ 1-thread run in deterministic mode; free mode within noise band; scaling curve published |
| G7 ckpt round-trip | JVM save → bridge → dense.pt loads in torch `load-checkpoint!` and evals to the same bpc; bank `.bin`s byte-compatible |

## 13. Milestones

| # | deliverable | accepts when | est. |
|---|---|---|---|
| M0 | ground truth: `jvm_bridge.py`, `dump_goldens.py`, `arch-sym24.edn` (tensor count/order/shapes from a live chain head) | dense.pt round-trips bit-identical; manifest reviewed | 1 wk |
| M1 | skeleton: deps.edn, tensor/params/bridge/config, load a chain head into JVM buffers | shapes + a few spot-check tensors match | 1 wk |
| M2 | dense forward (no banks): emb→blocks(SDPA-only)→head | G3 on a bank-ablated config | 1–2 wk |
| M3 | PKM + NetBank + SwitchGate forward, mmap bank_store | G3 full; Δ_local/Δ_net of a chain head match torch's eval battery | 1–2 wk |
| M4 | backward for everything + losses (incl. KD, freeze-trunk) | G1+G2 complete, G4 | 2–3 wk |
| M5 | optimizers + schedule + ckpt save/load + eval/ablation loop | G4 incl. optimizer deltas; G7 | 1–2 wk |
| M6 | threading (per-router, hogwild local V, deterministic mode) + bench | G5, G6 | 2 wk |
| M7 | native data sampling; spoon + chain-round UX (`run_jvm_bird.sh`-shaped entry) | 5-round local chain trains, Δ_net trajectory comparable to a torch local bird | 1–2 wk |
| M8 | (gated on user sign-off) harvest integration as a real bird | a JVM bird's push survives a real harvest tick un-dropped | 1 wk |

Total: ~10–15 engineer-weeks to M7. M2/M3 and the M4 grind are the
long poles. Every milestone is independently landable and useful (M3
alone gives a JVM inference engine off real chain checkpoints,
before any training work).

## 14. Risks and mitigations

- **Silent gradient bugs** — the classic hand-rolled failure. Mitigated
  by G2's double check (autograd dumps AND finite differences), G4's
  step-level norms, and G5's V-moved test which catches exactly the
  "everything runs, nothing learns" mode documented in CLAUDE.md.
- **Positional-order drift** (698-tensor contract). Mitigated by M0
  freezing order as reviewed data + G7 round-trip; the harvest's
  modal-count majority drop is the backstop, not the detector.
- **fp16 V_net on JVM**: no native fp16 arithmetic; convert per-row at
  gather/scatter via `Float.float16ToFloat` intrinsics. The prod sym24
  chain runs V_net fp32, so this is a compat path, not the hot path.
- **Numerics**: logsumexp/softmax must be max-subtracted like torch;
  KD KL at T=2 amplifies logit differences — G3's 1e-4 logit tolerance
  is deliberately tighter than "bpc matches".
- **Hogwild V_net collisions**: start with the safe per-step reduce;
  only relax to lock-striped hogwild with a measured win, in free
  (non-deterministic) mode only.
- **Simulated-WAN delay + step-time honesty**: replicate the delay
  config-gated so JVM-vs-torch step-time comparisons don't flatter the
  port by dropping a sleep torch pays.
- **Neanderthal API drift** (0.6x moves fast, per the 2025–26 release
  cadence): pin versions in deps.edn; the tensor.clj shim keeps the
  blast radius of an upgrade to one namespace.
- **Scope creep into recipe changes**: any place the port would "fix"
  a recipe choice (sampler, delay, schedule quirks) → replicate first,
  file a deviation note, change nothing without sign-off (CLAUDE.md
  rule 7).

## 14b. Reference-semantics findings and dispositions (2026-07-03)

Surfaced by the M5a optimizer-parity work; dispositions set by the user:

1. **Dense AdamW trains with decoupled `weight_decay=1e-2`** (torch
   default; `make-opt-dense` passes only `lr`). Disposition: replicate
   as-is on the JVM (done, bit-exact); **replace only if it
   demonstrably hurts** — tracked as a watch item.
2. **`MMLLM_LR_KAB_MULT` was inert in prod** (unset → K_a/K_b silently
   rode the dense schedule; the two-group mechanism in `make-opt-dense`
   + `set-opt-lrs!` was fully plumbed but never activated).
   Disposition: **activated per original #3-spike intent** —
   `extend_chain.sh` now defaults `KAB_MULT=0.15 → KAB_MULT_END=0.001`:
   addressing hill-climbs during wake, freezes during sleep so logitkd
   distills against stable Local addresses. Initial operating point
   only; cron-prod sweep discipline (≥3 harvests) applies before
   trusting. JVM mirror + golden regen tracked as a follow-up task.
3. **`lr-at-step` mixes reference frames** (ROUND_BASE-relative warmup,
   absolute-step cosine). Disposition: **intentional** — part of the
   deliberate curve shaping across overlapping chain rounds. Replicate
   exactly; do not "fix".
4. **Sparse Adam bias correction is per-param, not per-row** (a row
   first touched at step k gets step-k correction with zero moments),
   plus the `v_local_counter` grad-less-param tile-shift quirk.
   Disposition: replicate exactly (done, goldens cover both); **watch**
   for late-touched-row update spikes, replace only if a problem.

## 15. Non-goals (v1)

GPU/MPS execution; torch.compile-style fusion; the aesop curriculum
generators; Modal orchestration; speculative decoding; int8 banks;
feature-MSE distill and all env-gated-off heads (§1.5); replacing the
torch reference or the production chain. diamond-onnxrt serving
integration is a separate workstream that consumes this port's
checkpoints via the M0 bridge.
