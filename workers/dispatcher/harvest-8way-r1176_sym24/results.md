# harvest-8way-r1176 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1176 ctrl_bpc |
|--------|--------|--------------:|
| 7ExRT | fork-joly-os-mmllm-claude-train-sym24-49b35ba5-7ExRT | 2.3108 |
| pD8rV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c50155e7-pD8rV | 2.3145 |
| v4dLv | fork-joly-os-mmllm-claude-train-sym24-93c6d2a9-v4dLv | 2.3294 |
| B9aZR | fork-SeniorCareMarket-mmllm-claude-train-sym24-3c1ce8a7-B9aZR | 2.3329 |
| bPl6x | origin/claude/train-sym24-6f58e8b1-bPl6x | 2.5086 |
| Ti9FK | origin/claude/train-sym24-9ec9dc60-Ti9FK | 2.5089 |
| dkjZR | fork-slaa-us-mmllm-claude-train-sym24-9a17a895-dkjZR | 2.5108 |
| zxAbQ | fork-slaa-us-mmllm-claude-train-sym24-48f0b86c-zxAbQ | 2.5214 |
| **mean** | | **2.4172** |
| **best** | | **2.3108** |

## Chain progression R1175 → R1176

Previous harvest: `workers/dispatcher/harvest-9way-r1175_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4946         | 2.4172         | -0.0774 |
| ctrl_bpc best  | 2.3243         | 2.3108         | -0.0135 |

## Per-round trajectory (best bird: 7ExRT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1176 | 6566 | 2.3108 | +0.2520 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1175_sym24`
  - `workers/dispatcher/harvest-6way-r1175_sym24`

## Output

`workers/dispatcher/harvest-8way-r1176_sym24/round-1176/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

