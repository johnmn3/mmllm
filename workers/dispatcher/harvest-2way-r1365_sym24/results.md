# harvest-2way-r1365 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1365 ctrl_bpc |
|--------|--------|--------------:|
| BWL1X | origin/claude/train-sym24-8c857bfc-BWL1X | 3.1242 |
| zNYlb | origin/claude/train-sym24-4dc3a414-zNYlb | 3.1841 |
| **mean** | | **3.1542** |
| **best** | | **3.1242** |

## Chain progression R1364 → R1365

Previous harvest: `workers/dispatcher/harvest-5way-r1364_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3468         | 3.1542         | -0.1926 |
| ctrl_bpc best  | 3.1539         | 3.1242         | -0.0297 |

## Per-round trajectory (best bird: BWL1X)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1365 | 6660 | 3.1242 | +0.0958 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1364_sym24`

## Output

`workers/dispatcher/harvest-2way-r1365_sym24/round-1365/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

