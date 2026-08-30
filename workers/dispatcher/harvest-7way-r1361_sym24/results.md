# harvest-7way-r1361 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1361 ctrl_bpc |
|--------|--------|--------------:|
| BZ379 | fork-joly-os-mmllm-claude-train-sym24-7cac15b9-BZ379 | 3.1082 |
| lHSlz | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-125cf8b8-lHSlz | 3.1481 |
| 3ZqoW | fork-slaa-us-mmllm-claude-train-sym24-b0505dd0-3ZqoW | 3.2194 |
| AXPvk | origin/claude/train-sym24-d64cf9e8-AXPvk | 3.2330 |
| o7LlL | fork-SeniorCareMarket-mmllm-claude-train-sym24-38e3fc5c-o7LlL | 3.2603 |
| 97dWr | origin/claude/train-sym24-25878109-97dWr | 3.5412 |
| 132eS | origin/claude/train-sym24-105e9d43-132eS | 3.5468 |
| **mean** | | **3.2939** |
| **best** | | **3.1082** |

## Chain progression R1360 → R1361

Previous harvest: `workers/dispatcher/harvest-4way-r1360_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3649         | 3.2939         | -0.0710 |
| ctrl_bpc best  | 3.1348         | 3.1082         | -0.0266 |

## Per-round trajectory (best bird: BZ379)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1361 | 3600 | 3.1082 | +0.1297 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1360_sym24`
  - `workers/dispatcher/harvest-3way-r1360_sym24`

## Output

`workers/dispatcher/harvest-7way-r1361_sym24/round-1361/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

