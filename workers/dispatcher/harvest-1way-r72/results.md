# harvest-1way-r72 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R72 ctrl_bpc |
|--------|--------|--------------:|
| NYnlt | fork-SeniorCareMarket-mmllm-claude-train-21c567e2-NYnlt | 0.9313 |
| **mean** | | **0.9313** |
| **best** | | **0.9313** |

## Chain progression R71 → R72

Previous harvest: `workers/dispatcher/harvest-1way-r71`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0580         | 0.9313         | -0.1267 |
| ctrl_bpc best  | 1.0580         | 0.9313         | -0.1267 |

## Per-round trajectory (best bird: NYnlt)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 72 | 3346 | 0.9313 | +0.0103 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **435 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r71`

## Output

`workers/dispatcher/harvest-1way-r72/round-72/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

