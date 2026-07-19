# harvest-1way-r961 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R961 ctrl_bpc |
|--------|--------|--------------:|
| uc1hp | origin/claude/train-sym24-5288a93f-uc1hp | 3.0225 |
| **mean** | | **3.0225** |
| **best** | | **3.0225** |

## Chain progression R960 → R961

Previous harvest: `workers/dispatcher/harvest-11way-r960_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8917         | 3.0225         | +0.1308 |
| ctrl_bpc best  | 2.6345         | 3.0225         | +0.3880 |

## Per-round trajectory (best bird: uc1hp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 961 | 4428 | 3.0225 | +0.1695 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r960_sym24`

## Output

`workers/dispatcher/harvest-1way-r961_sym24/round-961/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

