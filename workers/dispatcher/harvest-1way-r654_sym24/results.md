# harvest-1way-r654 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R654 ctrl_bpc |
|--------|--------|--------------:|
| DbVfp | fork-SeniorCareMarket-mmllm-claude-train-sym24-e3c6e63d-DbVfp | 4.1777 |
| **mean** | | **4.1777** |
| **best** | | **4.1777** |

## Chain progression R653 → R654

Previous harvest: `workers/dispatcher/harvest-17way-r653_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.4032         | 4.1777         | -0.2255 |
| ctrl_bpc best  | 4.1705         | 4.1777         | +0.0072 |

## Per-round trajectory (best bird: DbVfp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 654 | 4336 | 4.1777 | +0.0281 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-13way-r653_sym24`

## Output

`workers/dispatcher/harvest-1way-r654_sym24/round-654/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

