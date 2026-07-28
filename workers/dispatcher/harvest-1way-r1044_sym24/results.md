# harvest-1way-r1044 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1044 ctrl_bpc |
|--------|--------|--------------:|
| bEBvO | origin/claude/train-sym24-459b2901-bEBvO | 2.8805 |
| **mean** | | **2.8805** |
| **best** | | **2.8805** |

## Chain progression R1043 → R1044

Previous harvest: `workers/dispatcher/harvest-8way-r1043_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5516         | 2.8805         | +0.3289 |
| ctrl_bpc best  | 2.4812         | 2.8805         | +0.3993 |

## Per-round trajectory (best bird: bEBvO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1044 | 6546 | 2.8805 | +0.1827 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1043_sym24`

## Output

`workers/dispatcher/harvest-1way-r1044_sym24/round-1044/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

