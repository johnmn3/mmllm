# harvest-4way-r1275 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1275 ctrl_bpc |
|--------|--------|--------------:|
| H4OSO | fork-joly-os-mmllm-claude-train-sym24-51e43a72-H4OSO | 2.2257 |
| 3jdme | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-05498bfe-3jdme | 2.4165 |
| LwaQU | fork-SeniorCareMarket-mmllm-claude-train-sym24-4ba0afb1-LwaQU | 2.4178 |
| RaDr9 | origin/claude/train-sym24-c4a6fe69-RaDr9 | 2.6245 |
| **mean** | | **2.4211** |
| **best** | | **2.2257** |

## Chain progression R1274 → R1275

Previous harvest: `workers/dispatcher/harvest-1way-r1274_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6283         | 2.4211         | -0.2072 |
| ctrl_bpc best  | 2.6283         | 2.2257         | -0.4026 |

## Per-round trajectory (best bird: H4OSO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1275 | 5478 | 2.2257 | +0.2598 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1274_sym24`

## Output

`workers/dispatcher/harvest-4way-r1275_sym24/round-1275/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

