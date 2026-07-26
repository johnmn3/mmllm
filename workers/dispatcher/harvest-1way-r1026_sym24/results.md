# harvest-1way-r1026 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1026 ctrl_bpc |
|--------|--------|--------------:|
| fodnE | origin/claude/train-sym24-5ec39541-fodnE | 2.5105 |
| **mean** | | **2.5105** |
| **best** | | **2.5105** |

## Chain progression R1025 → R1026

Previous harvest: `workers/dispatcher/harvest-2way-r1025_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7177         | 2.5105         | -0.2072 |
| ctrl_bpc best  | 2.5397         | 2.5105         | -0.0292 |

## Per-round trajectory (best bird: fodnE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1026 | 4231 | 2.5105 | +0.1901 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1025_sym24`

## Output

`workers/dispatcher/harvest-1way-r1026_sym24/round-1026/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

