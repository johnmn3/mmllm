# harvest-4way-r926 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R926 ctrl_bpc |
|--------|--------|--------------:|
| A2qhF | origin/claude/train-sym24-15c98f27-A2qhF | 2.7653 |
| Mxp5m | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1a8a34d3-Mxp5m | 2.9120 |
| DIgu4 | fork-joly-os-mmllm-claude-train-sym24-f7450f73-DIgu4 | 3.1158 |
| CxqFZ | fork-slaa-us-mmllm-claude-train-sym24-69f28014-CxqFZ | 3.1170 |
| **mean** | | **2.9775** |
| **best** | | **2.7653** |

## Chain progression R925 → R926

Previous harvest: `workers/dispatcher/harvest-2way-r925_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0240         | 2.9775         | -0.0465 |
| ctrl_bpc best  | 2.9207         | 2.7653         | -0.1554 |

## Per-round trajectory (best bird: A2qhF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 926 | 6606 | 2.7653 | +0.1458 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r925_sym24`

## Output

`workers/dispatcher/harvest-4way-r926_sym24/round-926/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

