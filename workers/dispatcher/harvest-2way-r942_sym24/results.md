# harvest-2way-r942 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R942 ctrl_bpc |
|--------|--------|--------------:|
| cwfQ3 | fork-slaa-us-mmllm-claude-train-sym24-16066d87-cwfQ3 | 2.8853 |
| am2qy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9021aede-am2qy | 3.0825 |
| **mean** | | **2.9839** |
| **best** | | **2.8853** |

## Chain progression R941 → R942

Previous harvest: `workers/dispatcher/harvest-4way-r941_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7404         | 2.9839         | +0.2435 |
| ctrl_bpc best  | 2.6712         | 2.8853         | +0.2141 |

## Per-round trajectory (best bird: cwfQ3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 942 | 6395 | 2.8853 | +0.1685 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r941_sym24`
  - `workers/dispatcher/harvest-4way-r941_sym24`

## Output

`workers/dispatcher/harvest-2way-r942_sym24/round-942/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

