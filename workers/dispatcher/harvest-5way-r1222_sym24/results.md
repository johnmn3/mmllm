# harvest-5way-r1222 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1222 ctrl_bpc |
|--------|--------|--------------:|
| NbZQf | fork-slaa-us-mmllm-claude-train-sym24-c007f9d8-NbZQf | 2.2577 |
| p2GWo | origin/claude/train-sym24-a3249f51-p2GWo | 2.2636 |
| 1UVsn | fork-SeniorCareMarket-mmllm-claude-train-sym24-39581564-1UVsn | 2.2797 |
| jQQP5 | fork-joly-os-mmllm-claude-train-sym24-b7259c90-jQQP5 | 2.2854 |
| 3bBBi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-c04b8c0b-3bBBi | 2.6571 |
| **mean** | | **2.3487** |
| **best** | | **2.2577** |

## Chain progression R1221 → R1222

Previous harvest: `workers/dispatcher/harvest-6way-r1221_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4061         | 2.3487         | -0.0574 |
| ctrl_bpc best  | 2.2620         | 2.2577         | -0.0043 |

## Per-round trajectory (best bird: NbZQf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1222 | 6457 | 2.2577 | +0.2717 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1221_sym24`

## Output

`workers/dispatcher/harvest-5way-r1222_sym24/round-1222/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

