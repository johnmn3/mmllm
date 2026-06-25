# harvest-4way-r765 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R765 ctrl_bpc |
|--------|--------|--------------:|
| 1RqeO | origin/claude/train-sym24-980a9efd-1RqeO | 3.2477 |
| GoxQp | fork-slaa-us-mmllm-claude-train-sym24-356e52da-GoxQp | 3.2818 |
| eZLOm | fork-davidwuchn-mmllm-claude-train-sym24-9d571efb-eZLOm | 3.6347 |
| LhJq8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-70e0fde8-LhJq8 | 3.6552 |
| **mean** | | **3.4548** |
| **best** | | **3.2477** |

## Chain progression R764 → R765

Previous harvest: `workers/dispatcher/harvest-3way-r764_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4261         | 3.4548         | +0.0288 |
| ctrl_bpc best  | 3.2591         | 3.2477         | -0.0114 |

## Per-round trajectory (best bird: 1RqeO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 765 | 6556 | 3.2477 | +0.7255 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r764_sym24`

## Output

`workers/dispatcher/harvest-4way-r765_sym24/round-765/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

