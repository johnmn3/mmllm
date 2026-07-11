# harvest-1way-r894 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R894 ctrl_bpc |
|--------|--------|--------------:|
| uxLW8 | origin/claude/train-sym24-cf109578-uxLW8 | 3.1897 |
| **mean** | | **3.1897** |
| **best** | | **3.1897** |

## Chain progression R893 → R894

Previous harvest: `workers/dispatcher/harvest-6way-r893_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8737         | 3.1897         | +0.3160 |
| ctrl_bpc best  | 2.8070         | 3.1897         | +0.3827 |

## Per-round trajectory (best bird: uxLW8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 894 | 6555 | 3.1897 | +0.2130 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r893_sym24`

## Output

`workers/dispatcher/harvest-1way-r894_sym24/round-894/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

