# harvest-1way-r157 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R157 ctrl_bpc |
|--------|--------|--------------:|
| S1agg | origin/claude/train-3c2229be-S1agg | 0.9905 |
| **mean** | | **0.9905** |
| **best** | | **0.9905** |

## Chain progression R154 → R157

Previous harvest: `workers/dispatcher/harvest-1way-r154`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9745         | 0.9905         | +0.0160 |
| ctrl_bpc best  | 0.9745         | 0.9905         | +0.0160 |

## Per-round trajectory (best bird: S1agg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 153 | 566 | 0.9924 | +0.0025 |
| 154 | 545 | 0.9745 | +0.0029 |
| 155 | 535 | 0.9473 | +0.0021 |
| 156 | 570 | 0.9755 | +0.0031 |
| 157 | 527 | 0.9905 | +0.0028 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3446 steps** from 94 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r152`

## Output

`workers/dispatcher/harvest-1way-r157/round-157/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

