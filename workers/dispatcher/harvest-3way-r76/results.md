# harvest-3way-r76 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R76 ctrl_bpc |
|--------|--------|--------------:|
| 10U2d | fork-joly-os-mmllm-claude-train-232cb928-10U2d | 0.9654 |
| aswkZ | fork-SeniorCareMarket-mmllm-claude-train-842f9c8a-aswkZ | 0.9811 |
| RdNcz | fork-SeniorCareMarket-com-mmllm-claude-train-275c1ec2-RdNcz | 1.0610 |
| **mean** | | **1.0025** |
| **best** | | **0.9654** |

## Chain progression R71 → R76

Previous harvest: `workers/dispatcher/harvest-1way-r71`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0580         | 1.0025         | -0.0555 |
| ctrl_bpc best  | 1.0580         | 0.9654         | -0.0926 |

## Per-round trajectory (best bird: 10U2d)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 72 | 523 | 0.9661 | +0.0063 |
| 73 | 541 | 0.9565 | +0.0026 |
| 74 | 548 | 0.9497 | +0.0053 |
| 75 | 564 | 0.9775 | +0.0066 |
| 76 | 534 | 0.9654 | +0.0099 |

## Cumulative training contribution

- This harvest: **105 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **490 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r71`

## Output

`workers/dispatcher/harvest-3way-r76/round-76/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

