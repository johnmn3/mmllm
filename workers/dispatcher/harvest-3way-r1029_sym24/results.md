# harvest-3way-r1029 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1029 ctrl_bpc |
|--------|--------|--------------:|
| bkRtX | fork-slaa-us-mmllm-claude-train-sym24-48fac693-bkRtX | 2.5272 |
| YQdp4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4a5f51eb-YQdp4 | 2.7063 |
| JmGJg | origin/claude/train-sym24-8a96ee1a-JmGJg | 2.9009 |
| **mean** | | **2.7115** |
| **best** | | **2.5272** |

## Chain progression R1028 → R1029

Previous harvest: `workers/dispatcher/harvest-5way-r1028_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6323         | 2.7115         | +0.0792 |
| ctrl_bpc best  | 2.5027         | 2.5272         | +0.0245 |

## Per-round trajectory (best bird: bkRtX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1029 | 6706 | 2.5272 | +0.2036 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1028_sym24`

## Output

`workers/dispatcher/harvest-3way-r1029_sym24/round-1029/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

