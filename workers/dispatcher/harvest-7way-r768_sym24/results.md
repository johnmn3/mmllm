# harvest-7way-r768 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R768 ctrl_bpc |
|--------|--------|--------------:|
| f1BoN | fork-slaa-us-mmllm-claude-train-sym24-0ea1bd24-f1BoN | 3.2390 |
| uFVuf | origin/claude/train-sym24-00cfeea3-uFVuf | 3.2474 |
| w3LTo | fork-joly-os-mmllm-claude-train-sym24-dba8dd8d-w3LTo | 3.3530 |
| KNTN2 | fork-slaa-us-mmllm-claude-train-sym24-c706a3a1-KNTN2 | 3.3641 |
| Aqach | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc1a247d-Aqach | 3.3828 |
| 1heDP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-a90b42e5-1heDP | 3.6239 |
| zSyLx | fork-davidwuchn-mmllm-claude-train-sym24-9d53040b-zSyLx | 3.6350 |
| **mean** | | **3.4065** |
| **best** | | **3.2390** |

## Chain progression R767 → R768

Previous harvest: `workers/dispatcher/harvest-12way-r767_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3072         | 3.4065         | +0.0993 |
| ctrl_bpc best  | 3.2354         | 3.2390         | +0.0036 |

## Per-round trajectory (best bird: f1BoN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 768 | 6473 | 3.2390 | +0.7281 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r767_sym24`

## Output

`workers/dispatcher/harvest-7way-r768_sym24/round-768/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

