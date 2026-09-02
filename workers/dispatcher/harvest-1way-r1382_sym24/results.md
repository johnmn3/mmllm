# harvest-1way-r1382 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1382 ctrl_bpc |
|--------|--------|--------------:|
| hQj7X | origin/claude/train-sym24-dceb810f-hQj7X | 3.0487 |
| **mean** | | **3.0487** |
| **best** | | **3.0487** |

## Chain progression R1381 → R1382

Previous harvest: `workers/dispatcher/harvest-2way-r1381_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0766         | 3.0487         | -0.0279 |
| ctrl_bpc best  | 3.0607         | 3.0487         | -0.0120 |

## Per-round trajectory (best bird: hQj7X)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1382 | 5385 | 3.0487 | +0.1152 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1381_sym24`

## Output

`workers/dispatcher/harvest-1way-r1382_sym24/round-1382/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

