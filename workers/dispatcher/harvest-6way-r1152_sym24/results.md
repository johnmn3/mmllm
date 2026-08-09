# harvest-6way-r1152 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1152 ctrl_bpc |
|--------|--------|--------------:|
| cdxzB | origin/claude/train-sym24-0ad7b95f-cdxzB | 2.3367 |
| l4UqZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8b3b6911-l4UqZ | 2.3604 |
| mIv2J | fork-joly-os-mmllm-claude-train-sym24-bff6fefa-mIv2J | 2.3674 |
| WG8kL | fork-slaa-us-mmllm-claude-train-sym24-1bc3be28-WG8kL | 2.5324 |
| Pks9P | fork-joly-os-mmllm-claude-train-sym24-3fb583c4-Pks9P | 2.5362 |
| V2ir7 | fork-SeniorCareMarket-mmllm-claude-train-sym24-bb20c8bf-V2ir7 | 2.5630 |
| **mean** | | **2.4494** |
| **best** | | **2.3367** |

## Chain progression R1151 → R1152

Previous harvest: `workers/dispatcher/harvest-9way-r1151_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5154         | 2.4494         | -0.0660 |
| ctrl_bpc best  | 2.3301         | 2.3367         | +0.0066 |

## Per-round trajectory (best bird: cdxzB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1152 | 3719 | 2.3367 | +0.2534 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1151_sym24`

## Output

`workers/dispatcher/harvest-6way-r1152_sym24/round-1152/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

