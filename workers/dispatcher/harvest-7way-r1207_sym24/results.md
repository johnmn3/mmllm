# harvest-7way-r1207 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1207 ctrl_bpc |
|--------|--------|--------------:|
| nkO4f | fork-joly-os-mmllm-claude-train-sym24-950a67cd-nkO4f | 2.2754 |
| uTOHG | origin/claude/train-sym24-62a30160-uTOHG | 2.2767 |
| aOuQa | fork-slaa-us-mmllm-claude-train-sym24-322c428f-aOuQa | 2.2982 |
| GVjKf | fork-joly-os-mmllm-claude-train-sym24-2c6c2335-GVjKf | 2.3016 |
| SAjMv | fork-slaa-us-mmllm-claude-train-sym24-fac5c4d8-SAjMv | 2.4665 |
| qNAT8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a3b93331-qNAT8 | 2.4690 |
| v8oPc | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-112a979f-v8oPc | 2.4721 |
| **mean** | | **2.3656** |
| **best** | | **2.2754** |

## Chain progression R1206 → R1207

Previous harvest: `workers/dispatcher/harvest-10way-r1206_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4804         | 2.3656         | -0.1148 |
| ctrl_bpc best  | 2.2812         | 2.2754         | -0.0058 |

## Per-round trajectory (best bird: nkO4f)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1207 | 6533 | 2.2754 | +0.2704 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1206_sym24`

## Output

`workers/dispatcher/harvest-7way-r1207_sym24/round-1207/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

