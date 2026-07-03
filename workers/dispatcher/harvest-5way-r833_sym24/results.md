# harvest-5way-r833 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R833 ctrl_bpc |
|--------|--------|--------------:|
| kywsO | fork-slaa-us-mmllm-claude-train-sym24-a60e40b8-kywsO | 2.9734 |
| lNtgI | origin/claude/train-sym24-7a4c867d-lNtgI | 2.9739 |
| jXd9T | fork-joly-os-mmllm-claude-train-sym24-bf633eec-jXd9T | 2.9790 |
| l0CGj | fork-SeniorCareMarket-mmllm-claude-train-sym24-5240c9bf-l0CGj | 2.9856 |
| yJS6i | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-25ca5866-yJS6i | 2.9864 |
| **mean** | | **2.9797** |
| **best** | | **2.9734** |

## Chain progression R832 → R833

Previous harvest: `workers/dispatcher/harvest-5way-r832_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0149         | 2.9797         | -0.0352 |
| ctrl_bpc best  | 2.9736         | 2.9734         | -0.0002 |

## Per-round trajectory (best bird: kywsO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 833 | 6531 | 2.9734 | +0.4743 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r832_sym24`
  - `workers/dispatcher/harvest-5way-r832_sym24`

## Output

`workers/dispatcher/harvest-5way-r833_sym24/round-833/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

