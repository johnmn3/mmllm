# harvest-1way-r914 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R914 ctrl_bpc |
|--------|--------|--------------:|
| xDldE | fork-SeniorCareMarket-mmllm-claude-train-sym24-6da2b555-xDldE | 2.7730 |
| **mean** | | **2.7730** |
| **best** | | **2.7730** |

## Chain progression R913 → R914

Previous harvest: `workers/dispatcher/harvest-5way-r913_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0258         | 2.7730         | -0.2528 |
| ctrl_bpc best  | 2.7482         | 2.7730         | +0.0248 |

## Per-round trajectory (best bird: xDldE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 914 | 3715 | 2.7730 | +0.2718 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r913_sym24`

## Output

`workers/dispatcher/harvest-1way-r914_sym24/round-914/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

