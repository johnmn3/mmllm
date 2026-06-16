# harvest-2way-r689 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R689 ctrl_bpc |
|--------|--------|--------------:|
| D0xHh | fork-slaa-us-mmllm-claude-train-sym24-fe5d4c5c-D0xHh | 3.7494 |
| jshSa | fork-joly-os-mmllm-claude-train-sym24-abfa3491-jshSa | 3.7613 |
| **mean** | | **3.7553** |
| **best** | | **3.7494** |

## Chain progression R688 → R689

Previous harvest: `workers/dispatcher/harvest-11way-r688_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8158         | 3.7553         | -0.0604 |
| ctrl_bpc best  | 3.6959         | 3.7494         | +0.0535 |

## Per-round trajectory (best bird: D0xHh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 689 | 6518 | 3.7494 | +0.4668 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r688_sym24`

## Output

`workers/dispatcher/harvest-2way-r689_sym24/round-689/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

