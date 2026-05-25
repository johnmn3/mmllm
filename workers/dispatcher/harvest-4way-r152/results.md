# harvest-4way-r152 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R152 ctrl_bpc |
|--------|--------|--------------:|
| yEkQF | fork-slaa-us-mmllm-claude-train-0b30d26f-yEkQF | 0.9766 |
| 6ofwJ | origin/claude/train-a448e185-6ofwJ | 0.9846 |
| ZyZzA | fork-joly-os-mmllm-claude-train-1cbcf52d-ZyZzA | 1.0627 |
| jVyWN | fork-SeniorCareMarket-com-mmllm-claude-train-d20a29bf-jVyWN | 1.1430 |
| **mean** | | **1.0417** |
| **best** | | **0.9766** |

## Chain progression R150 → R152

Previous harvest: `workers/dispatcher/harvest-4way-r150`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1011         | 1.0417         | -0.0594 |
| ctrl_bpc best  | 1.0689         | 0.9766         | -0.0923 |

## Per-round trajectory (best bird: yEkQF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 148 | 565 | 1.0581 | -0.0013 |
| 149 | 552 | 1.0729 | -0.0039 |
| 150 | 558 | 1.0031 | +0.0039 |
| 151 | 536 | 0.9968 | -0.0006 |
| 152 | 527 | 0.9766 | +0.0056 |

## Cumulative training contribution

- This harvest: **140 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **3411 steps** from 93 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r147`

## Output

`workers/dispatcher/harvest-4way-r152/round-152/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

