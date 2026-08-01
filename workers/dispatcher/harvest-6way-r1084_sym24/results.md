# harvest-6way-r1084 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1084 ctrl_bpc |
|--------|--------|--------------:|
| 35DjU | fork-SeniorCareMarket-mmllm-claude-train-sym24-dd5cb6ac-35DjU | 2.4317 |
| 3OQKp | origin/claude/train-sym24-525f551d-3OQKp | 2.4353 |
| 1to11 | fork-joly-os-mmllm-claude-train-sym24-1c8e391c-1to11 | 2.4510 |
| sTsDs | fork-slaa-us-mmllm-claude-train-sym24-eb3b685c-sTsDs | 2.4555 |
| 9Dy26 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1c7ff15f-9Dy26 | 2.8060 |
| ddNDP | origin/claude/train-sym24-0ccec44b-ddNDP | 2.8212 |
| **mean** | | **2.5668** |
| **best** | | **2.4317** |

## Chain progression R1083 → R1084

Previous harvest: `workers/dispatcher/harvest-6way-r1083_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4918         | 2.5668         | +0.0750 |
| ctrl_bpc best  | 2.4253         | 2.4317         | +0.0064 |

## Per-round trajectory (best bird: 35DjU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1084 | 5527 | 2.4317 | +0.2485 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1083_sym24`

## Output

`workers/dispatcher/harvest-6way-r1084_sym24/round-1084/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

