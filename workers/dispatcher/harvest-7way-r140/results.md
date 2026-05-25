# harvest-7way-r140 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R140 ctrl_bpc |
|--------|--------|--------------:|
| 40XoW | fork-slaa-us-mmllm-claude-train-89f75154-40XoW | 1.0228 |
| uzeIK | fork-SeniorCareMarket-com-mmllm-claude-train-9e4bf60e-uzeIK | 1.0553 |
| 1WiVU | origin/claude/train-a3bd052d-1WiVU | 1.0625 |
| 0xf1x | fork-SeniorCareMarket-mmllm-claude-train-59494e87-0xf1x | 1.0734 |
| PJiAF | fork-SeniorCareMarket-com-mmllm-claude-train-51c0ce7a-PJiAF | 1.0749 |
| xFNur | fork-slaa-us-mmllm-claude-train-1336e60d-xFNur | 1.0885 |
| dQbB7 | fork-joly-os-mmllm-claude-train-0bb176cb-dQbB7 | 1.1011 |
| **mean** | | **1.0684** |
| **best** | | **1.0228** |

## Chain progression R139 → R140

Previous harvest: `workers/dispatcher/harvest-3way-r139`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.0756         | 1.0684         | -0.0072 |
| ctrl_bpc best  | 1.0496         | 1.0228         | -0.0268 |

## Per-round trajectory (best bird: 40XoW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 140 | 611 | 1.0228 | +0.0022 |

## Cumulative training contribution

- This harvest: **189 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **3222 steps** from 87 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r135`
  - `workers/dispatcher/harvest-3way-r139`

## Output

`workers/dispatcher/harvest-7way-r140/round-140/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

