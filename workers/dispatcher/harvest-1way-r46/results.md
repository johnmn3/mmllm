# harvest-1way-r46 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R46 ctrl_bpc |
|--------|--------|--------------:|
| xPume | origin/claude/train-187df731-xPume | 0.9623 |
| **mean** | | **0.9623** |
| **best** | | **0.9623** |

## Chain progression R41 → R46

Previous harvest: `workers/dispatcher/harvest-1way-r41`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1498         | 0.9623         | -0.1875 |
| ctrl_bpc best  | 1.1498         | 0.9623         | -0.1875 |

## Per-round trajectory (best bird: xPume)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 42 | 568 | 1.0819 | +0.0045 |
| 43 | 526 | 1.0548 | +0.0044 |
| 44 | 543 | 1.0034 | +0.0052 |
| 45 | 519 | 1.0039 | +0.0110 |
| 46 | 552 | 0.9623 | +0.0042 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **210 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r41`

## Output

`workers/dispatcher/harvest-1way-r46/round-46/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

