# harvest-1way-r867 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R867 ctrl_bpc |
|--------|--------|--------------:|
| yAjDM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ea3d0384-yAjDM | 3.2431 |
| **mean** | | **3.2431** |
| **best** | | **3.2431** |

## Chain progression R866 → R867

Previous harvest: `workers/dispatcher/harvest-1way-r866_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9291         | 3.2431         | +0.3140 |
| ctrl_bpc best  | 2.9291         | 3.2431         | +0.3140 |

## Per-round trajectory (best bird: yAjDM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 867 | 6560 | 3.2431 | +0.4133 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r866_sym24`

## Output

`workers/dispatcher/harvest-1way-r867_sym24/round-867/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

