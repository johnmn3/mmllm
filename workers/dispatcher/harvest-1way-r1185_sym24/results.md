# harvest-1way-r1185 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1185 ctrl_bpc |
|--------|--------|--------------:|
| GzDVs | origin/claude/train-sym24-ef831967-GzDVs | 2.3143 |
| **mean** | | **2.3143** |
| **best** | | **2.3143** |

## Chain progression R1184 → R1185

Previous harvest: `workers/dispatcher/harvest-3way-r1184_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4293         | 2.3143         | -0.1150 |
| ctrl_bpc best  | 2.3010         | 2.3143         | +0.0133 |

## Per-round trajectory (best bird: GzDVs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1185 | 6485 | 2.3143 | +0.2467 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1184_sym24`

## Output

`workers/dispatcher/harvest-1way-r1185_sym24/round-1185/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

