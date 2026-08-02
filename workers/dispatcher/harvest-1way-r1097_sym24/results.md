# harvest-1way-r1097 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1097 ctrl_bpc |
|--------|--------|--------------:|
| gcfxx | origin/claude/train-sym24-535b7896-gcfxx | 2.5942 |
| **mean** | | **2.5942** |
| **best** | | **2.5942** |

## Chain progression R1096 → R1097

Previous harvest: `workers/dispatcher/harvest-7way-r1096_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5498         | 2.5942         | +0.0444 |
| ctrl_bpc best  | 2.3998         | 2.5942         | +0.1944 |

## Per-round trajectory (best bird: gcfxx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1097 | 6324 | 2.5942 | +0.2134 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1096_sym24`

## Output

`workers/dispatcher/harvest-1way-r1097_sym24/round-1097/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

