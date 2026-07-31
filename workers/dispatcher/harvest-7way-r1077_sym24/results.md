# harvest-7way-r1077 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1077 ctrl_bpc |
|--------|--------|--------------:|
| uS29O | origin/claude/train-sym24-7b22c5ee-uS29O | 2.4575 |
| 8cFEt | fork-SeniorCareMarket-mmllm-claude-train-sym24-9cf87157-8cFEt | 2.4653 |
| u55TY | fork-joly-os-mmllm-claude-train-sym24-aaaa0d62-u55TY | 2.4670 |
| 83WDi | fork-slaa-us-mmllm-claude-train-sym24-f6cb13c1-83WDi | 2.4702 |
| s8oCZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-72c239bb-s8oCZ | 2.6129 |
| EETuK | fork-slaa-us-mmllm-claude-train-sym24-ba53b3ad-EETuK | 2.6217 |
| ZNcFf | origin/claude/train-sym24-356be1bb-ZNcFf | 2.6223 |
| **mean** | | **2.5310** |
| **best** | | **2.4575** |

## Chain progression R1076 → R1077

Previous harvest: `workers/dispatcher/harvest-6way-r1076_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5413         | 2.5310         | -0.0103 |
| ctrl_bpc best  | 2.4328         | 2.4575         | +0.0247 |

## Per-round trajectory (best bird: uS29O)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1077 | 6801 | 2.4575 | +0.2192 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1076_sym24`
  - `workers/dispatcher/harvest-4way-r1076_sym24`

## Output

`workers/dispatcher/harvest-7way-r1077_sym24/round-1077/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

