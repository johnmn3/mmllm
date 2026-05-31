# harvest-5way-r108 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R108 ctrl_bpc |
|--------|--------|--------------:|
| tj16P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6de7cc17-tj16P | 3.1325 |
| EG78U | fork-slaa-us-mmllm-claude-train-sym24-36a5da84-EG78U | 3.1519 |
| 73IUZ | fork-davidwuchn-mmllm-claude-train-sym24-175e4bc8-73IUZ | 3.2074 |
| gCuzK | fork-joly-os-mmllm-claude-train-sym24-6ca1ebe5-gCuzK | 3.2229 |
| x0Hrd | origin/claude/train-sym24-2cddaa2e-x0Hrd | 3.2429 |
| **mean** | | **3.1915** |
| **best** | | **3.1325** |

## Per-round trajectory (best bird: tj16P)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 107 | 1194 | 3.2827 | +0.0035 |
| 108 | 1255 | 3.1325 | +0.0442 |

## Cumulative training contribution

- This harvest: **100 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **100 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r106_sym24`

## Output

`workers/dispatcher/harvest-5way-r108_sym24/round-108/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

