# harvest-1way-r1092 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1092 ctrl_bpc |
|--------|--------|--------------:|
| oZgfW | fork-joly-os-mmllm-claude-train-sym24-7fbc1b07-oZgfW | 2.8158 |
| **mean** | | **2.8158** |
| **best** | | **2.8158** |

## Chain progression R1091 → R1092

Previous harvest: `workers/dispatcher/harvest-5way-r1091_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4916         | 2.8158         | +0.3242 |
| ctrl_bpc best  | 2.4054         | 2.8158         | +0.4104 |

## Per-round trajectory (best bird: oZgfW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1092 | 3875 | 2.8158 | +0.2196 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1091_sym24`

## Output

`workers/dispatcher/harvest-1way-r1092_sym24/round-1092/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

