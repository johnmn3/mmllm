# harvest-1way-r630 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R630 ctrl_bpc |
|--------|--------|--------------:|
| qJAr4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c12865c3-qJAr4 | 2.1382 |
| **mean** | | **2.1382** |
| **best** | | **2.1382** |

## Chain progression R629 → R630

Previous harvest: `workers/dispatcher/harvest-3way-r629_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5016         | 2.1382         | -0.3634 |
| ctrl_bpc best  | 2.3368         | 2.1382         | -0.1986 |

## Per-round trajectory (best bird: qJAr4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 630 | 4776 | 2.1382 | +0.0615 |

## Cumulative training contribution

- This harvest: **50 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r629_sym24`

## Output

`workers/dispatcher/harvest-1way-r630_sym24/round-630/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

