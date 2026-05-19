# harvest-1way-r30 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R30 ctrl_bpc |
|--------|--------|--------------:|
| DEQ1e | fork-SeniorCareMarket-mmllm-claude-train-0dbc85b5-DEQ1e | 1.1424 |
| **mean** | | **1.1424** |
| **best** | | **1.1424** |

## Chain progression R27 → R30

Previous harvest: `workers/dispatcher/harvest-2way-r27`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1103         | 1.1424         | +0.0321 |
| ctrl_bpc best  | 1.1073         | 1.1424         | +0.0351 |

## Per-round trajectory (best bird: DEQ1e)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 28 | 727 | 1.0855 | +0.0086 |
| 29 | 738 | 1.1287 | +0.0112 |
| 30 | 723 | 1.1424 | +0.0060 |

## Cumulative training contribution

- This harvest: **21 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **21 steps** from 1 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r27`

## Output

`workers/dispatcher/harvest-1way-r30/round-30/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

