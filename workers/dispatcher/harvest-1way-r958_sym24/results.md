# harvest-1way-r958 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R958 ctrl_bpc |
|--------|--------|--------------:|
| 8wKBm | fork-slaa-us-mmllm-claude-train-sym24-41130e9b-8wKBm | 2.6279 |
| **mean** | | **2.6279** |
| **best** | | **2.6279** |

## Chain progression R957 → R958

Previous harvest: `workers/dispatcher/harvest-5way-r957_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8089         | 2.6279         | -0.1810 |
| ctrl_bpc best  | 2.6423         | 2.6279         | -0.0144 |

## Per-round trajectory (best bird: 8wKBm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 958 | 3541 | 2.6279 | +0.1681 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r957_sym24`

## Output

`workers/dispatcher/harvest-1way-r958_sym24/round-958/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

