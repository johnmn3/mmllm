# harvest-3way-r839 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R839 ctrl_bpc |
|--------|--------|--------------:|
| gpBK2 | fork-slaa-us-mmllm-claude-train-sym24-f69c06aa-gpBK2 | 2.9550 |
| BZayq | fork-SeniorCareMarket-mmllm-claude-train-sym24-e84a83b8-BZayq | 3.1156 |
| kSxTv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6c1eb161-kSxTv | 3.3301 |
| **mean** | | **3.1336** |
| **best** | | **2.9550** |

## Chain progression R838 → R839

Previous harvest: `workers/dispatcher/harvest-2way-r838_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2231         | 3.1336         | -0.0895 |
| ctrl_bpc best  | 3.1155         | 2.9550         | -0.1605 |

## Per-round trajectory (best bird: gpBK2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 839 | 4423 | 2.9550 | +0.3822 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r838_sym24`

## Output

`workers/dispatcher/harvest-3way-r839_sym24/round-839/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

