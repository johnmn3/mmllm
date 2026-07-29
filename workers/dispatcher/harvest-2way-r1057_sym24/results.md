# harvest-2way-r1057 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1057 ctrl_bpc |
|--------|--------|--------------:|
| LZmla | origin/claude/train-sym24-130b2d00-LZmla | 2.4609 |
| VZpil | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-98535987-VZpil | 2.6611 |
| **mean** | | **2.5610** |
| **best** | | **2.4609** |

## Chain progression R1056 → R1057

Previous harvest: `workers/dispatcher/harvest-5way-r1056_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6953         | 2.5610         | -0.1343 |
| ctrl_bpc best  | 2.4621         | 2.4609         | -0.0012 |

## Per-round trajectory (best bird: LZmla)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1057 | 6605 | 2.4609 | +0.2150 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1056_sym24`

## Output

`workers/dispatcher/harvest-2way-r1057_sym24/round-1057/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

