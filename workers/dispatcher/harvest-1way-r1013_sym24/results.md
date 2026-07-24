# harvest-1way-r1013 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1013 ctrl_bpc |
|--------|--------|--------------:|
| yBNor | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-26c221ae-yBNor | 2.9231 |
| **mean** | | **2.9231** |
| **best** | | **2.9231** |

## Chain progression R1012 → R1013

Previous harvest: `workers/dispatcher/harvest-5way-r1012_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5999         | 2.9231         | +0.3232 |
| ctrl_bpc best  | 2.5317         | 2.9231         | +0.3914 |

## Per-round trajectory (best bird: yBNor)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1013 | 3808 | 2.9231 | +0.1566 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1012_sym24`

## Output

`workers/dispatcher/harvest-1way-r1013_sym24/round-1013/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

