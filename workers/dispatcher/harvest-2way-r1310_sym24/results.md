# harvest-2way-r1310 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1310 ctrl_bpc |
|--------|--------|--------------:|
| GTmH5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e5e7a141-GTmH5 | 3.5297 |
| fXY8a | fork-slaa-us-mmllm-claude-train-sym24-0fb4fc65-fXY8a | 3.5513 |
| **mean** | | **3.5405** |
| **best** | | **3.5297** |

## Chain progression R1309 → R1310

Previous harvest: `workers/dispatcher/harvest-9way-r1309_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5737         | 3.5405         | -0.0332 |
| ctrl_bpc best  | 3.3840         | 3.5297         | +0.1457 |

## Per-round trajectory (best bird: GTmH5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1310 | 4503 | 3.5297 | +0.0697 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1309_sym24`

## Output

`workers/dispatcher/harvest-2way-r1310_sym24/round-1310/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

