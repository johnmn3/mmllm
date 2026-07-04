# harvest-1way-r843 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R843 ctrl_bpc |
|--------|--------|--------------:|
| Zox0C | fork-slaa-us-mmllm-claude-train-sym24-07e7cba8-Zox0C | 2.9565 |
| **mean** | | **2.9565** |
| **best** | | **2.9565** |

## Chain progression R842 → R843

Previous harvest: `workers/dispatcher/harvest-6way-r842_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0500         | 2.9565         | -0.0935 |
| ctrl_bpc best  | 2.9529         | 2.9565         | +0.0036 |

## Per-round trajectory (best bird: Zox0C)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 843 | 6484 | 2.9565 | +0.4765 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r842_sym24`

## Output

`workers/dispatcher/harvest-1way-r843_sym24/round-843/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

