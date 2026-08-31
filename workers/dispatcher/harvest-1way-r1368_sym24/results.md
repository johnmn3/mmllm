# harvest-1way-r1368 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1368 ctrl_bpc |
|--------|--------|--------------:|
| n72YW | origin/claude/train-sym24-59d78295-n72YW | 3.2665 |
| **mean** | | **3.2665** |
| **best** | | **3.2665** |

## Chain progression R1367 → R1368

Previous harvest: `workers/dispatcher/harvest-3way-r1367_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3467         | 3.2665         | -0.0802 |
| ctrl_bpc best  | 3.2239         | 3.2665         | +0.0426 |

## Per-round trajectory (best bird: n72YW)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1368 | 4520 | 3.2665 | +0.1142 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1367_sym24`

## Output

`workers/dispatcher/harvest-1way-r1368_sym24/round-1368/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

