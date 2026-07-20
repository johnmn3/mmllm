# harvest-1way-r976 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R976 ctrl_bpc |
|--------|--------|--------------:|
| 8bZiW | origin/claude/train-sym24-6bd2b070-8bZiW | 2.6229 |
| **mean** | | **2.6229** |
| **best** | | **2.6229** |

## Chain progression R975 → R976

Previous harvest: `workers/dispatcher/harvest-2way-r975_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8148         | 2.6229         | -0.1919 |
| ctrl_bpc best  | 2.6027         | 2.6229         | +0.0202 |

## Per-round trajectory (best bird: 8bZiW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 976 | 6775 | 2.6229 | +0.1820 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r975_sym24`

## Output

`workers/dispatcher/harvest-1way-r976_sym24/round-976/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

