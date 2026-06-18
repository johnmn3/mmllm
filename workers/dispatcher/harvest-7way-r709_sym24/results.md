# harvest-7way-r709 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R709 ctrl_bpc |
|--------|--------|--------------:|
| IaTPB | fork-davidwuchn-mmllm-claude-train-sym24-79a40905-IaTPB | 3.5610 |
| Am7xj | fork-davidwuchn-mmllm-claude-train-sym24-e65442c8-Am7xj | 3.5740 |
| fAYc2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7777edec-fAYc2 | 3.5929 |
| yxZMI | fork-joly-os-mmllm-claude-train-sym24-941a7162-yxZMI | 3.6005 |
| QTGTB | origin/claude/train-sym24-7ab28414-QTGTB | 3.6044 |
| L5C9s | fork-slaa-us-mmllm-claude-train-sym24-af134920-L5C9s | 3.6137 |
| 5V5oF | fork-joly-os-mmllm-claude-train-sym24-f35ee655-5V5oF | 3.9023 |
| **mean** | | **3.6355** |
| **best** | | **3.5610** |

## Chain progression R708 → R709

Previous harvest: `workers/dispatcher/harvest-15way-r708_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6750         | 3.6355         | -0.0395 |
| ctrl_bpc best  | 3.5686         | 3.5610         | -0.0076 |

## Per-round trajectory (best bird: IaTPB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 709 | 6552 | 3.5610 | +0.8900 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r708_sym24`
  - `workers/dispatcher/harvest-6way-r708_sym24`

## Output

`workers/dispatcher/harvest-7way-r709_sym24/round-709/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

