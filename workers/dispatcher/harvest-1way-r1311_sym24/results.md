# harvest-1way-r1311 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1311 ctrl_bpc |
|--------|--------|--------------:|
| X9c4N | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fb5d383e-X9c4N | 3.5344 |
| **mean** | | **3.5344** |
| **best** | | **3.5344** |

## Chain progression R1310 → R1311

Previous harvest: `workers/dispatcher/harvest-3way-r1310_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5482         | 3.5344         | -0.0138 |
| ctrl_bpc best  | 3.5297         | 3.5344         | +0.0047 |

## Per-round trajectory (best bird: X9c4N)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1311 | 4309 | 3.5344 | +0.0505 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1310_sym24`

## Output

`workers/dispatcher/harvest-1way-r1311_sym24/round-1311/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

