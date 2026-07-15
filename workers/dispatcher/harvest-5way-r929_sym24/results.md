# harvest-5way-r929 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R929 ctrl_bpc |
|--------|--------|--------------:|
| Degk4 | origin/claude/train-sym24-f8aecbce-Degk4 | 2.7160 |
| H9LWl | fork-slaa-us-mmllm-claude-train-sym24-dda8e4e6-H9LWl | 2.7167 |
| mljxZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9754fc96-mljxZ | 2.9008 |
| Wt0r8 | fork-joly-os-mmllm-claude-train-sym24-0ea448ea-Wt0r8 | 3.0978 |
| t3TA7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-48171657-t3TA7 | 3.1070 |
| **mean** | | **2.9077** |
| **best** | | **2.7160** |

## Chain progression R928 → R929

Previous harvest: `workers/dispatcher/harvest-4way-r928_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8260         | 2.9077         | +0.0817 |
| ctrl_bpc best  | 2.7143         | 2.7160         | +0.0017 |

## Per-round trajectory (best bird: Degk4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 929 | 6783 | 2.7160 | +0.1529 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r928_sym24`

## Output

`workers/dispatcher/harvest-5way-r929_sym24/round-929/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

