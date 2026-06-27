# harvest-1way-r784 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R784 ctrl_bpc |
|--------|--------|--------------:|
| 007j8 | fork-slaa-us-mmllm-claude-train-sym24-b843dd30-007j8 | 3.3106 |
| **mean** | | **3.3106** |
| **best** | | **3.3106** |

## Chain progression R783 → R784

Previous harvest: `workers/dispatcher/harvest-10way-r783_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3778         | 3.3106         | -0.0672 |
| ctrl_bpc best  | 3.1869         | 3.3106         | +0.1237 |

## Per-round trajectory (best bird: 007j8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 784 | 5387 | 3.3106 | +0.7172 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r783_sym24`

## Output

`workers/dispatcher/harvest-1way-r784_sym24/round-784/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

