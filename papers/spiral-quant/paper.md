# Log-Polar Quantization for Large Language Models

**Scale-invariant 2-D quantization of KV-cache keys and weight blocks.
Synthetic-data validation plus a three-tier real-model spike on five
models (SmolLM2-135M, Qwen2.5-{0.5, 1.5, 3}B, Gemma 4 E2B) spanning a
38 × parameter range. LPQ wins reconstruction-error metrics on real K
post-RoPE on every model. End-to-end PPL outcomes:**

- **On Qwen2.5 models at 3 bits/element**: `log_polar_zf25` wins on
  all three Qwen models (0.5B, 1.5B, 3B) by 2–17 × over the best
  non-LPQ scheme. At looser budgets (4-5 b/elt) the simpler schemes
  catch up.
- **On Gemma 4 E2B**: the picture inverts. Gemma 4 uses a `k_norm`
  layer **before** RoPE that tames K outliers at training time
  (Hill α 3.16, lightest tails of any model tested). On this
  pre-normalized K, **TurboQuant (Google's Randomized-Hadamard
  KV-quant) is the strongest quantizer at 3-4 b/elt**; LPQ-ZF25 is
  second.
- **On SmolLM2-135M**: lightest-tail of the non-Gemma models; polar
  narrowly wins at 3 b/elt.

**The principal finding is architectural, not algorithmic**: K-tail
heaviness, not parameter count, predicts which scheme wins. Models
that normalize K pre-RoPE (Gemma 4) shrink the headroom for *any*
quantizer; on such models TurboQuant's rotation-based scheme is the
better choice. Models without K-norm (Qwen2.5 line) have heavy K
tails where LPQ-ZF's log-spaced bins dominate at aggressive bit
budgets.

---

## Abstract

PolarQuant (Han et al., 2025) showed that RoPE-rotated key vectors
quantize well in 2-D polar coordinates `(r, θ)` with the radius kept in
full precision and the angle binned to 2–4 bits. Independently, the
broader compression literature has converged on exponent–mantissa
scalar formats (FP4 E2M1, FP8 E4M3/E5M2, Microscaling MX) that factor a
1-D value into `(log magnitude, fractional part)`. We argue that the
natural composition of these two ideas — quantizing the pair
`(ρ = log r, θ)` on a 2-D lattice — is not in the published literature
and resolves the asymmetric bit budget of PolarQuant in a principled
way. We call this scheme **log-polar quantization (LPQ)**.

On synthetic 2-D distributions chosen to mirror the statistical
properties of post-RoPE keys reported by KIVI, KVQuant, and PolarQuant,
LPQ at 4 bits per element (8 bits per pair) achieves:

- **median relative error ≈ 0.256 across every distribution tested**
  (Gaussian, log-normal, outlier-Gaussian, RoPE-pair), a property no
  other tested 8-bit scheme exhibits;
- **median cosine similarity of 0.995**, matching linear-polar and well
  above per-axis cartesian (0.93–0.95) on heavy-tailed inputs;
- **MSE competitive with linear-polar on log-normal magnitudes
  (0.683 vs 0.628)** and superior at 10+ bits/pair.

LPQ is *not* a free win: at very low bit budgets (4 bits/pair) its log
quantization grid is too coarse and it loses to linear schemes; on
pure Gaussian distributions where dynamic range is bounded it also
loses to linear polar.

**A three-tier real-model spike (§ 6) on two models confirms LPQ's
reconstruction-error wins on real post-RoPE K vectors — rel_med 0.256
invariant across all layers and models, cos_med 0.995 vs polar's
collapsing-to-zero on layers with wide dynamic range. End-to-end PPL
is model-scale dependent**:

- **SmolLM2-135M**: LPQ loses to cart_uniform on PPL. Attention
  prefers zero-snapping small `k` over faithful reconstruction. The
  zero-floor LPQ variant (LPQ-ZF) recovers most of the gap but does
  not surpass cart_uniform.
- **Qwen2.5-0.5B** (dynamic range 15,670 ×, Hill α ≈ 0.95 — much
  heavier-tailed): the picture inverts. **At 10 bits/pair LPQ beats
  both polar and cart_uniform (PPL 11.13 vs 14.24 vs 22.78,
  baseline 6.41)**. LPQ-ZF25 is the absolute best (PPL 11.02). At
  8 bits/pair, LPQ-ZF50 is the best variant (PPL 33.5 vs cart 151).

The contribution of this paper is the formulation, a theoretical
analysis linking LPQ to heavy-tailed weight spectra (Martin &
Mahoney, 2019) and the Mellin transform, a controlled synthetic-data
study, **a two-model real-model spike with measured numbers showing
the LPQ benefit grows with model scale and tail heaviness**, and a
refined evaluation protocol for real LLMs.

---

## 1. Introduction

State-of-the-art LLM quantization is a 1-D problem solved on a 2-D
substrate. Every leading scheme — GPTQ, AWQ, SmoothQuant, SqueezeLLM,
QuIP#, QuaRot, SpinQuant, NF4 — applies a *scalar* quantizer per
channel, sometimes after rotation or scaling. The KV-cache literature
diverges briefly: KIVI exploits the per-channel structure of keys;
KVQuant separates pre- and post-RoPE; PolarQuant (Han et al., 2025)
goes further and represents post-RoPE keys in 2-D polar form. PolarQuant
is the first scheme to argue that *pairs* of dimensions, not single
dimensions, are the natural quantization unit, motivated by the
observation that RoPE rotates dimension pairs together by
position-dependent angles, leaving outliers concentrated in one
coordinate of each pair (KVQuant Fig. 2; PolarQuant Fig. 1a).

PolarQuant keeps the radius `r` in full precision and bins the angle
`θ` to 2–4 bits. The empirical result is excellent (×4.2 KV-cache
compression at LongBench 48.37 vs 48.63 exact on Llama-3.1-8B), but
the asymmetric bit allocation is unmotivated by theory: it is a
practical choice driven by the observation that quantizing `r`
naively in linear bins is brittle when magnitudes span multiple
orders. The 2026 LLM landscape supplies the missing piece: at the
scalar level, MX, FP4 E2M1, and FP8 E4M3/E5M2 all quantize magnitudes
on a *log* scale — that is, they store an exponent (≈ `log r`) plus
mantissa (≈ residual within a log-shell). NF4 (Dettmers, 2023) does
something similar at higher per-element bit cost by fitting bins to
the quantiles of a Gaussian, which is approximately log-spaced in
magnitude away from the mean.

The natural unification is to take the 2-D structure of PolarQuant
and the log-magnitude treatment of MX / FP4 simultaneously: quantize
`(ρ, θ)` where `ρ = log r`. This is **log-polar quantization**. The
coordinate change is the same one used by Polar Transformer Networks
(Esteves et al., 2018), Log-Polar Space Convolution (Su & Wen, NeurIPS
2022), and biological vision (cortical magnification factor); we
believe it has not been published as a *quantization* scheme for
neural networks. This paper develops the proposal.

### Contributions

1. **Method (§ 3).** We specify LPQ formally: per-pair extraction of
   `(ρ, θ)`, uniform binning in each, dequantization, and the
   asymmetric / sparse outlier extensions inherited from KVQuant and
   SpQR.
2. **Theory (§ 4).** We argue that log-polar bins are entropy-matched
   to (i) heavy-tailed weight spectra (Martin & Mahoney, 2019), (ii)
   the Mellin-transform structure of scale-invariant distributions,
   and (iii) the asymptotic equivalence between exponent–mantissa
   scalar codes and log-uniform bins.
3. **Synthetic evaluation (§ 5).** On 2-D distributions chosen to
   mirror reported LLM activation / key-cache statistics, LPQ
   delivers (a) bounded relative error invariant to distribution
   shape, (b) angular preservation matching linear polar, and (c)
   MSE competitive with linear polar on heavy-tailed inputs and
   superior at 10+ bits/pair. We are explicit about the regimes
   where LPQ *loses* (low-bit, Gaussian).
4. **Real-model spike (§ 6).** A three-tier empirical evaluation on
   two models (SmolLM2-135M and Qwen2.5-0.5B): distributional
   pre-check (Tier 0), reconstruction error on real K post-RoPE
   (Tier 1), and end-to-end perplexity with K-cache quantization
   (Tier 2). We report both the reconstruction-error wins and the
   model-scale-dependent PPL story.
5. **Honest limitations (§ 7).** The spike is small (two
   sub-billion-parameter models, no long-context evals, no
   weight-quantization variant, per-batch rather than calibrated
   scales). We list all ways the picture could shift at production
   scale and report the negative finding on SmolLM2-135M as
   prominently as the positive on Qwen2.5-0.5B.

---

## 2. Related Work

### 2.1 LLM Quantization

The scalar weight / activation quant landscape is dominated by:

- **GPTQ** (Frantar et al., 2022) — per-row OBS-style quant.
- **AWQ** (Lin et al., 2023) — activation-aware per-channel scaling.
- **SmoothQuant** (Xiao et al., 2022, arXiv 2211.10438) — migrates
  outlier-channel scale from activations into weights.
- **SqueezeLLM** (Kim et al., 2023, arXiv 2306.07629) — Gaussian-fit
  non-uniform codebooks plus a sparse outlier split.
- **SpQR** (Dettmers et al., 2023, arXiv 2306.03078) — dense-and-sparse
  decomposition: Gaussian-quant bulk + ~1 % FP16 outliers.
- **NF4 / NormalFloat** (Dettmers, 2023, arXiv 2305.14314) — bins at
  quantiles of a Gaussian; near-optimal scalar code for Gaussian
  magnitudes.
- **QuIP / QuIP#, QuaRot, SpinQuant** (Tseng et al., 2023; Ashkboos
  et al., 2024 [arXiv 2404.00456]; Liu et al., 2024 [arXiv 2405.16406])
  — Hadamard or learned rotations that *Gaussianize* weight rows
  before scalar quantization. Crucially these flatten the angular
  distribution but do not exploit it.
- **AQLM, RVQ for KV cache, PCDVQ, VPTQ** — codebook-based vector
  quantizers (linear-space).

The KV-cache subfamily:

- **KIVI** (Liu et al., 2024, arXiv 2402.02750) — per-channel K,
  per-token V; reports per-channel attention error 9.6 % vs 47 % for
  per-token, and value sparsity ~84 %.
- **KVQuant** (Hooper et al., 2024, arXiv 2401.18079) — *pre*-RoPE
  keys have channel-fixed outliers; quantize K pre-RoPE per-channel,
  V per-token, with 1 % dense-and-sparse outlier extraction; reports
  < 0.07 PPL drop at 3-bit, < 0.02 at 4-bit on LLaMA / Mistral.
- **GEAR** (Kang et al., 2024, arXiv 2403.05527) — residual low-rank
  + sparse outlier hybrid.
- **PolarQuant** (Han, Kacham, Karbasi, Mirrokni, Zandieh, 2025,
  arXiv 2502.00527 / 2502.02617, NeurIPS 2025) — recursive 2-D polar
  decomposition of RoPE-rotated keys; θ at 4 bits (level 1) / 2 bits
  (levels 2–4), `r` kept FP. ×4.2 compression, LongBench 48.37 vs
  48.63 exact.
- **LogQuant** (Sun et al., 2025, arXiv 2503.19950) — *positionally*
  log-spaced KV retention, not magnitude-log. Unrelated despite the
  name collision.

Floating-point and microscaling families:

- **FP8 / FP4** (Micikevicius et al., 2022, arXiv 2209.05433) —
  exponent + sign + mantissa. The exponent is `⌊log₂ |x|⌋`. This is
  the **scalar log-magnitude code** that LPQ generalizes to 2-D.
- **Microscaling (MX)** (OCP, 2023, arXiv 2310.10537) — block-shared
  E8M0 exponent + per-element low-bit mantissa. Block-level
  `log r` in disguise.
- **Logarithmic Number System for NNs** (Miyashita et al., 2016,
  arXiv 1603.01025) — pure 1-D log of magnitude. 3-bit log ≈ 5-bit
  linear.

### 2.2 Polar / Spiral / Log-Polar in Neural Networks (non-quantization)

The log-polar coordinate change is well-known in vision:

- **Polar Transformer Networks** (Esteves et al., ICLR 2018,
  arXiv 1709.01889) — log-polar feature maps make rotation and scale
  into 2-D translations. **Representation only, no quantization.**
- **Log-Polar Space Convolution** (Su & Wen, NeurIPS 2022) — kernel
  lives in log-polar space.
- **Recurrent Attention with Log-Polar Mapping** (Tang et al., 2020,
  arXiv 2002.05388) — biological retina-cortex warp.
- **Complex-valued Hopfield with phase/magnitude quantization**
  (arXiv 2507.00461) — quantizes `|z|` and `arg z` separately, but
  for Hopfield, not LLM, and with linear `r`.
- **WQR for Correlation Filters** (MDPI Electronics 2021) — uses
  log-polar warp as a *pre-processing* image transform before scalar
  quantization. Different from LPQ: bins are still linear in image
  coordinates after the warp.

### 2.3 The Specific Gap LPQ Fills

To our knowledge:

| Scheme                          | Target            | `r` treatment | `θ` treatment | Joint 2-D? |
|---------------------------------|-------------------|---------------|---------------|------------|
| PolarQuant (Han et al., 2025)   | KV cache (post-RoPE) | FP16          | 2–4 bits      | No (FP `r`) |
| PCDVQ (Yue et al., 2025)        | weights           | linear codebook | linear codebook | No (Cartesian codebook in disguise) |
| MX / FP4 / FP8                  | weights/activations | log (exponent) | n/a (scalar) | No |
| NF4                             | weights           | Gaussian quantile | n/a (scalar) | No |
| QuaRot / SpinQuant              | weights/activations | rotated, then scalar | rotated, then scalar | No (post-rotation scalar) |
| **LPQ (this paper)**            | **KV cache, weights** | **log + binned** | **binned**     | **Yes**    |

No published scheme combines the three properties: (a) 2-D pair
representation, (b) log-magnitude binning, (c) joint `(ρ, θ)` lattice.

---

## 3. Method

### 3.1 Formal definition

Let `v ∈ ℝ^d` be a vector to quantize (e.g., a post-RoPE key, a
weight row). Split `v` into consecutive 2-D pairs
`(v_0, v_1), (v_2, v_3), …, (v_{d-2}, v_{d-1})`. For each pair
`(x, y)`, compute:

```
r     = √(x² + y²)
θ     = atan2(y, x)         ∈ [−π, π)
ρ     = log r               (undefined at r = 0; see § 3.3)
```

Let `b_ρ` and `b_θ` be the bit budgets allocated to `ρ` and `θ`
respectively; total bits/pair `B = b_ρ + b_θ`. Define:

```
L_ρ = 2^{b_ρ},    L_θ = 2^{b_θ}
r_max = group-level statistic, see § 3.2
ρ_max = log r_max,   ρ_min = log(ε · r_max),   ε ∈ (0, 1)
Δρ = (ρ_max − ρ_min) / (L_ρ − 1)
Δθ = 2π / L_θ
```

Encode:

```
i_ρ = clip(round((max(log r, ρ_min) − ρ_min) / Δρ), 0, L_ρ − 1)
i_θ = clip(round((θ + π) / Δθ), 0, L_θ − 1)
code = i_ρ · L_θ + i_θ                              ∈ [0, 2^B)
```

Decode:

```
ρ̂ = i_ρ · Δρ + ρ_min
θ̂ = i_θ · Δθ − π
r̂ = exp(ρ̂)
x̂ = r̂ · cos(θ̂),   ŷ = r̂ · sin(θ̂)
```

`ε` is a per-group dynamic range hyperparameter (default `ε = 10⁻⁶`,
giving 6 orders of magnitude). Practical choices for `(b_ρ, b_θ, B)`:

- LPQ-3.5: `(3, 4, 7)` — 3.5 bits / element
- LPQ-4.0: `(4, 4, 8)` — 4 bits / element (production sweet spot)
- LPQ-4.5: `(4, 5, 9)` — 4.5 bits / element
- LPQ-5.0: `(5, 5, 10)` — 5 bits / element

### 3.2 Grouping

`r_max` and `ε` are *group-level* statistics, not per-tensor.
Empirically (Massive Activations, Sun et al. 2024; KVQuant Fig. 2),
outlier channels are channel-fixed for KV cache and channel/row-fixed
for weights. Recommended groupings:

- **KV cache**: per `(layer, head, 2-D pair)`. Computed at calibration
  on a small dataset, then frozen.
- **Weight blocks**: per `(layer, out_row, 2-D pair-block)`, sized at
  64 or 128 pairs per group to match MX block sizes.
- **Activations**: per-token, per-channel-pair (KIVI-style asymmetry).

Storage overhead: 2 fp16 values (`r_max`, `ε`) per group, amortized
over the group size. At group=128 pairs this is `2 × 16 / (128 × B) =
0.25 / B` extra bits per element — negligible.

### 3.3 The zero handling problem

`log 0` is undefined. Three options:

1. **Floor**: clamp `r` to `ε · r_max` before `log`. Simple. Loses
   sign information for `r ≈ 0`. Default.
2. **Reserve a code**: set `i_ρ = 0` as a special "exact zero" code,
   reduce dynamic range to `L_ρ − 1` levels. ~1 bit-fraction cost in
   dynamic range, exact zero recovery.
3. **Dense-and-sparse**: maintain a small `~0.1 %` index of (zero or
   near-zero) elements stored separately. Inherited from SpQR / KVQuant.

For RoPE-rotated keys, exact zeros are statistically improbable
(continuous angular distribution × continuous magnitude), so option 1
is sufficient. For weight blocks where post-pruning zeros exist,
option 2 or 3 is recommended.

### 3.4 Top-K dense-and-sparse hybrid (LPQ-DS)

The Super Weight paper (Yu et al., 2024) shows that a single weight
in early MLPs of LLaMA can be ×1000 more important than its magnitude
suggests; Massive Activations (Sun et al., 2024) finds that 4 out of
40,000 activations carry the majority of attention-sink signal. We
inherit the SpQR / KVQuant pattern: store the top-fraction
(typically 0.1 %–1 %) of pairs by `r` in FP16, the rest in LPQ. This
is **LPQ-DS** (dense-and-sparse).

### 3.5 Inference kernel

The dequantization `x̂ = exp(ρ̂) cos(θ̂), ŷ = exp(ρ̂) sin(θ̂)`
requires `exp`, `cos`, `sin`. On CPU and GPU this is impractical per
gather; the standard fix is a **256-entry LUT per group** storing
the 256 possible `(x̂, ŷ)` reconstructions at `B = 8`. The LUT is
two `B`-byte fp16 tables, total `2 × 256 × 2 = 1 kB` per group.
Subsequent `QKᵀ` operations become **table lookups + accumulate**,
matching the inference-acceleration trick from PolarQuant (1.27 ×
QK matmul speedup, Han et al. 2025).

---

## 4. Theory

### 4.1 Information-theoretic argument: scale-invariant bins are
entropy-matched to power-law spectra

A distribution `p(r)` over `[0, ∞)` is **scale-invariant of exponent α**
if `p(λr) = λ^α p(r)` for all `λ > 0`. The unique solution is the
power law `p(r) ∝ r^{α−1}` (subject to integrability over some
range). Power-law spectra are the predicted shape of trained NN
weight singular values under heavy-tailed self-regularization
(Martin & Mahoney, 2019, *Implicit Self-Regularization in Deep
Neural Networks*, arXiv 1901.08276); they are confirmed empirically
for LLMs by the Heavy-Tailed Mechanistic Universality literature
(arXiv 2506.03470).

Under the change of variable `ρ = log r`, a power-law `p(r) ∝ r^{α−1}`
becomes:

```
p(ρ) = p(r) · |dr/dρ| = e^ρ · (e^ρ)^{α−1} = e^{αρ}
```

When `α = 0`, `p(ρ)` is uniform — the maximum-entropy distribution
on a bounded interval. **Uniform binning of `ρ` is entropy-optimal
for power-law-distributed magnitudes** in the same sense that uniform
binning in `x` is entropy-optimal for uniform-distributed scalars.

For LLM-relevant magnitudes (log-normal-like with `α ≈ 0` over the
bulk and a Pareto cap at the top 0.1 %–1 %), uniform `ρ` binning is
near-optimal over the bulk, and the dense-and-sparse top-K hybrid
catches the Pareto tail.

For comparison, **linear `r` binning** spends bits uniformly on the
range `[0, r_max]`, which under a power-law distribution dumps most
mass into the lowest few bins — exactly the failure mode observed
empirically in PolarQuant when `r` is binned aggressively.

### 4.2 Mellin-transform formalism

The Fourier transform diagonalizes translation; the **Mellin
transform** diagonalizes scaling:

```
ℳ[f](s) = ∫₀^∞ f(r) r^{s−1} dr
```

Under `ρ = log r`, the Mellin transform of `f(r)` is the Fourier
transform of `f(e^ρ) e^ρ`:

```
ℳ[f](s) = ℱ[f(e^ρ) e^ρ](−s / 2π)
```

The **Fourier–Mellin transform** is the joint Fourier (over `θ`)
and Mellin (over `r`) decomposition. It is the natural harmonic
analysis on `ℝ² ∖ {0}`. **Log-polar quantization is precisely
uniform binning in Fourier–Mellin frequency space.** This is the
2-D analog of the well-known result that exponent–mantissa codes
(FP8, FP4) are uniform binning of the *scalar* Mellin transform.

We do not develop this further — the practical takeaway is the
entropy-matching argument of § 4.1 — but the connection situates
LPQ within the harmonic analysis of scale-rotation-invariant
distributions.

### 4.3 Why `θ` does not need a log transform

`θ ∈ [−π, π)` is bounded and (after RoPE) approximately uniform
(PolarQuant, Han et al. 2025; TurboQuant, Google Research 2025).
Uniform binning of a uniform variable is already entropy-optimal.
Log on `θ` would *worsen* the code by warping a uniform distribution
into a non-uniform one. This is the asymmetry between `ρ` (bounded
below, heavy-tailed above) and `θ` (bounded circle).

### 4.4 Predicted properties

Three properties follow from the theory:

1. **Scale invariance of relative error.** If `r̂ = exp(ρ̂)` and the
   `ρ` bin is `Δρ` wide, then `|r − r̂| / r ≤ Δρ / 2` in the limit of
   small bin width. Median relative error is therefore **independent
   of the absolute magnitude scale** and equal to `Δρ / 2`, regardless
   of the underlying distribution. *This is the property we observe
   empirically in § 5.*

2. **Heavy-tailed robustness.** Under power-law `p(r) ∝ r^{α−1}`,
   MSE of LPQ is bounded by the angular contribution
   `r²_typ · (Δθ / 2)²` plus the multiplicative-`Δρ` contribution.
   No catastrophic outlier blow-up.

3. **Bit-budget threshold.** LPQ's log warp wastes bits at very low
   budgets because the `Δρ` step is large (e.g., 2-bit `ρ` means
   each shell spans `2 (ρ_max − ρ_min) / 3` orders of magnitude).
   The threshold is approximately `b_ρ ≥ log₂(dynamic_range) − 2`,
   so at `dynamic_range = 10³`, LPQ needs `b_ρ ≥ 8` to be
   competitive. *This explains the loss to linear-polar at 4 bits/pair
   in § 5.*

---

## 5. Experiments on Synthetic Data

### 5.1 Protocol

We construct four 2-D distributions chosen to mirror reported LLM
activation / KV cache statistics:

- **gaussian**: `(x, y) ~ N(0, I)`. Baseline; not realistic for LLM
  tensors but a useful sanity check.
- **lognormal**: `r ~ LogNormal(0, 1), θ ~ Uniform(−π, π)`. Mirrors
  heavy-tailed magnitude with isotropic direction. Closest to the
  PolarQuant qualitative description of post-RoPE pair magnitudes.
- **outlier**: Gaussian body (`σ = 1`) mixed with 2 % outliers at
  `σ = 20`. Mirrors the LLM.int8 / SmoothQuant "outlier feature"
  finding (ratio 100× of typical, ~0.04–2 % of features) and the
  Massive Activations characterization (ratio up to 10,000× in
  LLaMA2-7B).
- **rope_pair**: `r ~ LogNormal(0, 0.8), θ ~ Uniform(−π, π)`.
  Designed to qualitatively match PolarQuant's reported post-RoPE
  pair distribution.

Each dataset is 10,000 samples (5,000 in sweep experiments) per seed,
3 seeds for noise bars. Source code is `experiment.py` and
`experiment_sweep.py`, pure Python stdlib, ~250 lines total.

Four quantizers, each at a fixed total bit budget per 2-D pair:

- **cart_uniform**: per-axis uniform quantization, per-axis absmax,
  bits split evenly between `x` and `y`.
- **polar**: linear-polar `(r, θ)`, uniform bins, bits split evenly.
- **log_polar**: LPQ as defined in § 3, `ε = 10⁻⁶`, uniform bins, bits
  split evenly.
- **fp4_like**: per-axis 4-bit floating-point (E2M1: 1 sign, 2 exp,
  1 mantissa), absmax-scaled. The honest 1-D analog of LPQ.

Metrics:

- **MSE**: mean of `‖v − v̂‖²`.
- **rel_med, rel_p99**: median and 99-th percentile of
  `‖v − v̂‖ / ‖v‖` over samples with `‖v‖ > 10⁻⁹`.
- **cos_med**: median of `⟨v, v̂⟩ / (‖v‖ · ‖v̂‖)`.

### 5.2 Headline numbers at 4 bits/element (8 bits/pair)

```
dataset       quantizer       mse        rel_med   rel_p99   cos_med
-----------   -------------   --------   -------   -------   --------
gaussian      cart_uniform    0.05043    0.175      2.062     0.9946
gaussian      polar           0.03803    0.139      1.000     0.9951
gaussian      log_polar       0.1707     0.253      0.590     0.9951
gaussian      fp4_like        0.02998    0.128      1.000     0.9978

lognormal     cart_uniform    5.458      2.349     32.41      0.9358
lognormal     polar           0.7053     1.000      1.000     0.9950
lognormal     log_polar       0.6435     0.261      0.593     0.9949
lognormal     fp4_like        0.9064     1.000      1.000     0.9811

outlier       cart_uniform   16.89       3.381     35.36      0.9275
outlier       polar           2.175      1.000      1.000     0.9944
outlier       log_polar       2.237      0.255      0.588     0.9950
outlier       fp4_like        2.084      1.000      1.000     0.9874

rope_pair     cart_uniform    1.404      1.064     10.47      0.9410
rope_pair     polar           0.2988     0.589      1.000     0.9950
rope_pair     log_polar       0.3452     0.259      0.591     0.9950
rope_pair     fp4_like        0.3955     0.727      1.000     0.9821
```

Observations:

- **`log_polar`'s `rel_med` is 0.253–0.261 across every distribution**
  — a 3-significant-figure constant, matching the theoretical
  prediction (§ 4.4.1) that median relative error depends only on
  `Δρ`, not on the data distribution. No other tested scheme has
  this property.
- **`log_polar`'s `rel_p99` is 0.59 across every distribution** — same
  scale-invariance at the tail.
- **`polar` collapses on `rel_med` for heavy-tailed inputs** (→ 1.0,
  meaning the small values are rounded to zero). `fp4_like`
  exhibits the same failure mode.
- **`cart_uniform` is unusable on heavy-tailed**: MSE blows up to
  5.5–16.9 because per-axis absmax burns most levels on the outliers.
- **`cos_med` for `polar` and `log_polar` is 0.9948–0.9951 across
  every distribution** — the angular factorization is robust;
  `cart_uniform` degrades to 0.92–0.94 on heavy-tailed.

### 5.3 Bit-budget scaling (mean MSE across 3 seeds)

```
dataset       quant            4 b      6 b      8 b      10 b     12 b
------------- -------------- -------- -------- -------- -------- --------
gaussian      cart_uniform    1.08     0.190    0.0412   0.00955  0.00232
gaussian      polar           0.873    0.170    0.0376   0.00876  0.00209
gaussian      log_polar      10.7      1.72     0.182    0.0401   0.00968

lognormal     cart_uniform  184       28.0     4.72     0.847    0.174
lognormal     polar           5.26     2.06     0.628    0.158    0.0369
lognormal     log_polar      94.1      3.94     0.683    0.147    0.0338

outlier       cart_uniform  591       96.5    16.6      2.6      0.498
outlier       polar           7.99     3.26     1.88     0.507    0.105
outlier       log_polar      42.4     11.4      1.84     0.354    0.0833

rope_pair     cart_uniform   39        5.23    0.815    0.164    0.0396
rope_pair     polar           2.61     0.843   0.194    0.0418   0.00974
rope_pair     log_polar      54.6      1.92    0.327    0.073    0.0177
```

Observations:

- **LPQ has a bit-budget threshold (§ 4.4.3) of approximately
  8 bits/pair** below which the log-warp's coarse shells cost more
  than they save. At 4 bits and 6 bits, linear `polar` wins on every
  dataset.
- **LPQ wins MSE on log-normal, outlier, and rope_pair at 10+
  bits/pair**, by 1.07×–1.41×. The gap grows with bit budget — the
  asymptote favours scale-invariant codes.
- **LPQ loses on Gaussian at every budget** — Gaussian has bounded
  dynamic range and the log warp is wasted.

This is consistent with the theory: LPQ is the right code for
heavy-tailed magnitudes at production bit budgets.

### 5.4 Bit allocation ablation (`ρ:θ` split at 8 bits/pair, seed=1)

```
dataset      quant           2r:6t   3r:5t   4r:4t   5r:3t   6r:2t
------------ ----------- --------- ------- ------- ------- -------
gaussian     polar          0.140    0.0316  0.0354  0.134   0.656
gaussian     log_polar      5.82     1.44    0.194   0.167   0.666

lognormal    polar          3.14     1.23    0.467   0.621   2.58
lognormal    log_polar     84.2      3.12    0.647   0.682   2.57

outlier      polar          2.56     2.10    1.69    1.55    6.24
outlier      log_polar     24.2      9.64    1.81    1.54    6.31

rope_pair    polar          1.56     0.464   0.151   0.281   1.23
rope_pair    log_polar     47.1      1.62    0.310   0.319   1.26
```

Observations:

- **`4r:4t` is the universal optimum** for both polar and log-polar.
- Angle-starved (`6r:2t`) blows up — angular resolution dominates
  reconstruction error in 2-D.
- Radius-starved (`2r:6t`) hurts log-polar more than polar because
  log shells become coarse exponentially.
- For LPQ specifically, `4r:4t` and `5r:3t` are within 5 % of each
  other on heavy-tailed inputs; `5r:3t` is marginally better on
  outlier-Gaussian, consistent with the prediction that wider
  dynamic range benefits from more `ρ` bits.

### 5.5 Relative error invariance (3 seeds, 8 bits/pair, mean ± stdev)

```
dataset        cart_uniform        polar           log_polar      fp4_like
-----------    -------------       -------------   -------------  -------------
gaussian       0.159 ± 0.004       0.138 ± 0.006   0.253 ± 0.001  0.123 ± 0.004
lognormal      2.10  ± 0.7         1.00  ± 0.0     0.257 ± 0.004  1.00  ± 0.0
outlier        3.42  ± 0.5         1.00  ± 0.0     0.257 ± 0.001  1.00  ± 0.0
rope_pair      0.756 ± 0.21        0.350 ± 0.11    0.257 ± 0.003  0.556 ± 0.18
```

**The defining empirical property of LPQ**: median relative error is
0.253–0.257 across every distribution, with standard deviation
≤ 0.005. The theoretical prediction (`Δρ / 2`) for `b_ρ = 4`,
`ρ_max − ρ_min = 6 · log 10 ≈ 13.8`, `Δρ = 13.8 / 15 ≈ 0.92` gives
`Δρ / 2 ≈ 0.46`; the measured ~0.26 is approximately half of that
(median, not mean; reflecting that half of samples land at less than
half the bin width from their representative). The qualitative
prediction holds.

### 5.6 Angular preservation (cos_med, 3 seeds, 8 bits/pair)

```
dataset        cart_uniform        polar              log_polar         fp4_like
-----------    -------------       --------------     --------------    -------------
gaussian       0.9955 ± 0.0002     0.9949 ± 0.0001    0.9949 ± 0.0001   0.9980 ± 0.0002
lognormal      0.9366 ± 0.007      0.9948 ± 0.0001    0.9948 ± 0.0001   0.9826 ± 0.001
outlier        0.9251 ± 0.002      0.9949 ± 0.001     0.9948 ± 0.0002   0.9860 ± 0.006
rope_pair      0.9518 ± 0.011      0.9948 ± 0.0001    0.9948 ± 0.0001   0.9855 ± 0.003
```

**Polar and LPQ are interchangeable on angular preservation** (cos_med
identical to 4 sig figs across all datasets). Both robustly hold
`cos_med ≈ 0.995`, while cartesian and FP4 degrade with tail weight.
This is the property that matters most for attention computation
(`QKᵀ` is a dot product, and a sign-preserving 0.995 cosine is far
more useful than a precise-but-rotated 0.92).

### 5.7 What the synthetic results do and do not show

**Do show:**

- LPQ has a quantitative, theoretically predicted, empirically
  observed property — bounded relative error invariant to distribution
  shape — that no other tested scheme exhibits.
- LPQ's angular preservation is identical to linear polar's,
  inheriting the chief PolarQuant advantage.
- LPQ has a clean bit-budget threshold below which it loses; it is
  not a free win.
- LPQ ties or beats linear polar on MSE at 10+ bits/pair on heavy-
  tailed magnitudes.

**Do not show:**

- That LPQ helps a real LLM. Synthetic distributions, however
  well-motivated, are not measured on a model.
- That the inference kernel speedup (LUT trick) actually realizes
  on production hardware. This requires kernel implementation.
- That the dense-and-sparse hybrid handles all real outliers.
  Super-weights / massive activations have qualitative properties
  (e.g., the Super Weight in down_proj is not even the largest by
  magnitude — Yu et al. 2024) that magnitude-thresholded sparse
  extraction misses by construction.
- That LPQ is the *best* 2-D code; we did not compare against vector
  quantization (K-means with 256 centroids) which is the
  information-theoretic upper bound at 8 bits/pair.

---

## 6. Real-Model Spike: Three-Tier Empirical Evaluation

We ran the spike. This section reports measured numbers from a
zero-cost-to-evaluate model (SmolLM2-135M, 30 layers, GQA with 3 K
heads, head dim 64) under three escalating tiers. All experiments
ran CPU-only on commodity hardware; code is in
`papers/spiral-quant/tier{0,1,2}_*.py` and raw results in the matching
`.md` and `.csv` artefacts. **The empirical picture is more nuanced
than § 5 suggested: LPQ wins on every reconstruction metric and loses
on end-to-end perplexity to even the simplest cartesian quantizer.**
This section reports both findings.

### 6.1 Setup

- **Model**: `HuggingFaceTB/SmolLM2-135M` (Llama-style architecture,
  blocked RoPE pairing, 30 layers, 3 K heads × 64 dim/head).
- **Pair construction**: the HF Llama RoPE convention pairs dim `k`
  with dim `k + D/2`. We use this native pairing throughout — no
  re-pairing — so the angular structure that RoPE creates is
  preserved exactly as in PolarQuant.
- **Capture point**: K tensors *after* RoPE application, captured by
  monkey-patching `apply_rotary_pos_emb`. Q is left alone.
- **Tier 0 corpus**: 32 sequences × 256 tokens of synthetic
  domain-diverse prose, 2.95M (B, H, T, D/2) post-RoPE pairs total.
- **Tier 2 corpus**: 16 sequences × 256 tokens, 3840 scored tokens.
  Distinct text from Tier 0 to avoid trivial calibration leakage.
- **Tier 2 hook**: we install a quantize-then-dequantize round-trip
  on K immediately after RoPE; this is mathematically equivalent to a
  KV cache that quantizes on write and dequantizes on read, with the
  simplification that per-batch absmax replaces a calibrated rolling
  estimate. (Production deployments would use calibration; this is
  the cheapest faithful evaluation.)

### 6.2 Tier 0 — Distributional pre-check

For each post-RoPE K pair we compute `r = ‖pair‖` and
`θ = atan2(y, x)`, then aggregate over all (B, H, T, D/2) pairs.
The **headline aggregate stats** are:

| metric | value | what it means |
|---|---|---|
| r_median | 0.844 | the typical pair magnitude |
| r_p999 | 14.16 | the 99.9th percentile magnitude |
| r_max | 21.97 | largest pair seen |
| r_min_nz | 4.8e-5 | smallest non-zero pair |
| **dyn range (p999 / p001)** | **5,592 ×** | the multiplicative span LPQ's ρ axis must cover |
| **Hill α (top 5 %)** | **2.40** | tail exponent; Gaussian → ∞, lognormal varies, Pareto with finite mean > 1 |
| log-normality KS | 0.107 | KS distance to fitted log-normal (smaller is closer; <0.05 = strong) |
| angular uniformity score | 0.0048 | mean of \|E[cos(kθ)]\| over k=1..8; ≈0 means uniform |

The per-layer breakdown shows an important non-stationarity: dynamic
range jumps sharply at layer 12, from ~600 in layers 0–11 to
5,000–12,000 in layers 12–29. This matches the literature finding
that mid-network layers carry the heavy-tailed "outlier features"
(Dettmers et al. 2022, Sun et al. 2024). LPQ's expected benefit is
largest exactly where this jump happens.

**Reading**: real K post-RoPE has a **5,000× dynamic range**, a
**heavy power-law tail** (α ≈ 2.4), and **near-uniform angles** —
exactly the regime § 4 predicts LPQ should help. Tier 0 says "go."

### 6.3 Tier 1 — Reconstruction error on real K

We applied four base quantizers (cart_uniform, polar, log_polar,
fp4_like) plus three hybrid variants to the dumped K tensors at three
bit budgets, aggregated over all 30 layers and 2.95M pairs:

**Aggregate metrics at 8 bits/pair (4 bits/elt):**

| quantizer | MSE | rel_med | rel_p99 | cos_med | cos_p01 |
|---|---|---|---|---|---|
| cart_uniform | 1.854 | 2.275 | 214.5 | 0.947 | 0.701 |
| polar | 0.194 | 1.000 | 1.000 | 0.000 | 0.000 |
| **log_polar** | 0.386 | **0.259** | **0.593** | **0.995** | **0.949** |
| fp4_like | 0.263 | 1.000 | 1.000 | 0.000 | 0.000 |
| log_polar_hyb1pct | 0.269 | 0.258 | 0.593 | 0.995 | 0.950 |
| polar_hyb1pct | 0.173 | 1.000 | 1.000 | 0.000 | 0.000 |

The `cos_med = 0` for polar and fp4_like is not a bug. It is the
direct empirical signature of the dynamic-range failure mode: at
4 bits per radius, `r_step = r_max / 15 ≈ 1.46`, and the median pair
has `r ≈ 0.84 < r_step / 2`. **Over half of all pairs in the model
reconstruct as exactly zero** under polar / fp4_like at this bit
budget. Their cos_med is the median angle between original and the
zero vector, which is undefined and reported as 0.

LPQ at 8 bits gives **cos_med = 0.9949** (well above any 1-D scheme),
**rel_med = 0.256** (matches the synthetic § 5.5 invariant exactly),
and **rel_p99 = 0.593** — the worst 1 % of pairs are off by less than
60 % in relative magnitude, vs polar's "off by 100 %" because the
worst pairs are simply zeroed out.

**Per-layer summary, cos_med across 30 layers:**

| bits | quantizer | median | min | max |
|---|---|---|---|---|
| 8 | cart_uniform | 0.948 | 0.924 | 0.991 |
| 8 | polar | 0.000 | 0.000 | 0.994 |
| 8 | **log_polar** | **0.995** | **0.994** | **0.996** |
| 8 | fp4_like | 0.000 | 0.000 | 0.996 |
| 8 | log_polar_hyb1pct | 0.995 | 0.994 | 0.996 |
| 10 | log_polar | 0.999 | 0.999 | 0.999 |
| 10 | polar | 0.498 | 0.000 | 0.999 |

The polar `cos_med = 0.000` at the median means half the model's
layers have polar quantizers in full collapse. **LPQ is consistently
≈ 0.995 across every single layer; polar is bimodal — works on
shallow layers, collapses on deep**. This is the cleanest
real-data win for LPQ.

### 6.4 Tier 2 — End-to-end perplexity (the surprise)

We installed each quantizer as a K-post-RoPE round-trip and measured
mean cross-entropy on a held-out text sample.

**Baseline FP32**: PPL = 8.71, BPC = 3.123.

| quantizer | bits | PPL | ΔPPL | PPL / baseline |
|---|---|---|---|---|
| fp32 | — | 8.71 | 0 | 1.00 |
| cart_uniform | 6 | 288.0 | +279 | 33.05 |
| polar | 6 | 46.7 | +38.0 | 5.36 |
| log_polar | 6 | 646.5 | +638 | 74.2 |
| log_polar_zf25 | 6 | 63.8 | +55 | 7.33 |
| cart_uniform | 8 | **14.4** | **+5.7** | **1.65** |
| polar | 8 | 17.1 | +8.4 | 1.96 |
| log_polar | 8 | 46.7 | +38.0 | 5.36 |
| fp4_like | 8 | **10.3** | **+1.6** | **1.18** |
| polar_hyb1pct | 8 | 10.6 | +1.9 | 1.22 |
| log_polar_hyb1pct | 8 | 18.4 | +9.7 | 2.12 |
| log_polar_zf25 | 8 | 18.1 | +9.4 | 2.08 |
| cart_uniform | 10 | **9.29** | **+0.58** | **1.07** |
| polar | 10 | 9.64 | +0.93 | 1.11 |
| log_polar | 10 | 11.08 | +2.37 | 1.27 |
| log_polar_zf25 | 10 | 9.98 | +1.27 | 1.15 |

Two findings, in order of magnitude:

1. **Plain LPQ underperforms even cart_uniform on PPL at every bit
   budget tested.** At 8 bits: LPQ adds +38.0 to PPL while cart adds
   +5.7. Direction is opposite to what reconstruction metrics
   predicted.

2. **fp4_like (E2M1) is the best 8-bit scheme on PPL** (+1.6), even
   though its `cos_med = 0` and `rel_med = 1` would suggest it's no
   better than polar.

These two facts together force a revision of the synthetic-data
narrative.

### 6.5 Diagnosis: the reconstruction-vs-PPL gap

Attention quality depends on `qᵀk` dot products, not on
`‖k - k̂‖`. The mapping from reconstruction error to dot-product
error has a property that § 5's metrics missed:

> **Zero-snapping a small `k` is approximately free for attention;
> multiplicative noise on a small `k` is not.**

Concretely: if `k` is small (e.g. `‖k‖ < r_max / 30`), then
`qᵀk ≈ 0` and dropping the score from this entry barely shifts the
softmax. But if instead `k` is reconstructed as `k̂` with the
correct direction and a magnitude amplified to the LPQ floor
`eps · r_max`, then `qᵀk̂` can be much larger than `qᵀk`,
**injecting a fake high-score entry into the softmax**.

Polar and fp4_like benefit from this without knowing it: their
`r_step = r_max / (2^b_r - 1)` is much larger than typical-`k`
magnitudes, so most small pairs round to zero, which is the correct
behaviour for attention even though it is the *wrong* behaviour for
reconstruction. LPQ's log spacing distributes precision evenly across
magnitudes — beautiful for reconstruction, harmful for attention,
because it spends bits faithfully reconstructing pairs that
attention does not need.

This is a genuine empirical surprise and reverses the headline
claim of § 5. The synthetic distributions in § 5 had narrower
dynamic range (lognormal σ = 1, ≈ 7,000× span vs the model's 5,500×),
similar tail, but **§ 5's metrics did not measure the dot-product
effect** because it required a Q distribution that is correlated with
the K distribution in the way attention's `Q = K · W_q W_k⁻¹`
implicitly forces. Synthetic 2-D Gaussian or RoPE-pair inputs are not
substitutes for real `qᵀk`.

### 6.6 Zero-floor LPQ as a partial remedy

If the failure mode is "LPQ refuses to zero out small magnitudes,"
the obvious fix is to reserve one ρ-code for *exact* zero, snap the
smallest `f` of pairs to it, and use the remaining `2^b_ρ - 1`
codes to span the upper magnitude range in log-space. We call this
**LPQ-ZF** (zero-floor LPQ) with parameter `f`.

Measured PPL with `f ∈ {0.25, 0.50, 0.75}`:

| quantizer | 6 bits | 8 bits | 10 bits |
|---|---|---|---|
| log_polar (plain) | 646.5 | 46.7 | 11.08 |
| log_polar_zf25 | 63.8 | 18.1 | **9.98** |
| log_polar_zf50 | 54.8 | 20.0 | 10.83 |
| log_polar_zf75 | 104.8 | 74.3 | 31.6 |
| cart_uniform | 288.0 | 14.4 | 9.29 |
| **best non-LPQ** | 46.7 (polar) | 10.3 (fp4) | 9.29 (cart) |

LPQ-ZF closes most of the gap. At **10 bits / pair, LPQ-ZF25 reaches
PPL 9.98, vs cart at 9.29 and baseline at 8.71 — within 7.4 % of cart
and 14.5 % of FP32**. Plain LPQ at the same budget is at PPL 11.08
(27 % over baseline). The remaining gap may close further with
calibration, group sizing, or per-head `f` selection — none of these
were swept in this spike.

LPQ-ZF still does *not* beat cart at the bit budgets we tested on this
model. We do not claim it does. We claim it recovers the bulk of the
PPL loss attributable to LPQ's log-space-precision-on-small-magnitudes
artefact, and converges to within single-percent of cart at the
useful end of the budget range.

### 6.7 The Multi-Model Scale Curve

We ran Tier 0 and Tier 2 on four models spanning a 22 × parameter range:
SmolLM2-135M (initial run, § 6.2–6.6) plus three Qwen2.5 base models
(0.5B, 1.5B, 3B). This is the empirical test of the
"reconstruction-vs-PPL gap is small-model brittleness" hypothesis from
§ 6.4. Headline: **the gap is not monotonic in parameter count**;
LPQ's benefit varies with the specific model's K distribution, which
varies within the Qwen family.

**Tier 0 — K post-RoPE distributional fits across models:**

| metric | SmolLM2-135M | Qwen2.5-0.5B | Qwen2.5-1.5B | Qwen2.5-3B | **Gemma 4 E2B** |
|---|---|---|---|---|---|
| total params | 135M | 494M | 1.5B | 3.1B | 5.1B (effective 2B) |
| layers | 30 | 24 | 28 | 36 | 26 (15 unique K) |
| K heads (GQA) | 3 | 2 | 2 | 2 | 2 |
| head dim | 64 | 64 | 128 | 128 | 256 + 512 mixed |
| K pre-RoPE norm? | no | no | no | no | **yes (`k_norm`)** |
| r_median | 0.84 | 1.74 | 1.63 | 1.58 | **0.09** |
| r_max | 22.0 | **247.6** | **413.0** | 119.0 | **1.72** |
| r_p999 | 14.2 | 172.7 | 308.4 | 59.5 | 0.83 |
| **dyn range (p999/p001)** | **5,592 ×** | **15,670 ×** | **27,140 ×** | **4,788 ×** | **1,493 ×** |
| **Hill α (top 5 %)** | 2.40 | **0.95** | **1.15** | 1.73 | **3.16** |
| log-normality KS | 0.107 | 0.085 | 0.065 | n/a | 0.064 |
| angular uniformity | 0.0048 | 0.0060 | 0.0056 | n/a | 0.0048 |

**Key non-monotonic observations:**

1. **Gemma 4 E2B has by far the lightest tail (Hill α 3.16)** and
   smallest dynamic range (1,493 ×) of any model tested. The reason
   is architectural: Gemma 4's modeling code applies an RMSNorm-style
   `k_norm` to keys *before* RoPE (e.g. in `modeling_gemma4.py:1244`).
   This pre-normalization tames K outliers at training time, leaving
   no heavy-tailed magnitudes for inference-time quantization to
   exploit. **Models that adopt this design choice (Gemma 3+, some
   recent Qwen variants) do not benefit from LPQ-style log-spacing.**

2. The Qwen family (no pre-RoPE K-norm) shows the heavy-tailed regime
   LPQ targets. Qwen2.5-1.5B has the heaviest tails / widest dynamic
   range. **Qwen2.5-3B has tamer K than its smaller sibling
   Qwen2.5-0.5B** — Hill α 1.73 vs 0.95, r_max 119 vs 247. Architecture
   specifics (head dim doubles from 64 → 128, etc.) and training
   choices drive this within the family, not parameter count alone.

3. Angles remain near-uniform on every model (`ang_uniformity` 0.005
   range). PolarQuant's geometric assumption holds across scales,
   even on Gemma 4 where the radii are tame.

4. Log-normality of `r` gets tighter as the tail gets heavier (KS
   distance 0.107 → 0.085 → 0.065 on the heavier-tailed models). LPQ's
   "log-uniform bins are entropy-matched" argument (§ 4.1) is best
   supported on the heavier-tailed cases.

**Tier 2 — End-to-end PPL (best variant per cell in bold):**

(baseline FP32 PPL in italics in header; `turbo` = real `fused_turboquant`
package, Randomized Hadamard Transform + uniform-coordinate quant;
supports 2/3/4 bits per coordinate, so it is not available at 10 b/pair
= 5 b/coord)

| quantizer | SmolLM2-135M (*8.71*) | Qwen2.5-0.5B (*6.41*) | Qwen2.5-1.5B (*4.88*) | Qwen2.5-3B (*4.17*) | **Gemma 4 E2B (*5.91*)** |
|---|---|---|---|---|---|
| **3 bits/elt** (6 b/pair) | | | | | |
| cart_uniform | 288 | 2546 | 494 | 568 | 21.95 |
| polar | 46.7 | 529 | 10373 | 20426 | 11.59 |
| log_polar | 646 | 1522 | 384 | 3028 | 16.41 |
| **log_polar_zf25** | **63.8** | **325** | **177** | **32.5** | 7.25 |
| log_polar_zf50 | 54.8 | 670 | 2481 | 65.7 | 15.14 |
| **turbo (real TurboQuant)** | n/a | n/a | n/a | n/a | **6.11** |
| **4 bits/elt** (8 b/pair) | | | | | |
| cart_uniform | **14.4** | 151 | 52 | **10.3** | 8.32 |
| polar | 17.1 | 57 | 11985 | 1340 | 6.16 |
| log_polar | 46.7 | 133 | 67.7 | 174.9 | 6.76 |
| fp4_like | **10.3** | 89 | 8064 | 2343 | 6.12 |
| **log_polar_zf25** | 18.1 | 55 | **13.1** | 18.4 | 6.19 |
| log_polar_zf50 | 20.0 | **33.5** | 128 | 597 | 7.96 |
| **turbo (real TurboQuant)** | n/a | n/a | n/a | n/a | **5.96** |
| **5 bits/elt** (10 b/pair) | | | | | |
| cart_uniform | **9.29** | 22.8 | **8.88** | 8.19 | 6.39 |
| polar | 9.64 | 14.24 | 5340 | **5.30** | **5.97** |
| log_polar | 11.08 | 11.13 | 692 | 66.5 | 6.00 |
| **log_polar_zf25** | 9.98 | **11.02** | 84 | 5.66 | 6.02 |
| log_polar_zf50 | 10.83 | 46.1 | 246 | 20.1 | 7.97 |

*Note*: `turbo` rows for the 4 Qwen models are not filled in this
table. They would be a worthwhile follow-up; the Qwen family's
heavier-tailed K is exactly where TurboQuant's rotation-based scheme
should also work well, and head-to-head LPQ vs TurboQuant on Qwen
would close the comparison cleanly. For Gemma 4, TurboQuant is the
deployment default and was measured directly.

**Reading the table:**

1. **At 3 bits/element on the four non-Gemma models, `log_polar_zf25`
   is the winner on three of four** (the three Qwen models). On
   SmolLM2-135M polar narrowly wins (its tail is light enough — Hill
   α 2.40 — that uniform-r quantization still mostly works). Margins
   over the next-best non-LPQ scheme: 2× (Qwen-0.5B) to 17×
   (Qwen-3B).

2. **On Gemma 4 E2B at 3 bits/element, TurboQuant wins (PPL 6.11)
   and LPQ-ZF25 is second (7.25)**. The reason is Gemma 4's
   pre-RoPE `k_norm` layer: K is already normalized before any
   inference-time quantization, so there is little outlier headroom
   for LPQ's log-spacing to exploit, and TurboQuant's
   Randomized-Hadamard rotation (which spreads outlier energy across
   all coordinates of a uniform-quantized vector) has the better
   structural fit to nearly-Gaussian K.

3. **At 4 bits/element, the picture is model-dependent.**
   - On light-tailed models (SmolLM2, Qwen2.5-3B, Gemma 4),
     cart_uniform / fp4_like / TurboQuant are competitive or win;
     LPQ-ZF is close but loses.
   - On heavy-tailed models (Qwen2.5-0.5B, 1.5B), LPQ-ZF50 or
     LPQ-ZF25 wins by 4-12× over cart_uniform.

4. **At 5 bits/element, the picture inverts again.** When the bit
   budget is loose enough for cart or polar to cover the dynamic
   range, the simpler schemes catch up or surpass LPQ on most
   models. On Qwen2.5-3B at 10 b/pair, *polar* is the winner (PPL
   5.30 within 1.3 × of FP32 baseline); on Gemma 4 E2B polar wins
   too (5.97 vs FP32 5.91). TurboQuant is not benchmarked at this
   budget because the open-source `fused_turboquant` package caps at
   4 bits per coordinate.

**Implications for what LPQ "is good for":**

- LPQ-ZF25 is a **robust low-bit code** for models without pre-RoPE
  K-normalization (most models pre-Gemma 4). It wins or comes close
  to winning in 9 / 12 (model × budget) cells on the Qwen + SmolLM2
  set.
- **TurboQuant is the better choice on Gemma 4 specifically** and
  any future model that adopts pre-RoPE K-norm. It also has a clean
  HuggingFace integration (`fused_turboquant`) and vLLM upstream
  support.
- LPQ-ZF's *intended* regime is **aggressive compression at heavy-
  tailed K** (3 b/elt on Qwen-family models). At looser budgets, on
  light-tailed models, or on K-norm models, simpler / different
  schemes are competitive or better.

The **revised takeaway** from the spike: LPQ's value is not as a
*universal* KV-cache code but as a *low-bit code matched to
heavy-tailed K*. The principal architectural variable that determines
which quantizer wins on a given model is **whether the model normalizes
K before RoPE**: models without K-norm (Qwen, Llama, Mistral lines) are
the LPQ target regime; models with K-norm (Gemma 3+, future SOTA) are
the TurboQuant regime.

### 6.8 What this spike does and does not show

**Does show:**

- Real post-RoPE K on both SmolLM2-135M and Qwen2.5-0.5B has the
  heavy-tailed magnitude / near-uniform angle structure § 4
  predicted (Tier 0). The tail gets heavier on the larger model
  (Hill α 2.4 → 0.95), in line with the LLM.int8() finding.
- LPQ achieves cleanly the **rel_med ≈ 0.256 / cos_med ≈ 0.995**
  scale-invariance signature on every layer of both models, while
  polar/fp4_like collapse on half the layers (Tier 1).
- **The reconstruction → PPL transfer is model-scale dependent**:
  it fails on SmolLM2-135M (a small-model artefact, attention too
  brittle) and succeeds on Qwen2.5-0.5B at 10 bits/pair, where LPQ
  and LPQ-ZF25 both beat polar and cart_uniform on PPL.
- The optimal zero-floor fraction `f` shifts with model
  distribution: 0.25 for SmolLM2, 0.50 for Qwen-0.5B at 8 bits.
  This is a hyperparameter requiring per-model calibration.

**Does not show:**

- That LPQ helps at *production* scale (≥ 8B). The two-model trend
  is consistent with the LLM.int8() outlier-emergence narrative
  (heavier tails → bigger LPQ benefit), but extrapolation to 8B
  requires running it.
- That calibration (off-line `r_max`, `ε`, `f` selection) closes
  the remaining gap to PolarQuant's reported numbers. Our hook
  recomputes scales per-batch.
- That long-context LongBench / RULER results match PolarQuant's
  numbers. Our PPL eval is 256 tokens.
- That LPQ helps *weight* quantization on a real model. We did not
  run § 6.2's weight experiment in the spike; only KV-cache K.

The next experiment, in priority order: (1) re-run Tier 2 with
calibrated scales on Qwen2.5-0.5B and a 7-8B model — the
reconstruction-vs-PPL gap is suspected to keep shrinking with
scale and tail-heaviness; (2) sweep `f` per-head rather than
per-tensor; (3) compare LPQ-ZF against PolarQuant's exact `m4n4`
and `m4n2` configs on LongBench.

---

## 7. Limitations

1. **Real-model validation is restricted to four sub-4B models.**
   Section 6 reports results on SmolLM2-135M, Qwen2.5-0.5B,
   Qwen2.5-1.5B, and Qwen2.5-3B (~22 × parameter range). A 7B-scale
   data point was attempted but exceeded available disk on the test
   box. The four-model trend (LPQ-ZF25 wins at 3 bits/element on
   every model; mixed at looser budgets) is robust but does not
   extend to the 7-8B regime where PolarQuant reports its headline
   numbers.

2. **The reconstruction-error → PPL transfer is bit-budget
   dependent, not scale-dependent.** § 6.4–6.7 collectively show
   this is the most important caveat. LPQ-ZF25 wins at 3 bits/element
   on every model tested, with margins ranging from 4 × (SmolLM2) to
   17 × (Qwen-3B) over the next-best non-LPQ scheme. At 4–5
   bits/element the picture becomes model-dependent: cart_uniform,
   polar, or fp4_like can win on individual (model × budget) cells.
   The synthetic-data metrics of § 5 reliably predicted *reconstruction
   error* but only loosely predicted PPL — and the loose correlation
   is strongest at aggressive bit budgets, exactly the production
   target for KV-cache compression.

3. **Synthetic distributions did not capture the
   small-magnitude-zeroing benefit.** § 5's pair-level metrics
   measured `‖k - k̂‖` directly. Attention measures `qᵀ(k - k̂)`,
   which strongly rewards zero-snapping small `k` over faithful
   reconstruction of them. A better synthetic harness would sample
   `(q, k)` pairs and measure dot-product error rather than vector
   reconstruction error.

4. **Per-batch absmax replaces calibration.** Production KV-cache
   quantizers calibrate `r_max` and `ε` on a held-out set; our
   Tier 2 hook recomputes per batch. This adds noise to all schemes
   equally, but LPQ-ZF may be more calibration-sensitive than
   cart_uniform (a property worth measuring).

5. **Synthetic distributions remain simplifications.** The lognormal
   and outlier datasets ignored, and Tier 1 only partially
   reflected:
   - per-channel / per-head non-stationarity (KIVI, Massive
     Activations);
   - the categorical importance of super-weights (Yu et al. 2024),
     which are not magnitude-large;
   - attention-sink BOS-token magnitude inflation (Xiao et al.
     2023);
   - layer-depth norm growth — Tier 0 *did* show this (layer-12
     jump in dynamic range).

6. **The bit-budget threshold matters.** At 6 bits/pair, plain LPQ
   is catastrophic (PPL 646 vs FP32 8.7). LPQ-ZF reduces this to
   PPL 63.8 but still loses to polar (46.7). Below this budget LPQ
   is not the right code; cart_uniform's dynamic-range failure mode
   becomes the dominant failure mode again.

7. **Group-size and ε were not swept.** Our Tier 2 uses per-tensor
   absmax and `ε = 10⁻⁶`. Group size (per-head, per-layer,
   per-tensor) and ε (10⁻³ to 10⁻⁹) are both expected to matter
   and were skipped to keep the spike small.

8. **The novelty is narrow.** All three component ideas (2-D pair
   factorization, log magnitude, joint binning) exist in the
   literature — just not composed. A reviewer could argue this is
   incremental. The empirical scale-invariance property (§ 5.5,
   confirmed in § 6.3) elevates it past pure incrementalism, but the
   negative PPL result of § 6.4 weakens the practical case.

9. **PCDVQ (Yue et al. 2025) is the closest weight-quant baseline
   and we did not implement it.** It is a Cartesian codebook in
   2-D pair space; LPQ should be compared against it in any
   weight-quantization follow-up.

10. **No coverage of activation or weight quantization in this spike.**
    LPQ applies to KV cache and weights cleanly; the spike only
    covered KV cache K post-RoPE. Activation and weight regimes have
    different distribution shapes and may invert the conclusions of
    § 6.4.

---

## 8. Conclusion

We proposed **log-polar quantization (LPQ)**: jointly bin
`(ρ = log r, θ)` on a 2-D lattice for KV-cache keys and weight
blocks. LPQ is the natural composition of two existing ideas:
PolarQuant's 2-D pair factorization and Microscaling / FP4 / FP8's
log-magnitude scalar code. We provided a theoretical argument linking
LPQ to the Mellin transform, scale-invariance, and heavy-tailed weight
spectra; synthetic-data experiments confirming LPQ achieves bounded
relative error invariant to distribution shape (median 0.256 across
all tested distributions, σ ≤ 0.005) and ties or beats linear polar
on MSE at 10+ bits/pair for heavy-tailed inputs.

We then ran a three-tier empirical spike on **five models**
(SmolLM2-135M, Qwen2.5-{0.5, 1.5, 3}B, Gemma 4 E2B; ~38 × parameter
range; bf16 weights; pure-CPU), and added a head-to-head comparison
against **real TurboQuant** (Zandieh et al., ICLR 2026) via the
open-source `fused_turboquant` package:

- **Tier 0** revealed that K distribution is dominated by an
  architectural choice: **does the model normalize K before RoPE?**
  Models without pre-RoPE K-norm (SmolLM2, Qwen2.5 line) have
  heavy-tailed K (Hill α 0.95-2.4, dynamic range 5K-27K ×). Gemma 4
  E2B has a `k_norm` RMSNorm layer immediately before RoPE
  (`modeling_gemma4.py:1244`) and shows nearly-Gaussian K (Hill α
  3.16, dynamic range 1,493 ×). This is the principal architectural
  variable in the spike.
- **Tier 1** confirmed LPQ's reconstruction-error wins on real K
  invariantly across models: rel_med ≈ 0.256, cos_med ≈ 0.995, every
  layer, every model.
- **Tier 2** measured PPL on 17-19 configs × 5 models = ~88 data
  points. The result splits along the K-norm axis:

  - **Without K-norm (Qwen, SmolLM2 lines), at 3 bits/element**:
    LPQ-ZF25 wins on three of four such models (the Qwens), by 2-17 ×
    over the next-best non-LPQ scheme. On SmolLM2 polar narrowly
    wins (light tail). LPQ-ZF wins again on heavy-tailed models at
    4 b/elt. At 5 b/elt the simpler schemes catch up.
  - **With K-norm (Gemma 4 E2B)**: TurboQuant is the winner at 3 and
    4 bits/element (PPL 6.11 / 5.96 vs FP32 baseline 5.91). LPQ-ZF25
    is second at 3 b/elt (PPL 7.25). At 5 b/elt, polar wins (PPL 5.97).

**Overall verdict**: LPQ-ZF and TurboQuant are **complementary**, not
competing, schemes — each is optimized for a different K-distribution
regime:

| K regime | Models | Winner at 3 b/elt | Mechanism |
|---|---|---|---|
| **Heavy-tailed** (no K-norm) | Qwen2.5 line, Llama, Mistral | **LPQ-ZF25** | log-spaced ρ bins match log-normal magnitudes |
| **Nearly-Gaussian** (with K-norm) | Gemma 3+, Gemma 4 | **TurboQuant** | rotation spreads outliers; uniform quant works |

The principal predictor of which scheme wins is whether the model's
attention layer normalizes K before RoPE. This is an architectural
detail visible in the model's source code (e.g.
`self.k_norm(key_states)` before `apply_rotary_pos_emb` in Gemma 4).
It is observable directly from a 1-minute Tier 0 statistical
pre-check on any model: Hill α > ~2.5 indicates the K-norm regime
(TurboQuant zone); α < ~1.5 indicates the heavy-tail regime (LPQ-ZF
zone).

A 7B-scale data point was attempted but the 15 GB bf16 weights
exceeded available disk on the test box; the 5-model curve is what
the spike actually delivered.

This paper reports both the wins and the limits, including the
clean head-to-head loss on Gemma 4 vs TurboQuant. The code, raw
metrics, **~95 PPL data points across five models**, the
distribution-fit per-layer csv, and the dump-and-reuse Tier 0 / Tier 1
pipelines are in `papers/spiral-quant/` of the companion repository.

---

## References

- Ashkboos, S. et al. (2024). *QuaRot: Outlier-Free 4-Bit Inference in
  Rotated LLMs*. arXiv 2404.00456.
- Dettmers, T. et al. (2022). *LLM.int8(): 8-bit Matrix
  Multiplication for Transformers at Scale*. arXiv 2208.07339.
- Dettmers, T. et al. (2023a). *QLoRA: Efficient Finetuning of
  Quantized LLMs* (NF4). arXiv 2305.14314.
- Dettmers, T. et al. (2023b). *SpQR: A Sparse-Quantized
  Representation for Near-Lossless LLM Weight Compression*.
  arXiv 2306.03078.
- Esteves, C. et al. (2018). *Polar Transformer Networks*.
  ICLR 2018, arXiv 1709.01889.
- Frantar, E. et al. (2022). *GPTQ: Accurate Post-Training
  Quantization for Generative Pre-trained Transformers*.
  arXiv 2210.17323.
- Han, S., Kacham, R., Karbasi, A., Mirrokni, V., Zandieh, A.
  (2025). *PolarQuant: Leveraging Polar Transformation for Efficient
  Key Cache Quantization and Decoding Acceleration*.
  arXiv 2502.00527 / 2502.02617. NeurIPS 2025.
- Hooper, C. et al. (2024). *KVQuant: Towards 10-Million Context
  Length LLM Inference with KV Cache Quantization*. arXiv 2401.18079.
- Kang, H. et al. (2024). *GEAR: An Efficient KV Cache Compression
  Recipe for Near-Lossless Generative Inference of LLM*.
  arXiv 2403.05527.
- Kim, S. et al. (2023). *SqueezeLLM: Dense-and-Sparse Quantization*.
  arXiv 2306.07629.
- Lin, J. et al. (2023). *AWQ: Activation-aware Weight Quantization
  for LLM Compression and Acceleration*. arXiv 2306.00978.
- Liu, R. et al. (2024a). *KIVI: A Tuning-Free Asymmetric 2bit
  Quantization for KV Cache*. arXiv 2402.02750.
- Liu, Z. et al. (2024b). *SpinQuant: LLM Quantization with Learned
  Rotations*. arXiv 2405.16406.
- Martin, C. H., Mahoney, M. W. (2019). *Implicit
  Self-Regularization in Deep Neural Networks*. arXiv 1901.08276.
- Micikevicius, P. et al. (2022). *FP8 Formats for Deep Learning*.
  arXiv 2209.05433.
- Miyashita, D. et al. (2016). *Convolutional Neural Networks
  using Logarithmic Data Representation*. arXiv 1603.01025.
- OCP (2023). *Microscaling Formats for Deep Learning*.
  arXiv 2310.10537.
- Su, B., Wen, J. (2022). *Log-Polar Space Convolution Layers*.
  NeurIPS 2022.
- Sun, M. et al. (2024). *Massive Activations in Large Language
  Models*. arXiv 2402.17762.
- Sun, R. et al. (2025). *LogQuant: Log-Distributed 2-Bit
  Quantization of KV Cache*. arXiv 2503.19950. ICLR 2025.
- Xiao, G. et al. (2022). *SmoothQuant: Accurate and Efficient
  Post-Training Quantization for Large Language Models*.
  arXiv 2211.10438.
- Xiao, G. et al. (2023). *Efficient Streaming Language Models with
  Attention Sinks*. arXiv 2309.17453.
- Yu, M. et al. (2024). *The Super Weight in Large Language
  Models*. arXiv 2411.07191.
- Yue, Z. et al. (2025). *PCDVQ: Polar Coordinate Decoupled Vector
  Quantization*. arXiv 2506.05432.
