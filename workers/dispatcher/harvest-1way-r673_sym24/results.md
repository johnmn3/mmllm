# harvest-1way-r673 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R673 ctrl_bpc |
|--------|--------|--------------:|
| CAWKu | origin/claude/train-sym24-ab90ecd2-CAWKu | 3.8656 |
| **mean** | | **3.8656** |
| **best** | | **3.8656** |

## Chain progression R672 → R673

Previous harvest: `workers/dispatcher/harvest-4way-r672_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9684         | 3.8656         | -0.1028 |
| ctrl_bpc best  | 3.8554         | 3.8656         | +0.0102 |

## Per-round trajectory (best bird: CAWKu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 673 | 6348 | 3.8656 | +0.4479 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r672_sym24`

## Output

`workers/dispatcher/harvest-1way-r673_sym24/round-673/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

