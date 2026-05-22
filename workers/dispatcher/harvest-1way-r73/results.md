# harvest-1way-r73 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R73 ctrl_bpc |
|--------|--------|--------------:|
| 634Oq | fork-slaa-us-mmllm-claude-train-07b51253-634Oq | 1.0175 |
| **mean** | | **1.0175** |
| **best** | | **1.0175** |

## Chain progression R71 → R73

Previous harvest: `workers/dispatcher/harvest-1way-r71`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0580         | 1.0175         | -0.0405 |
| ctrl_bpc best  | 1.0580         | 1.0175         | -0.0405 |

## Per-round trajectory (best bird: 634Oq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 72 | 532 | 1.0318 | +0.0049 |
| 73 | 511 | 1.0175 | +0.0018 |

## Cumulative training contribution

- This harvest: **14 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **399 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r71`

## Output

`workers/dispatcher/harvest-1way-r73/round-73/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

