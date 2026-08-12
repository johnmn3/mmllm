# harvest-1way-r1180 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1180 ctrl_bpc |
|--------|--------|--------------:|
| dc4HU | origin/claude/train-sym24-bebab2ed-dc4HU | 2.5150 |
| **mean** | | **2.5150** |
| **best** | | **2.5150** |

## Chain progression R1179 → R1180

Previous harvest: `workers/dispatcher/harvest-3way-r1179_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5826         | 2.5150         | -0.0676 |
| ctrl_bpc best  | 2.3190         | 2.5150         | +0.1960 |

## Per-round trajectory (best bird: dc4HU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1180 | 4463 | 2.5150 | +0.2119 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1179_sym24`

## Output

`workers/dispatcher/harvest-1way-r1180_sym24/round-1180/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

