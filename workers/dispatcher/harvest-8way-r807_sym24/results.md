# harvest-8way-r807 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R807 ctrl_bpc |
|--------|--------|--------------:|
| wTzBO | fork-slaa-us-mmllm-claude-train-sym24-f15578c9-wTzBO | 3.0814 |
| LRAUW | fork-joly-os-mmllm-claude-train-sym24-fbf702e8-LRAUW | 3.0850 |
| hu9lk | origin/claude/train-sym24-fd391c54-hu9lk | 3.0985 |
| X096S | fork-SeniorCareMarket-mmllm-claude-train-sym24-c32d655d-X096S | 3.1128 |
| hFjLw | fork-davidwuchn-mmllm-claude-train-sym24-75c3d7ea-hFjLw | 3.2161 |
| ibE4Y | origin/claude/train-sym24-a7fa82f9-ibE4Y | 3.2350 |
| QuJam | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c0020e5d-QuJam | 3.4694 |
| Kyxjm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3fba014e-Kyxjm | 3.4711 |
| **mean** | | **3.2212** |
| **best** | | **3.0814** |

## Chain progression R806 → R807

Previous harvest: `workers/dispatcher/harvest-8way-r806_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1684         | 3.2212         | +0.0528 |
| ctrl_bpc best  | 3.0659         | 3.0814         | +0.0155 |

## Per-round trajectory (best bird: wTzBO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 807 | 6664 | 3.0814 | +0.5016 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r806_sym24`

## Output

`workers/dispatcher/harvest-8way-r807_sym24/round-807/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

