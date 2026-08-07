# harvest-1way-r1132 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1132 ctrl_bpc |
|--------|--------|--------------:|
| p6JZh | origin/claude/train-sym24-b8038002-p6JZh | 2.3774 |
| **mean** | | **2.3774** |
| **best** | | **2.3774** |

## Chain progression R1131 → R1132

Previous harvest: `workers/dispatcher/harvest-4way-r1131_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5097         | 2.3774         | -0.1323 |
| ctrl_bpc best  | 2.3510         | 2.3774         | +0.0264 |

## Per-round trajectory (best bird: p6JZh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1132 | 3626 | 2.3774 | +0.2518 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1131_sym24`

## Output

`workers/dispatcher/harvest-1way-r1132_sym24/round-1132/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

