# harvest-1way-r1384 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1384 ctrl_bpc |
|--------|--------|--------------:|
| mOTxd | origin/claude/train-sym24-03acfeb5-mOTxd | 3.2102 |
| **mean** | | **3.2102** |
| **best** | | **3.2102** |

## Chain progression R1383 → R1384

Previous harvest: `workers/dispatcher/harvest-1way-r1383_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0538         | 3.2102         | +0.1564 |
| ctrl_bpc best  | 3.0538         | 3.2102         | +0.1564 |

## Per-round trajectory (best bird: mOTxd)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1384 | 6467 | 3.2102 | +0.1192 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1383_sym24`

## Output

`workers/dispatcher/harvest-1way-r1384_sym24/round-1384/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

