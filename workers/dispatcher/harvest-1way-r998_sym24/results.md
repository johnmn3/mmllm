# harvest-1way-r998 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R998 ctrl_bpc |
|--------|--------|--------------:|
| 1wYoz | origin/claude/train-sym24-9ef82851-1wYoz | 2.7531 |
| **mean** | | **2.7531** |
| **best** | | **2.7531** |

## Chain progression R997 → R998

Previous harvest: `workers/dispatcher/harvest-4way-r997_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6755         | 2.7531         | +0.0776 |
| ctrl_bpc best  | 2.5719         | 2.7531         | +0.1812 |

## Per-round trajectory (best bird: 1wYoz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 998 | 6238 | 2.7531 | +0.1565 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r997_sym24`

## Output

`workers/dispatcher/harvest-1way-r998_sym24/round-998/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

