# harvest-1way-r1404 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1404 ctrl_bpc |
|--------|--------|--------------:|
| FxRIT | origin/claude/train-sym24-1ee5c23d-FxRIT | 3.7779 |
| **mean** | | **3.7779** |
| **best** | | **3.7779** |

## Chain progression R1403 → R1404

Previous harvest: `workers/dispatcher/harvest-2way-r1403_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4043         | 3.7779         | +0.3736 |
| ctrl_bpc best  | 3.3663         | 3.7779         | +0.4116 |

## Per-round trajectory (best bird: FxRIT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1404 | 3932 | 3.7779 | +0.0846 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1403_sym24`

## Output

`workers/dispatcher/harvest-1way-r1404_sym24/round-1404/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

