# harvest-2way-r838 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R838 ctrl_bpc |
|--------|--------|--------------:|
| oKNy0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-82847fb0-oKNy0 | 3.1155 |
| Fzadx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-10d8878b-Fzadx | 3.3308 |
| **mean** | | **3.2231** |
| **best** | | **3.1155** |

## Chain progression R837 → R838

Previous harvest: `workers/dispatcher/harvest-7way-r837_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0807         | 3.2231         | +0.1424 |
| ctrl_bpc best  | 2.9627         | 3.1155         | +0.1528 |

## Per-round trajectory (best bird: oKNy0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 838 | 6523 | 3.1155 | +0.3454 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1440 steps** from 18 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r837_sym24`

## Output

`workers/dispatcher/harvest-2way-r838_sym24/round-838/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

