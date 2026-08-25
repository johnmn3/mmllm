# harvest-1way-r1315 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1315 ctrl_bpc |
|--------|--------|--------------:|
| 4kVJ0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b0fa6220-4kVJ0 | 3.7697 |
| **mean** | | **3.7697** |
| **best** | | **3.7697** |

## Chain progression R1314 → R1315

Previous harvest: `workers/dispatcher/harvest-7way-r1314_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6515         | 3.7697         | +0.1182 |
| ctrl_bpc best  | 3.4246         | 3.7697         | +0.3451 |

## Per-round trajectory (best bird: 4kVJ0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1315 | 3731 | 3.7697 | +0.0392 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1314_sym24`

## Output

`workers/dispatcher/harvest-1way-r1315_sym24/round-1315/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

