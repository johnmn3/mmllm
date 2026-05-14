# Tier 0 — Distributional Pre-check


Model: `Qwen/Qwen2.5-0.5B`  

N_seqs × seq_len: 8 × 256  

Layers captured: 24  

Forward time (CPU): 6.5s


## Aggregate stats (all layers pooled)

- **n_pairs**: 3145728
- **r_mean**: 3.797
- **r_median**: 1.738
- **r_std**: 13.15
- **r_max**: 247.6
- **r_min_nz**: 0.0002587
- **r_p95**: 8.269
- **r_p99**: 50.3
- **r_p999**: 172.7
- **r_dyn_range**: 1.567e+04
- **tail_alpha_hill**: 0.9531
- **ang_uniformity_score**: 0.006026
- **log_normality_ks**: 0.08484


## Per-layer stats

| layer | r_median | r_p99 | r_p999 | r_dyn_range | tail_alpha_hill | ang_uniformity_score | log_normality_ks |
|---|---|---|---|---|---|---|---|
| 0 | 9.301 | 143.5 | 143.5 | 2897 | 21.09 | 0.04477 | 0.1834 |
| 1 | 2.106 | 172.6 | 173 | 1900 | 1.174 | 0.03575 | 0.1496 |
| 2 | 2.138 | 76.37 | 77.1 | 659.4 | 5.101 | 0.06599 | 0.1232 |
| 3 | 2.068 | 24.11 | 25.22 | 1895 | 2.476 | 0.04617 | 0.06752 |
| 4 | 1.653 | 17.72 | 18.48 | 1664 | 1.83 | 0.03041 | 0.06699 |
| 5 | 1.492 | 6.278 | 9.765 | 1325 | 2.665 | 0.02872 | 0.07452 |
| 6 | 1.718 | 6.08 | 7.606 | 850.1 | 4.148 | 0.03345 | 0.08144 |
| 7 | 1.795 | 5.985 | 11.4 | 1648 | 3.832 | 0.01836 | 0.06445 |
| 8 | 2.003 | 241.8 | 243.9 | 1.97e+04 | 0.508 | 0.01403 | 0.1585 |
| 9 | 1.818 | 8.742 | 10.64 | 1202 | 3.271 | 0.02838 | 0.06144 |
| 10 | 1.725 | 7.002 | 10.02 | 1276 | 3.326 | 0.04149 | 0.07255 |
| 11 | 1.649 | 7.611 | 9.882 | 1359 | 4.317 | 0.02456 | 0.07188 |
| 12 | 1.809 | 6.825 | 8.226 | 997.4 | 3.806 | 0.03177 | 0.05508 |
| 13 | 2.001 | 5.389 | 7.144 | 855.6 | 7.281 | 0.02684 | 0.06912 |
| 14 | 1.79 | 8.007 | 10.57 | 1205 | 2.846 | 0.02991 | 0.07908 |
| 15 | 1.731 | 8.785 | 9.779 | 997.3 | 3.025 | 0.02606 | 0.05334 |
| 16 | 1.863 | 5.798 | 8.181 | 765.6 | 7.738 | 0.03184 | 0.04904 |
| 17 | 1.413 | 6.246 | 8.82 | 962.7 | 5.458 | 0.02756 | 0.04791 |
| 18 | 1.851 | 7.429 | 8.972 | 900.3 | 3.124 | 0.0358 | 0.05858 |
| 19 | 1.791 | 10.08 | 10.99 | 1113 | 2.486 | 0.0318 | 0.06114 |
| 20 | 1.451 | 10.14 | 11.63 | 955.2 | 2.347 | 0.03914 | 0.05646 |
| 21 | 1.216 | 5.318 | 8.534 | 831.8 | 4.143 | 0.02991 | 0.0872 |
| 22 | 1.131 | 8.633 | 9.126 | 525.5 | 2.268 | 0.04622 | 0.06928 |
| 23 | 1.272 | 8.801 | 9.631 | 278.5 | 5.572 | 0.03499 | 0.04206 |

## Interpretation

- Median Hill tail exponent across layers: **3.3** (min 0.508, max 21.1). Lower = heavier tail. Gaussian ≈ ∞; lognormal varies; Pareto with finite mean has α > 1.
- Median dynamic range (p999/p001) across layers: **1.06e+03**. This is the multiplicative span LPQ's ρ axis needs to cover.
- Median KS distance to log-normal fit: **0.0683**. Lower = closer to lognormal. Values < 0.05 are strong support.
- Median angular uniformity score: **0.0318** (0 = perfectly uniform; the RoPE-pair angle distribution is reportedly near-uniform with mild concentration).