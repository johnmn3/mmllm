# harvest-4way-r1208 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1208 ctrl_bpc |
|--------|--------|--------------:|
| qQwIC | fork-slaa-us-mmllm-claude-train-sym24-91da294a-qQwIC | 2.2983 |
| WiyJa | fork-joly-os-mmllm-claude-train-sym24-b9b26ad5-WiyJa | 2.2996 |
| OOGIo | fork-SeniorCareMarket-mmllm-claude-train-sym24-df15e109-OOGIo | 2.3006 |
| MVTYp | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9c934801-MVTYp | 2.4698 |
| **mean** | | **2.3421** |
| **best** | | **2.2983** |

## Chain progression R1207 → R1208

Previous harvest: `workers/dispatcher/harvest-7way-r1207_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3656         | 2.3421         | -0.0235 |
| ctrl_bpc best  | 2.2754         | 2.2983         | +0.0229 |

## Per-round trajectory (best bird: qQwIC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1208 | 6374 | 2.2983 | +0.2414 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1207_sym24`

## Output

`workers/dispatcher/harvest-4way-r1208_sym24/round-1208/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

