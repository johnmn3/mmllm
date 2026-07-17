# harvest-4way-r948 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R948 ctrl_bpc |
|--------|--------|--------------:|
| mdWmC | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3c55f175-mdWmC | 2.8622 |
| ZYCEq | origin/claude/train-sym24-a7fe35dc-ZYCEq | 2.8651 |
| ACqnb | fork-SeniorCareMarket-mmllm-claude-train-sym24-3cb97ff1-ACqnb | 3.0590 |
| l5k5Z | fork-slaa-us-mmllm-claude-train-sym24-bd0befff-l5k5Z | 3.0603 |
| **mean** | | **2.9616** |
| **best** | | **2.8622** |

## Chain progression R947 → R948

Previous harvest: `workers/dispatcher/harvest-3way-r947_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7974         | 2.9616         | +0.1642 |
| ctrl_bpc best  | 2.6663         | 2.8622         | +0.1959 |

## Per-round trajectory (best bird: mdWmC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 948 | 6463 | 2.8622 | +0.1433 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r947_sym24`

## Output

`workers/dispatcher/harvest-4way-r948_sym24/round-948/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

