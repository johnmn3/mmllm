# harvest-1way-r1049 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1049 ctrl_bpc |
|--------|--------|--------------:|
| e2akY | origin/claude/train-sym24-b14ef3e6-e2akY | 2.5101 |
| **mean** | | **2.5101** |
| **best** | | **2.5101** |

## Chain progression R1048 → R1049

Previous harvest: `workers/dispatcher/harvest-4way-r1048_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7717         | 2.5101         | -0.2616 |
| ctrl_bpc best  | 2.5021         | 2.5101         | +0.0080 |

## Per-round trajectory (best bird: e2akY)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1049 | 6526 | 2.5101 | +0.1892 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1048_sym24`

## Output

`workers/dispatcher/harvest-1way-r1049_sym24/round-1049/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

