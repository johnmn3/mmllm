# harvest-5way-r850 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R850 ctrl_bpc |
|--------|--------|--------------:|
| fMApl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-360b98f4-fMApl | 2.9288 |
| QiDzE | fork-SeniorCareMarket-mmllm-claude-train-sym24-0a313c61-QiDzE | 2.9338 |
| hiX8o | fork-slaa-us-mmllm-claude-train-sym24-8b35f87a-hiX8o | 3.0720 |
| Z8rwG | origin/claude/train-sym24-778b2aa4-Z8rwG | 3.0741 |
| oURfM | fork-joly-os-mmllm-claude-train-sym24-875dde5e-oURfM | 3.3139 |
| **mean** | | **3.0645** |
| **best** | | **2.9288** |

## Chain progression R849 → R850

Previous harvest: `workers/dispatcher/harvest-8way-r849_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0439         | 3.0645         | +0.0206 |
| ctrl_bpc best  | 2.9266         | 2.9288         | +0.0022 |

## Per-round trajectory (best bird: fMApl)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 850 | 6599 | 2.9288 | +0.3945 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r849_sym24`

## Output

`workers/dispatcher/harvest-5way-r850_sym24/round-850/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

