# Training-Efficiency Composition Roadmap

**Status:** living doc · started 2026-06-26 · derived from a 5-agent SOTA sweep (2024–2026)
**Scope:** byte-level MoE-memory LM on a single 32 GB Apple-Silicon box (MLX), federated wave/harvest chain, distillation-as-consolidation.

---

## PRIME DIRECTIVE (read before touching anything)

1. **ADDITIVE ONLY.** Every item here is meant to **compose on top of the current config**, not replace it. The f256 lineage, the PKM netbanks, the router, the wave/harvest chain, the wake/sleep LR controller, and the distillation consolidation loop all stay.
2. **PRESERVE PROGRESS.** Do not scrap trained trunk/bank state to adopt an idea. Prefer A/B branches and live knobs (we already hot-reload `f256_live.json`) over destructive retrofits.
3. **ASK BEFORE REMOVING.** The only deletions allowed are documented *no-progress / negative-progress* items, and even those require explicit approval. They live in their own section below — flagged, not actioned.
4. **VALIDATE ON RETENTION PROBES.** Every adopted item is judged on the existing Δ_net / retention-probe discipline, not benchmark deltas (benchmark overfitting is real — see phi caveat).

Status tags used below:
`[ADD]` pure addition, no existing piece changes ·
`[ENH]` enhances an existing component in place ·
`[A/B]` swap to validate on a branch, keep current as control ·
`[NEXT-GEN — ASK]` larger architectural bet, needs approval ·
`[REMOVE? — ASK]` no-progress candidate, do not remove without sign-off.

---

## 0. The reality check (why most "speedup SOTA" is irrelevant here)

- **The CUDA efficiency stack does not exist on MLX:** FP8/MXFP/NVFP4, FlashAttention 1/2/3, Triton/Liger, torch.compile, bitsandbytes 8-bit optimizers, FSDP/ZeRO/TP/PP. The M5's FP8 hardware is inference-only. Ignore these headlines.
- **No optimizer beats a well-tuned AdamW by >~1.4× at our scale**, edge shrinks with size. Tune the AdamW baseline before believing any new-optimizer win.
- **B=2 is near-optimal, not a compromise.** Critical batch size scales with *data size, not model size*; small batches are more HP-robust and match large-batch per-FLOP; gradient accumulation is "wasteful single-replica." → leave batch alone.

Our four real channels: **native MLX kernels/precision · fewer steps · fewer tokens · higher quality-per-FLOP architecture.**

---

## 1. Current system (the substrate we compose onto)

**f256 baseline (completed w100, 2026-06-26):** avg bpc **2.670**, avg Δ_net **2.045**; per-module text 2.578 / math 2.625 / agentic 2.988 / code 2.488. Beat the w256 predecessor (3.12) and the whole cg lineage's empty-bank Δ_net. This `RB(100)` trunk+banks is the seed to compose onto. (Levers that got here: TOP_K=128 fill fix · saturation→wake/sleep→ramped→jittered trunk-LR cycle · period-5 endgame shape landing on the cool trough.)

- Byte-level LM, vocab 256; dense trunk d_model=256, d_ff=768, n_heads=4 (~25 M / ~101 MB).
- PKM netbanks: StreamV disk-streamed, sqrt_n=256, c_net=8, n_blocks=160 (~10 GB/module), TOP_K=128 fill; 4 modules (text/math/agentic/code).
- Two-level skill router (per-seq preselect K_LOAD + per-token top-k) + VQ block-routing.
- Federated wave/harvest: PAR=4 birds, FedAvg trunk+router, per-module V-union harvest, KEEP=3 janitor.
- Distillation: logit-KD from a LOCAL teacher into the netbank (the consolidation mechanism).
- Trunk-LR control: saturation-aware + **wake/sleep cyclic** controller, live-tunable via `f256_live.json` (hot-reload, structural-sweep mode built but off).
- Hot/cold expert offload: pread → bounded-LRU SSD streaming.

---

## 2. TIER 1 — compose now (native, cheap, high-confidence)

- **Muon optimizer** `[A/B]` — ~1.3–1.4× fewer steps **and ½ Adam's optimizer memory** (direct 32 GB win), matmul-only, bf16-stable, native in `mlx-optimizers` (+ core PR #1914). A/B on a branch against tuned AdamW; keep AdamW as control. Applies to the *dense trunk* optimizer; netbank sparse-Adam unchanged. `kellerjordan.github.io/posts/muon` · arXiv 2502.16982
- **WSD schedule** `[ENH]` — warmup → constant peak (≈½ cosine) → short √-shaped cooldown. Composes *under* the wake/sleep trunk-LR controller as the base-LR envelope; lets us branch/ship at any token count and inject data during decay. arXiv 2405.18392
- **Stability stack = the LR-thrash antidote** `[ENH]` — QK-norm (pre-RoPE) + z-loss (~1e-5) + **ZClip** (z-score grad-spike clip, ~37% fewer tokens-to-target, 2 scalars) + OLMo-2 reordered output-norm. Neither norm trick kills spikes alone; together they unlock a higher usable LR. Adds to the trunk; retrofit needs a short re-warm or apply on a fresh trunk branch. arXiv 2410.16682 · 2504.02507 · 2501.00656
- **Native compute hygiene** `[ADD]` — `mx.fast.scaled_dot_product_attention` with the `"causal"` *string* mask (~2.3× vs manual additive mask, fused backward); `mx.compile` per transformer block (~5× fused elementwise); **periodic `mx.eval`** to bound lazy-graph/memory growth (load-bearing for netbank buffers). BF16/FP16 AMP as the floor; `mx.checkpoint` + small batch for headroom.
- **EMA / LAWA weight averaging** `[ADD]` — window ≈1 % of budget → ~15–30 % fewer steps to target; stream checkpoints into a running-sum buffer (fits the bounded-buffer pattern). Doubles as an LR-decay surrogate. arXiv 2502.06761
- **Aux-loss-free router bias + sigmoid gate** `[ENH]` — ~10 lines on the existing router; removes the balance-vs-quality tradeoff → **direct fix for the router-monopoly / K_LOAD pain.** arXiv 2408.15664

## 3. TIER 2 — worth a spike (moderate setup, high upside)

- **Multi-token prediction, n≈8 byte heads (causal/sequential variant)** `[ADD]` — top architecture pick: MTP's "doesn't help small models" caveat *reverses* at byte level (+67 % MBPP, 1.7× less data in Meta's byte run). Extra heads share the trunk, dropped at inference. **Use sequential head compute** to avoid the prior NetBank-backward OOM. arXiv 2404.19737
- **Data-quality classifier (domain-matched)** `[ADD]` — retrain a fastText head with code/math/agentic positives (don't reuse FineWeb-Edu — prose-biased). CPU-only. DCLM arXiv 2406.11794
- **Online loss-based data mixing (ODM/ADO)** `[ENH]` — one bandit arm per corpus, ~0 % overhead; replaces stratified buckets with adaptive mixing. **DoReMi-style token-count weights do NOT port to byte-level** — use online/loss-space. arXiv 2312.02406
- **Per-domain repetition** `[ENH]` — ~4 epochs free / ~16 ceiling; set epochs *per corpus* (more for scarce math/agentic); code ~50 % as a ~2× data-extender. arXiv 2305.16264
- **µP / u-µP + CompleteP** `[ADD]` — tune LR/init on a 9–50 M proxy, transfer across trunk/module size; **coordinate-check**, and note dense-µP doesn't cover routing/top-k/PKM (MoE-µP). arXiv 2203.03466 · 2505.01618
- **BF16 stochastic-rounding optimizer** `[A/B]` — drops the FP32 master copy (unified-memory win) + LR robustness. Implementable in MLX, not packaged. arXiv 2502.20566
- **WRAP synthetic rephrasing** `[ADD]` — local ~7 B teacher rephrases real docs into styles (~3× speedup, grounded → less collapse). Offline, reusable. arXiv 2401.16380
- **Length curriculum (Dataset-Decomposition, per-doc buckets)** `[ENH]` — pays off *more* at byte level and avoids cross-corpus attention pollution. arXiv 2405.13226

## 4. TIER 3 — bigger bets (NEXT-GEN — ASK before committing)

- **Patching layer (BLT entropy-patch / SpaceByte / H-Net)** `[NEXT-GEN — ASK]` — effectively mandatory for serious byte-level *scaling*; mount the PKM-MoE on BLT's Latent Global Transformer (~50 % inference-FLOP save). H-Net is LR-thrash-prone (two interacting routers). Composes *in front of* the trunk; does not delete the trunk. arXiv 2412.09871
- **Linear backbone + sparse attention (RWKV-7 / Mamba-2, 1 attn per 6–8)** `[NEXT-GEN — ASK]` — byte sequences are ~4× longer so sequence-mixing dominates; MoE bank stays orthogonal. This *replaces attention layers* → explicit approval. arXiv 2503.14456 · 2405.21060
- **Memory-layer refinements** `[ENH]` — **query-batchnorm** (documented antidote to cold-expert/router-monopoly + flat-bank underfill), PEER single-neuron experts ("thousands of composable modules"), shared cross-layer memory pool, SiLU-gate + QK-norm on memory output. Enhance the existing PKM bank in place. arXiv 2407.04153 · 2412.09764
- **Drop-Upcycling bank seeding** `[ADD]` — partial re-init injects diversity → counters flat-bank underfill (for *new* banks; doesn't touch trained ones). arXiv 2502.19261
- **Infinite-compute recipe** `[A/B]` — 30× weight decay → ensemble epoched runs → distill to small student (17.5× data-efficiency, 83 % retained). arXiv 2509.14786

## 5. DISTILLATION (explicit focus) — compose onto the consolidation loop

- **Mobahi self-distillation / de-consolidation — INVESTIGATED → non-issue (see §6).** `[resolved]` The collapse needs pure soft-label distillation with teacher = previous student; we have neither (CE is the always-on base; the teacher is re-grounded on fresh data each wave). f256 Δ_net was monotonic through w100. No cap needed. Kept here only as the lens that *prompted* the investigation. arXiv 2002.05715
- **Distillation Scaling Law as a go/no-go gate** `[ADD]` — we're in the win quadrant (reusable teacher), but use a *moderate* teacher; too-strong a teacher *hurts* a small byte student (capacity gap). arXiv 2502.08606
- **Byte vocab=256 makes full logit-KD trivially cheap** `[ADD]` — the "sample 256 logits" tricks large-vocab models need are moot; do full-distribution KD directly.
- **Pre-released trace corpora (zero teacher calls, no ToS exposure):** s1K + tokenizer-independent "Wait" budget-forcing, Bespoke-Stratos-17K, OpenThoughts (R1-MIT / QwQ-Apache / Gemini-sourced). `[ADD]` arXiv 2501.19393
- **SDFT self-rewriting** `[ADD]` — model rewrites SFT data into its own distribution (cuts forgetting +10.71); analogous to our LOCAL-only output-KD. arXiv 2402.13669
- **Byte-specific distillation** (token-teacher → byte-student, >92 % retention at <10 % cost) `[ADD]` — strong if a good teacher exists. arXiv 2602.01007 *(2026 ID — verify)*
- **Flex-KD for hidden-state signal** `[A/B]` — selective-subspace, no projector; the principled replacement for the feature-MSE-on-full-residuals negative transfer (see removal candidate below).

---

## 6. REMOVAL CANDIDATES — **investigated 2026-06-26: both RESOLVED, nothing to remove**

A code+data investigation (two agents traced `mlx/trainer.py` + `core.lpy`; Δ_net trajectory analyzed across all f256 waves) closed both candidates. **No deletions proposed.**

- **Feature-MSE on the full residual** — **already disabled in the current config.** `MMLLM_DISTILL_OBJECTIVE=logitkd` sets the feature-MSE distill term to `0.0` ("logitkd replaces feature-MSE", trainer.py:977–980 / core.lpy:2882–2884). It only re-activates if the objective is switched back to `mse`. → *no action; Flex-KD remains the replacement if feature-distill is ever re-enabled.*
- **Uncapped iterative self-distill rounds** — **non-issue here.** The Mobahi collapse needs pure soft-label distillation with teacher = previous student. Neither holds: (1) ground-truth **CE is the always-on base** (`L = CE + KD_COEF·T²·KL`, KD ~1000× smaller than CE in magnitude), and (2) the **teacher is re-grounded on fresh data each wave** (V_local sleep-resets, teacher re-derived from this-wave's local bank), so the V_net recursion carries *state* but not a smoothed self-copy. Empirically Δ_net is monotonic, peaking at the latest wave (1.83 @ w91) — no de-consolidation. → *no cap needed.*

### Verified mechanism (the corrected mental model)
```
wave W:  V_net   = clone(RB(W-1))        ← PERSISTENT bank, accumulates across rounds
         V_local = fresh Gaussian init   ← sleep reset each wave
         teacher = trunk + fresh-trained V_local (net OFF, detached)
         student = trunk + carried V_net (locals OFF)
         loss = CE(full model, true bytes) + 1.0·T²·KL(teacher ‖ student)   [forward KL, Hinton T²]
         harvest: union bird V_net → RB(W) → feeds W+1
```
**What drives consolidation — OPEN TENSION, not resolved (correcting an earlier overstatement):** KD magnitude (~0.001) is small vs CE (~5–16), which *tempts* a "CE-driven / KD-vestigial" read — but that **contradicts the bisect** in [[mmllm-localmult-broke-distillation]], where killing the teacher (→ KD=0) drops Δ_net to ~0 *even with CE still running* (⇒ a learned teacher is necessary). KD updates V_net-only with the trunk frozen, so small *loss* ≠ small *gradient into the bank*. Net: the CE-vs-KD causal split is genuinely unresolved across our own findings ([[mmllm-output-kd-retention-verdict]]: architectural/not-loss; vs [[mmllm-localmult-broke-distillation]] + [[mmllm-real-distillation-works]]: teacher/KD necessary). **Do not assume either.**

**Teacher LR is correct, NOT throttled (correcting an earlier "stale memory" claim):** [[mmllm-localmult-broke-distillation]] is *not* stale — the bird deploys its prescribed fix. `LOCAL_MULT=0.05` is the **base**; the bird also sets `LOCAL_LR_WAKE=20.0` → effective teacher LR = **1.0 at wake** (local bank learns the round fast = strong teacher), settling to 0.05 at sleep. So the teacher is strong and the full wake/sleep LB regime is what's running. (Agent traced `_vlocal_lr = LOCAL_MULT·_wake_sleep(step)` correctly but didn't evaluate the wake multiplier → wrongly called it a "weaker teacher.")

**Distill-from-smarter-models channel:** CE-on-distilled-DATA (frontier synthetic/traces — WRAP, pre-released corpora) is a strong, independently-evidenced way to inject smarter-teacher knowledge — recommended on its own merits, **complementary to** (not a proven replacement for) the local→net KD.

---

## 7. Cross-cutting tensions to manage

- **Overtrain × low precision:** post-hoc-quantization damage grows with training tokens → use **QAT, not PTQ**, on the bank if overtraining.
- **Quality-ordered data × LR decay collide** (best data lands when LR≈0) → flatten decay if curriculum-ordering — dovetails with wake/sleep LR work.
- **µP is dense-theory** → untested against router/PKM; coordinate-check.
- **Continual / anti-forgetting:** constant-then-decay (no re-warm) forgets less; AdEMAMix and Data-Mixing-Laws have explicit anti-forgetting results → relevant to trunk-drift-as-forgetting.

## 8. Suggested sequencing (all reversible, all on branches)

1. Zero-risk adds first: native compute hygiene, EMA/LAWA, aux-loss-free router bias. (No trunk reset; seed from f256 `RB(100)`.) [Mobahi round-cap dropped — §6 resolved it as a non-issue.]
2. A/B Muon vs tuned-AdamW on a fresh-trunk branch; carry WSD + stability stack on that branch.
3. Data pipeline: domain-matched quality classifier + online mixing + per-domain repetition.
4. Spike MTP n≈8 byte heads (sequential) with a retention-probe gate.
5. Only then weigh the NEXT-GEN bets (patching layer, linear backbone) — explicit decision.

## 9. Sourcing caveat

WebFetch was permission-blocked in places; some figures are from arXiv abstracts + secondary sources, and a few 2025/2026 arXiv IDs (byte-distillation 2602.01007, infinite-compute, mixture-scaling, "Depth Delusion") are strong-but-not-independently-replicated — re-read primaries before citing formally.
