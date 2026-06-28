# harvest-3way-r790 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R790 ctrl_bpc |
|--------|--------|--------------:|
| S8oWM | fork-joly-os-mmllm-claude-train-sym24-ac8c1af6-S8oWM | 3.1704 |
| Ioqqj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a286a962-Ioqqj | 3.1842 |
| JzTpr | origin/claude/train-sym24-cd2933ee-JzTpr | 3.3129 |
| **mean** | | **3.2225** |
| **best** | | **3.1704** |

## Chain progression R789 → R790

Previous harvest: `workers/dispatcher/harvest-5way-r789_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2209         | 3.2225         | +0.0016 |
| ctrl_bpc best  | 3.1348         | 3.1704         | +0.0356 |

## Per-round trajectory (best bird: S8oWM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 790 | 6512 | 3.1704 | +0.5232 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r789_sym24`

## Output

`workers/dispatcher/harvest-3way-r790_sym24/round-790/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

