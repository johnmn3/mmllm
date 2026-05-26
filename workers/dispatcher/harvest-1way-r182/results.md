# harvest-1way-r182 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R182 ctrl_bpc |
|--------|--------|--------------:|
| Q3Pi0 | origin/claude/train-38f7a3fa-Q3Pi0 | 1.1746 |
| **mean** | | **1.1746** |
| **best** | | **1.1746** |

## Chain progression R178 → R182

Previous harvest: `workers/dispatcher/harvest-1way-r178`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.2355         | 1.1746         | -0.0609 |
| ctrl_bpc best  | 1.2355         | 1.1746         | -0.0609 |

## Per-round trajectory (best bird: Q3Pi0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 178 | 595 | 1.2355 | -0.0040 |
| 179 | 540 | 1.2017 | -0.0028 |
| 180 | 541 | 1.2180 | -0.0053 |
| 181 | 552 | 1.1789 | +0.0008 |
| 182 | 514 | 1.1746 | -0.0007 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3621 steps** from 99 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r177`

## Output

`workers/dispatcher/harvest-1way-r182/round-182/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

