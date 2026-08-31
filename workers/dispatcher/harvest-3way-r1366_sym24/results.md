# harvest-3way-r1366 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1366 ctrl_bpc |
|--------|--------|--------------:|
| Z4kvb | fork-SeniorCareMarket-mmllm-claude-train-sym24-7231ecda-Z4kvb | 3.1281 |
| 4rTlV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-eb52f81e-4rTlV | 3.1390 |
| 8NpZT | fork-joly-os-mmllm-claude-train-sym24-bd0f9422-8NpZT | 3.2839 |
| **mean** | | **3.1837** |
| **best** | | **3.1281** |

## Chain progression R610 → R1366

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.1837         | +1.0465 |
| ctrl_bpc best  | 2.1268         | 3.1281         | +1.0013 |

## Per-round trajectory (best bird: Z4kvb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1366 | 5307 | 3.1281 | +0.1212 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1365_sym24`
  - `workers/dispatcher/harvest-2way-r1365_sym24`

## Output

`workers/dispatcher/harvest-3way-r1366_sym24/round-1366/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

