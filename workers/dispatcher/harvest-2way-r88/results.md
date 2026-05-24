# harvest-2way-r88 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R88 ctrl_bpc |
|--------|--------|--------------:|
| M1oy4 | origin/claude/train-264b5f6f-M1oy4 | 0.9218 |
| hVfcL | origin/claude/train-e120e9df-hVfcL | 1.0788 |
| **mean** | | **1.0003** |
| **best** | | **0.9218** |

## Chain progression R83 → R88

Previous harvest: `workers/dispatcher/harvest-2way-r83`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0189         | 1.0003         | -0.0186 |
| ctrl_bpc best  | 0.9346         | 0.9218         | -0.0128 |

## Per-round trajectory (best bird: M1oy4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 84 | 608 | 0.9630 | +0.0060 |
| 85 | 522 | 0.9303 | +0.0050 |
| 86 | 547 | 0.9481 | +0.0086 |
| 87 | 539 | 0.9323 | +0.0054 |
| 88 | 536 | 0.9218 | +0.0085 |

## Cumulative training contribution

- This harvest: **50 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1848 steps** from 46 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r83`

## Output

`workers/dispatcher/harvest-2way-r88/round-88/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

