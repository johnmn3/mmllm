# harvest-1way-r1109 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1109 ctrl_bpc |
|--------|--------|--------------:|
| 254Q1 | fork-slaa-us-mmllm-claude-train-sym24-90315730-254Q1 | 2.5838 |
| **mean** | | **2.5838** |
| **best** | | **2.5838** |

## Chain progression R1108 → R1109

Previous harvest: `workers/dispatcher/harvest-6way-r1108_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4884         | 2.5838         | +0.0954 |
| ctrl_bpc best  | 2.3848         | 2.5838         | +0.1990 |

## Per-round trajectory (best bird: 254Q1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1109 | 3708 | 2.5838 | +0.2261 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1108_sym24`

## Output

`workers/dispatcher/harvest-1way-r1109_sym24/round-1109/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

