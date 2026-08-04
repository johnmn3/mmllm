# harvest-3way-r1108 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1108 ctrl_bpc |
|--------|--------|--------------:|
| U30Qg | origin/claude/train-sym24-54b7352e-U30Qg | 2.3876 |
| cRv2Y | fork-joly-os-mmllm-claude-train-sym24-a3a52013-cRv2Y | 2.3878 |
| yy0vd | fork-slaa-us-mmllm-claude-train-sym24-a9725c47-yy0vd | 2.4077 |
| **mean** | | **2.3944** |
| **best** | | **2.3876** |

## Chain progression R1107 → R1108

Previous harvest: `workers/dispatcher/harvest-3way-r1107_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4667         | 2.3944         | -0.0723 |
| ctrl_bpc best  | 2.4036         | 2.3876         | -0.0160 |

## Per-round trajectory (best bird: U30Qg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1108 | 6701 | 2.3876 | +0.2506 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1107_sym24`
  - `workers/dispatcher/harvest-3way-r1107_sym24`

## Output

`workers/dispatcher/harvest-3way-r1108_sym24/round-1108/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

