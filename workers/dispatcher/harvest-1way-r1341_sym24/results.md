# harvest-1way-r1341 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1341 ctrl_bpc |
|--------|--------|--------------:|
| 07b9b | origin/claude/train-sym24-572c15ed-07b9b | 3.3261 |
| **mean** | | **3.3261** |
| **best** | | **3.3261** |

## Chain progression R1340 → R1341

Previous harvest: `workers/dispatcher/harvest-1way-r1340_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3884         | 3.3261         | -0.0623 |
| ctrl_bpc best  | 3.3884         | 3.3261         | -0.0623 |

## Per-round trajectory (best bird: 07b9b)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1341 | 6257 | 3.3261 | +0.1050 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1340_sym24`

## Output

`workers/dispatcher/harvest-1way-r1341_sym24/round-1341/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

