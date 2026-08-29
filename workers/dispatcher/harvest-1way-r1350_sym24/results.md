# harvest-1way-r1350 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1350 ctrl_bpc |
|--------|--------|--------------:|
| UdKzA | origin/claude/train-sym24-42c940f0-UdKzA | 3.3549 |
| **mean** | | **3.3549** |
| **best** | | **3.3549** |

## Chain progression R1349 → R1350

Previous harvest: `workers/dispatcher/harvest-4way-r1349_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4754         | 3.3549         | -0.1205 |
| ctrl_bpc best  | 3.1625         | 3.3549         | +0.1924 |

## Per-round trajectory (best bird: UdKzA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1350 | 4392 | 3.3549 | +0.1028 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1349_sym24`

## Output

`workers/dispatcher/harvest-1way-r1350_sym24/round-1350/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

