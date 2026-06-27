# harvest-1way-r779 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R779 ctrl_bpc |
|--------|--------|--------------:|
| Q0OjS | origin/claude/train-sym24-00133f1a-Q0OjS | 3.2544 |
| **mean** | | **3.2544** |
| **best** | | **3.2544** |

## Chain progression R778 → R779

Previous harvest: `workers/dispatcher/harvest-6way-r778_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2314         | 3.2544         | +0.0230 |
| ctrl_bpc best  | 3.1993         | 3.2544         | +0.0551 |

## Per-round trajectory (best bird: Q0OjS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 779 | 6447 | 3.2544 | +0.5310 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r778_sym24`

## Output

`workers/dispatcher/harvest-1way-r779_sym24/round-779/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

