# harvest-1way-r134 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R134 ctrl_bpc |
|--------|--------|--------------:|
| 1tM3c | fork-SeniorCareMarket-mmllm-claude-train-76f245b8-1tM3c | 1.0662 |
| **mean** | | **1.0662** |
| **best** | | **1.0662** |

## Chain progression R129 → R134

Previous harvest: `workers/dispatcher/harvest-3way-r129`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.5075         | 1.0662         | -0.4413 |
| ctrl_bpc best  | 1.3191         | 1.0662         | -0.2529 |

## Per-round trajectory (best bird: 1tM3c)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 130 | 610 | 1.0658 | -0.0004 |
| 131 | 534 | 1.0810 | -0.0015 |
| 132 | 521 | 1.0669 | +0.0012 |
| 133 | 524 | 1.0966 | -0.0010 |
| 134 | 498 | 1.0662 | +0.0019 |

## Cumulative training contribution

- This harvest: **35 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **2928 steps** from 77 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r129`

## Output

`workers/dispatcher/harvest-1way-r134/round-134/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

