# harvest-4way-r94 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R94 ctrl_bpc |
|--------|--------|--------------:|
| 01wVW | fork-joly-os-mmllm-claude-train-4cf3c340-01wVW | 0.9403 |
| bCNaT | fork-SeniorCareMarket-com-mmllm-claude-train-8b90d578-bCNaT | 1.0207 |
| NGLsH | origin/claude/train-5f3130e8-NGLsH | 1.0357 |
| y3Lck | fork-slaa-us-mmllm-claude-train-50f45865-y3Lck | 1.0416 |
| **mean** | | **1.0096** |
| **best** | | **0.9403** |

## Chain progression R89 → R94

Previous harvest: `workers/dispatcher/harvest-fold2way-r89`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9881         | 1.0096         | +0.0215 |
| ctrl_bpc best  | 0.9293         | 0.9403         | +0.0110 |

## Per-round trajectory (best bird: 01wVW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 90 | 634 | 0.9130 | +0.0020 |
| 91 | 556 | 0.9337 | +0.0101 |
| 92 | 566 | 0.9279 | +0.0008 |
| 93 | 510 | 0.9330 | +0.0121 |
| 94 | 543 | 0.9403 | +0.0082 |

## Cumulative training contribution

- This harvest: **140 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **2123 steps** from 53 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-fold2way-r89`

## Output

`workers/dispatcher/harvest-4way-r94/round-94/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

