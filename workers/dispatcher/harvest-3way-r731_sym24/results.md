# harvest-3way-r731 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R731 ctrl_bpc |
|--------|--------|--------------:|
| BYQQ3 | fork-slaa-us-mmllm-claude-train-sym24-43f9cc78-BYQQ3 | 3.5010 |
| dsjDl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-079b7b67-dsjDl | 3.7991 |
| C911m | fork-davidwuchn-mmllm-claude-train-sym24-01258871-C911m | 3.8195 |
| **mean** | | **3.7065** |
| **best** | | **3.5010** |

## Chain progression R730 → R731

Previous harvest: `workers/dispatcher/harvest-6way-r730_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5244         | 3.7065         | +0.1821 |
| ctrl_bpc best  | 3.4270         | 3.5010         | +0.0740 |

## Per-round trajectory (best bird: BYQQ3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 731 | 5633 | 3.5010 | +0.8121 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r730_sym24`

## Output

`workers/dispatcher/harvest-3way-r731_sym24/round-731/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

