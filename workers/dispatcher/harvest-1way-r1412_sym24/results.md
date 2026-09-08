# harvest-1way-r1412 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1412 ctrl_bpc |
|--------|--------|--------------:|
| wsu0u | origin/claude/train-sym24-045313f2-wsu0u | 3.5872 |
| **mean** | | **3.5872** |
| **best** | | **3.5872** |

## Chain progression R1411 → R1412

Previous harvest: `workers/dispatcher/harvest-1way-r1411_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3031         | 3.5872         | +0.2841 |
| ctrl_bpc best  | 3.3031         | 3.5872         | +0.2841 |

## Per-round trajectory (best bird: wsu0u)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1412 | 6419 | 3.5872 | +0.2217 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1411_sym24`

## Output

`workers/dispatcher/harvest-1way-r1412_sym24/round-1412/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

