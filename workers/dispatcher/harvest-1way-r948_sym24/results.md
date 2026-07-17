# harvest-1way-r948 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R948 ctrl_bpc |
|--------|--------|--------------:|
| ZYCEq | origin/claude/train-sym24-a7fe35dc-ZYCEq | 2.8651 |
| **mean** | | **2.8651** |
| **best** | | **2.8651** |

## Chain progression R947 → R948

Previous harvest: `workers/dispatcher/harvest-3way-r947_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7974         | 2.8651         | +0.0677 |
| ctrl_bpc best  | 2.6663         | 2.8651         | +0.1988 |

## Per-round trajectory (best bird: ZYCEq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 948 | 4209 | 2.8651 | +0.1211 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r947_sym24`

## Output

`workers/dispatcher/harvest-1way-r948_sym24/round-948/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

