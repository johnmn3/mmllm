# harvest-3way-r854 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R854 ctrl_bpc |
|--------|--------|--------------:|
| wTJQq | origin/claude/train-sym24-051da065-wTJQq | 2.9177 |
| fe8VW | fork-slaa-us-mmllm-claude-train-sym24-76430e59-fe8VW | 2.9313 |
| 4U5hP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c362e397-4U5hP | 3.0794 |
| **mean** | | **2.9761** |
| **best** | | **2.9177** |

## Chain progression R853 → R854

Previous harvest: `workers/dispatcher/harvest-1way-r853_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9257         | 2.9761         | +0.0504 |
| ctrl_bpc best  | 2.9257         | 2.9177         | -0.0080 |

## Per-round trajectory (best bird: wTJQq)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 854 | 6644 | 2.9177 | +0.4592 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r853_sym24`

## Output

`workers/dispatcher/harvest-3way-r854_sym24/round-854/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

