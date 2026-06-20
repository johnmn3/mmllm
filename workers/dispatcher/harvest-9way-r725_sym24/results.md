# harvest-9way-r725 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R725 ctrl_bpc |
|--------|--------|--------------:|
| rpTxG | fork-slaa-us-mmllm-claude-train-sym24-21a8c994-rpTxG | 3.4821 |
| JCOIL | fork-joly-os-mmllm-claude-train-sym24-c7a75138-JCOIL | 3.4836 |
| p7n96 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6c9d5834-p7n96 | 3.4838 |
| J38Zs | fork-slaa-us-mmllm-claude-train-sym24-bb0dd18d-J38Zs | 3.4927 |
| CXoEP | fork-joly-os-mmllm-claude-train-sym24-f54f23ab-CXoEP | 3.5083 |
| RSixc | origin/claude/train-sym24-f99605d3-RSixc | 3.5268 |
| 51Um8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-979a5129-51Um8 | 3.5284 |
| anxsN | fork-davidwuchn-mmllm-claude-train-sym24-5c926a1a-anxsN | 3.5329 |
| Pbs1t | origin/claude/train-sym24-507548de-Pbs1t | 3.5345 |
| **mean** | | **3.5081** |
| **best** | | **3.4821** |

## Chain progression R724 → R725

Previous harvest: `workers/dispatcher/harvest-11way-r724_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5764         | 3.5081         | -0.0683 |
| ctrl_bpc best  | 3.4694         | 3.4821         | +0.0127 |

## Per-round trajectory (best bird: rpTxG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 725 | 4428 | 3.4821 | +0.9687 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r724_sym24`
  - `workers/dispatcher/harvest-2way-r724_sym24`

## Output

`workers/dispatcher/harvest-9way-r725_sym24/round-725/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

