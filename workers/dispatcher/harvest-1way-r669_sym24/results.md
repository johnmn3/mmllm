# harvest-1way-r669 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R669 ctrl_bpc |
|--------|--------|--------------:|
| l8P3T | fork-SeniorCareMarket-mmllm-claude-train-sym24-8cf56c3b-l8P3T | 4.2297 |
| **mean** | | **4.2297** |
| **best** | | **4.2297** |

## Chain progression R668 → R669

Previous harvest: `workers/dispatcher/harvest-11way-r668_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0831         | 4.2297         | +0.1466 |
| ctrl_bpc best  | 3.8806         | 4.2297         | +0.3491 |

## Per-round trajectory (best bird: l8P3T)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 669 | 4356 | 4.2297 | +0.3851 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r668_sym24`

## Output

`workers/dispatcher/harvest-1way-r669_sym24/round-669/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

