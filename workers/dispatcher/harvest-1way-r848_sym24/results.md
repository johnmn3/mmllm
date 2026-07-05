# harvest-1way-r848 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R848 ctrl_bpc |
|--------|--------|--------------:|
| IlADd | fork-SeniorCareMarket-mmllm-claude-train-sym24-a5262a87-IlADd | 3.3086 |
| **mean** | | **3.3086** |
| **best** | | **3.3086** |

## Chain progression R847 → R848

Previous harvest: `workers/dispatcher/harvest-1way-r847_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3164         | 3.3086         | -0.0078 |
| ctrl_bpc best  | 3.3164         | 3.3086         | -0.0078 |

## Per-round trajectory (best bird: IlADd)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 848 | 4402 | 3.3086 | +0.3267 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r847_sym24`

## Output

`workers/dispatcher/harvest-1way-r848_sym24/round-848/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

