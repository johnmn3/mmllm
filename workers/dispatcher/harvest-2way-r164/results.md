# harvest-2way-r164 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R164 ctrl_bpc |
|--------|--------|--------------:|
| 0RtZO | origin/claude/train-52002fa8-0RtZO | 1.0762 |
| 3Yp49 | origin/claude/train-7886084f-3Yp49 | 1.0862 |
| **mean** | | **1.0812** |
| **best** | | **1.0762** |

## Chain progression R162 → R164

Previous harvest: `workers/dispatcher/harvest-1way-r162`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0466         | 1.0812         | +0.0346 |
| ctrl_bpc best  | 1.0466         | 1.0762         | +0.0296 |

## Per-round trajectory (best bird: 0RtZO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 163 | 594 | 1.0470 | +0.0042 |
| 164 | 565 | 1.0762 | -0.0031 |

## Cumulative training contribution

- This harvest: **49 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **3565 steps** from 98 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r159`
  - `workers/dispatcher/harvest-1way-r162`

## Output

`workers/dispatcher/harvest-2way-r164/round-164/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

