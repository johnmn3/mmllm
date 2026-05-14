# Tier 0 — Distributional Pre-check


Model: `google/gemma-4-E2B`  

N_seqs × seq_len: 8 × 256  

Layers captured: 15  

Forward time (CPU): 106.5s


## Aggregate stats (all layers pooled)

- **n_pairs**: 4718592
- **r_mean**: 0.1168
- **r_median**: 0.09312
- **r_std**: 0.09744
- **r_max**: 1.716
- **r_min_nz**: 1.038e-05
- **r_p95**: 0.291
- **r_p99**: 0.4806
- **r_p999**: 0.8264
- **r_dyn_range**: 1493
- **tail_alpha_hill**: 3.164
- **ang_uniformity_score**: 0.004771
- **log_normality_ks**: 0.06395


## Per-layer stats

| layer | r_median | r_p99 | r_p999 | r_dyn_range | tail_alpha_hill | ang_uniformity_score | log_normality_ks |
|---|---|---|---|---|---|---|---|
| 0 | 0.07804 | 0.6098 | 0.9048 | 274.4 | 3.227 | 0.03529 | 0.06408 |
| 1 | 0.1293 | 0.4159 | 0.5422 | 121.2 | 5.681 | 0.02181 | 0.09851 |
| 2 | 0.1335 | 0.4217 | 0.6748 | 208.4 | 4.808 | 0.02686 | 0.09776 |
| 3 | 0.1001 | 0.6269 | 0.7476 | 196.7 | 2.853 | 0.01667 | 0.06419 |
| 4 | 0.06829 | 0.2313 | 0.3513 | 634.7 | 3.965 | 0.02849 | 0.1063 |
| 5 | 0.1188 | 0.5943 | 0.783 | 1726 | 3.169 | 0.02429 | 0.1322 |
| 6 | 0.1355 | 0.4179 | 0.7035 | 224.4 | 5.987 | 0.02489 | 0.08626 |
| 7 | 0.1331 | 0.4728 | 0.6056 | 307.6 | 4.531 | 0.01744 | 0.07422 |
| 8 | 0.1423 | 0.4777 | 0.5996 | 267 | 5.594 | 0.026 | 0.1089 |
| 9 | 0.06322 | 0.1853 | 0.2821 | 308.3 | 7.169 | 0.01459 | 0.0704 |
| 10 | 0.1109 | 0.51 | 0.6304 | 392.1 | 4.894 | 0.02645 | 0.05304 |
| 11 | 0.1098 | 0.5333 | 0.696 | 430.7 | 7.182 | 0.02141 | 0.07764 |
| 12 | 0.09416 | 0.8248 | 0.8707 | 459.7 | 1.909 | 0.02504 | 0.04854 |
| 13 | 0.08025 | 0.5949 | 1.218 | 2332 | 2.11 | 0.02136 | 0.1042 |
| 14 | 0.06642 | 0.1893 | 0.26 | 790.6 | 6.658 | 0.01463 | 0.1252 |

## Interpretation

- Median Hill tail exponent across layers: **4.81** (min 1.91, max 7.18). Lower = heavier tail. Gaussian ≈ ∞; lognormal varies; Pareto with finite mean has α > 1.
- Median dynamic range (p999/p001) across layers: **308**. This is the multiplicative span LPQ's ρ axis needs to cover.
- Median KS distance to log-normal fit: **0.0863**. Lower = closer to lognormal. Values < 0.05 are strong support.
- Median angular uniformity score: **0.0243** (0 = perfectly uniform; the RoPE-pair angle distribution is reportedly near-uniform with mild concentration).