# harvest-1way-r869 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R869 ctrl_bpc |
|--------|--------|--------------:|
| Bq2RP | fork-SeniorCareMarket-mmllm-claude-train-sym24-40bade77-Bq2RP | 3.0397 |
| **mean** | | **3.0397** |
| **best** | | **3.0397** |

## Chain progression R868 → R869

Previous harvest: `workers/dispatcher/harvest-6way-r868_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0275         | 3.0397         | +0.0122 |
| ctrl_bpc best  | 2.8663         | 3.0397         | +0.1734 |

## Per-round trajectory (best bird: Bq2RP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 869 | 6320 | 3.0397 | +0.4388 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r868_sym24`

## Output

`workers/dispatcher/harvest-1way-r869_sym24/round-869/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

