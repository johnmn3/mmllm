# harvest-1way-r828 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R828 ctrl_bpc |
|--------|--------|--------------:|
| 706Zq | fork-slaa-us-mmllm-claude-train-sym24-6e5382f5-706Zq | 3.0014 |
| **mean** | | **3.0014** |
| **best** | | **3.0014** |

## Chain progression R827 → R828

Previous harvest: `workers/dispatcher/harvest-1way-r827_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0039         | 3.0014         | -0.0025 |
| ctrl_bpc best  | 3.0039         | 3.0014         | -0.0025 |

## Per-round trajectory (best bird: 706Zq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 828 | 4347 | 3.0014 | +0.4886 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r827_sym24`

## Output

`workers/dispatcher/harvest-1way-r828_sym24/round-828/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

