# harvest-7way-r969 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R969 ctrl_bpc |
|--------|--------|--------------:|
| jKtf6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-470afc0b-jKtf6 | 2.6097 |
| cRZ3s | fork-slaa-us-mmllm-claude-train-sym24-5de83eb5-cRZ3s | 2.6204 |
| Ehlj2 | fork-slaa-us-mmllm-claude-train-sym24-1ee56901-Ehlj2 | 2.6375 |
| DUEAu | fork-joly-os-mmllm-claude-train-sym24-1def6b38-DUEAu | 2.8088 |
| rPNc0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4365229f-rPNc0 | 2.8113 |
| q5BRN | fork-joly-os-mmllm-claude-train-sym24-9355d113-q5BRN | 3.0015 |
| oOaOZ | origin/claude/train-sym24-86349f89-oOaOZ | 3.0137 |
| **mean** | | **2.7861** |
| **best** | | **2.6097** |

## Chain progression R968 → R969

Previous harvest: `workers/dispatcher/harvest-8way-r968_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6569         | 2.7861         | +0.1292 |
| ctrl_bpc best  | 2.6163         | 2.6097         | -0.0066 |

## Per-round trajectory (best bird: jKtf6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 969 | 5378 | 2.6097 | +0.1559 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r968_sym24`
  - `workers/dispatcher/harvest-8way-r968_sym24`

## Output

`workers/dispatcher/harvest-7way-r969_sym24/round-969/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

