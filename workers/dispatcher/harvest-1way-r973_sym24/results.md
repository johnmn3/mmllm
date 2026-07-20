# harvest-1way-r973 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R973 ctrl_bpc |
|--------|--------|--------------:|
| pmrUc | fork-SeniorCareMarket-mmllm-claude-train-sym24-1df995d4-pmrUc | 3.0035 |
| **mean** | | **3.0035** |
| **best** | | **3.0035** |

## Chain progression R972 → R973

Previous harvest: `workers/dispatcher/harvest-5way-r972_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7716         | 3.0035         | +0.2319 |
| ctrl_bpc best  | 2.6081         | 3.0035         | +0.3954 |

## Per-round trajectory (best bird: pmrUc)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 973 | 6242 | 3.0035 | +0.1538 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r972_sym24`

## Output

`workers/dispatcher/harvest-1way-r973_sym24/round-973/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

