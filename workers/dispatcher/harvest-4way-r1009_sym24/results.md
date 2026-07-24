# harvest-4way-r1009 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1009 ctrl_bpc |
|--------|--------|--------------:|
| bgTgG | fork-slaa-us-mmllm-claude-train-sym24-67263aea-bgTgG | 2.5378 |
| t7uOi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b1709516-t7uOi | 2.5698 |
| kFqJ4 | fork-joly-os-mmllm-claude-train-sym24-c3174568-kFqJ4 | 2.9298 |
| 9tKLR | fork-SeniorCareMarket-mmllm-claude-train-sym24-6e4f29bc-9tKLR | 2.9316 |
| **mean** | | **2.7422** |
| **best** | | **2.5378** |

## Chain progression R610 → R1009

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 2.7422         | +0.6050 |
| ctrl_bpc best  | 2.1268         | 2.5378         | +0.4110 |

## Per-round trajectory (best bird: bgTgG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1009 | 6687 | 2.5378 | +0.1629 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1008_sym24`
  - `workers/dispatcher/harvest-3way-r1008_sym24`

## Output

`workers/dispatcher/harvest-4way-r1009_sym24/round-1009/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

