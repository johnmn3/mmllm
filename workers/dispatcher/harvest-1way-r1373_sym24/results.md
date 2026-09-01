# harvest-1way-r1373 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1373 ctrl_bpc |
|--------|--------|--------------:|
| CcLTc | origin/claude/train-sym24-56d5438b-CcLTc | 3.6014 |
| **mean** | | **3.6014** |
| **best** | | **3.6014** |

## Chain progression R1372 → R1373

Previous harvest: `workers/dispatcher/harvest-1way-r1372_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6038         | 3.6014         | -0.0024 |
| ctrl_bpc best  | 3.6038         | 3.6014         | -0.0024 |

## Per-round trajectory (best bird: CcLTc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1373 | 4278 | 3.6014 | +0.1287 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1372_sym24`

## Output

`workers/dispatcher/harvest-1way-r1373_sym24/round-1373/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

