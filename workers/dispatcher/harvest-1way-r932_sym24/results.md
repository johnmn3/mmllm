# harvest-1way-r932 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R932 ctrl_bpc |
|--------|--------|--------------:|
| Aa4t8 | origin/claude/train-sym24-772320ea-Aa4t8 | 2.7318 |
| **mean** | | **2.7318** |
| **best** | | **2.7318** |

## Chain progression R931 → R932

Previous harvest: `workers/dispatcher/harvest-6way-r931_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9780         | 2.7318         | -0.2462 |
| ctrl_bpc best  | 2.6972         | 2.7318         | +0.0346 |

## Per-round trajectory (best bird: Aa4t8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 932 | 6365 | 2.7318 | +0.2369 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r931_sym24`

## Output

`workers/dispatcher/harvest-1way-r932_sym24/round-932/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

