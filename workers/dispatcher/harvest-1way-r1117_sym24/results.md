# harvest-1way-r1117 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1117 ctrl_bpc |
|--------|--------|--------------:|
| JaNNy | fork-joly-os-mmllm-claude-train-sym24-40a34eac-JaNNy | 2.3899 |
| **mean** | | **2.3899** |
| **best** | | **2.3899** |

## Chain progression R1116 → R1117

Previous harvest: `workers/dispatcher/harvest-6way-r1116_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5571         | 2.3899         | -0.1672 |
| ctrl_bpc best  | 2.3779         | 2.3899         | +0.0120 |

## Per-round trajectory (best bird: JaNNy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1117 | 3688 | 2.3899 | +0.2402 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1116_sym24`

## Output

`workers/dispatcher/harvest-1way-r1117_sym24/round-1117/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

