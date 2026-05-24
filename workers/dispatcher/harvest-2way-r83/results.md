# harvest-2way-r83 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R83 ctrl_bpc |
|--------|--------|--------------:|
| 4HjHZ | origin/claude/train-295e8c64-4HjHZ | 0.9346 |
| gl5I6 | origin/claude/train-19933e65-gl5I6 | 1.1031 |
| **mean** | | **1.0189** |
| **best** | | **0.9346** |

## Chain progression R82 → R83

Previous harvest: `workers/dispatcher/harvest-1way-r82`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9991         | 1.0189         | +0.0198 |
| ctrl_bpc best  | 0.9991         | 0.9346         | -0.0645 |

## Per-round trajectory (best bird: 4HjHZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 83 | 3602 | 0.9346 | +0.0069 |

## Cumulative training contribution

- This harvest: **100 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1798 steps** from 44 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r82`

## Output

`workers/dispatcher/harvest-2way-r83/round-83/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

