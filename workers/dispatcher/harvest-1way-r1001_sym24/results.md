# harvest-1way-r1001 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1001 ctrl_bpc |
|--------|--------|--------------:|
| 5DWu3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bfbc8f93-5DWu3 | 2.9496 |
| **mean** | | **2.9496** |
| **best** | | **2.9496** |

## Chain progression R1000 → R1001

Previous harvest: `workers/dispatcher/harvest-5way-r1000_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7252         | 2.9496         | +0.2244 |
| ctrl_bpc best  | 2.5585         | 2.9496         | +0.3911 |

## Per-round trajectory (best bird: 5DWu3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1001 | 6515 | 2.9496 | +0.1570 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1000_sym24`

## Output

`workers/dispatcher/harvest-1way-r1001_sym24/round-1001/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

