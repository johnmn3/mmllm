# harvest-3way-r1405 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1405 ctrl_bpc |
|--------|--------|--------------:|
| Fp9Qu | fork-SeniorCareMarket-mmllm-claude-train-sym24-e9238f43-Fp9Qu | 3.3002 |
| AiBEn | origin/claude/train-sym24-105e3350-AiBEn | 3.3531 |
| uGXsV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-349c01e1-uGXsV | 3.7088 |
| **mean** | | **3.4540** |
| **best** | | **3.3002** |

## Chain progression R1404 → R1405

Previous harvest: `workers/dispatcher/harvest-1way-r1404_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7779         | 3.4540         | -0.3239 |
| ctrl_bpc best  | 3.7779         | 3.3002         | -0.4777 |

## Per-round trajectory (best bird: Fp9Qu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1405 | 4201 | 3.3002 | +0.0822 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1404_sym24`

## Output

`workers/dispatcher/harvest-3way-r1405_sym24/round-1405/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

