# harvest-3way-r1370 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1370 ctrl_bpc |
|--------|--------|--------------:|
| 3zRWf | origin/claude/train-sym24-82e7babb-3zRWf | 3.1133 |
| h0cX1 | origin/claude/train-sym24-d73ce52a-h0cX1 | 3.1805 |
| WEC8V | origin/claude/train-sym24-4ead64a1-WEC8V | 3.5034 |
| **mean** | | **3.2657** |
| **best** | | **3.1133** |

## Chain progression R1369 → R1370

Previous harvest: `workers/dispatcher/harvest-5way-r1369_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2627         | 3.2657         | +0.0030 |
| ctrl_bpc best  | 3.0918         | 3.1133         | +0.0215 |

## Per-round trajectory (best bird: 3zRWf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1370 | 6628 | 3.1133 | +0.1029 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1369_sym24`
  - `workers/dispatcher/harvest-3way-r1369_sym24`

## Output

`workers/dispatcher/harvest-3way-r1370_sym24/round-1370/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

