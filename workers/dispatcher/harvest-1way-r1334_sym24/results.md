# harvest-1way-r1334 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1334 ctrl_bpc |
|--------|--------|--------------:|
| VzxcT | origin/claude/train-sym24-fe6adf9e-VzxcT | 3.6180 |
| **mean** | | **3.6180** |
| **best** | | **3.6180** |

## Chain progression R1333 → R1334

Previous harvest: `workers/dispatcher/harvest-4way-r1333_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4025         | 3.6180         | +0.2155 |
| ctrl_bpc best  | 3.3036         | 3.6180         | +0.3144 |

## Per-round trajectory (best bird: VzxcT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1334 | 6510 | 3.6180 | +0.0863 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1333_sym24`

## Output

`workers/dispatcher/harvest-1way-r1334_sym24/round-1334/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

