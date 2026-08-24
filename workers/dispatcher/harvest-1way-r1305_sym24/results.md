# harvest-1way-r1305 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1305 ctrl_bpc |
|--------|--------|--------------:|
| FdZ10 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f5466cbb-FdZ10 | 3.4957 |
| **mean** | | **3.4957** |
| **best** | | **3.4957** |

## Chain progression R1304 → R1305

Previous harvest: `workers/dispatcher/harvest-5way-r1304_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6270         | 3.4957         | -0.1313 |
| ctrl_bpc best  | 3.5458         | 3.4957         | -0.0501 |

## Per-round trajectory (best bird: FdZ10)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1305 | 3494 | 3.4957 | +0.0764 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1304_sym24`

## Output

`workers/dispatcher/harvest-1way-r1305_sym24/round-1305/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

