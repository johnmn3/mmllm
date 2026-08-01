# harvest-6way-r1083 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1083 ctrl_bpc |
|--------|--------|--------------:|
| jUZL2 | origin/claude/train-sym24-fc0aa01c-jUZL2 | 2.4253 |
| 9wcWH | origin/claude/train-sym24-6a6700d1-9wcWH | 2.4255 |
| XOVto | fork-slaa-us-mmllm-claude-train-sym24-2c7ac406-XOVto | 2.4458 |
| P7UqY | fork-joly-os-mmllm-claude-train-sym24-1c03dd11-P7UqY | 2.4498 |
| aRtOn | fork-SeniorCareMarket-mmllm-claude-train-sym24-eebd6ba6-aRtOn | 2.6000 |
| 09mXH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f5f504ce-09mXH | 2.6041 |
| **mean** | | **2.4918** |
| **best** | | **2.4253** |

## Chain progression R1082 → R1083

Previous harvest: `workers/dispatcher/harvest-4way-r1082_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6199         | 2.4918         | -0.1281 |
| ctrl_bpc best  | 2.4308         | 2.4253         | -0.0055 |

## Per-round trajectory (best bird: jUZL2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1083 | 6605 | 2.4253 | +0.2360 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1082_sym24`
  - `workers/dispatcher/harvest-4way-r1082_sym24`

## Output

`workers/dispatcher/harvest-6way-r1083_sym24/round-1083/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

