# harvest-1way-r691 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R691 ctrl_bpc |
|--------|--------|--------------:|
| BniYM | origin/claude/train-sym24-23590d81-BniYM | 3.6923 |
| **mean** | | **3.6923** |
| **best** | | **3.6923** |

## Chain progression R690 → R691

Previous harvest: `workers/dispatcher/harvest-3way-r690_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8268         | 3.6923         | -0.1345 |
| ctrl_bpc best  | 3.7260         | 3.6923         | -0.0337 |

## Per-round trajectory (best bird: BniYM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 691 | 5363 | 3.6923 | +0.4792 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r690_sym24`

## Output

`workers/dispatcher/harvest-1way-r691_sym24/round-691/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

