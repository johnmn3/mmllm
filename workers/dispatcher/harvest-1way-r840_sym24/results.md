# harvest-1way-r840 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R840 ctrl_bpc |
|--------|--------|--------------:|
| yYn37 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8cc747fd-yYn37 | 3.1526 |
| **mean** | | **3.1526** |
| **best** | | **3.1526** |

## Chain progression R839 → R840

Previous harvest: `workers/dispatcher/harvest-3way-r839_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1336         | 3.1526         | +0.0190 |
| ctrl_bpc best  | 2.9550         | 3.1526         | +0.1976 |

## Per-round trajectory (best bird: yYn37)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 840 | 6281 | 3.1526 | +0.4522 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r839_sym24`

## Output

`workers/dispatcher/harvest-1way-r840_sym24/round-840/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

