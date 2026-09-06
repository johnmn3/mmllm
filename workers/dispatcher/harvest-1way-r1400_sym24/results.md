# harvest-1way-r1400 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1400 ctrl_bpc |
|--------|--------|--------------:|
| g9RCT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f9db7285-g9RCT | 3.9386 |
| **mean** | | **3.9386** |
| **best** | | **3.9386** |

## Chain progression R1399 → R1400

Previous harvest: `workers/dispatcher/harvest-5way-r1399_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6823         | 3.9386         | +0.2563 |
| ctrl_bpc best  | 3.3309         | 3.9386         | +0.6077 |

## Per-round trajectory (best bird: g9RCT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1400 | 6298 | 3.9386 | +0.3170 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1399_sym24`

## Output

`workers/dispatcher/harvest-1way-r1400_sym24/round-1400/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

