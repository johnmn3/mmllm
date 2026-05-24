# harvest-1way-r89 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R89 ctrl_bpc |
|--------|--------|--------------:|
| Ist4S | origin/claude/train-df04ebb5-Ist4S | 1.0469 |
| **mean** | | **1.0469** |
| **best** | | **1.0469** |

## Chain progression R88 → R89

Previous harvest: `workers/dispatcher/harvest-fold3way-r88`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9965         | 1.0469         | +0.0504 |
| ctrl_bpc best  | 0.9218         | 1.0469         | +0.1251 |

## Per-round trajectory (best bird: Ist4S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 89 | 3734 | 1.0469 | +0.0127 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1933 steps** from 48 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-fold3way-r88`

## Output

`workers/dispatcher/harvest-1way-r89/round-89/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

