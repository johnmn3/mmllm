# harvest-4way-r1164 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1164 ctrl_bpc |
|--------|--------|--------------:|
| cdCUj | fork-slaa-us-mmllm-claude-train-sym24-5644727c-cdCUj | 2.3205 |
| iQ7C3 | fork-joly-os-mmllm-claude-train-sym24-bf2931d9-iQ7C3 | 2.3210 |
| u5aHB | fork-SeniorCareMarket-mmllm-claude-train-sym24-369ab108-u5aHB | 2.5284 |
| OoaiN | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-97e42b5a-OoaiN | 2.7199 |
| **mean** | | **2.4724** |
| **best** | | **2.3205** |

## Chain progression R1163 → R1164

Previous harvest: `workers/dispatcher/harvest-11way-r1163_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4592         | 2.4724         | +0.0132 |
| ctrl_bpc best  | 2.3178         | 2.3205         | +0.0027 |

## Per-round trajectory (best bird: cdCUj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1164 | 6674 | 2.3205 | +0.2695 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1163_sym24`

## Output

`workers/dispatcher/harvest-4way-r1164_sym24/round-1164/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

