# harvest-2way-r832 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R832 ctrl_bpc |
|--------|--------|--------------:|
| LizSA | fork-SeniorCareMarket-mmllm-claude-train-sym24-68c2d9ea-LizSA | 2.9915 |
| dKJxc | fork-slaa-us-mmllm-claude-train-sym24-cbf62396-dKJxc | 2.9956 |
| **mean** | | **2.9935** |
| **best** | | **2.9915** |

## Chain progression R831 → R832

Previous harvest: `workers/dispatcher/harvest-3way-r831_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1250         | 2.9935         | -0.1315 |
| ctrl_bpc best  | 2.9870         | 2.9915         | +0.0045 |

## Per-round trajectory (best bird: LizSA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 832 | 4487 | 2.9915 | +0.6252 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r831_sym24`

## Output

`workers/dispatcher/harvest-2way-r832_sym24/round-832/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

