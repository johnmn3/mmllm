# harvest-1way-r707 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R707 ctrl_bpc |
|--------|--------|--------------:|
| wkSQv | origin/claude/train-sym24-a38c7691-wkSQv | 3.9326 |
| **mean** | | **3.9326** |
| **best** | | **3.9326** |

## Chain progression R706 → R707

Previous harvest: `workers/dispatcher/harvest-6way-r706_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7610         | 3.9326         | +0.1716 |
| ctrl_bpc best  | 3.5805         | 3.9326         | +0.3521 |

## Per-round trajectory (best bird: wkSQv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 707 | 4426 | 3.9326 | +0.7446 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r706_sym24`

## Output

`workers/dispatcher/harvest-1way-r707_sym24/round-707/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

