# harvest-10way-r815 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R815 ctrl_bpc |
|--------|--------|--------------:|
| YVaP2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-63e5f982-YVaP2 | 3.0507 |
| CuXDO | fork-davidwuchn-mmllm-claude-train-sym24-ce9aaeff-CuXDO | 3.0543 |
| cLfmS | fork-slaa-us-mmllm-claude-train-sym24-476c83ee-cLfmS | 3.0592 |
| DUcgX | origin/claude/train-sym24-913523de-DUcgX | 3.0700 |
| fbEfv | origin/claude/train-sym24-ce9d8331-fbEfv | 3.0876 |
| Q3LzX | fork-joly-os-mmllm-claude-train-sym24-c9f1c0be-Q3LzX | 3.1884 |
| p69Aa | fork-slaa-us-mmllm-claude-train-sym24-cedc1749-p69Aa | 3.4126 |
| tHTm7 | fork-davidwuchn-mmllm-claude-train-sym24-a04faf34-tHTm7 | 3.4252 |
| W0n5X | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-3d58d787-W0n5X | 3.4256 |
| NQHtd | fork-joly-os-mmllm-claude-train-sym24-4c4e01e4-NQHtd | 3.4287 |
| **mean** | | **3.2202** |
| **best** | | **3.0507** |

## Chain progression R814 → R815

Previous harvest: `workers/dispatcher/harvest-5way-r814_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1128         | 3.2202         | +0.1074 |
| ctrl_bpc best  | 3.0590         | 3.0507         | -0.0083 |

## Per-round trajectory (best bird: YVaP2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 815 | 6388 | 3.0507 | +0.3562 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r814_sym24`
  - `workers/dispatcher/harvest-5way-r814_sym24`

## Output

`workers/dispatcher/harvest-10way-r815_sym24/round-815/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

