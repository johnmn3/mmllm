# harvest-3way-r696 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R696 ctrl_bpc |
|--------|--------|--------------:|
| Nr68u | fork-slaa-us-mmllm-claude-train-sym24-461f1edc-Nr68u | 3.6469 |
| ljqJ4 | origin/claude/train-sym24-c5115788-ljqJ4 | 3.6488 |
| X5gAG | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65f46340-X5gAG | 3.6675 |
| **mean** | | **3.6544** |
| **best** | | **3.6469** |

## Chain progression R695 → R696

Previous harvest: `workers/dispatcher/harvest-3way-r695_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6989         | 3.6544         | -0.0445 |
| ctrl_bpc best  | 3.6931         | 3.6469         | -0.0462 |

## Per-round trajectory (best bird: Nr68u)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 696 | 6486 | 3.6469 | +0.6647 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r695_sym24`

## Output

`workers/dispatcher/harvest-3way-r696_sym24/round-696/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

