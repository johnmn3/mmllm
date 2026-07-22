# harvest-1way-r993 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R993 ctrl_bpc |
|--------|--------|--------------:|
| eJck7 | origin/claude/train-sym24-756ad985-eJck7 | 2.9677 |
| **mean** | | **2.9677** |
| **best** | | **2.9677** |

## Chain progression R992 → R993

Previous harvest: `workers/dispatcher/harvest-6way-r992_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7737         | 2.9677         | +0.1940 |
| ctrl_bpc best  | 2.5721         | 2.9677         | +0.3956 |

## Per-round trajectory (best bird: eJck7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 993 | 6336 | 2.9677 | +0.1690 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r992_sym24`

## Output

`workers/dispatcher/harvest-1way-r993_sym24/round-993/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

