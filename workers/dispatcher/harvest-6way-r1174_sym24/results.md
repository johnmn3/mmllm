# harvest-6way-r1174 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1174 ctrl_bpc |
|--------|--------|--------------:|
| L0kvo | fork-joly-os-mmllm-claude-train-sym24-b8047900-L0kvo | 2.3127 |
| Eux55 | fork-SeniorCareMarket-mmllm-claude-train-sym24-bbfe9132-Eux55 | 2.3175 |
| lWGwa | origin/claude/train-sym24-85ab2f3b-lWGwa | 2.3182 |
| HkfZU | fork-slaa-us-mmllm-claude-train-sym24-f58c7496-HkfZU | 2.5111 |
| FbNLK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0f7e2d95-FbNLK | 2.7002 |
| KNufS | origin/claude/train-sym24-c49aeae1-KNufS | 2.7278 |
| **mean** | | **2.4812** |
| **best** | | **2.3127** |

## Chain progression R1173 → R1174

Previous harvest: `workers/dispatcher/harvest-9way-r1173_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4954         | 2.4812         | -0.0142 |
| ctrl_bpc best  | 2.3085         | 2.3127         | +0.0042 |

## Per-round trajectory (best bird: L0kvo)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1174 | 6512 | 2.3127 | +0.2672 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r1173_sym24`
  - `workers/dispatcher/harvest-9way-r1173_sym24`

## Output

`workers/dispatcher/harvest-6way-r1174_sym24/round-1174/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

