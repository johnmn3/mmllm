# harvest-8way-r1294 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1294 ctrl_bpc |
|--------|--------|--------------:|
| R5hUB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e1ead402-R5hUB | 4.1198 |
| Ua88E | origin/claude/train-sym24-fb469d92-Ua88E | 4.1293 |
| KYXf8 | fork-joly-os-mmllm-claude-train-sym24-1f6b6e82-KYXf8 | 4.1761 |
| JFGQn | origin/claude/train-sym24-16f24b9c-JFGQn | 4.1880 |
| dJVR3 | fork-slaa-us-mmllm-claude-train-sym24-857c0c8b-dJVR3 | 4.2469 |
| 7LBW4 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8ae07177-7LBW4 | 4.2925 |
| 9s0Oa | fork-SeniorCareMarket-mmllm-claude-train-sym24-2ba56897-9s0Oa | 4.6125 |
| QfYIY | fork-joly-os-mmllm-claude-train-sym24-5edd9639-QfYIY | 4.7152 |
| **mean** | | **4.3100** |
| **best** | | **4.1198** |

## Chain progression R1293 → R1294

Previous harvest: `workers/dispatcher/harvest-5way-r1293_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.4242         | 4.3100         | -0.1142 |
| ctrl_bpc best  | 4.3090         | 4.1198         | -0.1892 |

## Per-round trajectory (best bird: R5hUB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1294 | 3888 | 4.1198 | +0.0207 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1293_sym24`
  - `workers/dispatcher/harvest-5way-r1293_sym24`

## Output

`workers/dispatcher/harvest-8way-r1294_sym24/round-1294/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

