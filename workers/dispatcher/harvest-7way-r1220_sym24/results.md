# harvest-7way-r1220 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1220 ctrl_bpc |
|--------|--------|--------------:|
| EaQYK | origin/claude/train-sym24-16be6ffc-EaQYK | 2.2654 |
| J6WE1 | fork-slaa-us-mmllm-claude-train-sym24-c57423bf-J6WE1 | 2.2654 |
| EdkMB | origin/claude/train-sym24-cb616bd4-EdkMB | 2.2827 |
| ex6wU | fork-joly-os-mmllm-claude-train-sym24-a1087022-ex6wU | 2.2828 |
| lXh2l | fork-joly-os-mmllm-claude-train-sym24-e8c9f0bf-lXh2l | 2.2888 |
| tYUHR | fork-SeniorCareMarket-mmllm-claude-train-sym24-39b07472-tYUHR | 2.2967 |
| PRtDT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8a706df5-PRtDT | 2.4661 |
| **mean** | | **2.3068** |
| **best** | | **2.2654** |

## Chain progression R1219 → R1220

Previous harvest: `workers/dispatcher/harvest-7way-r1219_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4445         | 2.3068         | -0.1377 |
| ctrl_bpc best  | 2.2691         | 2.2654         | -0.0037 |

## Per-round trajectory (best bird: EaQYK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1220 | 4456 | 2.2654 | +0.2747 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1219_sym24`

## Output

`workers/dispatcher/harvest-7way-r1220_sym24/round-1220/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

