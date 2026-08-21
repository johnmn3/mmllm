# harvest-1way-r1272 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1272 ctrl_bpc |
|--------|--------|--------------:|
| 2JR3A | origin/claude/train-sym24-250eff5e-2JR3A | 2.6137 |
| **mean** | | **2.6137** |
| **best** | | **2.6137** |

## Chain progression R1271 → R1272

Previous harvest: `workers/dispatcher/harvest-7way-r1271_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4325         | 2.6137         | +0.1812 |
| ctrl_bpc best  | 2.2257         | 2.6137         | +0.3880 |

## Per-round trajectory (best bird: 2JR3A)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1272 | 6567 | 2.6137 | +0.2247 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1271_sym24`

## Output

`workers/dispatcher/harvest-1way-r1272_sym24/round-1272/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

