# harvest-8way-r790 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R790 ctrl_bpc |
|--------|--------|--------------:|
| vXzWh | fork-joly-os-mmllm-claude-train-sym24-e9225c65-vXzWh | 3.1467 |
| S8oWM | fork-joly-os-mmllm-claude-train-sym24-ac8c1af6-S8oWM | 3.1704 |
| 4wEa3 | origin/claude/train-sym24-451bc6b3-4wEa3 | 3.1723 |
| NREAl | fork-slaa-us-mmllm-claude-train-sym24-00b6329d-NREAl | 3.1794 |
| hnoSD | fork-davidwuchn-mmllm-claude-train-sym24-535553d6-hnoSD | 3.1802 |
| Ioqqj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a286a962-Ioqqj | 3.1842 |
| 9lNBf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a680839c-9lNBf | 3.2830 |
| JzTpr | origin/claude/train-sym24-cd2933ee-JzTpr | 3.3129 |
| **mean** | | **3.2036** |
| **best** | | **3.1467** |

## Chain progression R789 → R790

Previous harvest: `workers/dispatcher/harvest-5way-r789_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2209         | 3.2036         | -0.0173 |
| ctrl_bpc best  | 3.1348         | 3.1467         | +0.0119 |

## Per-round trajectory (best bird: vXzWh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 790 | 6602 | 3.1467 | +0.3440 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r789_sym24`
  - `workers/dispatcher/harvest-5way-r789_sym24`

## Output

`workers/dispatcher/harvest-8way-r790_sym24/round-790/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

