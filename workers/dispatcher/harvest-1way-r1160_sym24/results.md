# harvest-1way-r1160 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1160 ctrl_bpc |
|--------|--------|--------------:|
| O0cqt | origin/claude/train-sym24-8f3b1fbd-O0cqt | 2.3558 |
| **mean** | | **2.3558** |
| **best** | | **2.3558** |

## Chain progression R1159 → R1160

Previous harvest: `workers/dispatcher/harvest-5way-r1159_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5272         | 2.3558         | -0.1714 |
| ctrl_bpc best  | 2.3548         | 2.3558         | +0.0010 |

## Per-round trajectory (best bird: O0cqt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1160 | 5454 | 2.3558 | +0.2467 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1159_sym24`

## Output

`workers/dispatcher/harvest-1way-r1160_sym24/round-1160/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

