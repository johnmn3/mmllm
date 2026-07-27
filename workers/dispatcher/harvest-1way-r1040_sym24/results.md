# harvest-1way-r1040 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1040 ctrl_bpc |
|--------|--------|--------------:|
| 3WYn0 | origin/claude/train-sym24-9356795b-3WYn0 | 2.5029 |
| **mean** | | **2.5029** |
| **best** | | **2.5029** |

## Chain progression R1039 → R1040

Previous harvest: `workers/dispatcher/harvest-5way-r1039_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5471         | 2.5029         | -0.0442 |
| ctrl_bpc best  | 2.4825         | 2.5029         | +0.0204 |

## Per-round trajectory (best bird: 3WYn0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1040 | 6533 | 2.5029 | +0.2019 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1039_sym24`

## Output

`workers/dispatcher/harvest-1way-r1040_sym24/round-1040/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

