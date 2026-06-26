# harvest-20way-r768 — sparse-delta merge of 20 birds

## Worker endpoints

| handle | branch | R768 ctrl_bpc |
|--------|--------|--------------:|
| W7N8n | fork-SeniorCareMarket-mmllm-claude-train-sym24-f3ba91f1-W7N8n | 3.2333 |
| f1BoN | fork-slaa-us-mmllm-claude-train-sym24-0ea1bd24-f1BoN | 3.2390 |
| WTPMj | origin/claude/train-sym24-e0430618-WTPMj | 3.2398 |
| uFVuf | origin/claude/train-sym24-00cfeea3-uFVuf | 3.2474 |
| E6pJ9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7dcf4401-E6pJ9 | 3.2609 |
| 7ZTVx | fork-joly-os-mmllm-claude-train-sym24-1edfdbe1-7ZTVx | 3.2708 |
| 4Mi9h | fork-davidwuchn-mmllm-claude-train-sym24-5d5805b3-4Mi9h | 3.2771 |
| wJbao | fork-davidwuchn-mmllm-claude-train-sym24-f06f4cea-wJbao | 3.2833 |
| Bn4SD | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-528d4323-Bn4SD | 3.2867 |
| w3LTo | fork-joly-os-mmllm-claude-train-sym24-dba8dd8d-w3LTo | 3.3530 |
| mFyYX | origin/claude/train-sym24-081cffaf-mFyYX | 3.3574 |
| Pzuwq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-10dfb496-Pzuwq | 3.3582 |
| lMBhX | origin/claude/train-sym24-3912260e-lMBhX | 3.3620 |
| KNTN2 | fork-slaa-us-mmllm-claude-train-sym24-c706a3a1-KNTN2 | 3.3641 |
| 4u4uJ | fork-slaa-us-mmllm-claude-train-sym24-5c15c084-4u4uJ | 3.3652 |
| Aqach | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc1a247d-Aqach | 3.3828 |
| Pum2d | fork-joly-os-mmllm-claude-train-sym24-f3f9f758-Pum2d | 3.6103 |
| 1heDP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a90b42e5-1heDP | 3.6239 |
| zSyLx | fork-davidwuchn-mmllm-claude-train-sym24-9d53040b-zSyLx | 3.6350 |
| 8Ej55 | fork-slaa-us-mmllm-claude-train-sym24-e87db0c4-8Ej55 | 3.6650 |
| **mean** | | **3.3708** |
| **best** | | **3.2333** |

## Chain progression R767 → R768

Previous harvest: `workers/dispatcher/harvest-9way-r767_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3125         | 3.3708         | +0.0583 |
| ctrl_bpc best  | 3.2354         | 3.2333         | -0.0021 |

## Per-round trajectory (best bird: W7N8n)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 768 | 5330 | 3.2333 | +0.5963 |

## Cumulative training contribution

- This harvest: **1600 steps** from 20 bird(s)
- Across full ancestry (deduped by bird_id): **2320 steps** from 29 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-12way-r767_sym24`
  - `workers/dispatcher/harvest-2way-r767_sym24`
  - `workers/dispatcher/harvest-9way-r767_sym24`

## Output

`workers/dispatcher/harvest-20way-r768_sym24/round-768/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 20 workers)
- `dense.pt` (averaged across 20 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

