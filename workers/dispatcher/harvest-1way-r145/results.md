# harvest-1way-r145 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R145 ctrl_bpc |
|--------|--------|--------------:|
| 5j4Tr | fork-SeniorCareMarket-mmllm-claude-train-4e2e1e9e-5j4Tr | 1.0524 |
| **mean** | | **1.0524** |
| **best** | | **1.0524** |

## Chain progression R140 → R145

Previous harvest: `workers/dispatcher/harvest-7way-r140`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0684         | 1.0524         | -0.0160 |
| ctrl_bpc best  | 1.0228         | 1.0524         | +0.0296 |

## Per-round trajectory (best bird: 5j4Tr)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 141 | 584 | 1.0477 | -0.0005 |
| 142 | 519 | 1.0668 | -0.0028 |
| 143 | 537 | 1.0281 | +0.0000 |
| 144 | 535 | 1.0763 | -0.0002 |
| 145 | 523 | 1.0524 | +0.0009 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **3257 steps** from 88 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r140`

## Output

`workers/dispatcher/harvest-1way-r145/round-145/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

