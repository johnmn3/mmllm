# harvest-1way-r174 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R174 ctrl_bpc |
|--------|--------|--------------:|
| qBl9H | origin/claude/train-3a9bf8e0-qBl9H | 1.1284 |
| **mean** | | **1.1284** |
| **best** | | **1.1284** |

## Chain progression R172 → R174

Previous harvest: `workers/dispatcher/harvest-fold2way-r172`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1650         | 1.1284         | -0.0366 |
| ctrl_bpc best  | 1.1625         | 1.1284         | -0.0341 |

## Per-round trajectory (best bird: qBl9H)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 173 | 592 | 1.1504 | -0.0002 |
| 174 | 536 | 1.1284 | +0.0026 |

## Cumulative training contribution

- This harvest: **14 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3565 steps** from 98 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r172`

## Output

`workers/dispatcher/harvest-1way-r174/round-174/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

