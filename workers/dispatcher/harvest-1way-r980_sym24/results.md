# harvest-1way-r980 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R980 ctrl_bpc |
|--------|--------|--------------:|
| yY1v6 | origin/claude/train-sym24-424323a1-yY1v6 | 2.6168 |
| **mean** | | **2.6168** |
| **best** | | **2.6168** |

## Chain progression R979 → R980

Previous harvest: `workers/dispatcher/harvest-5way-r979_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7279         | 2.6168         | -0.1111 |
| ctrl_bpc best  | 2.5999         | 2.6168         | +0.0169 |

## Per-round trajectory (best bird: yY1v6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 980 | 6578 | 2.6168 | +0.1613 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r979_sym24`

## Output

`workers/dispatcher/harvest-1way-r980_sym24/round-980/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

