# harvest-11way-r1244 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1244 ctrl_bpc |
|--------|--------|--------------:|
| lTCNS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ba8402ea-lTCNS | 2.2409 |
| pgmYW | fork-SeniorCareMarket-mmllm-claude-train-sym24-a33c8db7-pgmYW | 2.2441 |
| JcQHi | fork-slaa-us-mmllm-claude-train-sym24-ecd77cf1-JcQHi | 2.2474 |
| k2PVr | fork-SeniorCareMarket-mmllm-claude-train-sym24-202c85ac-k2PVr | 2.2545 |
| sfCP1 | fork-joly-os-mmllm-claude-train-sym24-387259c0-sfCP1 | 2.2568 |
| LrOgA | origin/claude/train-sym24-38eec9de-LrOgA | 2.2600 |
| yYa5b | origin/claude/train-sym24-e3b5be82-yYa5b | 2.2617 |
| xzRM1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-bd8f0a67-xzRM1 | 2.2637 |
| kl41H | fork-slaa-us-mmllm-claude-train-sym24-9bc17c4d-kl41H | 2.4500 |
| 7Zp4l | fork-SeniorCareMarket-mmllm-claude-train-sym24-c8bd5253-7Zp4l | 2.6392 |
| WQRiM | fork-slaa-us-mmllm-claude-train-sym24-4d7e57ec-WQRiM | 2.6509 |
| **mean** | | **2.3427** |
| **best** | | **2.2409** |

## Chain progression R1243 → R1244

Previous harvest: `workers/dispatcher/harvest-4way-r1243_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4051         | 2.3427         | -0.0624 |
| ctrl_bpc best  | 2.2525         | 2.2409         | -0.0116 |

## Per-round trajectory (best bird: lTCNS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1244 | 6715 | 2.2409 | +0.2659 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r1243_sym24`
  - `workers/dispatcher/harvest-4way-r1243_sym24`

## Output

`workers/dispatcher/harvest-11way-r1244_sym24/round-1244/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

