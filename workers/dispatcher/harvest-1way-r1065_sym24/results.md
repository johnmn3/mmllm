# harvest-1way-r1065 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1065 ctrl_bpc |
|--------|--------|--------------:|
| 0AyT3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d413872d-0AyT3 | 2.8882 |
| **mean** | | **2.8882** |
| **best** | | **2.8882** |

## Chain progression R1064 → R1065

Previous harvest: `workers/dispatcher/harvest-3way-r1064_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7755         | 2.8882         | +0.1127 |
| ctrl_bpc best  | 2.6413         | 2.8882         | +0.2469 |

## Per-round trajectory (best bird: 0AyT3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1065 | 3997 | 2.8882 | +0.1966 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1064_sym24`

## Output

`workers/dispatcher/harvest-1way-r1065_sym24/round-1065/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

