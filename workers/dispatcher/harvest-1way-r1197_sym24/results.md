# harvest-1way-r1197 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1197 ctrl_bpc |
|--------|--------|--------------:|
| mUjCU | fork-slaa-us-mmllm-claude-train-sym24-929c54f1-mUjCU | 2.3041 |
| **mean** | | **2.3041** |
| **best** | | **2.3041** |

## Chain progression R1196 → R1197

Previous harvest: `workers/dispatcher/harvest-9way-r1196_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4521         | 2.3041         | -0.1480 |
| ctrl_bpc best  | 2.2848         | 2.3041         | +0.0193 |

## Per-round trajectory (best bird: mUjCU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1197 | 3859 | 2.3041 | +0.2428 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1196_sym24`

## Output

`workers/dispatcher/harvest-1way-r1197_sym24/round-1197/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

