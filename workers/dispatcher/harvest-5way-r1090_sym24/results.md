# harvest-5way-r1090 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1090 ctrl_bpc |
|--------|--------|--------------:|
| 2XUXN | origin/claude/train-sym24-f9364d43-2XUXN | 2.4119 |
| VXipy | origin/claude/train-sym24-f718900f-VXipy | 2.4206 |
| r3TAQ | fork-SeniorCareMarket-mmllm-claude-train-sym24-9027b6a2-r3TAQ | 2.4481 |
| eQQiF | fork-slaa-us-mmllm-claude-train-sym24-54bba42f-eQQiF | 2.8065 |
| xhysL | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-095a56d4-xhysL | 2.8163 |
| **mean** | | **2.5807** |
| **best** | | **2.4119** |

## Chain progression R1089 → R1090

Previous harvest: `workers/dispatcher/harvest-4way-r1089_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4215         | 2.5807         | +0.1592 |
| ctrl_bpc best  | 2.4040         | 2.4119         | +0.0079 |

## Per-round trajectory (best bird: 2XUXN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1090 | 6348 | 2.4119 | +0.2457 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1089_sym24`
  - `workers/dispatcher/harvest-4way-r1089_sym24`

## Output

`workers/dispatcher/harvest-5way-r1090_sym24/round-1090/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

