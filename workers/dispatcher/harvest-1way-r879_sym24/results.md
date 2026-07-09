# harvest-1way-r879 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R879 ctrl_bpc |
|--------|--------|--------------:|
| fmSXI | fork-SeniorCareMarket-mmllm-claude-train-sym24-41ae2ef9-fmSXI | 3.0173 |
| **mean** | | **3.0173** |
| **best** | | **3.0173** |

## Chain progression R878 → R879

Previous harvest: `workers/dispatcher/harvest-4way-r878_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9836         | 3.0173         | +0.0337 |
| ctrl_bpc best  | 2.8434         | 3.0173         | +0.1739 |

## Per-round trajectory (best bird: fmSXI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 879 | 4512 | 3.0173 | +0.4722 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r878_sym24`

## Output

`workers/dispatcher/harvest-1way-r879_sym24/round-879/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

