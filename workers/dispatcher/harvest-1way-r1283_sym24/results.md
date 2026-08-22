# harvest-1way-r1283 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1283 ctrl_bpc |
|--------|--------|--------------:|
| Z2Rn9 | fork-joly-os-mmllm-claude-train-sym24-1427f2c9-Z2Rn9 | 2.2156 |
| **mean** | | **2.2156** |
| **best** | | **2.2156** |

## Chain progression R1282 → R1283

Previous harvest: `workers/dispatcher/harvest-7way-r1282_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3443         | 2.2156         | -0.1287 |
| ctrl_bpc best  | 2.2278         | 2.2156         | -0.0122 |

## Per-round trajectory (best bird: Z2Rn9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1283 | 4206 | 2.2156 | +0.2544 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1282_sym24`

## Output

`workers/dispatcher/harvest-1way-r1283_sym24/round-1283/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

