# harvest-3way-r1218 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1218 ctrl_bpc |
|--------|--------|--------------:|
| iVE8P | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e2cad16f-iVE8P | 2.2838 |
| m0JXg | fork-SeniorCareMarket-mmllm-claude-train-sym24-b33c4d28-m0JXg | 2.2876 |
| 1VbtM | fork-slaa-us-mmllm-claude-train-sym24-63266b40-1VbtM | 2.2894 |
| **mean** | | **2.2869** |
| **best** | | **2.2838** |

## Chain progression R1217 → R1218

Previous harvest: `workers/dispatcher/harvest-8way-r1217_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3968         | 2.2869         | -0.1099 |
| ctrl_bpc best  | 2.2655         | 2.2838         | +0.0183 |

## Per-round trajectory (best bird: iVE8P)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1218 | 6588 | 2.2838 | +0.2487 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1217_sym24`

## Output

`workers/dispatcher/harvest-3way-r1218_sym24/round-1218/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

