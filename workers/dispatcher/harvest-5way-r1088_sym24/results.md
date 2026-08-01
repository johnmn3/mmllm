# harvest-5way-r1088 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1088 ctrl_bpc |
|--------|--------|--------------:|
| 2MMm3 | fork-slaa-us-mmllm-claude-train-sym24-70f16504-2MMm3 | 2.4082 |
| 2NjmX | origin/claude/train-sym24-75f7f2ae-2NjmX | 2.4237 |
| i9h4G | origin/claude/train-sym24-f2c06144-i9h4G | 2.4328 |
| mAYMJ | fork-SeniorCareMarket-mmllm-claude-train-sym24-20b0fb08-mAYMJ | 2.4331 |
| me5rv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-226e2fc5-me5rv | 2.4450 |
| **mean** | | **2.4286** |
| **best** | | **2.4082** |

## Chain progression R1087 → R1088

Previous harvest: `workers/dispatcher/harvest-6way-r1087_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6926         | 2.4286         | -0.2640 |
| ctrl_bpc best  | 2.4332         | 2.4082         | -0.0250 |

## Per-round trajectory (best bird: 2MMm3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1088 | 6732 | 2.4082 | +0.2324 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1087_sym24`

## Output

`workers/dispatcher/harvest-5way-r1088_sym24/round-1088/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

