# harvest-4way-r1025 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1025 ctrl_bpc |
|--------|--------|--------------:|
| 0ItDp | fork-SeniorCareMarket-mmllm-claude-train-sym24-d01b5bcb-0ItDp | 2.5369 |
| zT7cE | fork-joly-os-mmllm-claude-train-sym24-00cf0fe6-zT7cE | 2.5688 |
| Tll6q | fork-joly-os-mmllm-claude-train-sym24-be7cf5f5-Tll6q | 2.7087 |
| UbU3i | fork-slaa-us-mmllm-claude-train-sym24-850ea42f-UbU3i | 2.8957 |
| **mean** | | **2.6775** |
| **best** | | **2.5369** |

## Chain progression R1024 → R1025

Previous harvest: `workers/dispatcher/harvest-5way-r1024_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6401         | 2.6775         | +0.0374 |
| ctrl_bpc best  | 2.5182         | 2.5369         | +0.0187 |

## Per-round trajectory (best bird: 0ItDp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1025 | 6444 | 2.5369 | +0.1766 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1024_sym24`
  - `workers/dispatcher/harvest-5way-r1024_sym24`

## Output

`workers/dispatcher/harvest-4way-r1025_sym24/round-1025/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

