# harvest-4way-r1244 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1244 ctrl_bpc |
|--------|--------|--------------:|
| lTCNS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ba8402ea-lTCNS | 2.2409 |
| JcQHi | fork-slaa-us-mmllm-claude-train-sym24-ecd77cf1-JcQHi | 2.2474 |
| LrOgA | origin/claude/train-sym24-38eec9de-LrOgA | 2.2600 |
| 7Zp4l | fork-SeniorCareMarket-mmllm-claude-train-sym24-c8bd5253-7Zp4l | 2.6392 |
| **mean** | | **2.3469** |
| **best** | | **2.2409** |

## Chain progression R1243 → R1244

Previous harvest: `workers/dispatcher/harvest-16way-r1243_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4265         | 2.3469         | -0.0796 |
| ctrl_bpc best  | 2.2466         | 2.2409         | -0.0057 |

## Per-round trajectory (best bird: lTCNS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1244 | 6715 | 2.2409 | +0.2659 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1243_sym24`

## Output

`workers/dispatcher/harvest-4way-r1244_sym24/round-1244/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

