# harvest-17way-r725 — sparse-delta merge of 17 birds

## Worker endpoints

| handle | branch | R725 ctrl_bpc |
|--------|--------|--------------:|
| L9b3p | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9acab864-L9b3p | 3.4758 |
| rpTxG | fork-slaa-us-mmllm-claude-train-sym24-21a8c994-rpTxG | 3.4821 |
| JCOIL | fork-joly-os-mmllm-claude-train-sym24-c7a75138-JCOIL | 3.4836 |
| p7n96 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6c9d5834-p7n96 | 3.4838 |
| J38Zs | fork-slaa-us-mmllm-claude-train-sym24-bb0dd18d-J38Zs | 3.4927 |
| P8NiH | fork-davidwuchn-mmllm-claude-train-sym24-08a4f1c1-P8NiH | 3.4965 |
| CXoEP | fork-joly-os-mmllm-claude-train-sym24-f54f23ab-CXoEP | 3.5083 |
| xN9A6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9a7b88c7-xN9A6 | 3.5167 |
| RSixc | origin/claude/train-sym24-f99605d3-RSixc | 3.5268 |
| 2LaY7 | fork-davidwuchn-mmllm-claude-train-sym24-4e02115c-2LaY7 | 3.5278 |
| 51Um8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-979a5129-51Um8 | 3.5284 |
| anxsN | fork-davidwuchn-mmllm-claude-train-sym24-5c926a1a-anxsN | 3.5329 |
| McI1O | fork-joly-os-mmllm-claude-train-sym24-ace11be1-McI1O | 3.5341 |
| Pbs1t | origin/claude/train-sym24-507548de-Pbs1t | 3.5345 |
| IA8H2 | fork-SeniorCareMarket-mmllm-claude-train-sym24-e4790175-IA8H2 | 3.5356 |
| EMpj5 | fork-slaa-us-mmllm-claude-train-sym24-449eb09f-EMpj5 | 3.8103 |
| Th5jy | origin/claude/train-sym24-79013f1a-Th5jy | 3.8415 |
| **mean** | | **3.5477** |
| **best** | | **3.4758** |

## Chain progression R724 → R725

Previous harvest: `workers/dispatcher/harvest-2way-r724_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6420         | 3.5477         | -0.0943 |
| ctrl_bpc best  | 3.4694         | 3.4758         | +0.0064 |

## Per-round trajectory (best bird: L9b3p)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 725 | 6357 | 3.4758 | +1.3117 |

## Cumulative training contribution

- This harvest: **1360 steps** from 17 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r724_sym24`
  - `workers/dispatcher/harvest-2way-r724_sym24`

## Output

`workers/dispatcher/harvest-17way-r725_sym24/round-725/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 17 workers)
- `dense.pt` (averaged across 17 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

