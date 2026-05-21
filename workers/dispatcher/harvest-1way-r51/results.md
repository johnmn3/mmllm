# harvest-1way-r51 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R51 ctrl_bpc |
|--------|--------|--------------:|
| kmoim | origin/claude/train-0f6b3f2a-kmoim | 1.0290 |
| **mean** | | **1.0290** |
| **best** | | **1.0290** |

## Chain progression R46 → R51

Previous harvest: `workers/dispatcher/harvest-1way-r46`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9623         | 1.0290         | +0.0667 |
| ctrl_bpc best  | 0.9623         | 1.0290         | +0.0667 |

## Per-round trajectory (best bird: kmoim)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 47 | 532 | 1.0104 | +0.0105 |
| 48 | 552 | 1.0196 | +0.0011 |
| 49 | 525 | 0.9952 | +0.0099 |
| 50 | 531 | 1.0447 | +0.0027 |
| 51 | 527 | 1.0290 | +0.0059 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **245 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r46`

## Output

`workers/dispatcher/harvest-1way-r51/round-51/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

