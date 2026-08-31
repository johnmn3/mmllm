# harvest-2way-r1366 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1366 ctrl_bpc |
|--------|--------|--------------:|
| Z4kvb | fork-SeniorCareMarket-mmllm-claude-train-sym24-7231ecda-Z4kvb | 3.1281 |
| o4wsY | origin/claude/train-sym24-9e924264-o4wsY | 3.5097 |
| **mean** | | **3.3189** |
| **best** | | **3.1281** |

## Chain progression R1365 → R1366

Previous harvest: `workers/dispatcher/harvest-3way-r1365_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1950         | 3.3189         | +0.1239 |
| ctrl_bpc best  | 3.1242         | 3.1281         | +0.0039 |

## Per-round trajectory (best bird: Z4kvb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1366 | 5307 | 3.1281 | +0.1212 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1365_sym24`
  - `workers/dispatcher/harvest-2way-r1365_sym24`

## Output

`workers/dispatcher/harvest-2way-r1366_sym24/round-1366/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

