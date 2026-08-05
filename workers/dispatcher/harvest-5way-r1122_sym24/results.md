# harvest-5way-r1122 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1122 ctrl_bpc |
|--------|--------|--------------:|
| 2xNXw | fork-joly-os-mmllm-claude-train-sym24-e25c3c01-2xNXw | 2.3634 |
| UldUu | fork-joly-os-mmllm-claude-train-sym24-c2164371-UldUu | 2.3678 |
| G0yZr | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-20a901fb-G0yZr | 2.5582 |
| dYljN | origin/claude/train-sym24-cbc17401-dYljN | 2.5623 |
| IUYi9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3538504d-IUYi9 | 2.5697 |
| **mean** | | **2.4843** |
| **best** | | **2.3634** |

## Chain progression R1121 → R1122

Previous harvest: `workers/dispatcher/harvest-7way-r1121_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6555         | 2.4843         | -0.1712 |
| ctrl_bpc best  | 2.3944         | 2.3634         | -0.0310 |

## Per-round trajectory (best bird: 2xNXw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1122 | 3660 | 2.3634 | +0.2565 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1121_sym24`
  - `workers/dispatcher/harvest-7way-r1121_sym24`

## Output

`workers/dispatcher/harvest-5way-r1122_sym24/round-1122/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

