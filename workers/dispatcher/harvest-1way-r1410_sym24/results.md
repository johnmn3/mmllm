# harvest-1way-r1410 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1410 ctrl_bpc |
|--------|--------|--------------:|
| DcL8y | origin/claude/train-sym24-52e5673d-DcL8y | 3.8414 |
| **mean** | | **3.8414** |
| **best** | | **3.8414** |

## Chain progression R1409 → R1410

Previous harvest: `workers/dispatcher/harvest-4way-r1409_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5718         | 3.8414         | +0.2696 |
| ctrl_bpc best  | 3.3167         | 3.8414         | +0.5247 |

## Per-round trajectory (best bird: DcL8y)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1410 | 6512 | 3.8414 | +0.5166 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1409_sym24`

## Output

`workers/dispatcher/harvest-1way-r1410_sym24/round-1410/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

