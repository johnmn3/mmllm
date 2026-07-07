# harvest-2way-r864 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R864 ctrl_bpc |
|--------|--------|--------------:|
| 8fyxx | fork-SeniorCareMarket-mmllm-claude-train-sym24-a732ebc3-8fyxx | 2.9006 |
| zO5AB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f5374901-zO5AB | 3.2766 |
| **mean** | | **3.0886** |
| **best** | | **2.9006** |

## Chain progression R863 → R864

Previous harvest: `workers/dispatcher/harvest-4way-r863_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1735         | 3.0886         | -0.0849 |
| ctrl_bpc best  | 2.8813         | 2.9006         | +0.0193 |

## Per-round trajectory (best bird: 8fyxx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 864 | 6529 | 2.9006 | +0.3896 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r863_sym24`

## Output

`workers/dispatcher/harvest-2way-r864_sym24/round-864/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

