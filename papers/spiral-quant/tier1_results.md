# Tier 1 — Reconstruction error on real K (post-RoPE)


Source dump: `HuggingFaceTB/SmolLM2-135M`, N=32×256, 30 layers.


## Aggregate metrics (all layers pooled)

| bits | quantizer | mse | rmse | p99_err | p999_err | rel_med | rel_p99 | cos_med | cos_p01 |
|---|---|---|---|---|---|---|---|---|---|
| 6 | cart | 9.878 | 3.143 | 3.8 | 3.805 | 5.814 | 460.6 | 0.9282 | 0.6989 |
| 6 | polar | 0.8471 | 0.9204 | 2.574 | 4.599 | 1 | 1 | 0 | 0 |
| 6 | log_polar | 2.698 | 1.643 | 10.65 | 13.99 | 0.5142 | 1.682 | 0.9784 | 0.7563 |
| 8 | cart | 1.854 | 1.361 | 1.769 | 1.775 | 2.275 | 214.5 | 0.947 | 0.7007 |
| 8 | polar | 0.1937 | 0.4401 | 1.111 | 2.3 | 1 | 1 | 0 | 0 |
| 8 | log_polar | 0.3862 | 0.6215 | 2.575 | 5.334 | 0.2589 | 0.5933 | 0.995 | 0.9491 |
| 8 | fp4_like | 0.2633 | 0.5131 | 1.056 | 1.636 | 1 | 1 | -0 | -0 |
| 8 | log_polar_hyb1pct | 0.2691 | 0.5188 | 1.994 | 3.214 | 0.2575 | 0.5931 | 0.995 | 0.9496 |
| 8 | polar_hyb1pct | 0.1729 | 0.4158 | 0.999 | 1.463 | 1 | 1 | 0 | 0 |
| 8 | log_polar_hyb01pct | 0.3302 | 0.5747 | 2.493 | 3.789 | 0.2585 | 0.5931 | 0.995 | 0.9492 |
| 10 | cart | 0.387 | 0.6221 | 0.8524 | 0.8576 | 0.7826 | 103.3 | 0.9695 | 0.7046 |
| 10 | polar | 0.04895 | 0.2212 | 0.5664 | 1.055 | 0.3211 | 1 | 0.9963 | 0 |
| 10 | log_polar | 0.09625 | 0.3102 | 1.278 | 2.625 | 0.1273 | 0.2548 | 0.9987 | 0.9923 |

## Per-layer summary: MSE (median / min / max across 30 layers)

| bits | quantizer | mse_median | mse_min | mse_max |
|---|---|---|---|---|
| 6 | cart | 5.143 | 1.318 | 10.26 |
| 6 | log_polar | 1.407 | 0.6396 | 8.824 |
| 6 | polar | 0.4337 | 0.2303 | 1.411 |
| 8 | cart | 0.9333 | 0.2628 | 2.014 |
| 8 | fp4_like | 0.1374 | 0.07611 | 0.37 |
| 8 | log_polar | 0.2753 | 0.1646 | 1.573 |
| 8 | log_polar_hyb01pct | 0.2601 | 0.1498 | 1.564 |
| 8 | log_polar_hyb1pct | 0.167 | 0.07871 | 1.459 |
| 8 | polar | 0.1038 | 0.06154 | 0.2798 |
| 8 | polar_hyb1pct | 0.08707 | 0.0559 | 0.2434 |
| 10 | cart | 0.1931 | 0.05779 | 0.4252 |
| 10 | log_polar | 0.05441 | 0.03002 | 0.2697 |
| 10 | polar | 0.02871 | 0.01542 | 0.07677 |

## Per-layer summary: rel_med (median / min / max across 30 layers)

| bits | quantizer | rel_med_median | rel_med_min | rel_med_max |
|---|---|---|---|---|
| 6 | cart | 10.66 | 0.4664 | 36.07 |
| 6 | log_polar | 0.5004 | 0.4401 | 0.5538 |
| 6 | polar | 1 | 0.3614 | 1 |
| 8 | cart | 4.513 | 0.2564 | 16.35 |
| 8 | fp4_like | 1 | 0.168 | 1 |
| 8 | log_polar | 0.2561 | 0.2302 | 0.2844 |
| 8 | log_polar_hyb01pct | 0.256 | 0.2301 | 0.2844 |
| 8 | log_polar_hyb1pct | 0.2531 | 0.2293 | 0.2843 |
| 8 | polar | 1 | 0.1765 | 1 |
| 8 | polar_hyb1pct | 1 | 0.1765 | 1 |
| 10 | cart | 1.753 | 0.1154 | 7.45 |
| 10 | log_polar | 0.1258 | 0.1182 | 0.1326 |
| 10 | polar | 0.8698 | 0.08572 | 1 |

## Per-layer summary: cos_med (median / min / max across 30 layers)

| bits | quantizer | cos_med_median | cos_med_min | cos_med_max |
|---|---|---|---|---|
| 6 | cart | 0.9329 | 0.906 | 0.9656 |
| 6 | log_polar | 0.9784 | 0.9754 | 0.9818 |
| 6 | polar | 0 | 0 | 0.9642 |
| 8 | cart | 0.9482 | 0.9236 | 0.9911 |
| 8 | fp4_like | 0 | 0 | 0.9958 |
| 8 | log_polar | 0.9949 | 0.9941 | 0.9958 |
| 8 | log_polar_hyb01pct | 0.995 | 0.9941 | 0.9958 |
| 8 | log_polar_hyb1pct | 0.995 | 0.9942 | 0.9959 |
| 8 | polar | 0 | 0 | 0.994 |
| 8 | polar_hyb1pct | 0 | 0 | 0.9941 |
| 10 | cart | 0.967 | 0.9364 | 0.9977 |
| 10 | log_polar | 0.9988 | 0.9986 | 0.9989 |
| 10 | polar | 0.4979 | 0 | 0.9987 |