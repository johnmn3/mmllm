# harvest-3way-r1057 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1057 ctrl_bpc |
|--------|--------|--------------:|
| LZmla | origin/claude/train-sym24-130b2d00-LZmla | 2.4609 |
| o0Sfr | fork-joly-os-mmllm-claude-train-sym24-d7061d48-o0Sfr | 2.6459 |
| VZpil | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-98535987-VZpil | 2.6611 |
| **mean** | | **2.5893** |
| **best** | | **2.4609** |

## Chain progression R1056 → R1057

Previous harvest: `workers/dispatcher/harvest-5way-r1056_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6953         | 2.5893         | -0.1060 |
| ctrl_bpc best  | 2.4621         | 2.4609         | -0.0012 |

## Per-round trajectory (best bird: LZmla)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1057 | 6605 | 2.4609 | +0.2150 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1056_sym24`
  - `workers/dispatcher/harvest-4way-r1056_sym24`

## Output

`workers/dispatcher/harvest-3way-r1057_sym24/round-1057/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

