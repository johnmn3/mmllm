# harvest-1way-r66 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R66 ctrl_bpc |
|--------|--------|--------------:|
| fM0gL | fork-davidwuchn-mmllm-claude-train-ed4490eb-fM0gL | 1.0026 |
| **mean** | | **1.0026** |
| **best** | | **1.0026** |

## Chain progression R61 → R66

Previous harvest: `workers/dispatcher/harvest-1way-r61`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0890         | 1.0026         | -0.0864 |
| ctrl_bpc best  | 1.0890         | 1.0026         | -0.0864 |

## Per-round trajectory (best bird: fM0gL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 62 | 524 | 1.0269 | -0.0030 |
| 63 | 499 | 1.0042 | +0.0073 |
| 64 | 476 | 0.9936 | +0.0091 |
| 65 | 505 | 0.9917 | +0.0027 |
| 66 | 556 | 1.0026 | +0.0109 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **350 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r61`

## Output

`workers/dispatcher/harvest-1way-r66/round-66/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

