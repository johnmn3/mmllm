# harvest-5way-r1117 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1117 ctrl_bpc |
|--------|--------|--------------:|
| nqW69 | origin/claude/train-sym24-4c08adc8-nqW69 | 2.3677 |
| TjoFZ | fork-slaa-us-mmllm-claude-train-sym24-40cadc57-TjoFZ | 2.3700 |
| 9kAYV | fork-SeniorCareMarket-mmllm-claude-train-sym24-e4abf3d2-9kAYV | 2.3762 |
| JaNNy | fork-joly-os-mmllm-claude-train-sym24-40a34eac-JaNNy | 2.3899 |
| 6ix3t | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-888e7dea-6ix3t | 2.5745 |
| **mean** | | **2.4157** |
| **best** | | **2.3677** |

## Chain progression R1116 → R1117

Previous harvest: `workers/dispatcher/harvest-6way-r1116_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5571         | 2.4157         | -0.1414 |
| ctrl_bpc best  | 2.3779         | 2.3677         | -0.0102 |

## Per-round trajectory (best bird: nqW69)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1117 | 6625 | 2.3677 | +0.2435 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1116_sym24`
  - `workers/dispatcher/harvest-6way-r1116_sym24`

## Output

`workers/dispatcher/harvest-5way-r1117_sym24/round-1117/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

