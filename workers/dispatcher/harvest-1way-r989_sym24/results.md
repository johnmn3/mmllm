# harvest-1way-r989 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R989 ctrl_bpc |
|--------|--------|--------------:|
| 1spKG | origin/claude/train-sym24-1fa96a28-1spKG | 2.7742 |
| **mean** | | **2.7742** |
| **best** | | **2.7742** |

## Chain progression R988 → R989

Previous harvest: `workers/dispatcher/harvest-5way-r988_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7524         | 2.7742         | +0.0218 |
| ctrl_bpc best  | 2.5960         | 2.7742         | +0.1782 |

## Per-round trajectory (best bird: 1spKG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 989 | 6358 | 2.7742 | +0.1536 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r988_sym24`

## Output

`workers/dispatcher/harvest-1way-r989_sym24/round-989/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

