# harvest-1way-r1038 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1038 ctrl_bpc |
|--------|--------|--------------:|
| QYJAz | origin/claude/train-sym24-d4ad9ceb-QYJAz | 2.8769 |
| **mean** | | **2.8769** |
| **best** | | **2.8769** |

## Chain progression R1037 → R1038

Previous harvest: `workers/dispatcher/harvest-2way-r1037_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5354         | 2.8769         | +0.3415 |
| ctrl_bpc best  | 2.5136         | 2.8769         | +0.3633 |

## Per-round trajectory (best bird: QYJAz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1038 | 4354 | 2.8769 | +0.1874 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1037_sym24`

## Output

`workers/dispatcher/harvest-1way-r1038_sym24/round-1038/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

