# harvest-5way-r1275 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1275 ctrl_bpc |
|--------|--------|--------------:|
| H4OSO | fork-joly-os-mmllm-claude-train-sym24-51e43a72-H4OSO | 2.2257 |
| XYLu6 | fork-slaa-us-mmllm-claude-train-sym24-64f3e50d-XYLu6 | 2.4106 |
| 3jdme | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-05498bfe-3jdme | 2.4165 |
| LwaQU | fork-SeniorCareMarket-mmllm-claude-train-sym24-4ba0afb1-LwaQU | 2.4178 |
| RaDr9 | origin/claude/train-sym24-c4a6fe69-RaDr9 | 2.6245 |
| **mean** | | **2.4190** |
| **best** | | **2.2257** |

## Chain progression R1274 → R1275

Previous harvest: `workers/dispatcher/harvest-1way-r1274_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6283         | 2.4190         | -0.2093 |
| ctrl_bpc best  | 2.6283         | 2.2257         | -0.4026 |

## Per-round trajectory (best bird: H4OSO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1275 | 5478 | 2.2257 | +0.2598 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1274_sym24`

## Output

`workers/dispatcher/harvest-5way-r1275_sym24/round-1275/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

