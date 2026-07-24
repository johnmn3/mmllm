# harvest-4way-r1014 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1014 ctrl_bpc |
|--------|--------|--------------:|
| pbKQW | origin/claude/train-sym24-572e7bc9-pbKQW | 2.5272 |
| rUWk3 | fork-slaa-us-mmllm-claude-train-sym24-a38f3623-rUWk3 | 2.5509 |
| y3zpD | fork-SeniorCareMarket-mmllm-claude-train-sym24-b3ab43dd-y3zpD | 2.7251 |
| atKaf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ac42940b-atKaf | 2.9582 |
| **mean** | | **2.6904** |
| **best** | | **2.5272** |

## Chain progression R1013 → R1014

Previous harvest: `workers/dispatcher/harvest-4way-r1013_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7810         | 2.6904         | -0.0907 |
| ctrl_bpc best  | 2.5322         | 2.5272         | -0.0050 |

## Per-round trajectory (best bird: pbKQW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1014 | 3575 | 2.5272 | +0.1861 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1013_sym24`

## Output

`workers/dispatcher/harvest-4way-r1014_sym24/round-1014/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

