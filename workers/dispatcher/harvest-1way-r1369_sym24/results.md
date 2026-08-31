# harvest-1way-r1369 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1369 ctrl_bpc |
|--------|--------|--------------:|
| HOVyn | origin/claude/train-sym24-c717b1ab-HOVyn | 3.2173 |
| **mean** | | **3.2173** |
| **best** | | **3.2173** |

## Chain progression R1368 → R1369

Previous harvest: `workers/dispatcher/harvest-1way-r1368_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2665         | 3.2173         | -0.0492 |
| ctrl_bpc best  | 3.2665         | 3.2173         | -0.0492 |

## Per-round trajectory (best bird: HOVyn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1369 | 3757 | 3.2173 | +0.1248 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1368_sym24`

## Output

`workers/dispatcher/harvest-1way-r1369_sym24/round-1369/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

