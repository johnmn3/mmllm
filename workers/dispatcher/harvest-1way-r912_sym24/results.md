# harvest-1way-r912 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R912 ctrl_bpc |
|--------|--------|--------------:|
| MkXS2 | origin/claude/train-sym24-f6fa80b7-MkXS2 | 2.7694 |
| **mean** | | **2.7694** |
| **best** | | **2.7694** |

## Chain progression R911 → R912

Previous harvest: `workers/dispatcher/harvest-5way-r911_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8829         | 2.7694         | -0.1135 |
| ctrl_bpc best  | 2.7544         | 2.7694         | +0.0150 |

## Per-round trajectory (best bird: MkXS2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 912 | 6483 | 2.7694 | +0.2119 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r911_sym24`

## Output

`workers/dispatcher/harvest-1way-r912_sym24/round-912/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

