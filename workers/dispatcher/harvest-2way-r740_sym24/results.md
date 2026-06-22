# harvest-2way-r740 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R740 ctrl_bpc |
|--------|--------|--------------:|
| PNdu6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-b4b7c1c9-PNdu6 | 3.7508 |
| 6pRFV | fork-slaa-us-mmllm-claude-train-sym24-435ffd5f-6pRFV | 3.7781 |
| **mean** | | **3.7645** |
| **best** | | **3.7508** |

## Chain progression R739 → R740

Previous harvest: `workers/dispatcher/harvest-10way-r739_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4944         | 3.7645         | +0.2700 |
| ctrl_bpc best  | 3.3744         | 3.7508         | +0.3764 |

## Per-round trajectory (best bird: PNdu6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 740 | 6784 | 3.7508 | +0.6878 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r739_sym24`

## Output

`workers/dispatcher/harvest-2way-r740_sym24/round-740/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

