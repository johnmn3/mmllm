# harvest-4way-r1007 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1007 ctrl_bpc |
|--------|--------|--------------:|
| uCvE5 | fork-slaa-us-mmllm-claude-train-sym24-5d320a3e-uCvE5 | 2.5633 |
| mXiyj | fork-joly-os-mmllm-claude-train-sym24-32dff608-mXiyj | 2.5644 |
| fA1Hv | fork-SeniorCareMarket-mmllm-claude-train-sym24-c294e21c-fA1Hv | 2.5946 |
| JCL1a | origin/claude/train-sym24-8e84560e-JCL1a | 2.7549 |
| **mean** | | **2.6193** |
| **best** | | **2.5633** |

## Chain progression R1006 → R1007

Previous harvest: `workers/dispatcher/harvest-6way-r1006_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7171         | 2.6193         | -0.0978 |
| ctrl_bpc best  | 2.5450         | 2.5633         | +0.0183 |

## Per-round trajectory (best bird: uCvE5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1007 | 6559 | 2.5633 | +0.1553 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1006_sym24`

## Output

`workers/dispatcher/harvest-4way-r1007_sym24/round-1007/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

