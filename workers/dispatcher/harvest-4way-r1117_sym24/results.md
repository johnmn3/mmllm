# harvest-4way-r1117 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1117 ctrl_bpc |
|--------|--------|--------------:|
| nqW69 | origin/claude/train-sym24-4c08adc8-nqW69 | 2.3677 |
| 9kAYV | fork-SeniorCareMarket-mmllm-claude-train-sym24-e4abf3d2-9kAYV | 2.3762 |
| JaNNy | fork-joly-os-mmllm-claude-train-sym24-40a34eac-JaNNy | 2.3899 |
| 6ix3t | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-888e7dea-6ix3t | 2.5745 |
| **mean** | | **2.4271** |
| **best** | | **2.3677** |

## Chain progression R1116 → R1117

Previous harvest: `workers/dispatcher/harvest-6way-r1116_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5571         | 2.4271         | -0.1300 |
| ctrl_bpc best  | 2.3779         | 2.3677         | -0.0102 |

## Per-round trajectory (best bird: nqW69)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1117 | 6625 | 2.3677 | +0.2435 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1116_sym24`

## Output

`workers/dispatcher/harvest-4way-r1117_sym24/round-1117/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

