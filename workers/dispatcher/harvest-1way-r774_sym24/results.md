# harvest-1way-r774 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R774 ctrl_bpc |
|--------|--------|--------------:|
| 30i6Q | origin/claude/train-sym24-2b2134d6-30i6Q | 3.2533 |
| **mean** | | **3.2533** |
| **best** | | **3.2533** |

## Chain progression R773 → R774

Previous harvest: `workers/dispatcher/harvest-7way-r773_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3572         | 3.2533         | -0.1039 |
| ctrl_bpc best  | 3.2035         | 3.2533         | +0.0498 |

## Per-round trajectory (best bird: 30i6Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 774 | 6431 | 3.2533 | +0.5787 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r773_sym24`

## Output

`workers/dispatcher/harvest-1way-r774_sym24/round-774/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

