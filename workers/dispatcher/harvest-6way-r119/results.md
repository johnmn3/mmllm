# harvest-6way-r119 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R119 ctrl_bpc |
|--------|--------|--------------:|
| 3iAe3 | fork-SeniorCareMarket-mmllm-claude-train-73900efa-3iAe3 | 0.9135 |
| imI4z | fork-slaa-us-mmllm-claude-train-c3bf9094-imI4z | 0.9492 |
| jluuX | fork-davidwuchn-mmllm-claude-train-de3bc027-jluuX | 1.0205 |
| DImim | origin/claude/train-8f74367f-DImim | 1.0801 |
| sxjo8 | fork-SeniorCareMarket-com-mmllm-claude-train-882c5202-sxjo8 | 1.1011 |
| 7xhjN | fork-joly-os-mmllm-claude-train-7af65402-7xhjN | 1.1178 |
| **mean** | | **1.0304** |
| **best** | | **0.9135** |

## Chain progression R116 → R119

Previous harvest: `workers/dispatcher/harvest-5way-r116`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9853         | 1.0304         | +0.0451 |
| ctrl_bpc best  | 0.9211         | 0.9135         | -0.0076 |

## Per-round trajectory (best bird: 3iAe3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 115 | 591 | 0.9621 | +0.0078 |
| 116 | 516 | 0.9391 | +0.0102 |
| 117 | 509 | 0.9503 | +0.0020 |
| 118 | 541 | 0.9197 | +0.0068 |
| 119 | 526 | 0.9135 | +0.0043 |

## Cumulative training contribution

- This harvest: **210 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **2683 steps** from 70 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r114`

## Output

`workers/dispatcher/harvest-6way-r119/round-119/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

