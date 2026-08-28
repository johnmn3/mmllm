# harvest-1way-r1340 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1340 ctrl_bpc |
|--------|--------|--------------:|
| QVh3t | origin/claude/train-sym24-d247ca69-QVh3t | 3.3884 |
| **mean** | | **3.3884** |
| **best** | | **3.3884** |

## Chain progression R1339 → R1340

Previous harvest: `workers/dispatcher/harvest-3way-r1339_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2922         | 3.3884         | +0.0962 |
| ctrl_bpc best  | 3.2521         | 3.3884         | +0.1363 |

## Per-round trajectory (best bird: QVh3t)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1340 | 6488 | 3.3884 | +0.0958 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1339_sym24`

## Output

`workers/dispatcher/harvest-1way-r1340_sym24/round-1340/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

