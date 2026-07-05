# harvest-5way-r846 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R846 ctrl_bpc |
|--------|--------|--------------:|
| XWcIE | fork-SeniorCareMarket-mmllm-claude-train-sym24-69154145-XWcIE | 2.9391 |
| oB33J | fork-slaa-us-mmllm-claude-train-sym24-7d2c7800-oB33J | 2.9510 |
| oxbnT | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c00274f0-oxbnT | 2.9561 |
| uANok | fork-joly-os-mmllm-claude-train-sym24-6afe2818-uANok | 3.1007 |
| AMtij | fork-slaa-us-mmllm-claude-train-sym24-817f0b27-AMtij | 3.3176 |
| **mean** | | **3.0529** |
| **best** | | **2.9391** |

## Chain progression R845 → R846

Previous harvest: `workers/dispatcher/harvest-6way-r845_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1127         | 3.0529         | -0.0598 |
| ctrl_bpc best  | 2.9493         | 2.9391         | -0.0102 |

## Per-round trajectory (best bird: XWcIE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 846 | 6455 | 2.9391 | +0.2487 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r845_sym24`
  - `workers/dispatcher/harvest-6way-r845_sym24`

## Output

`workers/dispatcher/harvest-5way-r846_sym24/round-846/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

