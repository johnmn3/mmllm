# harvest-1way-r957 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R957 ctrl_bpc |
|--------|--------|--------------:|
| 7Cxjd | fork-SeniorCareMarket-mmllm-claude-train-sym24-c51ddded-7Cxjd | 2.6577 |
| **mean** | | **2.6577** |
| **best** | | **2.6577** |

## Chain progression R956 → R957

Previous harvest: `workers/dispatcher/harvest-5way-r956_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7988         | 2.6577         | -0.1411 |
| ctrl_bpc best  | 2.6360         | 2.6577         | +0.0217 |

## Per-round trajectory (best bird: 7Cxjd)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 957 | 4219 | 2.6577 | +0.2347 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r956_sym24`

## Output

`workers/dispatcher/harvest-1way-r957_sym24/round-957/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

