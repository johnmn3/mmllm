# harvest-1way-r1415 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1415 ctrl_bpc |
|--------|--------|--------------:|
| j8acm | fork-SeniorCareMarket-mmllm-claude-train-sym24-be27b95a-j8acm | 3.1685 |
| **mean** | | **3.1685** |
| **best** | | **3.1685** |

## Chain progression R1414 → R1415

Previous harvest: `workers/dispatcher/harvest-1way-r1414_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2114         | 3.1685         | -0.0429 |
| ctrl_bpc best  | 3.2114         | 3.1685         | -0.0429 |

## Per-round trajectory (best bird: j8acm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1415 | 7004 | 3.1685 | +0.1377 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1414_sym24`

## Output

`workers/dispatcher/harvest-1way-r1415_sym24/round-1415/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

