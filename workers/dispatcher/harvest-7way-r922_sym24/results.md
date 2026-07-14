# harvest-7way-r922 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R922 ctrl_bpc |
|--------|--------|--------------:|
| 5zOyL | fork-SeniorCareMarket-mmllm-claude-train-sym24-72fa4f50-5zOyL | 2.7258 |
| hUwPi | fork-slaa-us-mmllm-claude-train-sym24-a5120951-hUwPi | 2.7431 |
| WYN2l | fork-joly-os-mmllm-claude-train-sym24-22716c9d-WYN2l | 2.7438 |
| uM9Ud | origin/claude/train-sym24-0e3a797d-uM9Ud | 2.7557 |
| EIL5f | origin/claude/train-sym24-c510373b-EIL5f | 2.7596 |
| xnbxI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cc05e69c-xnbxI | 3.1176 |
| IZb0F | fork-joly-os-mmllm-claude-train-sym24-83dda418-IZb0F | 3.1329 |
| **mean** | | **2.8541** |
| **best** | | **2.7258** |

## Chain progression R921 → R922

Previous harvest: `workers/dispatcher/harvest-6way-r921_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9499         | 2.8541         | -0.0958 |
| ctrl_bpc best  | 2.7224         | 2.7258         | +0.0034 |

## Per-round trajectory (best bird: 5zOyL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 922 | 4409 | 2.7258 | +0.2053 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r921_sym24`
  - `workers/dispatcher/harvest-6way-r921_sym24`

## Output

`workers/dispatcher/harvest-7way-r922_sym24/round-922/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

