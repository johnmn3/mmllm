# harvest-7way-r949 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R949 ctrl_bpc |
|--------|--------|--------------:|
| lpEij | fork-slaa-us-mmllm-claude-train-sym24-4003fae0-lpEij | 2.7136 |
| eyVJY | origin/claude/train-sym24-9392bdab-eyVJY | 2.7170 |
| WPmKA | fork-joly-os-mmllm-claude-train-sym24-d09f24d2-WPmKA | 2.8472 |
| i3WUS | fork-joly-os-mmllm-claude-train-sym24-12231e10-i3WUS | 2.8476 |
| HtSem | origin/claude/train-sym24-223af3a5-HtSem | 2.8577 |
| 9dx7k | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-12976ab4-9dx7k | 2.8690 |
| i3CIv | fork-SeniorCareMarket-mmllm-claude-train-sym24-23390e7a-i3CIv | 3.0548 |
| **mean** | | **2.8438** |
| **best** | | **2.7136** |

## Chain progression R948 → R949

Previous harvest: `workers/dispatcher/harvest-8way-r948_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9112         | 2.8438         | -0.0674 |
| ctrl_bpc best  | 2.6590         | 2.7136         | +0.0546 |

## Per-round trajectory (best bird: lpEij)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 949 | 6511 | 2.7136 | +0.1740 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r948_sym24`
  - `workers/dispatcher/harvest-4way-r948_sym24`

## Output

`workers/dispatcher/harvest-7way-r949_sym24/round-949/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

