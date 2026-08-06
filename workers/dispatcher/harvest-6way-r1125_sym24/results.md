# harvest-6way-r1125 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1125 ctrl_bpc |
|--------|--------|--------------:|
| kyJbL | fork-SeniorCareMarket-mmllm-claude-train-sym24-3605f7d1-kyJbL | 2.3826 |
| Gf0li | origin/claude/train-sym24-85200554-Gf0li | 2.3852 |
| U9AoE | origin/claude/train-sym24-e93cf387-U9AoE | 2.5513 |
| XnMFV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3237fde9-XnMFV | 2.5639 |
| hZqWI | fork-slaa-us-mmllm-claude-train-sym24-777e5839-hZqWI | 2.5777 |
| Y1Go7 | fork-joly-os-mmllm-claude-train-sym24-3efdae5a-Y1Go7 | 2.7563 |
| **mean** | | **2.5362** |
| **best** | | **2.3826** |

## Chain progression R1124 → R1125

Previous harvest: `workers/dispatcher/harvest-3way-r1124_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3791         | 2.5362         | +0.1571 |
| ctrl_bpc best  | 2.3630         | 2.3826         | +0.0196 |

## Per-round trajectory (best bird: kyJbL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1125 | 3986 | 2.3826 | +0.2395 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1124_sym24`
  - `workers/dispatcher/harvest-3way-r1124_sym24`

## Output

`workers/dispatcher/harvest-6way-r1125_sym24/round-1125/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

