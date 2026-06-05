# harvest-4way-r611 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R611 ctrl_bpc |
|--------|--------|--------------:|
| WYePx | fork-slaa-us-mmllm-claude-train-sym24-5d3ed970-WYePx | 2.1281 |
| vSBUo | origin/claude/train-sym24-942c1ac3-vSBUo | 2.3508 |
| jC61Z | fork-davidwuchn-mmllm-claude-train-sym24-18e1ae38-jC61Z | 2.6013 |
| rZsj4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5200ae20-rZsj4 | 2.6076 |
| **mean** | | **2.4219** |
| **best** | | **2.1281** |

## Chain progression R610 → R611

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.4219         | +0.2847 |
| ctrl_bpc best  | 2.1268         | 2.1281         | +0.0013 |

## Per-round trajectory (best bird: WYePx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 611 | 5161 | 2.1281 | +0.0195 |

## Cumulative training contribution

- This harvest: **200 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **200 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-merge-r610_sym24`

## Output

`workers/dispatcher/harvest-4way-r611_sym24/round-611/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

