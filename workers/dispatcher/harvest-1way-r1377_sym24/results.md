# harvest-1way-r1377 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1377 ctrl_bpc |
|--------|--------|--------------:|
| p95bp | origin/claude/train-sym24-1cb977dc-p95bp | 3.4927 |
| **mean** | | **3.4927** |
| **best** | | **3.4927** |

## Chain progression R1376 → R1377

Previous harvest: `workers/dispatcher/harvest-1way-r1376_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2101         | 3.4927         | +0.2826 |
| ctrl_bpc best  | 3.2101         | 3.4927         | +0.2826 |

## Per-round trajectory (best bird: p95bp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1377 | 4429 | 3.4927 | +0.1044 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1376_sym24`

## Output

`workers/dispatcher/harvest-1way-r1377_sym24/round-1377/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

