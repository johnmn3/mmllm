# harvest-1way-r697 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R697 ctrl_bpc |
|--------|--------|--------------:|
| J3Wa6 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-13fb9883-J3Wa6 | 3.6939 |
| **mean** | | **3.6939** |
| **best** | | **3.6939** |

## Chain progression R696 → R697

Previous harvest: `workers/dispatcher/harvest-3way-r696_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6544         | 3.6939         | +0.0395 |
| ctrl_bpc best  | 3.6469         | 3.6939         | +0.0470 |

## Per-round trajectory (best bird: J3Wa6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 697 | 6415 | 3.6939 | +0.6765 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r696_sym24`

## Output

`workers/dispatcher/harvest-1way-r697_sym24/round-697/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

