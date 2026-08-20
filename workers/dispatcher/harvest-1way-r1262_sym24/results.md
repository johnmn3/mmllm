# harvest-1way-r1262 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1262 ctrl_bpc |
|--------|--------|--------------:|
| 1WClJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-95c5568a-1WClJ | 2.2318 |
| **mean** | | **2.2318** |
| **best** | | **2.2318** |

## Chain progression R1261 → R1262

Previous harvest: `workers/dispatcher/harvest-6way-r1261_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4089         | 2.2318         | -0.1771 |
| ctrl_bpc best  | 2.2392         | 2.2318         | -0.0074 |

## Per-round trajectory (best bird: 1WClJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1262 | 4475 | 2.2318 | +0.2602 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1261_sym24`

## Output

`workers/dispatcher/harvest-1way-r1262_sym24/round-1262/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

