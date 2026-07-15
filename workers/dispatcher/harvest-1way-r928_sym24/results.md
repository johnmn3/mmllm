# harvest-1way-r928 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R928 ctrl_bpc |
|--------|--------|--------------:|
| FFISx | origin/claude/train-sym24-e5a66d12-FFISx | 2.9110 |
| **mean** | | **2.9110** |
| **best** | | **2.9110** |

## Chain progression R927 → R928

Previous harvest: `workers/dispatcher/harvest-5way-r927_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9218         | 2.9110         | -0.0108 |
| ctrl_bpc best  | 2.7310         | 2.9110         | +0.1800 |

## Per-round trajectory (best bird: FFISx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 928 | 3608 | 2.9110 | +0.1833 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r927_sym24`

## Output

`workers/dispatcher/harvest-1way-r928_sym24/round-928/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

