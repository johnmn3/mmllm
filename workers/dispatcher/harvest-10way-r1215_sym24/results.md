# harvest-10way-r1215 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1215 ctrl_bpc |
|--------|--------|--------------:|
| R1pUa | fork-slaa-us-mmllm-claude-train-sym24-259a7be3-R1pUa | 2.2702 |
| 4LYON | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-730d84b7-4LYON | 2.2844 |
| rRngT | fork-joly-os-mmllm-claude-train-sym24-c8e49735-rRngT | 2.2921 |
| aQ97k | fork-SeniorCareMarket-mmllm-claude-train-sym24-ebb5032f-aQ97k | 2.2964 |
| DXCcS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b14f508e-DXCcS | 2.2969 |
| 0Iall | fork-SeniorCareMarket-mmllm-claude-train-sym24-1ca08256-0Iall | 2.3098 |
| ik2ym | fork-joly-os-mmllm-claude-train-sym24-3b9c94b0-ik2ym | 2.4615 |
| RTEur | fork-slaa-us-mmllm-claude-train-sym24-6fc75eba-RTEur | 2.4664 |
| biHWC | origin/claude/train-sym24-2001582f-biHWC | 2.6556 |
| rRdr0 | origin/claude/train-sym24-3e0901d8-rRdr0 | 2.6661 |
| **mean** | | **2.3999** |
| **best** | | **2.2702** |

## Chain progression R1214 → R1215

Previous harvest: `workers/dispatcher/harvest-15way-r1214_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4588         | 2.3999         | -0.0589 |
| ctrl_bpc best  | 2.2674         | 2.2702         | +0.0028 |

## Per-round trajectory (best bird: R1pUa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1215 | 6770 | 2.2702 | +0.2639 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r1214_sym24`
  - `workers/dispatcher/harvest-6way-r1214_sym24`

## Output

`workers/dispatcher/harvest-10way-r1215_sym24/round-1215/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

