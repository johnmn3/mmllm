# harvest-6way-r883 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R883 ctrl_bpc |
|--------|--------|--------------:|
| fYGg0 | fork-joly-os-mmllm-claude-train-sym24-e9a6c63d-fYGg0 | 2.8263 |
| jIptE | fork-SeniorCareMarket-mmllm-claude-train-sym24-88d6781d-jIptE | 2.8424 |
| boyvd | origin/claude/train-sym24-8b197ddb-boyvd | 2.8438 |
| hsC0V | fork-slaa-us-mmllm-claude-train-sym24-c50ab6d0-hsC0V | 3.0008 |
| woiLs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-dacd769c-woiLs | 3.0106 |
| FQpV4 | origin/claude/train-sym24-a33ce591-FQpV4 | 3.2077 |
| **mean** | | **2.9553** |
| **best** | | **2.8263** |

## Chain progression R882 → R883

Previous harvest: `workers/dispatcher/harvest-6way-r882_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0299         | 2.9553         | -0.0746 |
| ctrl_bpc best  | 2.8336         | 2.8263         | -0.0073 |

## Per-round trajectory (best bird: fYGg0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 883 | 6567 | 2.8263 | +0.3879 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r882_sym24`
  - `workers/dispatcher/harvest-5way-r882_sym24`

## Output

`workers/dispatcher/harvest-6way-r883_sym24/round-883/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

