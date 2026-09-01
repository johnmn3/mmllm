# harvest-1way-r1376 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1376 ctrl_bpc |
|--------|--------|--------------:|
| hbceK | origin/claude/train-sym24-16b69038-hbceK | 3.2101 |
| **mean** | | **3.2101** |
| **best** | | **3.2101** |

## Chain progression R1375 → R1376

Previous harvest: `workers/dispatcher/harvest-3way-r1375_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3936         | 3.2101         | -0.1835 |
| ctrl_bpc best  | 3.1795         | 3.2101         | +0.0306 |

## Per-round trajectory (best bird: hbceK)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1376 | 6538 | 3.2101 | +0.1294 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r1375_sym24`

## Output

`workers/dispatcher/harvest-1way-r1376_sym24/round-1376/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

