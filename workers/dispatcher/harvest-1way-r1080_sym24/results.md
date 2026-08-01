# harvest-1way-r1080 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1080 ctrl_bpc |
|--------|--------|--------------:|
| 3RNb0 | origin/claude/train-sym24-87b836c8-3RNb0 | 2.4547 |
| **mean** | | **2.4547** |
| **best** | | **2.4547** |

## Chain progression R1079 → R1080

Previous harvest: `workers/dispatcher/harvest-4way-r1079_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6741         | 2.4547         | -0.2194 |
| ctrl_bpc best  | 2.6182         | 2.4547         | -0.1635 |

## Per-round trajectory (best bird: 3RNb0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1080 | 6647 | 2.4547 | +0.2094 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1079_sym24`

## Output

`workers/dispatcher/harvest-1way-r1080_sym24/round-1080/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

