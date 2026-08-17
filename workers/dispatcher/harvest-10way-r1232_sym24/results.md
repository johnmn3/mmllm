# harvest-10way-r1232 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R1232 ctrl_bpc |
|--------|--------|--------------:|
| i1HJO | origin/claude/train-sym24-a4ee64c6-i1HJO | 2.2508 |
| hWHC5 | origin/claude/train-sym24-afcf5ea2-hWHC5 | 2.2755 |
| SU87a | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ffb6da9b-SU87a | 2.4543 |
| ZrQKZ | fork-joly-os-mmllm-claude-train-sym24-feaa71cf-ZrQKZ | 2.4557 |
| XXnSL | fork-slaa-us-mmllm-claude-train-sym24-fbb85b11-XXnSL | 2.4595 |
| 2TU8x | fork-SeniorCareMarket-mmllm-claude-train-sym24-30fb7459-2TU8x | 2.4599 |
| sv7Dk | fork-slaa-us-mmllm-claude-train-sym24-24eaa408-sv7Dk | 2.4625 |
| HSor4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ceda73df-HSor4 | 2.4676 |
| HNWx9 | fork-joly-os-mmllm-claude-train-sym24-c7897373-HNWx9 | 2.4724 |
| x7O0b | fork-joly-os-mmllm-claude-train-sym24-f0917b11-x7O0b | 2.6534 |
| **mean** | | **2.4412** |
| **best** | | **2.2508** |

## Chain progression R1231 → R1232

Previous harvest: `workers/dispatcher/harvest-6way-r1231_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3343         | 2.4412         | +0.1069 |
| ctrl_bpc best  | 2.2547         | 2.2508         | -0.0039 |

## Per-round trajectory (best bird: i1HJO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1232 | 3587 | 2.2508 | +0.2547 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1231_sym24`
  - `workers/dispatcher/harvest-6way-r1231_sym24`

## Output

`workers/dispatcher/harvest-10way-r1232_sym24/round-1232/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

