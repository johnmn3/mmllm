# harvest-3way-r807 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R807 ctrl_bpc |
|--------|--------|--------------:|
| X096S | fork-SeniorCareMarket-mmllm-claude-train-sym24-c32d655d-X096S | 3.1128 |
| ibE4Y | origin/claude/train-sym24-a7fa82f9-ibE4Y | 3.2350 |
| Kyxjm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3fba014e-Kyxjm | 3.4711 |
| **mean** | | **3.2730** |
| **best** | | **3.1128** |

## Chain progression R806 → R807

Previous harvest: `workers/dispatcher/harvest-8way-r806_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1684         | 3.2730         | +0.1046 |
| ctrl_bpc best  | 3.0659         | 3.1128         | +0.0469 |

## Per-round trajectory (best bird: X096S)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 807 | 6434 | 3.1128 | +0.5761 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r806_sym24`

## Output

`workers/dispatcher/harvest-3way-r807_sym24/round-807/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

