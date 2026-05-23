# harvest-1way-r68 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R68 ctrl_bpc |
|--------|--------|--------------:|
| PeunF | origin/claude/train-67505db4-PeunF | 0.9958 |
| **mean** | | **0.9958** |
| **best** | | **0.9958** |

## Chain progression R66 → R68

Previous harvest: `workers/dispatcher/harvest-fold2way-r66`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0957         | 0.9958         | -0.0999 |
| ctrl_bpc best  | 1.0583         | 0.9958         | -0.0625 |

## Per-round trajectory (best bird: PeunF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 67 | 576 | 0.9890 | +0.0026 |
| 68 | 549 | 0.9958 | +0.0084 |

## Cumulative training contribution

- This harvest: **14 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **364 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r66`

## Output

`workers/dispatcher/harvest-1way-r68/round-68/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

