# harvest-1way-r1056 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1056 ctrl_bpc |
|--------|--------|--------------:|
| oWXqk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-70bcddc7-oWXqk | 2.4621 |
| **mean** | | **2.4621** |
| **best** | | **2.4621** |

## Chain progression R1055 → R1056

Previous harvest: `workers/dispatcher/harvest-3way-r1055_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5459         | 2.4621         | -0.0838 |
| ctrl_bpc best  | 2.4823         | 2.4621         | -0.0202 |

## Per-round trajectory (best bird: oWXqk)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1056 | 6666 | 2.4621 | +0.2074 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1055_sym24`

## Output

`workers/dispatcher/harvest-1way-r1056_sym24/round-1056/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

