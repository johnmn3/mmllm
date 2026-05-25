# harvest-1way-r147 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R147 ctrl_bpc |
|--------|--------|--------------:|
| Niqqj | origin/claude/train-697bde5c-Niqqj | 1.0663 |
| **mean** | | **1.0663** |
| **best** | | **1.0663** |

## Chain progression R145 → R147

Previous harvest: `workers/dispatcher/harvest-fold5way-r145`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0669         | 1.0663         | -0.0006 |
| ctrl_bpc best  | 1.0524         | 1.0663         | +0.0139 |

## Per-round trajectory (best bird: Niqqj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 146 | 603 | 1.0667 | +0.0008 |
| 147 | 548 | 1.0663 | +0.0049 |

## Cumulative training contribution

- This harvest: **14 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3271 steps** from 89 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r145`

## Output

`workers/dispatcher/harvest-1way-r147/round-147/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

