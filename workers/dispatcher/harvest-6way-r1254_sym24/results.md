# harvest-6way-r1254 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1254 ctrl_bpc |
|--------|--------|--------------:|
| emqei | fork-SeniorCareMarket-mmllm-claude-train-sym24-b2af0efe-emqei | 2.2375 |
| I9HIy | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c892276e-I9HIy | 2.4519 |
| hV2uo | fork-joly-os-mmllm-claude-train-sym24-c556be66-hV2uo | 2.6392 |
| AUep9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-d9ac5a62-AUep9 | 2.6494 |
| hhuPY | fork-slaa-us-mmllm-claude-train-sym24-f1fbe58c-hhuPY | 2.6497 |
| uIp13 | fork-slaa-us-mmllm-claude-train-sym24-d3a64c80-uIp13 | 2.6608 |
| **mean** | | **2.5481** |
| **best** | | **2.2375** |

## Chain progression R1253 → R1254

Previous harvest: `workers/dispatcher/harvest-6way-r1253_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4112         | 2.5481         | +0.1369 |
| ctrl_bpc best  | 2.2520         | 2.2375         | -0.0145 |

## Per-round trajectory (best bird: emqei)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1254 | 5357 | 2.2375 | +0.2407 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1253_sym24`
  - `workers/dispatcher/harvest-6way-r1253_sym24`

## Output

`workers/dispatcher/harvest-6way-r1254_sym24/round-1254/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

