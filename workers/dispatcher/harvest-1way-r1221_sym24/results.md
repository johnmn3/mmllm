# harvest-1way-r1221 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1221 ctrl_bpc |
|--------|--------|--------------:|
| QfK5K | origin/claude/train-sym24-55487bf7-QfK5K | 2.2866 |
| **mean** | | **2.2866** |
| **best** | | **2.2866** |

## Chain progression R1220 → R1221

Previous harvest: `workers/dispatcher/harvest-7way-r1220_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3068         | 2.2866         | -0.0202 |
| ctrl_bpc best  | 2.2654         | 2.2866         | +0.0212 |

## Per-round trajectory (best bird: QfK5K)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1221 | 6404 | 2.2866 | +0.2459 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1220_sym24`

## Output

`workers/dispatcher/harvest-1way-r1221_sym24/round-1221/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

