# harvest-1way-r1123 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1123 ctrl_bpc |
|--------|--------|--------------:|
| f3ipU | origin/claude/train-sym24-ace91dcc-f3ipU | 2.7686 |
| **mean** | | **2.7686** |
| **best** | | **2.7686** |

## Chain progression R1122 → R1123

Previous harvest: `workers/dispatcher/harvest-5way-r1122_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4843         | 2.7686         | +0.2843 |
| ctrl_bpc best  | 2.3634         | 2.7686         | +0.4052 |

## Per-round trajectory (best bird: f3ipU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1123 | 5357 | 2.7686 | +0.2200 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1122_sym24`

## Output

`workers/dispatcher/harvest-1way-r1123_sym24/round-1123/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

