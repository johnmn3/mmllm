# harvest-1way-r1142 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1142 ctrl_bpc |
|--------|--------|--------------:|
| MDMt1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-73910d80-MDMt1 | 2.8014 |
| **mean** | | **2.8014** |
| **best** | | **2.8014** |

## Chain progression R1141 → R1142

Previous harvest: `workers/dispatcher/harvest-7way-r1141_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5410         | 2.8014         | +0.2604 |
| ctrl_bpc best  | 2.3417         | 2.8014         | +0.4597 |

## Per-round trajectory (best bird: MDMt1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1142 | 4081 | 2.8014 | +0.2134 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1141_sym24`

## Output

`workers/dispatcher/harvest-1way-r1142_sym24/round-1142/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

