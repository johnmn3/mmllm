# harvest-5way-r817 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R817 ctrl_bpc |
|--------|--------|--------------:|
| dsLbd | fork-slaa-us-mmllm-claude-train-sym24-fb8e3481-dsLbd | 3.0390 |
| 9J1M8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4062da4a-9J1M8 | 3.0497 |
| vIsMw | fork-joly-os-mmllm-claude-train-sym24-3da4ee48-vIsMw | 3.1651 |
| JQboN | fork-davidwuchn-mmllm-claude-train-sym24-d9706dd3-JQboN | 3.3926 |
| 6bN70 | origin/claude/train-sym24-acb6e1b9-6bN70 | 3.3972 |
| **mean** | | **3.2087** |
| **best** | | **3.0390** |

## Chain progression R816 → R817

Previous harvest: `workers/dispatcher/harvest-8way-r816_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1529         | 3.2087         | +0.0558 |
| ctrl_bpc best  | 3.0290         | 3.0390         | +0.0100 |

## Per-round trajectory (best bird: dsLbd)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 817 | 4347 | 3.0390 | +0.7261 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r816_sym24`

## Output

`workers/dispatcher/harvest-5way-r817_sym24/round-817/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

