# harvest-5way-r1056 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1056 ctrl_bpc |
|--------|--------|--------------:|
| oWXqk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-70bcddc7-oWXqk | 2.4621 |
| fGpcy | origin/claude/train-sym24-b60a7b5c-fGpcy | 2.6558 |
| uOtNg | fork-SeniorCareMarket-mmllm-claude-train-sym24-a250c028-uOtNg | 2.6559 |
| zKmvy | fork-slaa-us-mmllm-claude-train-sym24-43be2eac-zKmvy | 2.8436 |
| Pl6Gs | fork-joly-os-mmllm-claude-train-sym24-04024f5a-Pl6Gs | 2.8592 |
| **mean** | | **2.6953** |
| **best** | | **2.4621** |

## Chain progression R1055 → R1056

Previous harvest: `workers/dispatcher/harvest-3way-r1055_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5459         | 2.6953         | +0.1494 |
| ctrl_bpc best  | 2.4823         | 2.4621         | -0.0202 |

## Per-round trajectory (best bird: oWXqk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1056 | 6666 | 2.4621 | +0.2074 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1055_sym24`
  - `workers/dispatcher/harvest-3way-r1055_sym24`

## Output

`workers/dispatcher/harvest-5way-r1056_sym24/round-1056/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

