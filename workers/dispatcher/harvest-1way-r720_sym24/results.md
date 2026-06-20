# harvest-1way-r720 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R720 ctrl_bpc |
|--------|--------|--------------:|
| Up0hm | origin/claude/train-sym24-b1577add-Up0hm | 3.5431 |
| **mean** | | **3.5431** |
| **best** | | **3.5431** |

## Chain progression R719 → R720

Previous harvest: `workers/dispatcher/harvest-2way-r719_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7123         | 3.5431         | -0.1692 |
| ctrl_bpc best  | 3.5482         | 3.5431         | -0.0051 |

## Per-round trajectory (best bird: Up0hm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 720 | 5294 | 3.5431 | +0.8179 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r719_sym24`

## Output

`workers/dispatcher/harvest-1way-r720_sym24/round-720/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

