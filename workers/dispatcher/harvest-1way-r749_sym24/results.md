# harvest-1way-r749 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R749 ctrl_bpc |
|--------|--------|--------------:|
| T0RTJ | fork-slaa-us-mmllm-claude-train-sym24-43c6b2dd-T0RTJ | 3.4317 |
| **mean** | | **3.4317** |
| **best** | | **3.4317** |

## Chain progression R748 → R749

Previous harvest: `workers/dispatcher/harvest-8way-r748_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4495         | 3.4317         | -0.0178 |
| ctrl_bpc best  | 3.3437         | 3.4317         | +0.0880 |

## Per-round trajectory (best bird: T0RTJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 749 | 6388 | 3.4317 | +0.4634 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r748_sym24`

## Output

`workers/dispatcher/harvest-1way-r749_sym24/round-749/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

