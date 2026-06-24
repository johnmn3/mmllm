# harvest-1way-r752 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R752 ctrl_bpc |
|--------|--------|--------------:|
| vnBBQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-7ed29293-vnBBQ | 3.3561 |
| **mean** | | **3.3561** |
| **best** | | **3.3561** |

## Chain progression R751 → R752

Previous harvest: `workers/dispatcher/harvest-5way-r751_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4279         | 3.3561         | -0.0718 |
| ctrl_bpc best  | 3.3417         | 3.3561         | +0.0144 |

## Per-round trajectory (best bird: vnBBQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 752 | 3732 | 3.3561 | +0.5232 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r751_sym24`

## Output

`workers/dispatcher/harvest-1way-r752_sym24/round-752/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

