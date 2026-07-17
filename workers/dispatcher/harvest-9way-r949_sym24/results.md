# harvest-9way-r949 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R949 ctrl_bpc |
|--------|--------|--------------:|
| qcg3J | origin/claude/train-sym24-f5f6cc6e-qcg3J | 2.6610 |
| lpEij | fork-slaa-us-mmllm-claude-train-sym24-4003fae0-lpEij | 2.7136 |
| eyVJY | origin/claude/train-sym24-9392bdab-eyVJY | 2.7170 |
| WPmKA | fork-joly-os-mmllm-claude-train-sym24-d09f24d2-WPmKA | 2.8472 |
| i3WUS | fork-joly-os-mmllm-claude-train-sym24-12231e10-i3WUS | 2.8476 |
| HtSem | origin/claude/train-sym24-223af3a5-HtSem | 2.8577 |
| 8uOmK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-17e751e1-8uOmK | 2.8593 |
| 9dx7k | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-12976ab4-9dx7k | 2.8690 |
| i3CIv | fork-SeniorCareMarket-mmllm-claude-train-sym24-23390e7a-i3CIv | 3.0548 |
| **mean** | | **2.8252** |
| **best** | | **2.6610** |

## Chain progression R948 → R949

Previous harvest: `workers/dispatcher/harvest-8way-r948_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9112         | 2.8252         | -0.0860 |
| ctrl_bpc best  | 2.6590         | 2.6610         | +0.0020 |

## Per-round trajectory (best bird: qcg3J)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 949 | 6621 | 2.6610 | +0.1643 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r948_sym24`
  - `workers/dispatcher/harvest-4way-r948_sym24`
  - `workers/dispatcher/harvest-8way-r948_sym24`

## Output

`workers/dispatcher/harvest-9way-r949_sym24/round-949/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

