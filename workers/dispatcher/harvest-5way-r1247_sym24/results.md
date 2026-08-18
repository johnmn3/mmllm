# harvest-5way-r1247 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1247 ctrl_bpc |
|--------|--------|--------------:|
| oS8zU | fork-SeniorCareMarket-mmllm-claude-train-sym24-0f53202c-oS8zU | 2.2403 |
| 5AhYh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-43a4e260-5AhYh | 2.2477 |
| CyCjV | fork-SeniorCareMarket-mmllm-claude-train-sym24-3d681a22-CyCjV | 2.2693 |
| lnZls | fork-joly-os-mmllm-claude-train-sym24-68947a25-lnZls | 2.4469 |
| Yb2T4 | fork-slaa-us-mmllm-claude-train-sym24-c94bd7fb-Yb2T4 | 2.4517 |
| **mean** | | **2.3312** |
| **best** | | **2.2403** |

## Chain progression R1246 → R1247

Previous harvest: `workers/dispatcher/harvest-9way-r1246_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4063         | 2.3312         | -0.0751 |
| ctrl_bpc best  | 2.2411         | 2.2403         | -0.0008 |

## Per-round trajectory (best bird: oS8zU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1247 | 4092 | 2.2403 | +0.2585 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1246_sym24`
  - `workers/dispatcher/harvest-4way-r1246_sym24`

## Output

`workers/dispatcher/harvest-5way-r1247_sym24/round-1247/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

