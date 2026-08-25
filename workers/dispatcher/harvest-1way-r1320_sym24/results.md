# harvest-1way-r1320 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1320 ctrl_bpc |
|--------|--------|--------------:|
| uUajn | fork-SeniorCareMarket-mmllm-claude-train-sym24-f01d6c76-uUajn | 3.5000 |
| **mean** | | **3.5000** |
| **best** | | **3.5000** |

## Chain progression R1319 → R1320

Previous harvest: `workers/dispatcher/harvest-4way-r1319_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5528         | 3.5000         | -0.0528 |
| ctrl_bpc best  | 3.4495         | 3.5000         | +0.0505 |

## Per-round trajectory (best bird: uUajn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1320 | 4323 | 3.5000 | +0.0477 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1319_sym24`

## Output

`workers/dispatcher/harvest-1way-r1320_sym24/round-1320/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

