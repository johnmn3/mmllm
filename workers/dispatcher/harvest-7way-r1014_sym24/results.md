# harvest-7way-r1014 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1014 ctrl_bpc |
|--------|--------|--------------:|
| ggEXt | fork-SeniorCareMarket-mmllm-claude-train-sym24-abd0b59a-ggEXt | 2.5271 |
| pbKQW | origin/claude/train-sym24-572e7bc9-pbKQW | 2.5272 |
| A0gEW | fork-joly-os-mmllm-claude-train-sym24-aa7dcbd1-A0gEW | 2.5290 |
| rUWk3 | fork-slaa-us-mmllm-claude-train-sym24-a38f3623-rUWk3 | 2.5509 |
| BgeGq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-88e2b7fb-BgeGq | 2.7243 |
| y3zpD | fork-SeniorCareMarket-mmllm-claude-train-sym24-b3ab43dd-y3zpD | 2.7251 |
| atKaf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ac42940b-atKaf | 2.9582 |
| **mean** | | **2.6488** |
| **best** | | **2.5271** |

## Chain progression R1013 → R1014

Previous harvest: `workers/dispatcher/harvest-4way-r1013_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7810         | 2.6488         | -0.1322 |
| ctrl_bpc best  | 2.5322         | 2.5271         | -0.0051 |

## Per-round trajectory (best bird: ggEXt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1014 | 6323 | 2.5271 | +0.1664 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1013_sym24`
  - `workers/dispatcher/harvest-4way-r1013_sym24`

## Output

`workers/dispatcher/harvest-7way-r1014_sym24/round-1014/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

