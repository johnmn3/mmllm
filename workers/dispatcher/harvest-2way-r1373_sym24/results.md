# harvest-2way-r1373 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1373 ctrl_bpc |
|--------|--------|--------------:|
| zN7fz | origin/claude/train-sym24-30afcb3c-zN7fz | 3.0797 |
| CcLTc | origin/claude/train-sym24-56d5438b-CcLTc | 3.6014 |
| **mean** | | **3.3405** |
| **best** | | **3.0797** |

## Chain progression R1372 → R1373

Previous harvest: `workers/dispatcher/harvest-3way-r1372_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2305         | 3.3405         | +0.1100 |
| ctrl_bpc best  | 3.1144         | 3.0797         | -0.0347 |

## Per-round trajectory (best bird: zN7fz)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1373 | 6567 | 3.0797 | +0.1476 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1372_sym24`

## Output

`workers/dispatcher/harvest-2way-r1373_sym24/round-1373/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

