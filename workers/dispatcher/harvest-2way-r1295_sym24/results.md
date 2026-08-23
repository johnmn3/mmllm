# harvest-2way-r1295 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1295 ctrl_bpc |
|--------|--------|--------------:|
| vkJs9 | fork-slaa-us-mmllm-claude-train-sym24-845762d8-vkJs9 | 4.0499 |
| irkpi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-26db4181-irkpi | 4.1182 |
| **mean** | | **4.0840** |
| **best** | | **4.0499** |

## Chain progression R1294 → R1295

Previous harvest: `workers/dispatcher/harvest-8way-r1294_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.3100         | 4.0840         | -0.2260 |
| ctrl_bpc best  | 4.1198         | 4.0499         | -0.0699 |

## Per-round trajectory (best bird: vkJs9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1295 | 6581 | 4.0499 | +0.0295 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1294_sym24`

## Output

`workers/dispatcher/harvest-2way-r1295_sym24/round-1295/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

