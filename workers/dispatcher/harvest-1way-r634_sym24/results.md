# harvest-1way-r634 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R634 ctrl_bpc |
|--------|--------|--------------:|
| LIV2 | origin/claude/train-sym24-b205701b-LIV2 | 2.5945 |
| **mean** | | **2.5945** |
| **best** | | **2.5945** |

## Chain progression R632 → R634

Previous harvest: `workers/dispatcher/harvest-3way-r632_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2766         | 2.5945         | +0.3179 |
| ctrl_bpc best  | 2.1131         | 2.5945         | +0.4814 |

## Per-round trajectory (best bird: LIV2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 633 | — | 2.5902 | +0.0032 |
| 634 | — | 2.5945 | +0.0169 |

## Cumulative training contribution

- This harvest: **600 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **900 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r632_sym24`

## Output

`workers/dispatcher/harvest-1way-r634_sym24/round-634/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

