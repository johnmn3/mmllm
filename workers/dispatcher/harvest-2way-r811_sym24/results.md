# harvest-2way-r811 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R811 ctrl_bpc |
|--------|--------|--------------:|
| 8rCvI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9704444d-8rCvI | 3.0762 |
| qjVcV | fork-slaa-us-mmllm-claude-train-sym24-d755ca3e-qjVcV | 3.1926 |
| **mean** | | **3.1344** |
| **best** | | **3.0762** |

## Chain progression R810 → R811

Previous harvest: `workers/dispatcher/harvest-6way-r810_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3400         | 3.1344         | -0.2056 |
| ctrl_bpc best  | 3.0707         | 3.0762         | +0.0055 |

## Per-round trajectory (best bird: 8rCvI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 811 | 6367 | 3.0762 | +0.6245 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r810_sym24`

## Output

`workers/dispatcher/harvest-2way-r811_sym24/round-811/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

