# Tier 0 — Distributional Pre-check


Model: `google/gemma-3-270m`  

N_seqs × seq_len: 16 × 256  

Layers captured: 18  

Forward time (CPU): 44.0s


## Aggregate stats (all layers pooled)

- **n_pairs**: 9437184
- **r_mean**: 2.501
- **r_median**: 1.646
- **r_std**: 3.35
- **r_max**: 92.78
- **r_min_nz**: 3.242e-05
- **r_p95**: 7.299
- **r_p99**: 16.04
- **r_p999**: 34.21
- **r_dyn_range**: 3.421e+10
- **tail_alpha_hill**: 2.124
- **ang_uniformity_score**: 0.01168
- **log_normality_ks**: 0.04245


## Per-layer stats

| layer | r_median | r_p99 | r_p999 | r_dyn_range | tail_alpha_hill | ang_uniformity_score | log_normality_ks |
|---|---|---|---|---|---|---|---|
| 0 | 1.454 | 9.359 | 9.641 | 277.9 | 1.708 | 0.02513 | 0.08255 |
| 1 | 1.998 | 12.56 | 13.97 | 863 | 3.042 | 0.02903 | 0.07242 |
| 2 | 1.749 | 11.81 | 34.77 | 742.7 | 2.402 | 0.02357 | 0.08231 |
| 3 | 1.609 | 7.878 | 12.17 | 319.3 | 3.62 | 0.04051 | 0.05014 |
| 4 | 1.676 | 10.11 | 27.09 | 619.3 | 3.355 | 0.02497 | 0.0637 |
| 5 | 1.918 | 28.23 | 45.11 | 4.511e+10 | 4.661 | 0.02875 | 0.05893 |
| 6 | 1.458 | 7.137 | 22.81 | 1304 | 2.697 | 0.02537 | 0.07391 |
| 7 | 1.457 | 9.411 | 16.52 | 1112 | 3.473 | 0.03772 | 0.05352 |
| 8 | 1.518 | 11.49 | 19.83 | 1882 | 1.791 | 0.03436 | 0.05342 |
| 9 | 1.525 | 10.83 | 19.39 | 2212 | 2.982 | 0.02641 | 0.1045 |
| 10 | 1.899 | 19.79 | 26.48 | 1722 | 2.989 | 0.04496 | 0.05285 |
| 11 | 1.75 | 42.75 | 69.55 | 4642 | 2.047 | 0.03395 | 0.05783 |
| 12 | 1.343 | 13.94 | 20.37 | 2.037e+10 | 4.407 | 0.05178 | 0.07306 |
| 13 | 1.512 | 6.448 | 14.44 | 762.3 | 5.624 | 0.03275 | 0.05121 |
| 14 | 1.981 | 12.7 | 17.38 | 1.738e+10 | 3.192 | 0.05891 | 0.07269 |
| 15 | 1.414 | 13.94 | 28.8 | 1442 | 2.508 | 0.03556 | 0.05255 |
| 16 | 1.991 | 13.78 | 16.01 | 718.5 | 3.178 | 0.03716 | 0.0453 |
| 17 | 1.754 | 13.16 | 13.92 | 1.392e+10 | 4.462 | 0.02542 | 0.05223 |

## Interpretation

- Median Hill tail exponent across layers: **3.11** (min 1.71, max 5.62). Lower = heavier tail. Gaussian ≈ ∞; lognormal varies; Pareto with finite mean has α > 1.
- Median dynamic range (p999/p001) across layers: **1.37e+03**. This is the multiplicative span LPQ's ρ axis needs to cover.
- Median KS distance to log-normal fit: **0.0584**. Lower = closer to lognormal. Values < 0.05 are strong support.
- Median angular uniformity score: **0.0334** (0 = perfectly uniform; the RoPE-pair angle distribution is reportedly near-uniform with mild concentration).