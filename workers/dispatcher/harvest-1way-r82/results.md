# harvest-1way-r82 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R82 ctrl_bpc |
|--------|--------|--------------:|
| ODj8e | origin/claude/train-92566bd5-ODj8e | 0.9991 |
| **mean** | | **0.9991** |
| **best** | | **0.9991** |

## Chain progression R81 → R82

Previous harvest: `workers/dispatcher/harvest-1way-r81`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9555         | 0.9991         | +0.0436 |
| ctrl_bpc best  | 0.9555         | 0.9991         | +0.0436 |

## Per-round trajectory (best bird: ODj8e)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 80 | 319 | 0.9863 | +0.0078 |
| 81 | 284 | 0.9555 | +0.0054 |
| 82 | 259 | 0.9991 | +0.0142 |

## Cumulative training contribution

- This harvest: **9 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1698 steps** from 42 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r79`

## Output

`workers/dispatcher/harvest-1way-r82/round-82/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

