# harvest-5way-r789 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R789 ctrl_bpc |
|--------|--------|--------------:|
| HHU3e | origin/claude/train-sym24-3041c691-HHU3e | 3.1348 |
| uUAdG | fork-slaa-us-mmllm-claude-train-sym24-2a6aed58-uUAdG | 3.1556 |
| Qa64N | fork-SeniorCareMarket-mmllm-claude-train-sym24-31285760-Qa64N | 3.2204 |
| 7Sbju | fork-joly-os-mmllm-claude-train-sym24-04bc83ae-7Sbju | 3.2901 |
| 1xeB5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6cf677c8-1xeB5 | 3.3036 |
| **mean** | | **3.2209** |
| **best** | | **3.1348** |

## Chain progression R788 → R789

Previous harvest: `workers/dispatcher/harvest-3way-r788_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3296         | 3.2209         | -0.1087 |
| ctrl_bpc best  | 3.1429         | 3.1348         | -0.0081 |

## Per-round trajectory (best bird: HHU3e)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 789 | 6616 | 3.1348 | +0.5001 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r788_sym24`

## Output

`workers/dispatcher/harvest-5way-r789_sym24/round-789/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

