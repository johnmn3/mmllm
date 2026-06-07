# harvest-3way-r632 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R632 ctrl_bpc |
|--------|--------|--------------:|
| WhpTw | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-83b5d2f2-WhpTw | 2.1131 |
| hArCI | origin/claude/train-sym24-8402b883-hArCI | 2.1332 |
| s42iF | fork-slaa-us-mmllm-claude-train-sym24-ca1418bd-s42iF | 2.5836 |
| **mean** | | **2.2766** |
| **best** | | **2.1131** |

## Chain progression R631 → R632

Previous harvest: `workers/dispatcher/harvest-2way-r631_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1245         | 2.2766         | +0.1521 |
| ctrl_bpc best  | 2.1158         | 2.1131         | -0.0027 |

## Per-round trajectory (best bird: WhpTw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 632 | 5164 | 2.1131 | +0.0539 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **450 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r631_sym24`

## Output

`workers/dispatcher/harvest-3way-r632_sym24/round-632/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

