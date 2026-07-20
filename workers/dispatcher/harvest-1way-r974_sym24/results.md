# harvest-1way-r974 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R974 ctrl_bpc |
|--------|--------|--------------:|
| keJib | fork-SeniorCareMarket-mmllm-claude-train-sym24-59ba3b43-keJib | 2.7955 |
| **mean** | | **2.7955** |
| **best** | | **2.7955** |

## Chain progression R973 → R974

Previous harvest: `workers/dispatcher/harvest-3way-r973_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8693         | 2.7955         | -0.0738 |
| ctrl_bpc best  | 2.5980         | 2.7955         | +0.1975 |

## Per-round trajectory (best bird: keJib)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 974 | 5449 | 2.7955 | +0.1516 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r973_sym24`

## Output

`workers/dispatcher/harvest-1way-r974_sym24/round-974/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

