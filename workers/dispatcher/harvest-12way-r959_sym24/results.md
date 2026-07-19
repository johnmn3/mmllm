# harvest-12way-r959 — sparse-delta merge of 12 birds

## Worker endpoints

| handle | branch | R959 ctrl_bpc |
|--------|--------|--------------:|
| 1CCwK | fork-slaa-us-mmllm-claude-train-sym24-dfed33f8-1CCwK | 2.6287 |
| nRXeZ | origin/claude/train-sym24-e83ecfaf-nRXeZ | 2.6351 |
| HyyCm | fork-joly-os-mmllm-claude-train-sym24-4bc0f81d-HyyCm | 2.6484 |
| 7isKs | fork-slaa-us-mmllm-claude-train-sym24-05dad6cf-7isKs | 2.6486 |
| QKCRp | fork-SeniorCareMarket-mmllm-claude-train-sym24-cbfb81db-QKCRp | 2.6522 |
| 3hK5f | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-83651f51-3hK5f | 2.6617 |
| ctS43 | fork-SeniorCareMarket-mmllm-claude-train-sym24-2a525e76-ctS43 | 2.6787 |
| ZkXZZ | origin/claude/train-sym24-e881a926-ZkXZZ | 2.8282 |
| ZfoW9 | origin/claude/train-sym24-8c4f4ac8-ZfoW9 | 2.8385 |
| 5Zk0K | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0837e308-5Zk0K | 2.8412 |
| qVwOc | fork-joly-os-mmllm-claude-train-sym24-38f7dec2-qVwOc | 2.8566 |
| 0eUFt | fork-joly-os-mmllm-claude-train-sym24-2607ec68-0eUFt | 2.8881 |
| **mean** | | **2.7338** |
| **best** | | **2.6287** |

## Chain progression R958 → R959

Previous harvest: `workers/dispatcher/harvest-9way-r958_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7706         | 2.7338         | -0.0368 |
| ctrl_bpc best  | 2.6279         | 2.6287         | +0.0008 |

## Per-round trajectory (best bird: 1CCwK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 959 | 6458 | 2.6287 | +0.1724 |

## Cumulative training contribution

- This harvest: **960 steps** from 12 bird(s)
- Across full ancestry (deduped by bird_id): **1680 steps** from 21 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r958_sym24`
  - `workers/dispatcher/harvest-7way-r958_sym24`
  - `workers/dispatcher/harvest-9way-r958_sym24`

## Output

`workers/dispatcher/harvest-12way-r959_sym24/round-959/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 12 workers)
- `dense.pt` (averaged across 12 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

