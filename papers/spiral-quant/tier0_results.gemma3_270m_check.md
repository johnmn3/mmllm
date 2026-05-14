# Tier 0 — Distributional Pre-check


Model: `google/gemma-3-270m`  

N_seqs × seq_len: 4 × 128  

Layers captured: 18  

Forward time (CPU): 3.7s


## Aggregate stats (all layers pooled)

- **n_pairs**: 1179648
- **r_mean**: 2.518
- **r_median**: 1.594
- **r_std**: 3.607
- **r_max**: 90.24
- **r_min_nz**: 2.713e-05
- **r_p95**: 7.422
- **r_p99**: 17.74
- **r_p999**: 40.65
- **r_dyn_range**: 4.065e+10
- **tail_alpha_hill**: 1.969
- **ang_uniformity_score**: 0.0127
- **log_normality_ks**: 0.04428


## Per-layer stats

| layer | r_median | r_p99 | r_p999 | r_dyn_range | tail_alpha_hill | ang_uniformity_score | log_normality_ks |
|---|---|---|---|---|---|---|---|
| 0 | 1.415 | 9.359 | 12.18 | 583.3 | 1.926 | 0.01893 | 0.06316 |
| 1 | 1.928 | 12.57 | 17.61 | 1505 | 3.008 | 0.02662 | 0.08572 |
| 2 | 1.662 | 12.76 | 39.27 | 1362 | 2.214 | 0.02436 | 0.07032 |
| 3 | 1.581 | 9.036 | 14.08 | 614.1 | 4.031 | 0.03891 | 0.05398 |
| 4 | 1.648 | 12.95 | 29.25 | 781.9 | 2.303 | 0.02389 | 0.05124 |
| 5 | 1.643 | 31.95 | 48.27 | 4.827e+10 | 3.776 | 0.0292 | 0.05049 |
| 6 | 1.349 | 7.144 | 27.8 | 2148 | 2.538 | 0.02931 | 0.06061 |
| 7 | 1.446 | 10.4 | 21.76 | 2213 | 2.922 | 0.03676 | 0.04905 |
| 8 | 1.492 | 13.47 | 19.8 | 3626 | 2.382 | 0.022 | 0.0495 |
| 9 | 1.45 | 12.31 | 22.63 | 2767 | 2.608 | 0.03141 | 0.08865 |
| 10 | 1.853 | 19.79 | 32.25 | 4359 | 2.815 | 0.04564 | 0.04547 |
| 11 | 1.692 | 52.98 | 74.92 | 9081 | 1.794 | 0.03504 | 0.05972 |
| 12 | 1.346 | 16.38 | 22.88 | 2.288e+10 | 3.828 | 0.05535 | 0.06559 |
| 13 | 1.518 | 7.561 | 16.78 | 1232 | 4.071 | 0.02099 | 0.04511 |
| 14 | 1.882 | 14.1 | 20.07 | 2.007e+10 | 3.111 | 0.06178 | 0.0609 |
| 15 | 1.411 | 16.15 | 33.18 | 2280 | 2.059 | 0.03126 | 0.0467 |
| 16 | 1.789 | 13.78 | 17.82 | 1488 | 3.1 | 0.0223 | 0.04107 |
| 17 | 1.815 | 13.16 | 13.92 | 1.392e+10 | 4.272 | 0.03249 | 0.05071 |

## Interpretation

- Median Hill tail exponent across layers: **2.87** (min 1.79, max 4.27). Lower = heavier tail. Gaussian ≈ ∞; lognormal varies; Pareto with finite mean has α > 1.
- Median dynamic range (p999/p001) across layers: **2.25e+03**. This is the multiplicative span LPQ's ρ axis needs to cover.
- Median KS distance to log-normal fit: **0.0526**. Lower = closer to lognormal. Values < 0.05 are strong support.
- Median angular uniformity score: **0.0303** (0 = perfectly uniform; the RoPE-pair angle distribution is reportedly near-uniform with mild concentration).