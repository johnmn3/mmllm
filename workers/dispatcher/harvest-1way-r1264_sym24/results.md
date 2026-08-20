# harvest-1way-r1264 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1264 ctrl_bpc |
|--------|--------|--------------:|
| NuCYZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-52492907-NuCYZ | 2.2521 |
| **mean** | | **2.2521** |
| **best** | | **2.2521** |

## Chain progression R1263 → R1264

Previous harvest: `workers/dispatcher/harvest-6way-r1263_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4303         | 2.2521         | -0.1782 |
| ctrl_bpc best  | 2.2288         | 2.2521         | +0.0233 |

## Per-round trajectory (best bird: NuCYZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1264 | 5373 | 2.2521 | +0.2428 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1263_sym24`

## Output

`workers/dispatcher/harvest-1way-r1264_sym24/round-1264/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

