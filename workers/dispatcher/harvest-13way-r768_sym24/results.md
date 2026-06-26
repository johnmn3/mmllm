# harvest-13way-r768 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R768 ctrl_bpc |
|--------|--------|--------------:|
| f1BoN | fork-slaa-us-mmllm-claude-train-sym24-0ea1bd24-f1BoN | 3.2390 |
| uFVuf | origin/claude/train-sym24-00cfeea3-uFVuf | 3.2474 |
| E6pJ9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7dcf4401-E6pJ9 | 3.2609 |
| 7ZTVx | fork-joly-os-mmllm-claude-train-sym24-1edfdbe1-7ZTVx | 3.2708 |
| 4Mi9h | fork-davidwuchn-mmllm-claude-train-sym24-5d5805b3-4Mi9h | 3.2771 |
| w3LTo | fork-joly-os-mmllm-claude-train-sym24-dba8dd8d-w3LTo | 3.3530 |
| Pzuwq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-10dfb496-Pzuwq | 3.3582 |
| lMBhX | origin/claude/train-sym24-3912260e-lMBhX | 3.3620 |
| KNTN2 | fork-slaa-us-mmllm-claude-train-sym24-c706a3a1-KNTN2 | 3.3641 |
| Aqach | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc1a247d-Aqach | 3.3828 |
| 1heDP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a90b42e5-1heDP | 3.6239 |
| zSyLx | fork-davidwuchn-mmllm-claude-train-sym24-9d53040b-zSyLx | 3.6350 |
| 8Ej55 | fork-slaa-us-mmllm-claude-train-sym24-e87db0c4-8Ej55 | 3.6650 |
| **mean** | | **3.3876** |
| **best** | | **3.2390** |

## Chain progression R767 → R768

Previous harvest: `workers/dispatcher/harvest-9way-r767_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3125         | 3.3876         | +0.0751 |
| ctrl_bpc best  | 3.2354         | 3.2390         | +0.0036 |

## Per-round trajectory (best bird: f1BoN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 768 | 6473 | 3.2390 | +0.7281 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1760 steps** from 22 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r767_sym24`
  - `workers/dispatcher/harvest-9way-r767_sym24`

## Output

`workers/dispatcher/harvest-13way-r768_sym24/round-768/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

