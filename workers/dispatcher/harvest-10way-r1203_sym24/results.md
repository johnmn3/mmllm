# harvest-10way-r1203 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1203 ctrl_bpc |
|--------|--------|--------------:|
| 96fK3 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-288164c8-96fK3 | 2.2775 |
| W14nG | fork-joly-os-mmllm-claude-train-sym24-f305c79e-W14nG | 2.2829 |
| PPrPh | fork-joly-os-mmllm-claude-train-sym24-0566f890-PPrPh | 2.2846 |
| sET5W | fork-slaa-us-mmllm-claude-train-sym24-29d21dbb-sET5W | 2.3067 |
| wOcFQ | fork-slaa-us-mmllm-claude-train-sym24-44fae692-wOcFQ | 2.4726 |
| IZfcH | fork-slaa-us-mmllm-claude-train-sym24-1f79584c-IZfcH | 2.4759 |
| utZYu | fork-SeniorCareMarket-mmllm-claude-train-sym24-afa5c1c1-utZYu | 2.4793 |
| XI2kf | origin/claude/train-sym24-e69253bb-XI2kf | 2.4800 |
| a1Rgy | origin/claude/train-sym24-6ca38825-a1Rgy | 2.4864 |
| BsOfj | origin/claude/train-sym24-cfd64747-BsOfj | 2.6900 |
| **mean** | | **2.4236** |
| **best** | | **2.2775** |

## Chain progression R1202 → R1203

Previous harvest: `workers/dispatcher/harvest-7way-r1202_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5057         | 2.4236         | -0.0821 |
| ctrl_bpc best  | 2.2838         | 2.2775         | -0.0063 |

## Per-round trajectory (best bird: 96fK3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1203 | 6573 | 2.2775 | +0.2729 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1202_sym24`
  - `workers/dispatcher/harvest-3way-r1202_sym24`
  - `workers/dispatcher/harvest-7way-r1202_sym24`

## Output

`workers/dispatcher/harvest-10way-r1203_sym24/round-1203/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

