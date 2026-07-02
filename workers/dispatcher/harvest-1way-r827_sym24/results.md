# harvest-1way-r827 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R827 ctrl_bpc |
|--------|--------|--------------:|
| JqYD2 | origin/claude/train-sym24-bb6cacfa-JqYD2 | 3.0039 |
| **mean** | | **3.0039** |
| **best** | | **3.0039** |

## Chain progression R826 → R827

Previous harvest: `workers/dispatcher/harvest-4way-r826_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2358         | 3.0039         | -0.2319 |
| ctrl_bpc best  | 3.0224         | 3.0039         | -0.0185 |

## Per-round trajectory (best bird: JqYD2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 827 | 6971 | 3.0039 | +0.5804 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r826_sym24`

## Output

`workers/dispatcher/harvest-1way-r827_sym24/round-827/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

