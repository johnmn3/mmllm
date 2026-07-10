# harvest-1way-r882 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R882 ctrl_bpc |
|--------|--------|--------------:|
| o6Pad | origin/claude/train-sym24-d0b73420-o6Pad | 3.2201 |
| **mean** | | **3.2201** |
| **best** | | **3.2201** |

## Chain progression R881 → R882

Previous harvest: `workers/dispatcher/harvest-7way-r881_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1131         | 3.2201         | +0.1070 |
| ctrl_bpc best  | 2.8444         | 3.2201         | +0.3757 |

## Per-round trajectory (best bird: o6Pad)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 882 | 6574 | 3.2201 | +0.3810 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r881_sym24`

## Output

`workers/dispatcher/harvest-1way-r882_sym24/round-882/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

