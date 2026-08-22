# harvest-6way-r1281 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1281 ctrl_bpc |
|--------|--------|--------------:|
| NkBMd | fork-joly-os-mmllm-claude-train-sym24-ca8ded60-NkBMd | 2.2222 |
| UubWV | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0434509e-UubWV | 2.2321 |
| NXHAi | origin/claude/train-sym24-f7a8a085-NXHAi | 2.2454 |
| NoWDU | fork-slaa-us-mmllm-claude-train-sym24-48e92006-NoWDU | 2.2524 |
| 78h9s | fork-SeniorCareMarket-mmllm-claude-train-sym24-d4cb3fc0-78h9s | 2.4079 |
| I9ymC | origin/claude/train-sym24-20f9411c-I9ymC | 2.4134 |
| **mean** | | **2.2956** |
| **best** | | **2.2222** |

## Chain progression R1280 → R1281

Previous harvest: `workers/dispatcher/harvest-7way-r1280_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4255         | 2.2956         | -0.1299 |
| ctrl_bpc best  | 2.2204         | 2.2222         | +0.0018 |

## Per-round trajectory (best bird: NkBMd)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1281 | 6638 | 2.2222 | +0.2564 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1280_sym24`
  - `workers/dispatcher/harvest-5way-r1280_sym24`

## Output

`workers/dispatcher/harvest-6way-r1281_sym24/round-1281/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

