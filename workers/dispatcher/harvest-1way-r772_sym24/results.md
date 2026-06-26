# harvest-1way-r772 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R772 ctrl_bpc |
|--------|--------|--------------:|
| DFipy | origin/claude/train-sym24-dafa657a-DFipy | 3.2213 |
| **mean** | | **3.2213** |
| **best** | | **3.2213** |

## Chain progression R771 → R772

Previous harvest: `workers/dispatcher/harvest-3way-r771_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4973         | 3.2213         | -0.2760 |
| ctrl_bpc best  | 3.2597         | 3.2213         | -0.0384 |

## Per-round trajectory (best bird: DFipy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 772 | 5408 | 3.2213 | +0.5530 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r771_sym24`

## Output

`workers/dispatcher/harvest-1way-r772_sym24/round-772/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

