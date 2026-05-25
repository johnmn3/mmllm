# harvest-1way-r159 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R159 ctrl_bpc |
|--------|--------|--------------:|
| XwN3J | origin/claude/train-9de6d41c-XwN3J | 1.0770 |
| **mean** | | **1.0770** |
| **best** | | **1.0770** |

## Chain progression R157 → R159

Previous harvest: `workers/dispatcher/harvest-fold2way-r157`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0132         | 1.0770         | +0.0638 |
| ctrl_bpc best  | 0.9905         | 1.0770         | +0.0865 |

## Per-round trajectory (best bird: XwN3J)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 155 | 574 | 1.0297 | +0.0033 |
| 156 | 540 | 1.0279 | +0.0046 |
| 157 | 515 | 1.0820 | +0.0039 |
| 158 | 564 | 1.0620 | +0.0055 |
| 159 | 508 | 1.0770 | +0.0004 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3460 steps** from 95 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r154`

## Output

`workers/dispatcher/harvest-1way-r159/round-159/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

