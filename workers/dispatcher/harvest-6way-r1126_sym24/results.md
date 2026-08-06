# harvest-6way-r1126 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1126 ctrl_bpc |
|--------|--------|--------------:|
| FLtdv | origin/claude/train-sym24-ea712677-FLtdv | 2.3597 |
| g9Zxk | fork-slaa-us-mmllm-claude-train-sym24-f6b990eb-g9Zxk | 2.3765 |
| lGJRs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1d2d0f81-lGJRs | 2.3778 |
| jDQ9W | fork-joly-os-mmllm-claude-train-sym24-9c6678a5-jDQ9W | 2.3964 |
| RyDzA | fork-SeniorCareMarket-mmllm-claude-train-sym24-d6441ad1-RyDzA | 2.5610 |
| caL6o | origin/claude/train-sym24-b1d3b96f-caL6o | 2.7861 |
| **mean** | | **2.4762** |
| **best** | | **2.3597** |

## Chain progression R1125 → R1126

Previous harvest: `workers/dispatcher/harvest-6way-r1125_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5362         | 2.4762         | -0.0600 |
| ctrl_bpc best  | 2.3826         | 2.3597         | -0.0229 |

## Per-round trajectory (best bird: FLtdv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1126 | 6819 | 2.3597 | +0.2568 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1125_sym24`
  - `workers/dispatcher/harvest-3way-r1125_sym24`
  - `workers/dispatcher/harvest-6way-r1125_sym24`

## Output

`workers/dispatcher/harvest-6way-r1126_sym24/round-1126/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

