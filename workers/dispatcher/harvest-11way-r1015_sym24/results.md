# harvest-11way-r1015 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1015 ctrl_bpc |
|--------|--------|--------------:|
| qElNF | fork-SeniorCareMarket-mmllm-claude-train-sym24-5b5e5e21-qElNF | 2.5366 |
| iyxOV | origin/claude/train-sym24-500669d1-iyxOV | 2.5369 |
| qon2C | fork-slaa-us-mmllm-claude-train-sym24-2a39118e-qon2C | 2.5477 |
| WZzvq | fork-joly-os-mmllm-claude-train-sym24-ee9c132d-WZzvq | 2.5538 |
| KrIeY | fork-joly-os-mmllm-claude-train-sym24-2d7afce3-KrIeY | 2.7282 |
| YVvDC | fork-SeniorCareMarket-mmllm-claude-train-sym24-43d0f22f-YVvDC | 2.7441 |
| HGwOO | origin/claude/train-sym24-38570c75-HGwOO | 2.7449 |
| D44s1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1c1e3b63-D44s1 | 2.9068 |
| DuAwJ | origin/claude/train-sym24-a541256f-DuAwJ | 2.9175 |
| 6eG0h | fork-slaa-us-mmllm-claude-train-sym24-4b2e0e2d-6eG0h | 2.9247 |
| J5FT8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c3f3a6a1-J5FT8 | 2.9269 |
| **mean** | | **2.7335** |
| **best** | | **2.5366** |

## Chain progression R1014 → R1015

Previous harvest: `workers/dispatcher/harvest-9way-r1014_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6681         | 2.7335         | +0.0654 |
| ctrl_bpc best  | 2.5271         | 2.5366         | +0.0095 |

## Per-round trajectory (best bird: qElNF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1015 | 6387 | 2.5366 | +0.1740 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1600 steps** from 20 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1014_sym24`
  - `workers/dispatcher/harvest-7way-r1014_sym24`
  - `workers/dispatcher/harvest-9way-r1014_sym24`

## Output

`workers/dispatcher/harvest-11way-r1015_sym24/round-1015/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

