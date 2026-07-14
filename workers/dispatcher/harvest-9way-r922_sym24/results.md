# harvest-9way-r922 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R922 ctrl_bpc |
|--------|--------|--------------:|
| 5zOyL | fork-SeniorCareMarket-mmllm-claude-train-sym24-72fa4f50-5zOyL | 2.7258 |
| HsU9o | origin/claude/train-sym24-fa047d7c-HsU9o | 2.7261 |
| hUwPi | fork-slaa-us-mmllm-claude-train-sym24-a5120951-hUwPi | 2.7431 |
| WYN2l | fork-joly-os-mmllm-claude-train-sym24-22716c9d-WYN2l | 2.7438 |
| E3nA4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-03f6846c-E3nA4 | 2.7460 |
| uM9Ud | origin/claude/train-sym24-0e3a797d-uM9Ud | 2.7557 |
| EIL5f | origin/claude/train-sym24-c510373b-EIL5f | 2.7596 |
| xnbxI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cc05e69c-xnbxI | 3.1176 |
| IZb0F | fork-joly-os-mmllm-claude-train-sym24-83dda418-IZb0F | 3.1329 |
| **mean** | | **2.8278** |
| **best** | | **2.7258** |

## Chain progression R921 → R922

Previous harvest: `workers/dispatcher/harvest-6way-r921_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9499         | 2.8278         | -0.1221 |
| ctrl_bpc best  | 2.7224         | 2.7258         | +0.0034 |

## Per-round trajectory (best bird: 5zOyL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 922 | 4409 | 2.7258 | +0.2053 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r921_sym24`
  - `workers/dispatcher/harvest-2way-r921_sym24`
  - `workers/dispatcher/harvest-6way-r921_sym24`

## Output

`workers/dispatcher/harvest-9way-r922_sym24/round-922/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

