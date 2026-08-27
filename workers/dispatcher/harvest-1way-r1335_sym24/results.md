# harvest-1way-r1335 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1335 ctrl_bpc |
|--------|--------|--------------:|
| p7BZy | origin/claude/train-sym24-a6747aa1-p7BZy | 3.3759 |
| **mean** | | **3.3759** |
| **best** | | **3.3759** |

## Chain progression R1334 → R1335

Previous harvest: `workers/dispatcher/harvest-1way-r1334_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6180         | 3.3759         | -0.2421 |
| ctrl_bpc best  | 3.6180         | 3.3759         | -0.2421 |

## Per-round trajectory (best bird: p7BZy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1335 | 6562 | 3.3759 | +0.1115 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1334_sym24`

## Output

`workers/dispatcher/harvest-1way-r1335_sym24/round-1335/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

