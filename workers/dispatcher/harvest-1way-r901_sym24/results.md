# harvest-1way-r901 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R901 ctrl_bpc |
|--------|--------|--------------:|
| FD66w | fork-SeniorCareMarket-mmllm-claude-train-sym24-c1273a63-FD66w | 2.7967 |
| **mean** | | **2.7967** |
| **best** | | **2.7967** |

## Chain progression R900 → R901

Previous harvest: `workers/dispatcher/harvest-3way-r900_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9103         | 2.7967         | -0.1136 |
| ctrl_bpc best  | 2.8119         | 2.7967         | -0.0152 |

## Per-round trajectory (best bird: FD66w)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 901 | 3899 | 2.7967 | +0.2066 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r900_sym24`

## Output

`workers/dispatcher/harvest-1way-r901_sym24/round-901/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

