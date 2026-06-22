# harvest-7way-r740 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R740 ctrl_bpc |
|--------|--------|--------------:|
| 39Iph | origin/claude/train-sym24-4f184020-39Iph | 3.3827 |
| XNZTS | fork-joly-os-mmllm-claude-train-sym24-99580ae6-XNZTS | 3.4113 |
| A7Cds | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e279ca2b-A7Cds | 3.4558 |
| PNdu6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-b4b7c1c9-PNdu6 | 3.7508 |
| LR5TZ | fork-davidwuchn-mmllm-claude-train-sym24-32325397-LR5TZ | 3.7511 |
| g8vZ7 | fork-slaa-us-mmllm-claude-train-sym24-1e4942a2-g8vZ7 | 3.7660 |
| 6pRFV | fork-slaa-us-mmllm-claude-train-sym24-435ffd5f-6pRFV | 3.7781 |
| **mean** | | **3.6137** |
| **best** | | **3.3827** |

## Chain progression R739 → R740

Previous harvest: `workers/dispatcher/harvest-10way-r739_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4944         | 3.6137         | +0.1193 |
| ctrl_bpc best  | 3.3744         | 3.3827         | +0.0083 |

## Per-round trajectory (best bird: 39Iph)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 740 | 6795 | 3.3827 | +0.7464 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r739_sym24`
  - `workers/dispatcher/harvest-7way-r739_sym24`

## Output

`workers/dispatcher/harvest-7way-r740_sym24/round-740/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

