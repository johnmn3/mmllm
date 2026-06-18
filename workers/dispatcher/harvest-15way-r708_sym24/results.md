# harvest-15way-r708 — sparse-delta merge of 15 birds

## Worker endpoints

| handle | branch | R708 ctrl_bpc |
|--------|--------|--------------:|
| mcJdT | fork-davidwuchn-mmllm-claude-train-sym24-621223a5-mcJdT | 3.5686 |
| KDW9g | origin/claude/train-sym24-bf20cad2-KDW9g | 3.5725 |
| CJdkY | fork-davidwuchn-mmllm-claude-train-sym24-b6af3aa7-CJdkY | 3.5772 |
| vuB8G | origin/claude/train-sym24-67813b0e-vuB8G | 3.5830 |
| gFik3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6b9bf411-gFik3 | 3.6082 |
| ocuyZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6b07727e-ocuyZ | 3.6121 |
| bWzyP | fork-SeniorCareMarket-mmllm-claude-train-sym24-a9dfbd2c-bWzyP | 3.6124 |
| DyxCQ | fork-slaa-us-mmllm-claude-train-sym24-42479f05-DyxCQ | 3.6128 |
| HQvEs | fork-SeniorCareMarket-mmllm-claude-train-sym24-ff79a659-HQvEs | 3.6163 |
| b7NXg | fork-slaa-us-mmllm-claude-train-sym24-15321eb3-b7NXg | 3.6168 |
| HA5sd | fork-joly-os-mmllm-claude-train-sym24-592fb8a6-HA5sd | 3.6249 |
| p0kut | fork-joly-os-mmllm-claude-train-sym24-c41dc38e-p0kut | 3.6262 |
| DGvDy | origin/claude/train-sym24-ed55154f-DGvDy | 3.9123 |
| Nzt0J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-884b61f6-Nzt0J | 3.9145 |
| 4SEij | fork-slaa-us-mmllm-claude-train-sym24-221351ce-4SEij | 4.0665 |
| **mean** | | **3.6750** |
| **best** | | **3.5686** |

## Chain progression R707 → R708

Previous harvest: `workers/dispatcher/harvest-3way-r707_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9335         | 3.6750         | -0.2585 |
| ctrl_bpc best  | 3.9301         | 3.5686         | -0.3615 |

## Per-round trajectory (best bird: mcJdT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 708 | 4522 | 3.5686 | +0.5910 |

## Cumulative training contribution

- This harvest: **1200 steps** from 15 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r707_sym24`
  - `workers/dispatcher/harvest-3way-r707_sym24`

## Output

`workers/dispatcher/harvest-15way-r708_sym24/round-708/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 15 workers)
- `dense.pt` (averaged across 15 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

