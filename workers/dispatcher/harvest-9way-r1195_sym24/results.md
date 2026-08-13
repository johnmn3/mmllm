# harvest-9way-r1195 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1195 ctrl_bpc |
|--------|--------|--------------:|
| SB2fy | fork-SeniorCareMarket-mmllm-claude-train-sym24-f340e308-SB2fy | 2.2812 |
| KmHG8 | fork-SeniorCareMarket-mmllm-claude-train-sym24-0c4e6757-KmHG8 | 2.3101 |
| lv9l9 | fork-slaa-us-mmllm-claude-train-sym24-cc8311ff-lv9l9 | 2.3109 |
| ohyXu | fork-joly-os-mmllm-claude-train-sym24-485fabeb-ohyXu | 2.4850 |
| CG5Eq | origin/claude/train-sym24-d6fda9c3-CG5Eq | 2.4963 |
| w0CwU | fork-joly-os-mmllm-claude-train-sym24-a0cc208c-w0CwU | 2.5222 |
| 0IRXW | fork-slaa-us-mmllm-claude-train-sym24-ecc2e52a-0IRXW | 2.6841 |
| PceKA | origin/claude/train-sym24-0d8534db-PceKA | 2.6899 |
| 4sEJj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6cce72de-4sEJj | 2.6967 |
| **mean** | | **2.4974** |
| **best** | | **2.2812** |

## Chain progression R1194 → R1195

Previous harvest: `workers/dispatcher/harvest-6way-r1194_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3659         | 2.4974         | +0.1315 |
| ctrl_bpc best  | 2.2894         | 2.2812         | -0.0082 |

## Per-round trajectory (best bird: SB2fy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1195 | 6682 | 2.2812 | +0.2635 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1194_sym24`
  - `workers/dispatcher/harvest-6way-r1194_sym24`

## Output

`workers/dispatcher/harvest-9way-r1195_sym24/round-1195/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

