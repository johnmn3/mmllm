# harvest-5way-r856 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R856 ctrl_bpc |
|--------|--------|--------------:|
| mXMZG | origin/claude/train-sym24-51028135-mXMZG | 2.9048 |
| V77EH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f7213d7d-V77EH | 2.9060 |
| 9fEvV | fork-joly-os-mmllm-claude-train-sym24-2e3aa74f-9fEvV | 2.9159 |
| JGA8B | fork-slaa-us-mmllm-claude-train-sym24-498fca7f-JGA8B | 3.0759 |
| yhjhI | fork-SeniorCareMarket-mmllm-claude-train-sym24-2d3c754b-yhjhI | 3.2957 |
| **mean** | | **3.0197** |
| **best** | | **2.9048** |

## Chain progression R855 → R856

Previous harvest: `workers/dispatcher/harvest-3way-r855_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1722         | 3.0197         | -0.1525 |
| ctrl_bpc best  | 2.9259         | 2.9048         | -0.0211 |

## Per-round trajectory (best bird: mXMZG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 856 | 5387 | 2.9048 | +0.4732 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r855_sym24`

## Output

`workers/dispatcher/harvest-5way-r856_sym24/round-856/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

