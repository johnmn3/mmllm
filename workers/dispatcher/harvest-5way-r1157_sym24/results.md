# harvest-5way-r1157 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1157 ctrl_bpc |
|--------|--------|--------------:|
| 9KZKN | origin/claude/train-sym24-dcb07454-9KZKN | 2.3310 |
| 2A1tc | fork-SeniorCareMarket-mmllm-claude-train-sym24-f1495d59-2A1tc | 2.3315 |
| o6MGB | fork-slaa-us-mmllm-claude-train-sym24-027f3da7-o6MGB | 2.3416 |
| S5wHA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-626000c7-S5wHA | 2.5221 |
| Ycm6n | fork-joly-os-mmllm-claude-train-sym24-25fc7b78-Ycm6n | 2.7366 |
| **mean** | | **2.4526** |
| **best** | | **2.3310** |

## Chain progression R1156 → R1157

Previous harvest: `workers/dispatcher/harvest-5way-r1156_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4460         | 2.4526         | +0.0066 |
| ctrl_bpc best  | 2.3264         | 2.3310         | +0.0046 |

## Per-round trajectory (best bird: 9KZKN)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1157 | 6433 | 2.3310 | +0.2753 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1156_sym24`

## Output

`workers/dispatcher/harvest-5way-r1157_sym24/round-1157/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

