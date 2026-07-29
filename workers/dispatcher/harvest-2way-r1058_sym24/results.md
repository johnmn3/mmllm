# harvest-2way-r1058 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1058 ctrl_bpc |
|--------|--------|--------------:|
| 8TV8F | origin/claude/train-sym24-72254b39-8TV8F | 2.6454 |
| PGXP6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7754350a-PGXP6 | 2.8525 |
| **mean** | | **2.7489** |
| **best** | | **2.6454** |

## Chain progression R1057 → R1058

Previous harvest: `workers/dispatcher/harvest-6way-r1057_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6277         | 2.7489         | +0.1212 |
| ctrl_bpc best  | 2.4609         | 2.6454         | +0.1845 |

## Per-round trajectory (best bird: 8TV8F)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1058 | 5320 | 2.6454 | +0.1913 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1057_sym24`

## Output

`workers/dispatcher/harvest-2way-r1058_sym24/round-1058/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

