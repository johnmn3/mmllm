# harvest-8way-r1208 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1208 ctrl_bpc |
|--------|--------|--------------:|
| 1AnJo | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4c799d43-1AnJo | 2.2958 |
| qQwIC | fork-slaa-us-mmllm-claude-train-sym24-91da294a-qQwIC | 2.2983 |
| WiyJa | fork-joly-os-mmllm-claude-train-sym24-b9b26ad5-WiyJa | 2.2996 |
| OOGIo | fork-SeniorCareMarket-mmllm-claude-train-sym24-df15e109-OOGIo | 2.3006 |
| MVTYp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9c934801-MVTYp | 2.4698 |
| cwg4G | origin/claude/train-sym24-7a7fa357-cwg4G | 2.4736 |
| 1em6W | fork-joly-os-mmllm-claude-train-sym24-f6506ba1-1em6W | 2.6668 |
| kxYsZ | fork-slaa-us-mmllm-claude-train-sym24-1193f001-kxYsZ | 2.6689 |
| **mean** | | **2.4342** |
| **best** | | **2.2958** |

## Chain progression R1207 → R1208

Previous harvest: `workers/dispatcher/harvest-7way-r1207_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3656         | 2.4342         | +0.0686 |
| ctrl_bpc best  | 2.2754         | 2.2958         | +0.0204 |

## Per-round trajectory (best bird: 1AnJo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1208 | 6509 | 2.2958 | +0.2492 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1207_sym24`
  - `workers/dispatcher/harvest-7way-r1207_sym24`

## Output

`workers/dispatcher/harvest-8way-r1208_sym24/round-1208/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

