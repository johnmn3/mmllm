# harvest-1way-r844 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R844 ctrl_bpc |
|--------|--------|--------------:|
| 59SP9 | origin/claude/train-sym24-cf61e8dd-59SP9 | 2.9527 |
| **mean** | | **2.9527** |
| **best** | | **2.9527** |

## Chain progression R843 → R844

Previous harvest: `workers/dispatcher/harvest-3way-r843_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0021         | 2.9527         | -0.0494 |
| ctrl_bpc best  | 2.9531         | 2.9527         | -0.0004 |

## Per-round trajectory (best bird: 59SP9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 844 | 6745 | 2.9527 | +0.2917 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r843_sym24`

## Output

`workers/dispatcher/harvest-1way-r844_sym24/round-844/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

