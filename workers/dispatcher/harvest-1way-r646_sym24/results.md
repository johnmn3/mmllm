# harvest-1way-r646 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R646 ctrl_bpc |
|--------|--------|--------------:|
| HRZ5m | origin/claude/train-sym24-31840344-HRZ5m | 4.9277 |
| **mean** | | **4.9277** |
| **best** | | **4.9277** |

## Chain progression R645 → R646

Previous harvest: `workers/dispatcher/harvest-2way-r645_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.4925         | 4.9277         | +0.4352 |
| ctrl_bpc best  | 4.4850         | 4.9277         | +0.4427 |

## Per-round trajectory (best bird: HRZ5m)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 646 | 6237 | 4.9277 | +0.0320 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r645_sym24`

## Output

`workers/dispatcher/harvest-1way-r646_sym24/round-646/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

