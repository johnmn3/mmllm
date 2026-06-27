# harvest-1way-r783 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R783 ctrl_bpc |
|--------|--------|--------------:|
| sWH1Q | fork-SeniorCareMarket-mmllm-claude-train-sym24-fd39a753-sWH1Q | 3.1869 |
| **mean** | | **3.1869** |
| **best** | | **3.1869** |

## Chain progression R782 → R783

Previous harvest: `workers/dispatcher/harvest-17way-r782_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2967         | 3.1869         | -0.1098 |
| ctrl_bpc best  | 3.1844         | 3.1869         | +0.0025 |

## Per-round trajectory (best bird: sWH1Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 783 | 6472 | 3.1869 | +0.6227 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r782_sym24`

## Output

`workers/dispatcher/harvest-1way-r783_sym24/round-783/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

