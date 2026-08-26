# harvest-6way-r1327 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1327 ctrl_bpc |
|--------|--------|--------------:|
| kxuMG | fork-slaa-us-mmllm-claude-train-sym24-7afd615a-kxuMG | 3.3393 |
| ALHtF | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-749ec95c-ALHtF | 3.3519 |
| 2bOqV | fork-SeniorCareMarket-mmllm-claude-train-sym24-99759eb6-2bOqV | 3.3569 |
| ojVxS | fork-joly-os-mmllm-claude-train-sym24-d9446a15-ojVxS | 3.3823 |
| cqli7 | fork-joly-os-mmllm-claude-train-sym24-ccee9ea8-cqli7 | 3.3877 |
| c21SV | fork-SeniorCareMarket-mmllm-claude-train-sym24-3b804734-c21SV | 3.6882 |
| **mean** | | **3.4177** |
| **best** | | **3.3393** |

## Chain progression R1326 → R1327

Previous harvest: `workers/dispatcher/harvest-7way-r1326_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4238         | 3.4177         | -0.0061 |
| ctrl_bpc best  | 3.3055         | 3.3393         | +0.0338 |

## Per-round trajectory (best bird: kxuMG)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1327 | 6424 | 3.3393 | +0.0814 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1326_sym24`
  - `workers/dispatcher/harvest-7way-r1326_sym24`

## Output

`workers/dispatcher/harvest-6way-r1327_sym24/round-1327/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

