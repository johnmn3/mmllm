# harvest-6way-r1161 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1161 ctrl_bpc |
|--------|--------|--------------:|
| su9hL | origin/claude/train-sym24-f15b4c55-su9hL | 2.3258 |
| r3fWG | fork-slaa-us-mmllm-claude-train-sym24-675682d0-r3fWG | 2.5432 |
| KURQD | fork-joly-os-mmllm-claude-train-sym24-1ac4cf27-KURQD | 2.7106 |
| hrWnR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2ed0a2fb-hrWnR | 2.7117 |
| AEph4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-6fdd7926-AEph4 | 2.7122 |
| 3e3KG | origin/claude/train-sym24-255bdfe2-3e3KG | 2.7159 |
| **mean** | | **2.6199** |
| **best** | | **2.3258** |

## Chain progression R1160 → R1161

Previous harvest: `workers/dispatcher/harvest-2way-r1160_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3430         | 2.6199         | +0.2769 |
| ctrl_bpc best  | 2.3301         | 2.3258         | -0.0043 |

## Per-round trajectory (best bird: su9hL)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1161 | 4015 | 2.3258 | +0.2599 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1160_sym24`
  - `workers/dispatcher/harvest-2way-r1160_sym24`

## Output

`workers/dispatcher/harvest-6way-r1161_sym24/round-1161/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

