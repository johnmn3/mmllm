# harvest-1way-r979 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R979 ctrl_bpc |
|--------|--------|--------------:|
| XDDuB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-471f5631-XDDuB | 2.6397 |
| **mean** | | **2.6397** |
| **best** | | **2.6397** |

## Chain progression R978 → R979

Previous harvest: `workers/dispatcher/harvest-8way-r978_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7374         | 2.6397         | -0.0977 |
| ctrl_bpc best  | 2.6021         | 2.6397         | +0.0376 |

## Per-round trajectory (best bird: XDDuB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 979 | 3631 | 2.6397 | +0.1604 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r978_sym24`

## Output

`workers/dispatcher/harvest-1way-r979_sym24/round-979/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

