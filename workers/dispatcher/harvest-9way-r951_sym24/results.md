# harvest-9way-r951 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R951 ctrl_bpc |
|--------|--------|--------------:|
| oj52Q | fork-joly-os-mmllm-claude-train-sym24-3a4329a8-oj52Q | 2.6556 |
| YoTEd | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1280e17c-YoTEd | 2.6674 |
| z4NrT | fork-slaa-us-mmllm-claude-train-sym24-ac494491-z4NrT | 2.6682 |
| 57W9h | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc08cea8-57W9h | 2.6697 |
| w4Vxo | fork-slaa-us-mmllm-claude-train-sym24-5bb5143f-w4Vxo | 2.6726 |
| JScWe | origin/claude/train-sym24-5abe126b-JScWe | 2.8526 |
| jEIpJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-cc0abd45-jEIpJ | 3.0452 |
| v2chy | origin/claude/train-sym24-1405ca1c-v2chy | 3.0623 |
| OauLl | fork-joly-os-mmllm-claude-train-sym24-997912c3-OauLl | 3.0676 |
| **mean** | | **2.8179** |
| **best** | | **2.6556** |

## Chain progression R950 → R951

Previous harvest: `workers/dispatcher/harvest-8way-r950_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8641         | 2.8179         | -0.0462 |
| ctrl_bpc best  | 2.6494         | 2.6556         | +0.0062 |

## Per-round trajectory (best bird: oj52Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 951 | 6904 | 2.6556 | +0.1606 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r950_sym24`
  - `workers/dispatcher/harvest-8way-r950_sym24`

## Output

`workers/dispatcher/harvest-9way-r951_sym24/round-951/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

