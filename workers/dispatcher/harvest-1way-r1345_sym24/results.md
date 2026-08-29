# harvest-1way-r1345 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1345 ctrl_bpc |
|--------|--------|--------------:|
| eaY1v | origin/claude/train-sym24-f7676886-eaY1v | 3.2736 |
| **mean** | | **3.2736** |
| **best** | | **3.2736** |

## Chain progression R1344 → R1345

Previous harvest: `workers/dispatcher/harvest-3way-r1344_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2879         | 3.2736         | -0.0143 |
| ctrl_bpc best  | 3.2132         | 3.2736         | +0.0604 |

## Per-round trajectory (best bird: eaY1v)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1345 | 4397 | 3.2736 | +0.0863 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1344_sym24`

## Output

`workers/dispatcher/harvest-1way-r1345_sym24/round-1345/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

