# harvest-13way-r709 — sparse-delta merge of 13 birds

## Worker endpoints

| handle | branch | R709 ctrl_bpc |
|--------|--------|--------------:|
| IaTPB | fork-davidwuchn-mmllm-claude-train-sym24-79a40905-IaTPB | 3.5610 |
| Am7xj | fork-davidwuchn-mmllm-claude-train-sym24-e65442c8-Am7xj | 3.5740 |
| fAYc2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7777edec-fAYc2 | 3.5929 |
| yxZMI | fork-joly-os-mmllm-claude-train-sym24-941a7162-yxZMI | 3.6005 |
| QTGTB | origin/claude/train-sym24-7ab28414-QTGTB | 3.6044 |
| TaStZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-fe1861d6-TaStZ | 3.6085 |
| L5C9s | fork-slaa-us-mmllm-claude-train-sym24-af134920-L5C9s | 3.6137 |
| AuNLO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dc325590-AuNLO | 3.6226 |
| KKBPw | fork-joly-os-mmllm-claude-train-sym24-9d04ea5d-KKBPw | 3.6292 |
| 5V5oF | fork-joly-os-mmllm-claude-train-sym24-f35ee655-5V5oF | 3.9023 |
| Bka0n | origin/claude/train-sym24-8bf026df-Bka0n | 3.9026 |
| 1qt9D | fork-slaa-us-mmllm-claude-train-sym24-7460b555-1qt9D | 3.9146 |
| fsCnj | fork-joly-os-mmllm-claude-train-sym24-f12ed6b7-fsCnj | 3.9238 |
| **mean** | | **3.6962** |
| **best** | | **3.5610** |

## Chain progression R708 → R709

Previous harvest: `workers/dispatcher/harvest-6way-r708_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7849         | 3.6962         | -0.0887 |
| ctrl_bpc best  | 3.5772         | 3.5610         | -0.0162 |

## Per-round trajectory (best bird: IaTPB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 709 | 6552 | 3.5610 | +0.8900 |

## Cumulative training contribution

- This harvest: **1040 steps** from 13 bird(s)
- Across full ancestry (deduped by bird_id): **1520 steps** from 19 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r708_sym24`
  - `workers/dispatcher/harvest-6way-r708_sym24`

## Output

`workers/dispatcher/harvest-13way-r709_sym24/round-709/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 13 workers)
- `dense.pt` (averaged across 13 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

