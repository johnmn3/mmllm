# harvest-1way-r1383 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1383 ctrl_bpc |
|--------|--------|--------------:|
| JIB6M | origin/claude/train-sym24-c1d8c0b4-JIB6M | 3.0538 |
| **mean** | | **3.0538** |
| **best** | | **3.0538** |

## Chain progression R1382 → R1383

Previous harvest: `workers/dispatcher/harvest-1way-r1382_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0487         | 3.0538         | +0.0051 |
| ctrl_bpc best  | 3.0487         | 3.0538         | +0.0051 |

## Per-round trajectory (best bird: JIB6M)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1383 | 5528 | 3.0538 | +0.0913 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1382_sym24`

## Output

`workers/dispatcher/harvest-1way-r1383_sym24/round-1383/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

