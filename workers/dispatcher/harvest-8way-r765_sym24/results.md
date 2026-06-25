# harvest-8way-r765 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R765 ctrl_bpc |
|--------|--------|--------------:|
| 1hTZE | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-592b618c-1hTZE | 3.2432 |
| 1RqeO | origin/claude/train-sym24-980a9efd-1RqeO | 3.2477 |
| GoxQp | fork-slaa-us-mmllm-claude-train-sym24-356e52da-GoxQp | 3.2818 |
| BwIAF | fork-joly-os-mmllm-claude-train-sym24-4730e587-BwIAF | 3.3737 |
| eZLOm | fork-davidwuchn-mmllm-claude-train-sym24-9d571efb-eZLOm | 3.6347 |
| bEZd0 | fork-joly-os-mmllm-claude-train-sym24-abc77be7-bEZd0 | 3.6474 |
| LhJq8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-70e0fde8-LhJq8 | 3.6552 |
| 7q50s | fork-davidwuchn-mmllm-claude-train-sym24-364e3021-7q50s | 3.6818 |
| **mean** | | **3.4707** |
| **best** | | **3.2432** |

## Chain progression R764 → R765

Previous harvest: `workers/dispatcher/harvest-3way-r764_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4261         | 3.4707         | +0.0446 |
| ctrl_bpc best  | 3.2591         | 3.2432         | -0.0159 |

## Per-round trajectory (best bird: 1hTZE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 765 | 6620 | 3.2432 | +0.6193 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r764_sym24`
  - `workers/dispatcher/harvest-3way-r764_sym24`

## Output

`workers/dispatcher/harvest-8way-r765_sym24/round-765/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

