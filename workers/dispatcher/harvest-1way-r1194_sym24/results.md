# harvest-1way-r1194 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1194 ctrl_bpc |
|--------|--------|--------------:|
| hWU2H | fork-joly-os-mmllm-claude-train-sym24-240fa1be-hWU2H | 2.3040 |
| **mean** | | **2.3040** |
| **best** | | **2.3040** |

## Chain progression R1193 → R1194

Previous harvest: `workers/dispatcher/harvest-11way-r1193_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3735         | 2.3040         | -0.0695 |
| ctrl_bpc best  | 2.2911         | 2.3040         | +0.0129 |

## Per-round trajectory (best bird: hWU2H)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1194 | 6674 | 2.3040 | +0.2677 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1193_sym24`

## Output

`workers/dispatcher/harvest-1way-r1194_sym24/round-1194/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

