# harvest-4way-r1047 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1047 ctrl_bpc |
|--------|--------|--------------:|
| b0bNe | fork-slaa-us-mmllm-claude-train-sym24-f4fadd82-b0bNe | 2.5082 |
| KPUEH | fork-SeniorCareMarket-mmllm-claude-train-sym24-55c26339-KPUEH | 2.5172 |
| KTmN5 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1dd39062-KTmN5 | 2.6652 |
| UAvWH | origin/claude/train-sym24-4c06d6de-UAvWH | 2.6771 |
| **mean** | | **2.5919** |
| **best** | | **2.5082** |

## Chain progression R1046 → R1047

Previous harvest: `workers/dispatcher/harvest-2way-r1046_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6960         | 2.5919         | -0.1041 |
| ctrl_bpc best  | 2.5146         | 2.5082         | -0.0064 |

## Per-round trajectory (best bird: b0bNe)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1047 | 6733 | 2.5082 | +0.1906 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1046_sym24`
  - `workers/dispatcher/harvest-2way-r1046_sym24`

## Output

`workers/dispatcher/harvest-4way-r1047_sym24/round-1047/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

