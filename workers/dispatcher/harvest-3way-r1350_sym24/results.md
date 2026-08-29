# harvest-3way-r1350 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1350 ctrl_bpc |
|--------|--------|--------------:|
| owD4m | fork-SeniorCareMarket-mmllm-claude-train-sym24-4d6f90aa-owD4m | 3.3321 |
| UdKzA | origin/claude/train-sym24-42c940f0-UdKzA | 3.3549 |
| xZBro | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-88b36998-xZBro | 3.6899 |
| **mean** | | **3.4590** |
| **best** | | **3.3321** |

## Chain progression R1349 → R1350

Previous harvest: `workers/dispatcher/harvest-4way-r1349_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4754         | 3.4590         | -0.0164 |
| ctrl_bpc best  | 3.1625         | 3.3321         | +0.1696 |

## Per-round trajectory (best bird: owD4m)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1350 | 6555 | 3.3321 | +0.0922 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1349_sym24`

## Output

`workers/dispatcher/harvest-3way-r1350_sym24/round-1350/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

