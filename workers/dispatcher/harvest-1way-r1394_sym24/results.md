# harvest-1way-r1394 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1394 ctrl_bpc |
|--------|--------|--------------:|
| k0VN4 | origin/claude/train-sym24-a457c1d0-k0VN4 | 4.0118 |
| **mean** | | **4.0118** |
| **best** | | **4.0118** |

## Chain progression R1393 → R1394

Previous harvest: `workers/dispatcher/harvest-2way-r1393_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7417         | 4.0118         | +0.2701 |
| ctrl_bpc best  | 3.6921         | 4.0118         | +0.3197 |

## Per-round trajectory (best bird: k0VN4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1394 | 6570 | 4.0118 | +0.0400 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1393_sym24`

## Output

`workers/dispatcher/harvest-1way-r1394_sym24/round-1394/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

