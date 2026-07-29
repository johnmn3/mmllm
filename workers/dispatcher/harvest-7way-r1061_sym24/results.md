# harvest-7way-r1061 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1061 ctrl_bpc |
|--------|--------|--------------:|
| uZusE | origin/claude/train-sym24-ba8cfc85-uZusE | 2.4555 |
| SKw1V | origin/claude/train-sym24-2fc83abb-SKw1V | 2.4643 |
| 6lztH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-edb872eb-6lztH | 2.4795 |
| xe71e | fork-slaa-us-mmllm-claude-train-sym24-e019bd4b-xe71e | 2.4906 |
| 7hntC | fork-joly-os-mmllm-claude-train-sym24-9994af28-7hntC | 2.4946 |
| Aec7x | fork-slaa-us-mmllm-claude-train-sym24-05a03ed6-Aec7x | 2.8483 |
| BpHCz | fork-SeniorCareMarket-mmllm-claude-train-sym24-9da16164-BpHCz | 2.8590 |
| **mean** | | **2.5845** |
| **best** | | **2.4555** |

## Chain progression R1060 → R1061

Previous harvest: `workers/dispatcher/harvest-7way-r1060_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5582         | 2.5845         | +0.0263 |
| ctrl_bpc best  | 2.4603         | 2.4555         | -0.0048 |

## Per-round trajectory (best bird: uZusE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1061 | 4282 | 2.4555 | +0.2085 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r1060_sym24`
  - `workers/dispatcher/harvest-7way-r1060_sym24`

## Output

`workers/dispatcher/harvest-7way-r1061_sym24/round-1061/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

