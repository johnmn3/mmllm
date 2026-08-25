# harvest-1way-r1316 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1316 ctrl_bpc |
|--------|--------|--------------:|
| 6XNIi | fork-slaa-us-mmllm-claude-train-sym24-2ab59362-6XNIi | 3.7372 |
| **mean** | | **3.7372** |
| **best** | | **3.7372** |

## Chain progression R1315 → R1316

Previous harvest: `workers/dispatcher/harvest-6way-r1315_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5997         | 3.7372         | +0.1375 |
| ctrl_bpc best  | 3.3720         | 3.7372         | +0.3652 |

## Per-round trajectory (best bird: 6XNIi)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1316 | 4293 | 3.7372 | +0.0392 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1315_sym24`

## Output

`workers/dispatcher/harvest-1way-r1316_sym24/round-1316/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

