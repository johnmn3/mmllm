# harvest-1way-r1171 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1171 ctrl_bpc |
|--------|--------|--------------:|
| H7YH9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a7f508f4-H7YH9 | 2.3349 |
| **mean** | | **2.3349** |
| **best** | | **2.3349** |

## Chain progression R1170 → R1171

Previous harvest: `workers/dispatcher/harvest-7way-r1170_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4127         | 2.3349         | -0.0778 |
| ctrl_bpc best  | 2.3084         | 2.3349         | +0.0265 |

## Per-round trajectory (best bird: H7YH9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1171 | 4427 | 2.3349 | +0.2451 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1170_sym24`

## Output

`workers/dispatcher/harvest-1way-r1171_sym24/round-1171/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

