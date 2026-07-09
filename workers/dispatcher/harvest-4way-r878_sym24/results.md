# harvest-4way-r878 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R878 ctrl_bpc |
|--------|--------|--------------:|
| 7uLN8 | fork-joly-os-mmllm-claude-train-sym24-4d68acaf-7uLN8 | 2.8434 |
| W1Pod | fork-slaa-us-mmllm-claude-train-sym24-f1895b47-W1Pod | 2.8569 |
| 0gzXr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-d4bbfdcf-0gzXr | 3.0116 |
| AjafD | origin/claude/train-sym24-43831538-AjafD | 3.2227 |
| **mean** | | **2.9836** |
| **best** | | **2.8434** |

## Chain progression R877 → R878

Previous harvest: `workers/dispatcher/harvest-7way-r877_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9874         | 2.9836         | -0.0038 |
| ctrl_bpc best  | 2.8559         | 2.8434         | -0.0125 |

## Per-round trajectory (best bird: 7uLN8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 878 | 6501 | 2.8434 | +0.3100 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r877_sym24`
  - `workers/dispatcher/harvest-6way-r877_sym24`
  - `workers/dispatcher/harvest-7way-r877_sym24`

## Output

`workers/dispatcher/harvest-4way-r878_sym24/round-878/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

