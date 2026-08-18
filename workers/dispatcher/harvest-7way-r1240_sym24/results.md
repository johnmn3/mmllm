# harvest-7way-r1240 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1240 ctrl_bpc |
|--------|--------|--------------:|
| BDZmc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1ff0a38a-BDZmc | 2.2508 |
| j93a7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-71641b4b-j93a7 | 2.2569 |
| t7txy | fork-joly-os-mmllm-claude-train-sym24-4830e987-t7txy | 2.2613 |
| SMv8P | origin/claude/train-sym24-0c31172f-SMv8P | 2.4523 |
| qByHr | fork-slaa-us-mmllm-claude-train-sym24-ca76e3cf-qByHr | 2.6418 |
| 6YW5d | origin/claude/train-sym24-717aafb1-6YW5d | 2.6464 |
| tAWbc | fork-SeniorCareMarket-mmllm-claude-train-sym24-b2a32639-tAWbc | 2.6497 |
| **mean** | | **2.4513** |
| **best** | | **2.2508** |

## Chain progression R1239 → R1240

Previous harvest: `workers/dispatcher/harvest-6way-r1239_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4161         | 2.4513         | +0.0352 |
| ctrl_bpc best  | 2.2519         | 2.2508         | -0.0011 |

## Per-round trajectory (best bird: BDZmc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1240 | 3837 | 2.2508 | +0.2631 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1239_sym24`
  - `workers/dispatcher/harvest-2way-r1239_sym24`
  - `workers/dispatcher/harvest-6way-r1239_sym24`

## Output

`workers/dispatcher/harvest-7way-r1240_sym24/round-1240/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

