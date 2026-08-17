# harvest-1way-r1236 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1236 ctrl_bpc |
|--------|--------|--------------:|
| RcPfW | fork-slaa-us-mmllm-claude-train-sym24-3d2804a9-RcPfW | 2.6538 |
| **mean** | | **2.6538** |
| **best** | | **2.6538** |

## Chain progression R1235 → R1236

Previous harvest: `workers/dispatcher/harvest-6way-r1235_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4298         | 2.6538         | +0.2240 |
| ctrl_bpc best  | 2.2648         | 2.6538         | +0.3890 |

## Per-round trajectory (best bird: RcPfW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1236 | 3550 | 2.6538 | +0.2234 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1235_sym24`

## Output

`workers/dispatcher/harvest-1way-r1236_sym24/round-1236/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

