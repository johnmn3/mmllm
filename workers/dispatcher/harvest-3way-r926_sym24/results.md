# harvest-3way-r926 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R926 ctrl_bpc |
|--------|--------|--------------:|
| Mxp5m | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1a8a34d3-Mxp5m | 2.9120 |
| DIgu4 | fork-joly-os-mmllm-claude-train-sym24-f7450f73-DIgu4 | 3.1158 |
| CxqFZ | fork-slaa-us-mmllm-claude-train-sym24-69f28014-CxqFZ | 3.1170 |
| **mean** | | **3.0483** |
| **best** | | **2.9120** |

## Chain progression R610 → R926

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.0483         | +0.9111 |
| ctrl_bpc best  | 2.1268         | 2.9120         | +0.7852 |

## Per-round trajectory (best bird: Mxp5m)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 926 | 6421 | 2.9120 | +0.1923 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r925_sym24`

## Output

`workers/dispatcher/harvest-3way-r926_sym24/round-926/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

