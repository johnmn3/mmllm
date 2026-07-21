# harvest-8way-r978 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R978 ctrl_bpc |
|--------|--------|--------------:|
| nBbXE | fork-joly-os-mmllm-claude-train-sym24-f9e0b953-nBbXE | 2.6021 |
| pdjip | fork-slaa-us-mmllm-claude-train-sym24-ff8ecfcd-pdjip | 2.6099 |
| lrdGs | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5b6815e6-lrdGs | 2.6284 |
| uL3Oz | origin/claude/train-sym24-8a3f16f9-uL3Oz | 2.6382 |
| QM0Nq | origin/claude/train-sym24-2606bb66-QM0Nq | 2.6408 |
| uupMm | fork-joly-os-mmllm-claude-train-sym24-8f5d305c-uupMm | 2.7877 |
| ZdtN6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-80c47f69-ZdtN6 | 2.9831 |
| VeZRB | fork-joly-os-mmllm-claude-train-sym24-3101e8b2-VeZRB | 3.0091 |
| **mean** | | **2.7374** |
| **best** | | **2.6021** |

## Chain progression R977 → R978

Previous harvest: `workers/dispatcher/harvest-7way-r977_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7526         | 2.7374         | -0.0152 |
| ctrl_bpc best  | 2.6082         | 2.6021         | -0.0061 |

## Per-round trajectory (best bird: nBbXE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 978 | 6345 | 2.6021 | +0.2062 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r977_sym24`
  - `workers/dispatcher/harvest-4way-r977_sym24`
  - `workers/dispatcher/harvest-7way-r977_sym24`

## Output

`workers/dispatcher/harvest-8way-r978_sym24/round-978/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

