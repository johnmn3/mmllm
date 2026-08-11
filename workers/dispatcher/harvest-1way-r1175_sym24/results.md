# harvest-1way-r1175 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1175 ctrl_bpc |
|--------|--------|--------------:|
| Tmjjb | origin/claude/train-sym24-642d7d97-Tmjjb | 2.3243 |
| **mean** | | **2.3243** |
| **best** | | **2.3243** |

## Chain progression R1174 → R1175

Previous harvest: `workers/dispatcher/harvest-6way-r1174_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4812         | 2.3243         | -0.1569 |
| ctrl_bpc best  | 2.3127         | 2.3243         | +0.0116 |

## Per-round trajectory (best bird: Tmjjb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1175 | 6446 | 2.3243 | +0.2435 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1174_sym24`

## Output

`workers/dispatcher/harvest-1way-r1175_sym24/round-1175/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

