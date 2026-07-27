# harvest-1way-r1035 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1035 ctrl_bpc |
|--------|--------|--------------:|
| UZzv6 | origin/claude/train-sym24-6c1c056c-UZzv6 | 2.9053 |
| **mean** | | **2.9053** |
| **best** | | **2.9053** |

## Chain progression R1034 → R1035

Previous harvest: `workers/dispatcher/harvest-6way-r1034_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6076         | 2.9053         | +0.2977 |
| ctrl_bpc best  | 2.5112         | 2.9053         | +0.3941 |

## Per-round trajectory (best bird: UZzv6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1035 | 6804 | 2.9053 | +0.1712 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1034_sym24`

## Output

`workers/dispatcher/harvest-1way-r1035_sym24/round-1035/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

