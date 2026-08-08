# harvest-3way-r1139 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1139 ctrl_bpc |
|--------|--------|--------------:|
| i06wo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-94fb6973-i06wo | 2.3566 |
| Mo6M6 | fork-slaa-us-mmllm-claude-train-sym24-842bbf8b-Mo6M6 | 2.7622 |
| 1IDeP | fork-SeniorCareMarket-mmllm-claude-train-sym24-1009ed4e-1IDeP | 2.7652 |
| **mean** | | **2.6280** |
| **best** | | **2.3566** |

## Chain progression R1138 → R1139

Previous harvest: `workers/dispatcher/harvest-10way-r1138_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5499         | 2.6280         | +0.0781 |
| ctrl_bpc best  | 2.3490         | 2.3566         | +0.0076 |

## Per-round trajectory (best bird: i06wo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1139 | 6447 | 2.3566 | +0.2419 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1138_sym24`

## Output

`workers/dispatcher/harvest-3way-r1139_sym24/round-1139/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

