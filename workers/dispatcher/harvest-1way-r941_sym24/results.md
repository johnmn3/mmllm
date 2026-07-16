# harvest-1way-r941 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R941 ctrl_bpc |
|--------|--------|--------------:|
| eQpSa | origin/claude/train-sym24-378f1104-eQpSa | 2.7046 |
| **mean** | | **2.7046** |
| **best** | | **2.7046** |

## Chain progression R940 → R941

Previous harvest: `workers/dispatcher/harvest-1way-r940_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8931         | 2.7046         | -0.1885 |
| ctrl_bpc best  | 2.8931         | 2.7046         | -0.1885 |

## Per-round trajectory (best bird: eQpSa)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 941 | 4486 | 2.7046 | +0.1656 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r940_sym24`

## Output

`workers/dispatcher/harvest-1way-r941_sym24/round-941/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

