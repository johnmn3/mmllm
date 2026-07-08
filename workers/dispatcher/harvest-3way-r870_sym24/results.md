# harvest-3way-r870 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R870 ctrl_bpc |
|--------|--------|--------------:|
| hdoUn | fork-SeniorCareMarket-mmllm-claude-train-sym24-240e2e2a-hdoUn | 2.8703 |
| c5XNG | fork-slaa-us-mmllm-claude-train-sym24-78c84044-c5XNG | 2.8879 |
| Qe0Z7 | origin/claude/train-sym24-8f707622-Qe0Z7 | 3.2371 |
| **mean** | | **2.9984** |
| **best** | | **2.8703** |

## Chain progression R869 → R870

Previous harvest: `workers/dispatcher/harvest-1way-r869_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0397         | 2.9984         | -0.0413 |
| ctrl_bpc best  | 3.0397         | 2.8703         | -0.1694 |

## Per-round trajectory (best bird: hdoUn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 870 | 6580 | 2.8703 | +0.4088 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r869_sym24`

## Output

`workers/dispatcher/harvest-3way-r870_sym24/round-870/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

