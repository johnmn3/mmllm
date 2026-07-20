# harvest-1way-r977 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R977 ctrl_bpc |
|--------|--------|--------------:|
| TH9w3 | origin/claude/train-sym24-ee936c7b-TH9w3 | 2.9932 |
| **mean** | | **2.9932** |
| **best** | | **2.9932** |

## Chain progression R976 → R977

Previous harvest: `workers/dispatcher/harvest-3way-r976_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6189         | 2.9932         | +0.3743 |
| ctrl_bpc best  | 2.6002         | 2.9932         | +0.3930 |

## Per-round trajectory (best bird: TH9w3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 977 | 4396 | 2.9932 | +0.1572 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r976_sym24`

## Output

`workers/dispatcher/harvest-1way-r977_sym24/round-977/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

