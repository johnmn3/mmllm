# harvest-2way-r135 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R135 ctrl_bpc |
|--------|--------|--------------:|
| laJF7 | origin/claude/train-7b40f04a-laJF7 | 1.0654 |
| QjXOx | fork-slaa-us-mmllm-claude-train-61caad64-QjXOx | 1.0858 |
| **mean** | | **1.0756** |
| **best** | | **1.0654** |

## Chain progression R134 → R135

Previous harvest: `workers/dispatcher/harvest-fold4way-r134`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0859         | 1.0756         | -0.0103 |
| ctrl_bpc best  | 1.0662         | 1.0654         | -0.0008 |

## Per-round trajectory (best bird: laJF7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 135 | 643 | 1.0654 | -0.0001 |

## Cumulative training contribution

- This harvest: **14 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **2942 steps** from 79 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r134`

## Output

`workers/dispatcher/harvest-2way-r135/round-135/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

