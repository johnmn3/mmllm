# harvest-1way-r1055 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1055 ctrl_bpc |
|--------|--------|--------------:|
| QxQ2U | fork-SeniorCareMarket-mmllm-claude-train-sym24-78892790-QxQ2U | 2.6639 |
| **mean** | | **2.6639** |
| **best** | | **2.6639** |

## Chain progression R1054 → R1055

Previous harvest: `workers/dispatcher/harvest-1way-r1054_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8569         | 2.6639         | -0.1930 |
| ctrl_bpc best  | 2.8569         | 2.6639         | -0.1930 |

## Per-round trajectory (best bird: QxQ2U)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1055 | 4418 | 2.6639 | +0.1925 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1054_sym24`

## Output

`workers/dispatcher/harvest-1way-r1055_sym24/round-1055/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

