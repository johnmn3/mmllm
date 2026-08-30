# harvest-1way-r1360 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1360 ctrl_bpc |
|--------|--------|--------------:|
| vscIg | origin/claude/train-sym24-83c3e293-vscIg | 3.5434 |
| **mean** | | **3.5434** |
| **best** | | **3.5434** |

## Chain progression R1359 → R1360

Previous harvest: `workers/dispatcher/harvest-3way-r1359_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3025         | 3.5434         | +0.2409 |
| ctrl_bpc best  | 3.1518         | 3.5434         | +0.3916 |

## Per-round trajectory (best bird: vscIg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1360 | 3645 | 3.5434 | +0.0599 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1359_sym24`

## Output

`workers/dispatcher/harvest-1way-r1360_sym24/round-1360/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

