# harvest-1way-r956 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R956 ctrl_bpc |
|--------|--------|--------------:|
| ShJqG | origin/claude/train-sym24-1d4e9542-ShJqG | 2.6360 |
| **mean** | | **2.6360** |
| **best** | | **2.6360** |

## Chain progression R955 → R956

Previous harvest: `workers/dispatcher/harvest-7way-r955_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8590         | 2.6360         | -0.2230 |
| ctrl_bpc best  | 2.6530         | 2.6360         | -0.0170 |

## Per-round trajectory (best bird: ShJqG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 956 | 6657 | 2.6360 | +0.1690 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r955_sym24`

## Output

`workers/dispatcher/harvest-1way-r956_sym24/round-956/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

