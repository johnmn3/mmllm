# harvest-1way-r1333 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1333 ctrl_bpc |
|--------|--------|--------------:|
| IybJ1 | origin/claude/train-sym24-7411d82c-IybJ1 | 3.3198 |
| **mean** | | **3.3198** |
| **best** | | **3.3198** |

## Chain progression R1332 → R1333

Previous harvest: `workers/dispatcher/harvest-2way-r1332_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3550         | 3.3198         | -0.0352 |
| ctrl_bpc best  | 3.3489         | 3.3198         | -0.0291 |

## Per-round trajectory (best bird: IybJ1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1333 | 6312 | 3.3198 | +0.0828 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1332_sym24`

## Output

`workers/dispatcher/harvest-1way-r1333_sym24/round-1333/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

