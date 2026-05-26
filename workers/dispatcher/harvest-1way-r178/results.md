# harvest-1way-r178 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R178 ctrl_bpc |
|--------|--------|--------------:|
| Q3Pi0 | origin/claude/train-38f7a3fa-Q3Pi0 | 1.2355 |
| **mean** | | **1.2355** |
| **best** | | **1.2355** |

## Chain progression R177 → R178

Previous harvest: `workers/dispatcher/harvest-1way-r177`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1974         | 1.2355         | +0.0381 |
| ctrl_bpc best  | 1.1974         | 1.2355         | +0.0381 |

## Per-round trajectory (best bird: Q3Pi0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 178 | 595 | 1.2355 | -0.0040 |

## Cumulative training contribution

- This harvest: **7 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3593 steps** from 99 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r177`

## Output

`workers/dispatcher/harvest-1way-r178/round-178/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

