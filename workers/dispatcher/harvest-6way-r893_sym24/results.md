# harvest-6way-r893 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R893 ctrl_bpc |
|--------|--------|--------------:|
| 1sXeb | fork-slaa-us-mmllm-claude-train-sym24-9fba1fbd-1sXeb | 2.8070 |
| vmMKv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3e479156-vmMKv | 2.8270 |
| 620wb | fork-joly-os-mmllm-claude-train-sym24-be45cc72-620wb | 2.8300 |
| EjS8e | fork-SeniorCareMarket-mmllm-claude-train-sym24-36ff0b09-EjS8e | 2.8309 |
| SUIeP | origin/claude/train-sym24-6fcd0b3b-SUIeP | 2.9711 |
| 5RBVe | origin/claude/train-sym24-24944dd7-5RBVe | 2.9759 |
| **mean** | | **2.8737** |
| **best** | | **2.8070** |

## Chain progression R892 → R893

Previous harvest: `workers/dispatcher/harvest-8way-r892_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0000         | 2.8737         | -0.1263 |
| ctrl_bpc best  | 2.8053         | 2.8070         | +0.0017 |

## Per-round trajectory (best bird: 1sXeb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 893 | 6600 | 2.8070 | +0.2819 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r892_sym24`
  - `workers/dispatcher/harvest-6way-r892_sym24`

## Output

`workers/dispatcher/harvest-6way-r893_sym24/round-893/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

