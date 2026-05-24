# harvest-1way-r114 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R114 ctrl_bpc |
|--------|--------|--------------:|
| N7VrV | fork-SeniorCareMarket-mmllm-claude-train-48b190d9-N7VrV | 0.9911 |
| **mean** | | **0.9911** |
| **best** | | **0.9911** |

## Chain progression R111 → R114

Previous harvest: `workers/dispatcher/harvest-1way-r111`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0171         | 0.9911         | -0.0260 |
| ctrl_bpc best  | 1.0171         | 0.9911         | -0.0260 |

## Per-round trajectory (best bird: N7VrV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 112 | 641 | 0.9941 | +0.0041 |
| 113 | 510 | 0.9894 | +0.0038 |
| 114 | 554 | 0.9911 | +0.0025 |

## Cumulative training contribution

- This harvest: **21 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **2473 steps** from 64 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r111`

## Output

`workers/dispatcher/harvest-1way-r114/round-114/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

