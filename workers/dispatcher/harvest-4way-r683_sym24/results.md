# harvest-4way-r683 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R683 ctrl_bpc |
|--------|--------|--------------:|
| XyduD | fork-SeniorCareMarket-mmllm-claude-train-sym24-01425ec4-XyduD | 3.7654 |
| CZZbA | fork-slaa-us-mmllm-claude-train-sym24-cb77b0bb-CZZbA | 3.7906 |
| uHkr7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3758d534-uHkr7 | 3.8194 |
| PsiMA | fork-davidwuchn-mmllm-claude-train-sym24-c408fff4-PsiMA | 3.8380 |
| **mean** | | **3.8034** |
| **best** | | **3.7654** |

## Chain progression R682 → R683

Previous harvest: `workers/dispatcher/harvest-1way-r682_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8031         | 3.8034         | +0.0002 |
| ctrl_bpc best  | 3.8031         | 3.7654         | -0.0377 |

## Per-round trajectory (best bird: XyduD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 683 | 4358 | 3.7654 | +0.5577 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r682_sym24`

## Output

`workers/dispatcher/harvest-4way-r683_sym24/round-683/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

