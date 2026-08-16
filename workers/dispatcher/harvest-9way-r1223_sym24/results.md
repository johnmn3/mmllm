# harvest-9way-r1223 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1223 ctrl_bpc |
|--------|--------|--------------:|
| LeS8V | fork-slaa-us-mmllm-claude-train-sym24-bacac56d-LeS8V | 2.2555 |
| AeZ7h | fork-SeniorCareMarket-mmllm-claude-train-sym24-327b4f57-AeZ7h | 2.2564 |
| UBH4t | fork-joly-os-mmllm-claude-train-sym24-a5aecfaa-UBH4t | 2.2600 |
| pJrlg | origin/claude/train-sym24-f20b7b22-pJrlg | 2.2768 |
| GqAKX | fork-joly-os-mmllm-claude-train-sym24-babb14ee-GqAKX | 2.2788 |
| t8thk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-be7f0dda-t8thk | 2.2873 |
| Awzdt | origin/claude/train-sym24-33987d3b-Awzdt | 2.4614 |
| QSKOU | fork-SeniorCareMarket-mmllm-claude-train-sym24-97fe5b45-QSKOU | 2.4673 |
| mFjc8 | fork-slaa-us-mmllm-claude-train-sym24-1cc3b530-mFjc8 | 2.6699 |
| **mean** | | **2.3570** |
| **best** | | **2.2555** |

## Chain progression R1222 → R1223

Previous harvest: `workers/dispatcher/harvest-5way-r1222_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3487         | 2.3570         | +0.0083 |
| ctrl_bpc best  | 2.2577         | 2.2555         | -0.0022 |

## Per-round trajectory (best bird: LeS8V)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1223 | 6477 | 2.2555 | +0.2688 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1222_sym24`
  - `workers/dispatcher/harvest-5way-r1222_sym24`

## Output

`workers/dispatcher/harvest-9way-r1223_sym24/round-1223/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

