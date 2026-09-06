# harvest-2way-r1406 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1406 ctrl_bpc |
|--------|--------|--------------:|
| HjpbQ | origin/claude/train-sym24-b8696dc2-HjpbQ | 3.2479 |
| aCGkl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-63ab80e7-aCGkl | 3.6412 |
| **mean** | | **3.4446** |
| **best** | | **3.2479** |

## Chain progression R1405 → R1406

Previous harvest: `workers/dispatcher/harvest-3way-r1405_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4540         | 3.4446         | -0.0095 |
| ctrl_bpc best  | 3.3002         | 3.2479         | -0.0523 |

## Per-round trajectory (best bird: HjpbQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1406 | 3422 | 3.2479 | +0.1227 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1405_sym24`

## Output

`workers/dispatcher/harvest-2way-r1406_sym24/round-1406/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

