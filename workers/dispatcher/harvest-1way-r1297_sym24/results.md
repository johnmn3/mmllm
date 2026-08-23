# harvest-1way-r1297 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1297 ctrl_bpc |
|--------|--------|--------------:|
| epucm | fork-slaa-us-mmllm-claude-train-sym24-646fa089-epucm | 3.8413 |
| **mean** | | **3.8413** |
| **best** | | **3.8413** |

## Chain progression R1296 → R1297

Previous harvest: `workers/dispatcher/harvest-4way-r1296_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9848         | 3.8413         | -0.1435 |
| ctrl_bpc best  | 3.9342         | 3.8413         | -0.0929 |

## Per-round trajectory (best bird: epucm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1297 | 4371 | 3.8413 | +0.0563 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1296_sym24`

## Output

`workers/dispatcher/harvest-1way-r1297_sym24/round-1297/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

