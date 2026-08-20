# harvest-1way-r1258 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1258 ctrl_bpc |
|--------|--------|--------------:|
| QlonI | fork-SeniorCareMarket-mmllm-claude-train-sym24-8dda44c0-QlonI | 2.2323 |
| **mean** | | **2.2323** |
| **best** | | **2.2323** |

## Chain progression R1257 → R1258

Previous harvest: `workers/dispatcher/harvest-9way-r1257_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3775         | 2.2323         | -0.1452 |
| ctrl_bpc best  | 2.2354         | 2.2323         | -0.0031 |

## Per-round trajectory (best bird: QlonI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1258 | 3762 | 2.2323 | +0.2478 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1257_sym24`

## Output

`workers/dispatcher/harvest-1way-r1258_sym24/round-1258/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

