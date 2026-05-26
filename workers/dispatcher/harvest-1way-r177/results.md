# harvest-1way-r177 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R177 ctrl_bpc |
|--------|--------|--------------:|
| qBl9H | origin/claude/train-3a9bf8e0-qBl9H | 1.1974 |
| **mean** | | **1.1974** |
| **best** | | **1.1974** |

## Chain progression R174 → R177

Previous harvest: `workers/dispatcher/harvest-1way-r174`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1284         | 1.1974         | +0.0690 |
| ctrl_bpc best  | 1.1284         | 1.1974         | +0.0690 |

## Per-round trajectory (best bird: qBl9H)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 173 | 592 | 1.1504 | -0.0002 |
| 174 | 536 | 1.1284 | +0.0026 |
| 175 | 553 | 1.1112 | +0.0012 |
| 176 | 583 | 1.1550 | -0.0031 |
| 177 | 533 | 1.1974 | -0.0052 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3586 steps** from 98 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r172`

## Output

`workers/dispatcher/harvest-1way-r177/round-177/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

