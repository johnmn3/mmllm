# harvest-4way-r1013 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1013 ctrl_bpc |
|--------|--------|--------------:|
| DUsqm | fork-SeniorCareMarket-mmllm-claude-train-sym24-3107a232-DUsqm | 2.5322 |
| HGYiV | fork-slaa-us-mmllm-claude-train-sym24-3d37e87d-HGYiV | 2.7441 |
| yBNor | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-26c221ae-yBNor | 2.9231 |
| UZl4T | origin/claude/train-sym24-89be1fec-UZl4T | 2.9247 |
| **mean** | | **2.7810** |
| **best** | | **2.5322** |

## Chain progression R1012 → R1013

Previous harvest: `workers/dispatcher/harvest-5way-r1012_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5999         | 2.7810         | +0.1811 |
| ctrl_bpc best  | 2.5317         | 2.5322         | +0.0005 |

## Per-round trajectory (best bird: DUsqm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1013 | 6426 | 2.5322 | +0.1695 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1012_sym24`

## Output

`workers/dispatcher/harvest-4way-r1013_sym24/round-1013/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

