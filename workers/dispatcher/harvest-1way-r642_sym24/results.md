# harvest-1way-r642 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R642 ctrl_bpc |
|--------|--------|--------------:|
| 73sj2 | fork-slaa-us-mmllm-claude-train-sym24-09c9658f-73sj2 | 5.1180 |
| **mean** | | **5.1180** |
| **best** | | **5.1180** |

## Chain progression R641 → R642

Previous harvest: `workers/dispatcher/harvest-2way-r641_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.9679         | 5.1180         | +0.1501 |
| ctrl_bpc best  | 4.7236         | 5.1180         | +0.3944 |

## Per-round trajectory (best bird: 73sj2)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 642 | 6248 | 5.1180 | +0.0310 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **2880 steps** from 36 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r641_sym24`

## Output

`workers/dispatcher/harvest-1way-r642_sym24/round-642/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

