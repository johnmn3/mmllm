# harvest-1way-r1099 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1099 ctrl_bpc |
|--------|--------|--------------:|
| 9mkO6 | origin/claude/train-sym24-e8da2d89-9mkO6 | 2.6021 |
| **mean** | | **2.6021** |
| **best** | | **2.6021** |

## Chain progression R1098 → R1099

Previous harvest: `workers/dispatcher/harvest-4way-r1098_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4160         | 2.6021         | +0.1861 |
| ctrl_bpc best  | 2.3996         | 2.6021         | +0.2025 |

## Per-round trajectory (best bird: 9mkO6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1099 | 6582 | 2.6021 | +0.2108 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1098_sym24`

## Output

`workers/dispatcher/harvest-1way-r1099_sym24/round-1099/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

