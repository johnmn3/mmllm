# harvest-4way-r1180 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1180 ctrl_bpc |
|--------|--------|--------------:|
| 2L2tO | fork-slaa-us-mmllm-claude-train-sym24-7e81165b-2L2tO | 2.3203 |
| o3ZRd | fork-SeniorCareMarket-mmllm-claude-train-sym24-fb947848-o3ZRd | 2.3210 |
| dc4HU | origin/claude/train-sym24-bebab2ed-dc4HU | 2.5150 |
| CBhJb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a904ad88-CBhJb | 2.6889 |
| **mean** | | **2.4613** |
| **best** | | **2.3203** |

## Chain progression R1179 → R1180

Previous harvest: `workers/dispatcher/harvest-3way-r1179_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5826         | 2.4613         | -0.1213 |
| ctrl_bpc best  | 2.3190         | 2.3203         | +0.0013 |

## Per-round trajectory (best bird: 2L2tO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1180 | 6636 | 2.3203 | +0.2445 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1179_sym24`

## Output

`workers/dispatcher/harvest-4way-r1180_sym24/round-1180/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

