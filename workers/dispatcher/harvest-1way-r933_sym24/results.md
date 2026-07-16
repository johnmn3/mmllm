# harvest-1way-r933 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R933 ctrl_bpc |
|--------|--------|--------------:|
| GZ295 | origin/claude/train-sym24-f2602246-GZ295 | 3.0913 |
| **mean** | | **3.0913** |
| **best** | | **3.0913** |

## Chain progression R932 → R933

Previous harvest: `workers/dispatcher/harvest-3way-r932_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7818         | 3.0913         | +0.3095 |
| ctrl_bpc best  | 2.7116         | 3.0913         | +0.3797 |

## Per-round trajectory (best bird: GZ295)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 933 | 5361 | 3.0913 | +0.1753 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r932_sym24`

## Output

`workers/dispatcher/harvest-1way-r933_sym24/round-933/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

