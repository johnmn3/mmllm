# harvest-1way-r1093 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1093 ctrl_bpc |
|--------|--------|--------------:|
| Sub9I | origin/claude/train-sym24-e12fbe44-Sub9I | 2.4075 |
| **mean** | | **2.4075** |
| **best** | | **2.4075** |

## Chain progression R1092 → R1093

Previous harvest: `workers/dispatcher/harvest-3way-r1092_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6131         | 2.4075         | -0.2056 |
| ctrl_bpc best  | 2.4116         | 2.4075         | -0.0041 |

## Per-round trajectory (best bird: Sub9I)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1093 | 5282 | 2.4075 | +0.2383 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1092_sym24`

## Output

`workers/dispatcher/harvest-1way-r1093_sym24/round-1093/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

