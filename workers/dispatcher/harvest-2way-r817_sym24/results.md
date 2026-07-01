# harvest-2way-r817 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R817 ctrl_bpc |
|--------|--------|--------------:|
| 9J1M8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4062da4a-9J1M8 | 3.0497 |
| 6bN70 | origin/claude/train-sym24-acb6e1b9-6bN70 | 3.3972 |
| **mean** | | **3.2235** |
| **best** | | **3.0497** |

## Chain progression R816 → R817

Previous harvest: `workers/dispatcher/harvest-8way-r816_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1529         | 3.2235         | +0.0706 |
| ctrl_bpc best  | 3.0290         | 3.0497         | +0.0207 |

## Per-round trajectory (best bird: 9J1M8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 817 | 6350 | 3.0497 | +0.6428 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r816_sym24`

## Output

`workers/dispatcher/harvest-2way-r817_sym24/round-817/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

