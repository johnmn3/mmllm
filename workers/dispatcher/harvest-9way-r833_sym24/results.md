# harvest-9way-r833 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R833 ctrl_bpc |
|--------|--------|--------------:|
| l7bhP | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b5b8460d-l7bhP | 2.9703 |
| kywsO | fork-slaa-us-mmllm-claude-train-sym24-a60e40b8-kywsO | 2.9734 |
| lNtgI | origin/claude/train-sym24-7a4c867d-lNtgI | 2.9739 |
| jXd9T | fork-joly-os-mmllm-claude-train-sym24-bf633eec-jXd9T | 2.9790 |
| l0CGj | fork-SeniorCareMarket-mmllm-claude-train-sym24-5240c9bf-l0CGj | 2.9856 |
| yJS6i | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-25ca5866-yJS6i | 2.9864 |
| 4Mwhg | fork-joly-os-mmllm-claude-train-sym24-8d96fc28-4Mwhg | 3.1257 |
| EkYQk | fork-slaa-us-mmllm-claude-train-sym24-9ac56da9-EkYQk | 3.3545 |
| uEztS | fork-SeniorCareMarket-mmllm-claude-train-sym24-21e5bc36-uEztS | 3.3581 |
| **mean** | | **3.0785** |
| **best** | | **2.9703** |

## Chain progression R832 → R833

Previous harvest: `workers/dispatcher/harvest-5way-r832_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0149         | 3.0785         | +0.0636 |
| ctrl_bpc best  | 2.9736         | 2.9703         | -0.0033 |

## Per-round trajectory (best bird: l7bhP)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 833 | 6661 | 2.9703 | +0.5086 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r832_sym24`
  - `workers/dispatcher/harvest-5way-r832_sym24`

## Output

`workers/dispatcher/harvest-9way-r833_sym24/round-833/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

