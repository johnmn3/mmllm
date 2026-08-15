# harvest-1way-r1210 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1210 ctrl_bpc |
|--------|--------|--------------:|
| 2sW6c | origin/claude/train-sym24-1ec647cb-2sW6c | 2.4748 |
| **mean** | | **2.4748** |
| **best** | | **2.4748** |

## Chain progression R1209 → R1210

Previous harvest: `workers/dispatcher/harvest-6way-r1209_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4746         | 2.4748         | +0.0002 |
| ctrl_bpc best  | 2.2915         | 2.4748         | +0.1833 |

## Per-round trajectory (best bird: 2sW6c)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1210 | 6450 | 2.4748 | +0.2261 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1209_sym24`

## Output

`workers/dispatcher/harvest-1way-r1210_sym24/round-1210/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

