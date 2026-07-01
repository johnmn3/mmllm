# harvest-1way-r820 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R820 ctrl_bpc |
|--------|--------|--------------:|
| 6ysxB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6a4d1e97-6ysxB | 3.0409 |
| **mean** | | **3.0409** |
| **best** | | **3.0409** |

## Chain progression R819 → R820

Previous harvest: `workers/dispatcher/harvest-11way-r819_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1748         | 3.0409         | -0.1339 |
| ctrl_bpc best  | 3.0247         | 3.0409         | +0.0162 |

## Per-round trajectory (best bird: 6ysxB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 820 | 4076 | 3.0409 | +0.5363 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r819_sym24`

## Output

`workers/dispatcher/harvest-1way-r820_sym24/round-820/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

