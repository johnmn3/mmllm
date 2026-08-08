# harvest-6way-r1142 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1142 ctrl_bpc |
|--------|--------|--------------:|
| D8Ip7 | fork-joly-os-mmllm-claude-train-sym24-6ab1e59a-D8Ip7 | 2.5373 |
| YgETL | origin/claude/train-sym24-7c38d2e3-YgETL | 2.5482 |
| rSHI4 | fork-SeniorCareMarket-mmllm-claude-train-sym24-b6a44cf4-rSHI4 | 2.5499 |
| xrjf8 | fork-slaa-us-mmllm-claude-train-sym24-924e43f5-xrjf8 | 2.7402 |
| 9Zw0R | fork-joly-os-mmllm-claude-train-sym24-231eb53b-9Zw0R | 2.7469 |
| MDMt1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-73910d80-MDMt1 | 2.8014 |
| **mean** | | **2.6540** |
| **best** | | **2.5373** |

## Chain progression R1141 → R1142

Previous harvest: `workers/dispatcher/harvest-7way-r1141_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5410         | 2.6540         | +0.1130 |
| ctrl_bpc best  | 2.3417         | 2.5373         | +0.1956 |

## Per-round trajectory (best bird: D8Ip7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1142 | 6515 | 2.5373 | +0.2213 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1141_sym24`
  - `workers/dispatcher/harvest-7way-r1141_sym24`

## Output

`workers/dispatcher/harvest-6way-r1142_sym24/round-1142/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

