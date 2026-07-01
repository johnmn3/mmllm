# harvest-7way-r817 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R817 ctrl_bpc |
|--------|--------|--------------:|
| z9MPs | fork-davidwuchn-mmllm-claude-train-sym24-b4a2f3e9-z9MPs | 3.0375 |
| dsLbd | fork-slaa-us-mmllm-claude-train-sym24-fb8e3481-dsLbd | 3.0390 |
| 9J1M8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4062da4a-9J1M8 | 3.0497 |
| vIsMw | fork-joly-os-mmllm-claude-train-sym24-3da4ee48-vIsMw | 3.1651 |
| Vy9Nk | fork-joly-os-mmllm-claude-train-sym24-b7098593-Vy9Nk | 3.1748 |
| JQboN | fork-davidwuchn-mmllm-claude-train-sym24-d9706dd3-JQboN | 3.3926 |
| 6bN70 | origin/claude/train-sym24-acb6e1b9-6bN70 | 3.3972 |
| **mean** | | **3.1794** |
| **best** | | **3.0375** |

## Chain progression R816 → R817

Previous harvest: `workers/dispatcher/harvest-8way-r816_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1529         | 3.1794         | +0.0265 |
| ctrl_bpc best  | 3.0290         | 3.0375         | +0.0085 |

## Per-round trajectory (best bird: z9MPs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 817 | 4294 | 3.0375 | +0.5288 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r816_sym24`
  - `workers/dispatcher/harvest-8way-r816_sym24`

## Output

`workers/dispatcher/harvest-7way-r817_sym24/round-817/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

