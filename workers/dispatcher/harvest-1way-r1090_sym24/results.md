# harvest-1way-r1090 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1090 ctrl_bpc |
|--------|--------|--------------:|
| VXipy | origin/claude/train-sym24-f718900f-VXipy | 2.4206 |
| **mean** | | **2.4206** |
| **best** | | **2.4206** |

## Chain progression R1089 → R1090

Previous harvest: `workers/dispatcher/harvest-4way-r1089_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4215         | 2.4206         | -0.0009 |
| ctrl_bpc best  | 2.4040         | 2.4206         | +0.0166 |

## Per-round trajectory (best bird: VXipy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1090 | 6577 | 2.4206 | +0.2208 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1089_sym24`

## Output

`workers/dispatcher/harvest-1way-r1090_sym24/round-1090/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

