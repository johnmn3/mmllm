# harvest-4way-r1232 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1232 ctrl_bpc |
|--------|--------|--------------:|
| sv7Dk | fork-slaa-us-mmllm-claude-train-sym24-24eaa408-sv7Dk | 2.4625 |
| HSor4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ceda73df-HSor4 | 2.4676 |
| HNWx9 | fork-joly-os-mmllm-claude-train-sym24-c7897373-HNWx9 | 2.4724 |
| x7O0b | fork-joly-os-mmllm-claude-train-sym24-f0917b11-x7O0b | 2.6534 |
| **mean** | | **2.5140** |
| **best** | | **2.4625** |

## Chain progression R1231 → R1232

Previous harvest: `workers/dispatcher/harvest-10way-r1231_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3219         | 2.5140         | +0.1921 |
| ctrl_bpc best  | 2.2498         | 2.4625         | +0.2127 |

## Per-round trajectory (best bird: sv7Dk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1232 | 6515 | 2.4625 | +0.2202 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1231_sym24`

## Output

`workers/dispatcher/harvest-4way-r1232_sym24/round-1232/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

