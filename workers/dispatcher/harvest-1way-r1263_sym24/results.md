# harvest-1way-r1263 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1263 ctrl_bpc |
|--------|--------|--------------:|
| Smp3m | origin/claude/train-sym24-436d6582-Smp3m | 2.6297 |
| **mean** | | **2.6297** |
| **best** | | **2.6297** |

## Chain progression R1262 → R1263

Previous harvest: `workers/dispatcher/harvest-6way-r1262_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2994         | 2.6297         | +0.3303 |
| ctrl_bpc best  | 2.2318         | 2.6297         | +0.3979 |

## Per-round trajectory (best bird: Smp3m)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1263 | 3771 | 2.6297 | +0.2174 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1262_sym24`

## Output

`workers/dispatcher/harvest-1way-r1263_sym24/round-1263/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

