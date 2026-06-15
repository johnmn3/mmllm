# harvest-7way-r683 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R683 ctrl_bpc |
|--------|--------|--------------:|
| XyduD | fork-SeniorCareMarket-mmllm-claude-train-sym24-01425ec4-XyduD | 3.7654 |
| 5CqqH | fork-davidwuchn-mmllm-claude-train-sym24-36e02e55-5CqqH | 3.7780 |
| CZZbA | fork-slaa-us-mmllm-claude-train-sym24-cb77b0bb-CZZbA | 3.7906 |
| uHkr7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3758d534-uHkr7 | 3.8194 |
| PsiMA | fork-davidwuchn-mmllm-claude-train-sym24-c408fff4-PsiMA | 3.8380 |
| EHA4x | origin/claude/train-sym24-95f4937f-EHA4x | 4.0629 |
| avY8T | fork-joly-os-mmllm-claude-train-sym24-6d3a3846-avY8T | 4.1232 |
| **mean** | | **3.8825** |
| **best** | | **3.7654** |

## Chain progression R682 → R683

Previous harvest: `workers/dispatcher/harvest-1way-r682_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8031         | 3.8825         | +0.0794 |
| ctrl_bpc best  | 3.8031         | 3.7654         | -0.0377 |

## Per-round trajectory (best bird: XyduD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 683 | 4358 | 3.7654 | +0.5577 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r682_sym24`

## Output

`workers/dispatcher/harvest-7way-r683_sym24/round-683/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

