# harvest-1way-r41 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R41 ctrl_bpc |
|--------|--------|--------------:|
| R9IEG | origin/claude/train-16d5a63e-R9IEG | 1.1498 |
| **mean** | | **1.1498** |
| **best** | | **1.1498** |

## Chain progression R36 → R41

Previous harvest: `workers/dispatcher/harvest-3way-r36`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1237         | 1.1498         | +0.0261 |
| ctrl_bpc best  | 1.0954         | 1.1498         | +0.0544 |

## Per-round trajectory (best bird: R9IEG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 37 | 453 | 1.0852 | +0.0054 |
| 38 | 454 | 1.0758 | +0.0005 |
| 39 | 434 | 1.1087 | +0.0040 |
| 40 | 438 | 1.1582 | -0.0032 |
| 41 | 440 | 1.1498 | +0.0044 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **175 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r36`

## Output

`workers/dispatcher/harvest-1way-r41/round-41/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

