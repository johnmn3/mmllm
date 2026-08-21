# harvest-1way-r1274 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1274 ctrl_bpc |
|--------|--------|--------------:|
| 6kqXV | fork-slaa-us-mmllm-claude-train-sym24-0f1c1596-6kqXV | 2.6283 |
| **mean** | | **2.6283** |
| **best** | | **2.6283** |

## Chain progression R1273 → R1274

Previous harvest: `workers/dispatcher/harvest-5way-r1273_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3870         | 2.6283         | +0.2413 |
| ctrl_bpc best  | 2.2268         | 2.6283         | +0.4015 |

## Per-round trajectory (best bird: 6kqXV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1274 | 3666 | 2.6283 | +0.2244 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1273_sym24`

## Output

`workers/dispatcher/harvest-1way-r1274_sym24/round-1274/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

