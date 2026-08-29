# harvest-1way-r1346 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1346 ctrl_bpc |
|--------|--------|--------------:|
| 7WTkw | origin/claude/train-sym24-41c87a37-7WTkw | 3.2713 |
| **mean** | | **3.2713** |
| **best** | | **3.2713** |

## Chain progression R1345 → R1346

Previous harvest: `workers/dispatcher/harvest-4way-r1345_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4771         | 3.2713         | -0.2058 |
| ctrl_bpc best  | 3.2448         | 3.2713         | +0.0265 |

## Per-round trajectory (best bird: 7WTkw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1346 | 5254 | 3.2713 | +0.0881 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1345_sym24`

## Output

`workers/dispatcher/harvest-1way-r1346_sym24/round-1346/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

