# harvest-5way-r1139 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1139 ctrl_bpc |
|--------|--------|--------------:|
| QxzS8 | fork-joly-os-mmllm-claude-train-sym24-a54f8200-QxzS8 | 2.3423 |
| i06wo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-94fb6973-i06wo | 2.3566 |
| XyAn2 | origin/claude/train-sym24-ffc8e380-XyAn2 | 2.5570 |
| Mo6M6 | fork-slaa-us-mmllm-claude-train-sym24-842bbf8b-Mo6M6 | 2.7622 |
| 1IDeP | fork-SeniorCareMarket-mmllm-claude-train-sym24-1009ed4e-1IDeP | 2.7652 |
| **mean** | | **2.5567** |
| **best** | | **2.3423** |

## Chain progression R1138 → R1139

Previous harvest: `workers/dispatcher/harvest-10way-r1138_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5499         | 2.5567         | +0.0068 |
| ctrl_bpc best  | 2.3490         | 2.3423         | -0.0067 |

## Per-round trajectory (best bird: QxzS8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1139 | 6675 | 2.3423 | +0.2498 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1138_sym24`
  - `workers/dispatcher/harvest-6way-r1138_sym24`

## Output

`workers/dispatcher/harvest-5way-r1139_sym24/round-1139/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

