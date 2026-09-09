# harvest-1way-r1417 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1417 ctrl_bpc |
|--------|--------|--------------:|
| ENthI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-275a129b-ENthI | 3.1366 |
| **mean** | | **3.1366** |
| **best** | | **3.1366** |

## Chain progression R1416 → R1417

Previous harvest: `workers/dispatcher/harvest-4way-r1416_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1988         | 3.1366         | -0.0622 |
| ctrl_bpc best  | 3.1610         | 3.1366         | -0.0244 |

## Per-round trajectory (best bird: ENthI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1417 | 3531 | 3.1366 | +0.1508 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1416_sym24`

## Output

`workers/dispatcher/harvest-1way-r1417_sym24/round-1417/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

