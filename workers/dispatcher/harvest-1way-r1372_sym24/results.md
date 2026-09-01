# harvest-1way-r1372 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1372 ctrl_bpc |
|--------|--------|--------------:|
| tt0mC | origin/claude/train-sym24-245551df-tt0mC | 3.6038 |
| **mean** | | **3.6038** |
| **best** | | **3.6038** |

## Chain progression R1371 → R1372

Previous harvest: `workers/dispatcher/harvest-5way-r1371_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2592         | 3.6038         | +0.3446 |
| ctrl_bpc best  | 3.1489         | 3.6038         | +0.4549 |

## Per-round trajectory (best bird: tt0mC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1372 | 6632 | 3.6038 | +0.1359 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1371_sym24`

## Output

`workers/dispatcher/harvest-1way-r1372_sym24/round-1372/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

