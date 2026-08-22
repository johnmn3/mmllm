# harvest-8way-r1279 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1279 ctrl_bpc |
|--------|--------|--------------:|
| tFngV | fork-slaa-us-mmllm-claude-train-sym24-cf03d8a3-tFngV | 2.2426 |
| GLHLu | fork-joly-os-mmllm-claude-train-sym24-008b2f79-GLHLu | 2.2488 |
| iCo5v | fork-joly-os-mmllm-claude-train-sym24-71305a11-iCo5v | 2.2584 |
| yzm93 | fork-slaa-us-mmllm-claude-train-sym24-cff8248c-yzm93 | 2.4139 |
| ZCkig | origin/claude/train-sym24-7e48c873-ZCkig | 2.4156 |
| 138rx | origin/claude/train-sym24-5e50caf7-138rx | 2.6136 |
| CkoaH | fork-SeniorCareMarket-mmllm-claude-train-sym24-9c441992-CkoaH | 2.6162 |
| W3wrP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5f89bca1-W3wrP | 2.6183 |
| **mean** | | **2.4284** |
| **best** | | **2.2426** |

## Chain progression R1278 → R1279

Previous harvest: `workers/dispatcher/harvest-6way-r1278_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.2997         | 2.4284         | +0.1287 |
| ctrl_bpc best  | 2.2282         | 2.2426         | +0.0144 |

## Per-round trajectory (best bird: tFngV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1279 | 4420 | 2.2426 | +0.2396 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1278_sym24`
  - `workers/dispatcher/harvest-6way-r1278_sym24`

## Output

`workers/dispatcher/harvest-8way-r1279_sym24/round-1279/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

