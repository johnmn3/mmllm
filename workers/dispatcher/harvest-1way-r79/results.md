# harvest-1way-r79 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R79 ctrl_bpc |
|--------|--------|--------------:|
| ikQ2E | origin/claude/train-fa0ba3d9-ikQ2E | 0.9749 |
| **mean** | | **0.9749** |
| **best** | | **0.9749** |

## Chain progression R78 → R79

Previous harvest: `workers/dispatcher/harvest-fold7way-r78`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 0.9997         | 0.9749         | -0.0248 |
| ctrl_bpc best  | 0.9208         | 0.9749         | +0.0541 |

## Per-round trajectory (best bird: ikQ2E)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 79 | 3586 | 0.9749 | +0.0059 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1689 steps** from 41 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-fold7way-r78`

## Output

`workers/dispatcher/harvest-1way-r79/round-79/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

