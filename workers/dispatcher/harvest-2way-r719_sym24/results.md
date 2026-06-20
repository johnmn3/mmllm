# harvest-2way-r719 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R719 ctrl_bpc |
|--------|--------|--------------:|
| 0YXqX | origin/claude/train-sym24-48fe968a-0YXqX | 3.5482 |
| vj0iJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c092002b-vj0iJ | 3.8765 |
| **mean** | | **3.7123** |
| **best** | | **3.5482** |

## Chain progression R718 → R719

Previous harvest: `workers/dispatcher/harvest-5way-r718_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7363         | 3.7123         | -0.0240 |
| ctrl_bpc best  | 3.5185         | 3.5482         | +0.0297 |

## Per-round trajectory (best bird: 0YXqX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 719 | 6521 | 3.5482 | +1.0206 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r718_sym24`

## Output

`workers/dispatcher/harvest-2way-r719_sym24/round-719/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

