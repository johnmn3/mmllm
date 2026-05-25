# harvest-3way-r139 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R139 ctrl_bpc |
|--------|--------|--------------:|
| JKHjn | fork-joly-os-mmllm-claude-train-73fc4ed8-JKHjn | 1.0496 |
| laJF7 | origin/claude/train-7b40f04a-laJF7 | 1.0831 |
| QjXOx | fork-slaa-us-mmllm-claude-train-61caad64-QjXOx | 1.0942 |
| **mean** | | **1.0756** |
| **best** | | **1.0496** |

## Chain progression R135 → R139

Previous harvest: `workers/dispatcher/harvest-2way-r135`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0756         | 1.0756         | +0.0000 |
| ctrl_bpc best  | 1.0654         | 1.0496         | -0.0158 |

## Per-round trajectory (best bird: JKHjn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 135 | 384 | 1.0873 | +0.0008 |
| 136 | 373 | 1.0823 | +0.0003 |
| 137 | 366 | 1.0500 | -0.0011 |
| 138 | 394 | 1.0750 | +0.0007 |
| 139 | 362 | 1.0496 | -0.0029 |

## Cumulative training contribution

- This harvest: **105 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **3033 steps** from 80 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r134`

## Output

`workers/dispatcher/harvest-3way-r139/round-139/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

