# harvest-2way-r879 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R879 ctrl_bpc |
|--------|--------|--------------:|
| TiVb7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f464f0e6-TiVb7 | 3.0137 |
| fmSXI | fork-SeniorCareMarket-mmllm-claude-train-sym24-41ae2ef9-fmSXI | 3.0173 |
| **mean** | | **3.0155** |
| **best** | | **3.0137** |

## Chain progression R878 → R879

Previous harvest: `workers/dispatcher/harvest-4way-r878_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9836         | 3.0155         | +0.0319 |
| ctrl_bpc best  | 2.8434         | 3.0137         | +0.1703 |

## Per-round trajectory (best bird: TiVb7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 879 | 6486 | 3.0137 | +0.3397 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r878_sym24`

## Output

`workers/dispatcher/harvest-2way-r879_sym24/round-879/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

