# harvest-6way-r811 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R811 ctrl_bpc |
|--------|--------|--------------:|
| 8rCvI | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9704444d-8rCvI | 3.0762 |
| POCD1 | origin/claude/train-sym24-3b7a6647-POCD1 | 3.0938 |
| qjVcV | fork-slaa-us-mmllm-claude-train-sym24-d755ca3e-qjVcV | 3.1926 |
| WXi2V | origin/claude/train-sym24-52787350-WXi2V | 3.1947 |
| LMZDG | fork-slaa-us-mmllm-claude-train-sym24-ccbf167c-LMZDG | 3.4336 |
| 7jUDl | fork-joly-os-mmllm-claude-train-sym24-da6b23ed-7jUDl | 3.4355 |
| **mean** | | **3.2377** |
| **best** | | **3.0762** |

## Chain progression R810 → R811

Previous harvest: `workers/dispatcher/harvest-6way-r810_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3400         | 3.2377         | -0.1023 |
| ctrl_bpc best  | 3.0707         | 3.0762         | +0.0055 |

## Per-round trajectory (best bird: 8rCvI)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 811 | 6367 | 3.0762 | +0.6245 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r810_sym24`

## Output

`workers/dispatcher/harvest-6way-r811_sym24/round-811/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

