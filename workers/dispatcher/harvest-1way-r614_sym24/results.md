# harvest-1way-r614 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R614 ctrl_bpc |
|--------|--------|--------------:|
| dhpxt | origin/claude/train-sym24-ab3f0f58-dhpxt | 2.1483 |
| **mean** | | **2.1483** |
| **best** | | **2.1483** |

## Chain progression R613 → R614

Previous harvest: `workers/dispatcher/harvest-3way-r613_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3637         | 2.1483         | -0.2154 |
| ctrl_bpc best  | 2.1473         | 2.1483         | +0.0010 |

## Per-round trajectory (best bird: dhpxt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 614 | 5182 | 2.1483 | +0.0252 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **500 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r613_sym24`

## Output

`workers/dispatcher/harvest-1way-r614_sym24/round-614/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

