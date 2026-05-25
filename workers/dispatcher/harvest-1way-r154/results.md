# harvest-1way-r154 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R154 ctrl_bpc |
|--------|--------|--------------:|
| S1agg | origin/claude/train-3c2229be-S1agg | 0.9745 |
| **mean** | | **0.9745** |
| **best** | | **0.9745** |

## Chain progression R152 → R154

Previous harvest: `workers/dispatcher/harvest-4way-r152`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0417         | 0.9745         | -0.0672 |
| ctrl_bpc best  | 0.9766         | 0.9745         | -0.0021 |

## Per-round trajectory (best bird: S1agg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 153 | 566 | 0.9924 | +0.0025 |
| 154 | 545 | 0.9745 | +0.0029 |

## Cumulative training contribution

- This harvest: **14 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3425 steps** from 94 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r152`

## Output

`workers/dispatcher/harvest-1way-r154/round-154/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

