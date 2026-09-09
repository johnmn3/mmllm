# harvest-1way-r1420 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1420 ctrl_bpc |
|--------|--------|--------------:|
| s7Rmy | origin/claude/train-sym24-92cb6044-s7Rmy | 3.4416 |
| **mean** | | **3.4416** |
| **best** | | **3.4416** |

## Chain progression R1419 → R1420

Previous harvest: `workers/dispatcher/harvest-4way-r1419_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2204         | 3.4416         | +0.2212 |
| ctrl_bpc best  | 3.0917         | 3.4416         | +0.3499 |

## Per-round trajectory (best bird: s7Rmy)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1420 | 3717 | 3.4416 | +0.2063 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1419_sym24`

## Output

`workers/dispatcher/harvest-1way-r1420_sym24/round-1420/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

