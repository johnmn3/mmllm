# harvest-1way-r1017 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1017 ctrl_bpc |
|--------|--------|--------------:|
| UPg0w | origin/claude/train-sym24-2992c2ce-UPg0w | 2.5522 |
| **mean** | | **2.5522** |
| **best** | | **2.5522** |

## Chain progression R1016 → R1017

Previous harvest: `workers/dispatcher/harvest-9way-r1016_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6777         | 2.5522         | -0.1255 |
| ctrl_bpc best  | 2.5242         | 2.5522         | +0.0280 |

## Per-round trajectory (best bird: UPg0w)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1017 | 6592 | 2.5522 | +0.1791 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1016_sym24`

## Output

`workers/dispatcher/harvest-1way-r1017_sym24/round-1017/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

