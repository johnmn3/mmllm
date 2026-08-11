# harvest-9way-r1168 — sparse-delta merge of 9 birds

## Worker endpoints

| handle | branch | R1168 ctrl_bpc |
|--------|--------|--------------:|
| jeEX0 | fork-SeniorCareMarket-mmllm-claude-train-sym24-488e5696-jeEX0 | 2.3175 |
| nF25R | fork-joly-os-mmllm-claude-train-sym24-ea0568e2-nF25R | 2.3235 |
| zXs03 | fork-slaa-us-mmllm-claude-train-sym24-9fde9599-zXs03 | 2.3280 |
| bkU0a | fork-slaa-us-mmllm-claude-train-sym24-2f52c9d0-bkU0a | 2.3341 |
| C3r61 | fork-SeniorCareMarket-mmllm-claude-train-sym24-02f92b85-C3r61 | 2.3410 |
| dMNhw | origin/claude/train-sym24-df14662d-dMNhw | 2.3456 |
| V4wEH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ddc2cbb2-V4wEH | 2.5114 |
| Rj5X0 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-1368f96c-Rj5X0 | 2.7077 |
| uMBQ6 | fork-joly-os-mmllm-claude-train-sym24-77eb636e-uMBQ6 | 2.7106 |
| **mean** | | **2.4355** |
| **best** | | **2.3175** |

## Chain progression R1167 → R1168

Previous harvest: `workers/dispatcher/harvest-6way-r1167_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4878         | 2.4355         | -0.0523 |
| ctrl_bpc best  | 2.3192         | 2.3175         | -0.0017 |

## Per-round trajectory (best bird: jeEX0)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1168 | 3747 | 2.3175 | +0.2509 |

## Cumulative training contribution

- This harvest: **720 steps** from 9 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1167_sym24`
  - `workers/dispatcher/harvest-6way-r1167_sym24`

## Output

`workers/dispatcher/harvest-9way-r1168_sym24/round-1168/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 9 workers)
- `dense.pt` (averaged across 9 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

