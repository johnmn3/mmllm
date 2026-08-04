# harvest-6way-r1106 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1106 ctrl_bpc |
|--------|--------|--------------:|
| OLQHR | fork-slaa-us-mmllm-claude-train-sym24-5cc0b6e9-OLQHR | 2.3908 |
| GMvOA | origin/claude/train-sym24-182abe27-GMvOA | 2.4071 |
| uTUVW | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fdee99c7-uTUVW | 2.4090 |
| raQLx | fork-SeniorCareMarket-mmllm-claude-train-sym24-4175142e-raQLx | 2.4156 |
| yIYLG | origin/claude/train-sym24-1a88c8ca-yIYLG | 2.7811 |
| wzvPe | fork-joly-os-mmllm-claude-train-sym24-91f0561c-wzvPe | 2.7875 |
| **mean** | | **2.5318** |
| **best** | | **2.3908** |

## Chain progression R1105 → R1106

Previous harvest: `workers/dispatcher/harvest-7way-r1105_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4938         | 2.5318         | +0.0381 |
| ctrl_bpc best  | 2.3893         | 2.3908         | +0.0015 |

## Per-round trajectory (best bird: OLQHR)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1106 | 3777 | 2.3908 | +0.2461 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1105_sym24`
  - `workers/dispatcher/harvest-7way-r1105_sym24`

## Output

`workers/dispatcher/harvest-6way-r1106_sym24/round-1106/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

