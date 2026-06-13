# harvest-13way-r667 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R667 ctrl_bpc |
|--------|--------|--------------:|
| YPVdo | fork-SeniorCareMarket-mmllm-claude-train-sym24-c5a41e1d-YPVdo | 3.8934 |
| navt1 | fork-davidwuchn-mmllm-claude-train-sym24-49cdc0d9-navt1 | 3.9045 |
| 8z1fK | fork-slaa-us-mmllm-claude-train-sym24-c0016dcf-8z1fK | 3.9171 |
| K8Xxg | fork-davidwuchn-mmllm-claude-train-sym24-46b34628-K8Xxg | 3.9189 |
| uHCGN | origin/claude/train-sym24-9a217749-uHCGN | 3.9412 |
| qUSPs | fork-joly-os-mmllm-claude-train-sym24-d93b2323-qUSPs | 3.9458 |
| Fu4ds | origin/claude/train-sym24-45856087-Fu4ds | 3.9459 |
| Cg6AF | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc9c76d7-Cg6AF | 3.9592 |
| X1pev | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1418df83-X1pev | 3.9730 |
| TnUra | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e5c0fcae-TnUra | 4.0099 |
| 7AJ6a | fork-joly-os-mmllm-claude-train-sym24-eb63477a-7AJ6a | 4.0110 |
| lpBG1 | fork-joly-os-mmllm-claude-train-sym24-0b7de31a-lpBG1 | 4.2415 |
| MB1CF | fork-slaa-us-mmllm-claude-train-sym24-31f150cb-MB1CF | 4.2552 |
| **mean** | | **3.9936** |
| **best** | | **3.8934** |

## Chain progression R666 → R667

Previous harvest: `workers/dispatcher/harvest-8way-r666_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9987         | 3.9936         | -0.0051 |
| ctrl_bpc best  | 3.9071         | 3.8934         | -0.0137 |

## Per-round trajectory (best bird: YPVdo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 667 | 6569 | 3.8934 | +0.2429 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r666_sym24`
  - `workers/dispatcher/harvest-8way-r666_sym24`

## Output

`workers/dispatcher/harvest-13way-r667_sym24/round-667/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

