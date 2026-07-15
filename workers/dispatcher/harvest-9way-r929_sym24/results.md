# harvest-9way-r929 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R929 ctrl_bpc |
|--------|--------|--------------:|
| DTYFp | origin/claude/train-sym24-b0613a9e-DTYFp | 2.7103 |
| Degk4 | origin/claude/train-sym24-f8aecbce-Degk4 | 2.7160 |
| H9LWl | fork-slaa-us-mmllm-claude-train-sym24-dda8e4e6-H9LWl | 2.7167 |
| tAH84 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f9edd9c4-tAH84 | 2.7206 |
| sHdiS | origin/claude/train-sym24-dba955ab-sHdiS | 2.7208 |
| mljxZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9754fc96-mljxZ | 2.9008 |
| Wt0r8 | fork-joly-os-mmllm-claude-train-sym24-0ea448ea-Wt0r8 | 3.0978 |
| t3TA7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-48171657-t3TA7 | 3.1070 |
| xR3jT | fork-slaa-us-mmllm-claude-train-sym24-bce79df5-xR3jT | 3.1284 |
| **mean** | | **2.8687** |
| **best** | | **2.7103** |

## Chain progression R928 → R929

Previous harvest: `workers/dispatcher/harvest-4way-r928_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8260         | 2.8687         | +0.0427 |
| ctrl_bpc best  | 2.7143         | 2.7103         | -0.0040 |

## Per-round trajectory (best bird: DTYFp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 929 | 6841 | 2.7103 | +0.2112 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r928_sym24`

## Output

`workers/dispatcher/harvest-9way-r929_sym24/round-929/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

