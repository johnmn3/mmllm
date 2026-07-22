# harvest-1way-r994 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R994 ctrl_bpc |
|--------|--------|--------------:|
| SH2a2 | origin/claude/train-sym24-92608b89-SH2a2 | 2.7645 |
| **mean** | | **2.7645** |
| **best** | | **2.7645** |

## Chain progression R993 → R994

Previous harvest: `workers/dispatcher/harvest-5way-r993_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7819         | 2.7645         | -0.0174 |
| ctrl_bpc best  | 2.5936         | 2.7645         | +0.1709 |

## Per-round trajectory (best bird: SH2a2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 994 | 6412 | 2.7645 | +0.1646 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r993_sym24`

## Output

`workers/dispatcher/harvest-1way-r994_sym24/round-994/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

