# harvest-1way-r916 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R916 ctrl_bpc |
|--------|--------|--------------:|
| lLHuD | origin/claude/train-sym24-ecaf5f17-lLHuD | 2.7570 |
| **mean** | | **2.7570** |
| **best** | | **2.7570** |

## Chain progression R915 → R916

Previous harvest: `workers/dispatcher/harvest-6way-r915_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8852         | 2.7570         | -0.1282 |
| ctrl_bpc best  | 2.7381         | 2.7570         | +0.0189 |

## Per-round trajectory (best bird: lLHuD)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 916 | 6514 | 2.7570 | +0.2078 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r915_sym24`

## Output

`workers/dispatcher/harvest-1way-r916_sym24/round-916/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

