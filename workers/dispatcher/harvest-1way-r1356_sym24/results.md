# harvest-1way-r1356 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1356 ctrl_bpc |
|--------|--------|--------------:|
| abUZe | origin/claude/train-sym24-bb09722d-abUZe | 3.2840 |
| **mean** | | **3.2840** |
| **best** | | **3.2840** |

## Chain progression R1355 → R1356

Previous harvest: `workers/dispatcher/harvest-5way-r1355_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3567         | 3.2840         | -0.0727 |
| ctrl_bpc best  | 3.2876         | 3.2840         | -0.0036 |

## Per-round trajectory (best bird: abUZe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1356 | 6518 | 3.2840 | +0.1302 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1355_sym24`

## Output

`workers/dispatcher/harvest-1way-r1356_sym24/round-1356/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

