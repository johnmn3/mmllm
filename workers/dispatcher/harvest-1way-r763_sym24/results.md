# harvest-1way-r763 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R763 ctrl_bpc |
|--------|--------|--------------:|
| LFWVD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0fdb0521-LFWVD | 3.2594 |
| **mean** | | **3.2594** |
| **best** | | **3.2594** |

## Chain progression R762 → R763

Previous harvest: `workers/dispatcher/harvest-1way-r762_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3235         | 3.2594         | -0.0641 |
| ctrl_bpc best  | 3.3235         | 3.2594         | -0.0641 |

## Per-round trajectory (best bird: LFWVD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 763 | 5379 | 3.2594 | +0.5712 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r762_sym24`

## Output

`workers/dispatcher/harvest-1way-r763_sym24/round-763/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

