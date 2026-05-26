# harvest-1way-r167 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R167 ctrl_bpc |
|--------|--------|--------------:|
| 0RtZO | origin/claude/train-52002fa8-0RtZO | 1.0898 |
| **mean** | | **1.0898** |
| **best** | | **1.0898** |

## Chain progression R164 → R167

Previous harvest: `workers/dispatcher/harvest-2way-r164`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0812         | 1.0898         | +0.0086 |
| ctrl_bpc best  | 1.0762         | 1.0898         | +0.0136 |

## Per-round trajectory (best bird: 0RtZO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 163 | 594 | 1.0470 | +0.0042 |
| 164 | 565 | 1.0762 | -0.0031 |
| 165 | 527 | 1.0694 | +0.0011 |
| 166 | 538 | 1.1284 | +0.0027 |
| 167 | 553 | 1.0898 | +0.0009 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3516 steps** from 96 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r162`

## Output

`workers/dispatcher/harvest-1way-r167/round-167/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

