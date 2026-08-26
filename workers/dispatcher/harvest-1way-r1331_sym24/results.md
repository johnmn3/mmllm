# harvest-1way-r1331 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1331 ctrl_bpc |
|--------|--------|--------------:|
| LXBEL | origin/claude/train-sym24-20b13f04-LXBEL | 3.3124 |
| **mean** | | **3.3124** |
| **best** | | **3.3124** |

## Chain progression R1330 → R1331

Previous harvest: `workers/dispatcher/harvest-5way-r1330_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4066         | 3.3124         | -0.0942 |
| ctrl_bpc best  | 3.2691         | 3.3124         | +0.0433 |

## Per-round trajectory (best bird: LXBEL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1331 | 6359 | 3.3124 | +0.0893 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1330_sym24`

## Output

`workers/dispatcher/harvest-1way-r1331_sym24/round-1331/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

