# harvest-8way-r822 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R822 ctrl_bpc |
|--------|--------|--------------:|
| sShwU | origin/claude/train-sym24-5fc7aeda-sShwU | 3.0094 |
| vBaWf | fork-slaa-us-mmllm-claude-train-sym24-abcfa93d-vBaWf | 3.0094 |
| irlum | fork-slaa-us-mmllm-claude-train-sym24-71855994-irlum | 3.0105 |
| njcgN | origin/claude/train-sym24-2e9d560f-njcgN | 3.0276 |
| 3vjXG | fork-joly-os-mmllm-claude-train-sym24-b241db7c-3vjXG | 3.0374 |
| ZiXto | fork-joly-os-mmllm-claude-train-sym24-38937089-ZiXto | 3.0377 |
| hag3H | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-62404a76-hag3H | 3.1557 |
| Xo0HJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-699b2402-Xo0HJ | 3.1642 |
| **mean** | | **3.0565** |
| **best** | | **3.0094** |

## Chain progression R821 → R822

Previous harvest: `workers/dispatcher/harvest-7way-r821_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1806         | 3.0565         | -0.1241 |
| ctrl_bpc best  | 3.0212         | 3.0094         | -0.0118 |

## Per-round trajectory (best bird: sShwU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 822 | 6590 | 3.0094 | +0.4788 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r821_sym24`
  - `workers/dispatcher/harvest-7way-r821_sym24`

## Output

`workers/dispatcher/harvest-8way-r822_sym24/round-822/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

