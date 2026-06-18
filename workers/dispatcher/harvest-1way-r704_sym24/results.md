# harvest-1way-r704 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R704 ctrl_bpc |
|--------|--------|--------------:|
| c4Du5 | origin/claude/train-sym24-813c4a54-c4Du5 | 3.5994 |
| **mean** | | **3.5994** |
| **best** | | **3.5994** |

## Chain progression R703 → R704

Previous harvest: `workers/dispatcher/harvest-4way-r703_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.7146         | 3.5994         | -0.1152 |
| ctrl_bpc best  | 3.5916         | 3.5994         | +0.0078 |

## Per-round trajectory (best bird: c4Du5)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 704 | 6534 | 3.5994 | +0.5312 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r703_sym24`

## Output

`workers/dispatcher/harvest-1way-r704_sym24/round-704/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

