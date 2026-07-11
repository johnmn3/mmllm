# harvest-1way-r893 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R893 ctrl_bpc |
|--------|--------|--------------:|
| vmMKv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3e479156-vmMKv | 2.8270 |
| **mean** | | **2.8270** |
| **best** | | **2.8270** |

## Chain progression R892 → R893

Previous harvest: `workers/dispatcher/harvest-8way-r892_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0000         | 2.8270         | -0.1730 |
| ctrl_bpc best  | 2.8053         | 2.8270         | +0.0217 |

## Per-round trajectory (best bird: vmMKv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 893 | 6584 | 2.8270 | +0.2175 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r892_sym24`

## Output

`workers/dispatcher/harvest-1way-r893_sym24/round-893/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

