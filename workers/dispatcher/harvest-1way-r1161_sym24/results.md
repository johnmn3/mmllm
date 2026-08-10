# harvest-1way-r1161 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1161 ctrl_bpc |
|--------|--------|--------------:|
| su9hL | origin/claude/train-sym24-f15b4c55-su9hL | 2.3258 |
| **mean** | | **2.3258** |
| **best** | | **2.3258** |

## Chain progression R1160 → R1161

Previous harvest: `workers/dispatcher/harvest-2way-r1160_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3430         | 2.3258         | -0.0172 |
| ctrl_bpc best  | 2.3301         | 2.3258         | -0.0043 |

## Per-round trajectory (best bird: su9hL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1161 | 4015 | 2.3258 | +0.2599 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1160_sym24`

## Output

`workers/dispatcher/harvest-1way-r1161_sym24/round-1161/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

