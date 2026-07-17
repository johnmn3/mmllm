# harvest-1way-r946 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R946 ctrl_bpc |
|--------|--------|--------------:|
| YFbeq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-82b0621f-YFbeq | 2.8609 |
| **mean** | | **2.8609** |
| **best** | | **2.8609** |

## Chain progression R945 → R946

Previous harvest: `workers/dispatcher/harvest-8way-r945_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8717         | 2.8609         | -0.0108 |
| ctrl_bpc best  | 2.6833         | 2.8609         | +0.1776 |

## Per-round trajectory (best bird: YFbeq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 946 | 6414 | 2.8609 | +0.1239 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r945_sym24`

## Output

`workers/dispatcher/harvest-1way-r946_sym24/round-946/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

