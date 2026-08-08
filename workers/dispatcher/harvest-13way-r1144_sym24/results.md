# harvest-13way-r1144 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R1144 ctrl_bpc |
|--------|--------|--------------:|
| Lb5fC | fork-joly-os-mmllm-claude-train-sym24-f2225729-Lb5fC | 2.3381 |
| lkGKz | fork-joly-os-mmllm-claude-train-sym24-8cdab328-lkGKz | 2.3476 |
| tuAM0 | origin/claude/train-sym24-478c4b48-tuAM0 | 2.3542 |
| 130bk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3988456d-130bk | 2.3545 |
| ryt4T | fork-slaa-us-mmllm-claude-train-sym24-a72f1168-ryt4T | 2.3660 |
| ROXfV | fork-slaa-us-mmllm-claude-train-sym24-927a2541-ROXfV | 2.3672 |
| kH8E9 | fork-slaa-us-mmllm-claude-train-sym24-29d98f50-kH8E9 | 2.4606 |
| EIDrh | fork-SeniorCareMarket-mmllm-claude-train-sym24-37705e71-EIDrh | 2.5396 |
| 4w13o | origin/claude/train-sym24-5365ec5f-4w13o | 2.5418 |
| R9zB1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bb8ef9e3-R9zB1 | 2.5428 |
| WLiGc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-baf4f6a4-WLiGc | 2.5452 |
| 8n4KI | fork-SeniorCareMarket-mmllm-claude-train-sym24-efb4e9cb-8n4KI | 2.7340 |
| ZFBYl | fork-SeniorCareMarket-mmllm-claude-train-sym24-a38d95a1-ZFBYl | 2.7446 |
| **mean** | | **2.4797** |
| **best** | | **2.3381** |

## Chain progression R1143 → R1144

Previous harvest: `workers/dispatcher/harvest-5way-r1143_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5017         | 2.4797         | -0.0220 |
| ctrl_bpc best  | 2.3442         | 2.3381         | -0.0061 |

## Per-round trajectory (best bird: Lb5fC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1144 | 6707 | 2.3381 | +0.2583 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r1143_sym24`
  - `workers/dispatcher/harvest-17way-r1143_sym24`
  - `workers/dispatcher/harvest-5way-r1143_sym24`

## Output

`workers/dispatcher/harvest-13way-r1144_sym24/round-1144/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

