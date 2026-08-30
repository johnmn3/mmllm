# harvest-4way-r1356 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1356 ctrl_bpc |
|--------|--------|--------------:|
| 4mz22 | origin/claude/train-sym24-85247435-4mz22 | 3.1885 |
| ReNXo | fork-SeniorCareMarket-mmllm-claude-train-sym24-d6fba824-ReNXo | 3.1949 |
| abUZe | origin/claude/train-sym24-bb09722d-abUZe | 3.2840 |
| KKDmU | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3e41bfd2-KKDmU | 3.4044 |
| **mean** | | **3.2679** |
| **best** | | **3.1885** |

## Chain progression R1355 → R1356

Previous harvest: `workers/dispatcher/harvest-5way-r1355_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3567         | 3.2679         | -0.0888 |
| ctrl_bpc best  | 3.2876         | 3.1885         | -0.0991 |

## Per-round trajectory (best bird: 4mz22)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1356 | 6405 | 3.1885 | +0.1164 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1355_sym24`
  - `workers/dispatcher/harvest-5way-r1355_sym24`

## Output

`workers/dispatcher/harvest-4way-r1356_sym24/round-1356/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

