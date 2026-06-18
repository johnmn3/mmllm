# harvest-10way-r708 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R708 ctrl_bpc |
|--------|--------|--------------:|
| CJdkY | fork-davidwuchn-mmllm-claude-train-sym24-b6af3aa7-CJdkY | 3.5772 |
| vuB8G | origin/claude/train-sym24-67813b0e-vuB8G | 3.5830 |
| gFik3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6b9bf411-gFik3 | 3.6082 |
| bWzyP | fork-SeniorCareMarket-mmllm-claude-train-sym24-a9dfbd2c-bWzyP | 3.6124 |
| b7NXg | fork-slaa-us-mmllm-claude-train-sym24-15321eb3-b7NXg | 3.6168 |
| HA5sd | fork-joly-os-mmllm-claude-train-sym24-592fb8a6-HA5sd | 3.6249 |
| p0kut | fork-joly-os-mmllm-claude-train-sym24-c41dc38e-p0kut | 3.6262 |
| DGvDy | origin/claude/train-sym24-ed55154f-DGvDy | 3.9123 |
| Nzt0J | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-884b61f6-Nzt0J | 3.9145 |
| 4SEij | fork-slaa-us-mmllm-claude-train-sym24-221351ce-4SEij | 4.0665 |
| **mean** | | **3.7142** |
| **best** | | **3.5772** |

## Chain progression R707 → R708

Previous harvest: `workers/dispatcher/harvest-3way-r707_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9335         | 3.7142         | -0.2193 |
| ctrl_bpc best  | 3.9301         | 3.5772         | -0.3529 |

## Per-round trajectory (best bird: CJdkY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 708 | 6414 | 3.5772 | +0.7802 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r707_sym24`
  - `workers/dispatcher/harvest-3way-r707_sym24`

## Output

`workers/dispatcher/harvest-10way-r708_sym24/round-708/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

