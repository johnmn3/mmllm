# harvest-1way-r162 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R162 ctrl_bpc |
|--------|--------|--------------:|
| 9SFH5 | origin/claude/train-4963bd41-9SFH5 | 1.0466 |
| **mean** | | **1.0466** |
| **best** | | **1.0466** |

## Chain progression R159 → R162

Previous harvest: `workers/dispatcher/harvest-1way-r159`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0770         | 1.0466         | -0.0304 |
| ctrl_bpc best  | 1.0770         | 1.0466         | -0.0304 |

## Per-round trajectory (best bird: 9SFH5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 158 | 574 | 0.9799 | +0.0026 |
| 159 | 577 | 1.0477 | +0.0037 |
| 160 | 520 | 0.9988 | +0.0030 |
| 161 | 527 | 1.0251 | +0.0041 |
| 162 | 547 | 1.0466 | +0.0005 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3481 steps** from 95 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r157`

## Output

`workers/dispatcher/harvest-1way-r162/round-162/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

