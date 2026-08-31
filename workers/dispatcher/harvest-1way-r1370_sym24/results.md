# harvest-1way-r1370 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1370 ctrl_bpc |
|--------|--------|--------------:|
| WEC8V | origin/claude/train-sym24-4ead64a1-WEC8V | 3.5034 |
| **mean** | | **3.5034** |
| **best** | | **3.5034** |

## Chain progression R1369 → R1370

Previous harvest: `workers/dispatcher/harvest-5way-r1369_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2627         | 3.5034         | +0.2407 |
| ctrl_bpc best  | 3.0918         | 3.5034         | +0.4116 |

## Per-round trajectory (best bird: WEC8V)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1370 | 6576 | 3.5034 | +0.1026 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1369_sym24`

## Output

`workers/dispatcher/harvest-1way-r1370_sym24/round-1370/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

