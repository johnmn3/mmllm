# harvest-1way-r762 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R762 ctrl_bpc |
|--------|--------|--------------:|
| Zn6hj | fork-davidwuchn-mmllm-claude-train-sym24-d589cd51-Zn6hj | 3.3235 |
| **mean** | | **3.3235** |
| **best** | | **3.3235** |

## Chain progression R761 → R762

Previous harvest: `workers/dispatcher/harvest-1way-r761_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3050         | 3.3235         | +0.0185 |
| ctrl_bpc best  | 3.3050         | 3.3235         | +0.0185 |

## Per-round trajectory (best bird: Zn6hj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 762 | 4292 | 3.3235 | +0.6075 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r761_sym24`

## Output

`workers/dispatcher/harvest-1way-r762_sym24/round-762/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

