# harvest-6way-r1057 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1057 ctrl_bpc |
|--------|--------|--------------:|
| LZmla | origin/claude/train-sym24-130b2d00-LZmla | 2.4609 |
| 20IFM | fork-SeniorCareMarket-mmllm-claude-train-sym24-03b8089f-20IFM | 2.4643 |
| o0Sfr | fork-joly-os-mmllm-claude-train-sym24-d7061d48-o0Sfr | 2.6459 |
| VZpil | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-98535987-VZpil | 2.6611 |
| dahuq | fork-slaa-us-mmllm-claude-train-sym24-d531fd40-dahuq | 2.6729 |
| GJaVW | origin/claude/train-sym24-051380d8-GJaVW | 2.8612 |
| **mean** | | **2.6277** |
| **best** | | **2.4609** |

## Chain progression R1056 → R1057

Previous harvest: `workers/dispatcher/harvest-5way-r1056_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6953         | 2.6277         | -0.0676 |
| ctrl_bpc best  | 2.4621         | 2.4609         | -0.0012 |

## Per-round trajectory (best bird: LZmla)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1057 | 6605 | 2.4609 | +0.2150 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1056_sym24`
  - `workers/dispatcher/harvest-4way-r1056_sym24`
  - `workers/dispatcher/harvest-5way-r1056_sym24`

## Output

`workers/dispatcher/harvest-6way-r1057_sym24/round-1057/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

