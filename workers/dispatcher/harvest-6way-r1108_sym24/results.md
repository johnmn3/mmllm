# harvest-6way-r1108 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1108 ctrl_bpc |
|--------|--------|--------------:|
| fSR5l | fork-SeniorCareMarket-mmllm-claude-train-sym24-07ba1c25-fSR5l | 2.3848 |
| U30Qg | origin/claude/train-sym24-54b7352e-U30Qg | 2.3876 |
| cRv2Y | fork-joly-os-mmllm-claude-train-sym24-a3a52013-cRv2Y | 2.3878 |
| yy0vd | fork-slaa-us-mmllm-claude-train-sym24-a9725c47-yy0vd | 2.4077 |
| WXrPw | origin/claude/train-sym24-94dc808b-WXrPw | 2.5809 |
| MrDJv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-323989cb-MrDJv | 2.7814 |
| **mean** | | **2.4884** |
| **best** | | **2.3848** |

## Chain progression R1107 → R1108

Previous harvest: `workers/dispatcher/harvest-3way-r1107_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4667         | 2.4884         | +0.0217 |
| ctrl_bpc best  | 2.4036         | 2.3848         | -0.0188 |

## Per-round trajectory (best bird: fSR5l)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1108 | 6833 | 2.3848 | +0.2513 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1107_sym24`
  - `workers/dispatcher/harvest-3way-r1107_sym24`

## Output

`workers/dispatcher/harvest-6way-r1108_sym24/round-1108/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

