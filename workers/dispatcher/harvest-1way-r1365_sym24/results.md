# harvest-1way-r1365 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1365 ctrl_bpc |
|--------|--------|--------------:|
| zNYlb | origin/claude/train-sym24-4dc3a414-zNYlb | 3.1841 |
| **mean** | | **3.1841** |
| **best** | | **3.1841** |

## Chain progression R1364 → R1365

Previous harvest: `workers/dispatcher/harvest-5way-r1364_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3468         | 3.1841         | -0.1627 |
| ctrl_bpc best  | 3.1539         | 3.1841         | +0.0302 |

## Per-round trajectory (best bird: zNYlb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1365 | 6617 | 3.1841 | +0.1675 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1364_sym24`

## Output

`workers/dispatcher/harvest-1way-r1365_sym24/round-1365/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

