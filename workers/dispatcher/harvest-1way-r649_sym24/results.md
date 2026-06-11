# harvest-1way-r649 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R649 ctrl_bpc |
|--------|--------|--------------:|
| 4gNV4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5d27a931-4gNV4 | 4.3552 |
| **mean** | | **4.3552** |
| **best** | | **4.3552** |

## Chain progression R648 → R649

Previous harvest: `workers/dispatcher/harvest-2way-r648_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.6010         | 4.3552         | -0.2458 |
| ctrl_bpc best  | 4.3865         | 4.3552         | -0.0313 |

## Per-round trajectory (best bird: 4gNV4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 649 | 6440 | 4.3552 | +0.0569 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r648_sym24`

## Output

`workers/dispatcher/harvest-1way-r649_sym24/round-649/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

