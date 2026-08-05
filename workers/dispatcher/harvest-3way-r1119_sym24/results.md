# harvest-3way-r1119 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R1119 ctrl_bpc |
|--------|--------|--------------:|
| egKNn | fork-joly-os-mmllm-claude-train-sym24-89452461-egKNn | 2.3714 |
| dsaRq | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5aacbdf7-dsaRq | 2.5677 |
| isgo2 | origin/claude/train-sym24-7f5d8bc4-isgo2 | 2.7921 |
| **mean** | | **2.5771** |
| **best** | | **2.3714** |

## Chain progression R1118 → R1119

Previous harvest: `workers/dispatcher/harvest-6way-r1118_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5160         | 2.5771         | +0.0611 |
| ctrl_bpc best  | 2.3683         | 2.3714         | +0.0031 |

## Per-round trajectory (best bird: egKNn)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1119 | 4349 | 2.3714 | +0.2462 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1118_sym24`
  - `workers/dispatcher/harvest-3way-r1118_sym24`

## Output

`workers/dispatcher/harvest-3way-r1119_sym24/round-1119/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

