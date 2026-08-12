# harvest-1way-r1184 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1184 ctrl_bpc |
|--------|--------|--------------:|
| qLQ5z | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1f3e6444-qLQ5z | 2.3010 |
| **mean** | | **2.3010** |
| **best** | | **2.3010** |

## Chain progression R1183 → R1184

Previous harvest: `workers/dispatcher/harvest-5way-r1183_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4698         | 2.3010         | -0.1688 |
| ctrl_bpc best  | 2.3234         | 2.3010         | -0.0224 |

## Per-round trajectory (best bird: qLQ5z)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1184 | 3840 | 2.3010 | +0.2804 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1183_sym24`

## Output

`workers/dispatcher/harvest-1way-r1184_sym24/round-1184/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

