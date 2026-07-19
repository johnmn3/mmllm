# harvest-6way-r967 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R967 ctrl_bpc |
|--------|--------|--------------:|
| 1NeY0 | fork-joly-os-mmllm-claude-train-sym24-0c88b9b2-1NeY0 | 2.6177 |
| YNiaP | fork-joly-os-mmllm-claude-train-sym24-8444e020-YNiaP | 2.6622 |
| TUdBT | origin/claude/train-sym24-4e24ebfe-TUdBT | 2.6850 |
| 5fTih | fork-slaa-us-mmllm-claude-train-sym24-1117c322-5fTih | 3.0031 |
| TACfZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-43087804-TACfZ | 3.0136 |
| ZJuti | origin/claude/train-sym24-59c859e5-ZJuti | 3.0149 |
| **mean** | | **2.8327** |
| **best** | | **2.6177** |

## Chain progression R966 → R967

Previous harvest: `workers/dispatcher/harvest-6way-r966_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7272         | 2.8327         | +0.1055 |
| ctrl_bpc best  | 2.6255         | 2.6177         | -0.0078 |

## Per-round trajectory (best bird: 1NeY0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 967 | 4141 | 2.6177 | +0.1437 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r966_sym24`
  - `workers/dispatcher/harvest-6way-r966_sym24`

## Output

`workers/dispatcher/harvest-6way-r967_sym24/round-967/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

