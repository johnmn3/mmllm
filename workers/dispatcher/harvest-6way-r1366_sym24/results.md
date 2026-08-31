# harvest-6way-r1366 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1366 ctrl_bpc |
|--------|--------|--------------:|
| Z4kvb | fork-SeniorCareMarket-mmllm-claude-train-sym24-7231ecda-Z4kvb | 3.1281 |
| 4rTlV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-eb52f81e-4rTlV | 3.1390 |
| kTmdp | origin/claude/train-sym24-42f8a3cd-kTmdp | 3.1714 |
| 8NpZT | fork-joly-os-mmllm-claude-train-sym24-bd0f9422-8NpZT | 3.2839 |
| kJMSd | origin/claude/train-sym24-c13e6055-kJMSd | 3.4797 |
| o4wsY | origin/claude/train-sym24-9e924264-o4wsY | 3.5097 |
| **mean** | | **3.2853** |
| **best** | | **3.1281** |

## Chain progression R1365 → R1366

Previous harvest: `workers/dispatcher/harvest-3way-r1365_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1950         | 3.2853         | +0.0903 |
| ctrl_bpc best  | 3.1242         | 3.1281         | +0.0039 |

## Per-round trajectory (best bird: Z4kvb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1366 | 5307 | 3.1281 | +0.1212 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1365_sym24`
  - `workers/dispatcher/harvest-2way-r1365_sym24`
  - `workers/dispatcher/harvest-3way-r1365_sym24`

## Output

`workers/dispatcher/harvest-6way-r1366_sym24/round-1366/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

