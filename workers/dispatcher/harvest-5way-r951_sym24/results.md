# harvest-5way-r951 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R951 ctrl_bpc |
|--------|--------|--------------:|
| oj52Q | fork-joly-os-mmllm-claude-train-sym24-3a4329a8-oj52Q | 2.6556 |
| z4NrT | fork-slaa-us-mmllm-claude-train-sym24-ac494491-z4NrT | 2.6682 |
| 57W9h | fork-SeniorCareMarket-mmllm-claude-train-sym24-fc08cea8-57W9h | 2.6697 |
| w4Vxo | fork-slaa-us-mmllm-claude-train-sym24-5bb5143f-w4Vxo | 2.6726 |
| JScWe | origin/claude/train-sym24-5abe126b-JScWe | 2.8526 |
| **mean** | | **2.7037** |
| **best** | | **2.6556** |

## Chain progression R950 → R951

Previous harvest: `workers/dispatcher/harvest-12way-r950_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8449         | 2.7037         | -0.1412 |
| ctrl_bpc best  | 2.6494         | 2.6556         | +0.0062 |

## Per-round trajectory (best bird: oj52Q)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 951 | 6904 | 2.6556 | +0.1606 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r950_sym24`
  - `workers/dispatcher/harvest-8way-r950_sym24`

## Output

`workers/dispatcher/harvest-5way-r951_sym24/round-951/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

