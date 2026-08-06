# harvest-1way-r1125 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1125 ctrl_bpc |
|--------|--------|--------------:|
| Gf0li | origin/claude/train-sym24-85200554-Gf0li | 2.3852 |
| **mean** | | **2.3852** |
| **best** | | **2.3852** |

## Chain progression R1124 → R1125

Previous harvest: `workers/dispatcher/harvest-3way-r1124_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3791         | 2.3852         | +0.0061 |
| ctrl_bpc best  | 2.3630         | 2.3852         | +0.0222 |

## Per-round trajectory (best bird: Gf0li)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1125 | 6545 | 2.3852 | +0.2417 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1124_sym24`

## Output

`workers/dispatcher/harvest-1way-r1125_sym24/round-1125/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

