# harvest-6way-r1009 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1009 ctrl_bpc |
|--------|--------|--------------:|
| 44fN7 | origin/claude/train-sym24-5d7de610-44fN7 | 2.5354 |
| bgTgG | fork-slaa-us-mmllm-claude-train-sym24-67263aea-bgTgG | 2.5378 |
| t7uOi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b1709516-t7uOi | 2.5698 |
| 6avPd | origin/claude/train-sym24-96d1116b-6avPd | 2.9273 |
| kFqJ4 | fork-joly-os-mmllm-claude-train-sym24-c3174568-kFqJ4 | 2.9298 |
| 9tKLR | fork-SeniorCareMarket-mmllm-claude-train-sym24-6e4f29bc-9tKLR | 2.9316 |
| **mean** | | **2.7386** |
| **best** | | **2.5354** |

## Chain progression R1008 → R1009

Previous harvest: `workers/dispatcher/harvest-3way-r1008_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7322         | 2.7386         | +0.0064 |
| ctrl_bpc best  | 2.7262         | 2.5354         | -0.1908 |

## Per-round trajectory (best bird: 44fN7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1009 | 6487 | 2.5354 | +0.1765 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1008_sym24`
  - `workers/dispatcher/harvest-3way-r1008_sym24`

## Output

`workers/dispatcher/harvest-6way-r1009_sym24/round-1009/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

