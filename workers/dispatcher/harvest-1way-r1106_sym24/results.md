# harvest-1way-r1106 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1106 ctrl_bpc |
|--------|--------|--------------:|
| GMvOA | origin/claude/train-sym24-182abe27-GMvOA | 2.4071 |
| **mean** | | **2.4071** |
| **best** | | **2.4071** |

## Chain progression R1105 → R1106

Previous harvest: `workers/dispatcher/harvest-7way-r1105_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4938         | 2.4071         | -0.0867 |
| ctrl_bpc best  | 2.3893         | 2.4071         | +0.0178 |

## Per-round trajectory (best bird: GMvOA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1106 | 3794 | 2.4071 | +0.2394 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1105_sym24`

## Output

`workers/dispatcher/harvest-1way-r1106_sym24/round-1106/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

