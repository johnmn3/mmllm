# harvest-1way-r1421 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1421 ctrl_bpc |
|--------|--------|--------------:|
| IahBI | origin/claude/train-sym24-d57dfd58-IahBI | 3.1934 |
| **mean** | | **3.1934** |
| **best** | | **3.1934** |

## Chain progression R1420 → R1421

Previous harvest: `workers/dispatcher/harvest-1way-r1420_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4416         | 3.1934         | -0.2482 |
| ctrl_bpc best  | 3.4416         | 3.1934         | -0.2482 |

## Per-round trajectory (best bird: IahBI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1421 | 6510 | 3.1934 | +0.1759 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1420_sym24`

## Output

`workers/dispatcher/harvest-1way-r1421_sym24/round-1421/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

