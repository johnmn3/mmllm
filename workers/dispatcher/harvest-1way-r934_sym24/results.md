# harvest-1way-r934 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R934 ctrl_bpc |
|--------|--------|--------------:|
| t7PrQ | origin/claude/train-sym24-474844f3-t7PrQ | 3.1254 |
| **mean** | | **3.1254** |
| **best** | | **3.1254** |

## Chain progression R933 → R934

Previous harvest: `workers/dispatcher/harvest-4way-r933_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7984         | 3.1254         | +0.3270 |
| ctrl_bpc best  | 2.6912         | 3.1254         | +0.4342 |

## Per-round trajectory (best bird: t7PrQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 934 | 6507 | 3.1254 | +0.1901 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r933_sym24`

## Output

`workers/dispatcher/harvest-1way-r934_sym24/round-934/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

