# harvest-2way-r631 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R631 ctrl_bpc |
|--------|--------|--------------:|
| N7qoA | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-21a04972-N7qoA | 2.1158 |
| UHgMW | fork-slaa-us-mmllm-claude-train-sym24-0ecca79b-UHgMW | 2.1331 |
| **mean** | | **2.1245** |
| **best** | | **2.1158** |

## Chain progression R630 → R631

Previous harvest: `workers/dispatcher/harvest-1way-r630_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1382         | 2.1245         | -0.0137 |
| ctrl_bpc best  | 2.1382         | 2.1158         | -0.0224 |

## Per-round trajectory (best bird: N7qoA)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 631 | 5193 | 2.1158 | +0.0515 |

## Cumulative training contribution

- This harvest: **100 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **550 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r630_sym24`

## Output

`workers/dispatcher/harvest-2way-r631_sym24/round-631/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

