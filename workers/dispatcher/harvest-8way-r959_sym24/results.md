# harvest-8way-r959 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R959 ctrl_bpc |
|--------|--------|--------------:|
| 1CCwK | fork-slaa-us-mmllm-claude-train-sym24-dfed33f8-1CCwK | 2.6287 |
| nRXeZ | origin/claude/train-sym24-e83ecfaf-nRXeZ | 2.6351 |
| HyyCm | fork-joly-os-mmllm-claude-train-sym24-4bc0f81d-HyyCm | 2.6484 |
| 7isKs | fork-slaa-us-mmllm-claude-train-sym24-05dad6cf-7isKs | 2.6486 |
| QKCRp | fork-SeniorCareMarket-mmllm-claude-train-sym24-cbfb81db-QKCRp | 2.6522 |
| ZfoW9 | origin/claude/train-sym24-8c4f4ac8-ZfoW9 | 2.8385 |
| 5Zk0K | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0837e308-5Zk0K | 2.8412 |
| qVwOc | fork-joly-os-mmllm-claude-train-sym24-38f7dec2-qVwOc | 2.8566 |
| **mean** | | **2.7187** |
| **best** | | **2.6287** |

## Chain progression R958 → R959

Previous harvest: `workers/dispatcher/harvest-9way-r958_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7706         | 2.7187         | -0.0519 |
| ctrl_bpc best  | 2.6279         | 2.6287         | +0.0008 |

## Per-round trajectory (best bird: 1CCwK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 959 | 6458 | 2.6287 | +0.1724 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r958_sym24`
  - `workers/dispatcher/harvest-7way-r958_sym24`

## Output

`workers/dispatcher/harvest-8way-r959_sym24/round-959/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

