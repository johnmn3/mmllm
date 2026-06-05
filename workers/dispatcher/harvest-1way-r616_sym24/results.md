# harvest-1way-r616 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R616 ctrl_bpc |
|--------|--------|--------------:|
| BZiaJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-aec8b47d-BZiaJ | 2.1452 |
| **mean** | | **2.1452** |
| **best** | | **2.1452** |

## Chain progression R615 → R616

Previous harvest: `workers/dispatcher/harvest-3way-r615_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2900         | 2.1452         | -0.1448 |
| ctrl_bpc best  | 2.1282         | 2.1452         | +0.0170 |

## Per-round trajectory (best bird: BZiaJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 616 | 5183 | 2.1452 | +0.0352 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r615_sym24`

## Output

`workers/dispatcher/harvest-1way-r616_sym24/round-616/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

