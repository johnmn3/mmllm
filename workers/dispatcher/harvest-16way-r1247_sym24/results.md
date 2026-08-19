# harvest-16way-r1247 — sparse-delta merge of 16 birds

## Worker endpoints

| handle | branch | R1247 ctrl_bpc |
|--------|--------|--------------:|
| oS8zU | fork-SeniorCareMarket-mmllm-claude-train-sym24-0f53202c-oS8zU | 2.2403 |
| 5AhYh | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-43a4e260-5AhYh | 2.2477 |
| 9Kyqh | fork-joly-os-mmllm-claude-train-sym24-2202c323-9Kyqh | 2.2499 |
| 7kclb | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8c202c54-7kclb | 2.2530 |
| flv6z | fork-SeniorCareMarket-mmllm-claude-train-sym24-f99ca8f9-flv6z | 2.2533 |
| LcC2I | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-584bb226-LcC2I | 2.2618 |
| u2Ruy | fork-joly-os-mmllm-claude-train-sym24-1f4953e5-u2Ruy | 2.2633 |
| sx7V0 | origin/claude/train-sym24-36776118-sx7V0 | 2.2654 |
| ZEpMa | origin/claude/train-sym24-ea339ccc-ZEpMa | 2.2681 |
| CyCjV | fork-SeniorCareMarket-mmllm-claude-train-sym24-3d681a22-CyCjV | 2.2693 |
| 7gJlf | origin/claude/train-sym24-e5b64b3a-7gJlf | 2.4443 |
| lnZls | fork-joly-os-mmllm-claude-train-sym24-68947a25-lnZls | 2.4469 |
| Yb2T4 | fork-slaa-us-mmllm-claude-train-sym24-c94bd7fb-Yb2T4 | 2.4517 |
| 8mDrI | fork-joly-os-mmllm-claude-train-sym24-24d4b2aa-8mDrI | 2.6346 |
| Cc9Ns | fork-slaa-us-mmllm-claude-train-sym24-9c245fdf-Cc9Ns | 2.6363 |
| Y1o14 | fork-slaa-us-mmllm-claude-train-sym24-0893bd2f-Y1o14 | 2.6436 |
| **mean** | | **2.3643** |
| **best** | | **2.2403** |

## Chain progression R1246 → R1247

Previous harvest: `workers/dispatcher/harvest-9way-r1246_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4063         | 2.3643         | -0.0420 |
| ctrl_bpc best  | 2.2411         | 2.2403         | -0.0008 |

## Per-round trajectory (best bird: oS8zU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1247 | 4092 | 2.2403 | +0.2585 |

## Cumulative training contribution

- This harvest: **1280 steps** from 16 bird(s)
- Across full ancestry (deduped by bird_id): **2000 steps** from 25 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1246_sym24`
  - `workers/dispatcher/harvest-4way-r1246_sym24`
  - `workers/dispatcher/harvest-9way-r1246_sym24`

## Output

`workers/dispatcher/harvest-16way-r1247_sym24/round-1247/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 16 workers)
- `dense.pt` (averaged across 16 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

