# harvest-1way-r1118 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1118 ctrl_bpc |
|--------|--------|--------------:|
| 4HcaU | origin/claude/train-sym24-84f4d79d-4HcaU | 2.3737 |
| **mean** | | **2.3737** |
| **best** | | **2.3737** |

## Chain progression R1117 → R1118

Previous harvest: `workers/dispatcher/harvest-5way-r1117_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4157         | 2.3737         | -0.0420 |
| ctrl_bpc best  | 2.3677         | 2.3737         | +0.0060 |

## Per-round trajectory (best bird: 4HcaU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1118 | 6653 | 2.3737 | +0.2556 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1117_sym24`

## Output

`workers/dispatcher/harvest-1way-r1118_sym24/round-1118/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

