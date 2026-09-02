# harvest-2way-r1381 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1381 ctrl_bpc |
|--------|--------|--------------:|
| YrMEn | fork-SeniorCareMarket-mmllm-claude-train-sym24-30960dd6-YrMEn | 3.0607 |
| j9gy4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7ac1ee2f-j9gy4 | 3.0925 |
| **mean** | | **3.0766** |
| **best** | | **3.0607** |

## Chain progression R1380 → R1381

Previous harvest: `workers/dispatcher/harvest-2way-r1380_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3162         | 3.0766         | -0.2396 |
| ctrl_bpc best  | 3.2056         | 3.0607         | -0.1449 |

## Per-round trajectory (best bird: YrMEn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1381 | 6342 | 3.0607 | +0.1204 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1380_sym24`

## Output

`workers/dispatcher/harvest-2way-r1381_sym24/round-1381/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

