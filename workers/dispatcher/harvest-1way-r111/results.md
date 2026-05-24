# harvest-1way-r111 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R111 ctrl_bpc |
|--------|--------|--------------:|
| D1eg0 | fork-SeniorCareMarket-mmllm-claude-train-ca469458-D1eg0 | 1.0171 |
| **mean** | | **1.0171** |
| **best** | | **1.0171** |

## Chain progression R108 → R111

Previous harvest: `workers/dispatcher/harvest-4way-r108`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0116         | 1.0171         | +0.0055 |
| ctrl_bpc best  | 0.9448         | 1.0171         | +0.0723 |

## Per-round trajectory (best bird: D1eg0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 109 | 651 | 0.9759 | +0.0119 |
| 110 | 574 | 0.9587 | +0.0133 |
| 111 | 541 | 1.0171 | +0.0131 |

## Cumulative training contribution

- This harvest: **21 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **2452 steps** from 63 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r108`

## Output

`workers/dispatcher/harvest-1way-r111/round-111/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

