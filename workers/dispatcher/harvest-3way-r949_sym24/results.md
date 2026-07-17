# harvest-3way-r949 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R949 ctrl_bpc |
|--------|--------|--------------:|
| eyVJY | origin/claude/train-sym24-9392bdab-eyVJY | 2.7170 |
| HtSem | origin/claude/train-sym24-223af3a5-HtSem | 2.8577 |
| 9dx7k | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-12976ab4-9dx7k | 2.8690 |
| **mean** | | **2.8146** |
| **best** | | **2.7170** |

## Chain progression R948 → R949

Previous harvest: `workers/dispatcher/harvest-8way-r948_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9112         | 2.8146         | -0.0966 |
| ctrl_bpc best  | 2.6590         | 2.7170         | +0.0580 |

## Per-round trajectory (best bird: eyVJY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 949 | 6735 | 2.7170 | +0.1050 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r948_sym24`

## Output

`workers/dispatcher/harvest-3way-r949_sym24/round-949/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

