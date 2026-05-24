# harvest-1way-r86 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R86 ctrl_bpc |
|--------|--------|--------------:|
| HLd24 | origin/claude/train-a45c4e56-HLd24 | 0.9461 |
| **mean** | | **0.9461** |
| **best** | | **0.9461** |

## Chain progression R83 → R86

Previous harvest: `workers/dispatcher/harvest-2way-r83`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0189         | 0.9461         | -0.0728 |
| ctrl_bpc best  | 0.9346         | 0.9461         | +0.0115 |

## Per-round trajectory (best bird: HLd24)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 84 | 677 | 0.9611 | +0.0044 |
| 85 | 529 | 0.9280 | +0.0036 |
| 86 | 540 | 0.9461 | +0.0071 |

## Cumulative training contribution

- This harvest: **21 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1819 steps** from 45 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r83`

## Output

`workers/dispatcher/harvest-1way-r86/round-86/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

