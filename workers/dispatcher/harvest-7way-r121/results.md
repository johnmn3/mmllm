# harvest-7way-r121 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R121 ctrl_bpc |
|--------|--------|--------------:|
| 9hqLh | fork-davidwuchn-mmllm-claude-train-0ed5768b-9hqLh | 0.9290 |
| ETurF | fork-SeniorCareMarket-com-mmllm-claude-train-b498cd41-ETurF | 0.9744 |
| ylriD | fork-joly-os-mmllm-claude-train-10bbcfed-ylriD | 0.9796 |
| TO5r9 | fork-slaa-us-mmllm-claude-train-dc02120a-TO5r9 | 0.9882 |
| TeZx8 | fork-SeniorCareMarket-mmllm-claude-train-d56d2e7a-TeZx8 | 1.0302 |
| elyko | origin/claude/train-3d87afbc-elyko | 1.0787 |
| Pngcc | origin/claude/train-3b9ccbc0-Pngcc | 1.3829 |
| **mean** | | **1.0519** |
| **best** | | **0.9290** |

## Chain progression R119 → R121

Previous harvest: `workers/dispatcher/harvest-6way-r119`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0304         | 1.0519         | +0.0215 |
| ctrl_bpc best  | 0.9135         | 0.9290         | +0.0155 |

## Per-round trajectory (best bird: 9hqLh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 117 | 610 | 0.9509 | +0.0111 |
| 118 | 548 | 0.9335 | +0.0059 |
| 119 | 540 | 0.9718 | +0.0151 |
| 120 | 514 | 0.9441 | +0.0098 |
| 121 | 487 | 0.9290 | +0.0117 |

## Cumulative training contribution

- This harvest: **224 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **3047 steps** from 81 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r116`
  - `workers/dispatcher/harvest-6way-r119`

## Output

`workers/dispatcher/harvest-7way-r121/round-121/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

