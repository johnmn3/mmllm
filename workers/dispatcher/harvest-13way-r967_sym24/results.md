# harvest-13way-r967 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R967 ctrl_bpc |
|--------|--------|--------------:|
| DZGbP | fork-joly-os-mmllm-claude-train-sym24-913e35b5-DZGbP | 2.6160 |
| 1NeY0 | fork-joly-os-mmllm-claude-train-sym24-0c88b9b2-1NeY0 | 2.6177 |
| hyKjV | fork-slaa-us-mmllm-claude-train-sym24-48016e1e-hyKjV | 2.6209 |
| wbMQk | origin/claude/train-sym24-5cc000d7-wbMQk | 2.6457 |
| YNiaP | fork-joly-os-mmllm-claude-train-sym24-8444e020-YNiaP | 2.6622 |
| a39Fr | fork-SeniorCareMarket-mmllm-claude-train-sym24-ec228b8f-a39Fr | 2.6677 |
| TUdBT | origin/claude/train-sym24-4e24ebfe-TUdBT | 2.6850 |
| Z9qgI | fork-SeniorCareMarket-mmllm-claude-train-sym24-f28be261-Z9qgI | 2.8198 |
| 5fTih | fork-slaa-us-mmllm-claude-train-sym24-1117c322-5fTih | 3.0031 |
| TACfZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-43087804-TACfZ | 3.0136 |
| ZJuti | origin/claude/train-sym24-59c859e5-ZJuti | 3.0149 |
| 52jCg | fork-slaa-us-mmllm-claude-train-sym24-b3a5917f-52jCg | 3.0248 |
| Bb4cw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f960bbd0-Bb4cw | 3.0260 |
| **mean** | | **2.8013** |
| **best** | | **2.6160** |

## Chain progression R966 → R967

Previous harvest: `workers/dispatcher/harvest-6way-r966_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7272         | 2.8013         | +0.0741 |
| ctrl_bpc best  | 2.6255         | 2.6160         | -0.0095 |

## Per-round trajectory (best bird: DZGbP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 967 | 4361 | 2.6160 | +0.1559 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r966_sym24`
  - `workers/dispatcher/harvest-6way-r966_sym24`

## Output

`workers/dispatcher/harvest-13way-r967_sym24/round-967/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

