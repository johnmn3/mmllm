# harvest-1way-r103 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R103 ctrl_bpc |
|--------|--------|--------------:|
| DXgxJ | fork-SeniorCareMarket-mmllm-claude-train-23f12a03-DXgxJ | 1.0209 |
| **mean** | | **1.0209** |
| **best** | | **1.0209** |

## Chain progression R99 → R103

Previous harvest: `workers/dispatcher/harvest-fold6way-r99`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0025         | 1.0209         | +0.0184 |
| ctrl_bpc best  | 0.9641         | 1.0209         | +0.0568 |

## Per-round trajectory (best bird: DXgxJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 100 | 653 | 1.0033 | +0.0085 |
| 101 | 545 | 1.0036 | +0.0058 |
| 102 | 572 | 1.0513 | +0.0082 |
| 103 | 510 | 1.0209 | +0.0089 |

## Cumulative training contribution

- This harvest: **28 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **2186 steps** from 55 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r99`

## Output

`workers/dispatcher/harvest-1way-r103/round-103/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

