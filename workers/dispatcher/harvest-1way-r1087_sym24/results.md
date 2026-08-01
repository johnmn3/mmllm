# harvest-1way-r1087 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1087 ctrl_bpc |
|--------|--------|--------------:|
| emEAE | fork-joly-os-mmllm-claude-train-sym24-1a2a3433-emEAE | 2.4332 |
| **mean** | | **2.4332** |
| **best** | | **2.4332** |

## Chain progression R1086 → R1087

Previous harvest: `workers/dispatcher/harvest-5way-r1086_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6184         | 2.4332         | -0.1852 |
| ctrl_bpc best  | 2.4134         | 2.4332         | +0.0198 |

## Per-round trajectory (best bird: emEAE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1087 | 4345 | 2.4332 | +0.2345 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1086_sym24`

## Output

`workers/dispatcher/harvest-1way-r1087_sym24/round-1087/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

