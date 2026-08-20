# harvest-8way-r1264 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1264 ctrl_bpc |
|--------|--------|--------------:|
| WTayf | fork-slaa-us-mmllm-claude-train-sym24-ec37054e-WTayf | 2.2423 |
| 4LaQo | origin/claude/train-sym24-14befd81-4LaQo | 2.2462 |
| TEgC9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-833a9a5b-TEgC9 | 2.2480 |
| NuCYZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-52492907-NuCYZ | 2.2521 |
| N38l2 | fork-joly-os-mmllm-claude-train-sym24-1014014a-N38l2 | 2.2541 |
| uyddq | fork-SeniorCareMarket-mmllm-claude-train-sym24-52273b20-uyddq | 2.2559 |
| 63lcc | fork-slaa-us-mmllm-claude-train-sym24-0ee2815e-63lcc | 2.4267 |
| IMEc2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-de3902ff-IMEc2 | 2.6356 |
| **mean** | | **2.3201** |
| **best** | | **2.2423** |

## Chain progression R1263 → R1264

Previous harvest: `workers/dispatcher/harvest-6way-r1263_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4303         | 2.3201         | -0.1102 |
| ctrl_bpc best  | 2.2288         | 2.2423         | +0.0135 |

## Per-round trajectory (best bird: WTayf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1264 | 3556 | 2.2423 | +0.2497 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1263_sym24`
  - `workers/dispatcher/harvest-6way-r1263_sym24`

## Output

`workers/dispatcher/harvest-8way-r1264_sym24/round-1264/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

