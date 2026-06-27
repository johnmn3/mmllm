# harvest-1way-r781 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R781 ctrl_bpc |
|--------|--------|--------------:|
| 5Iiv9 | origin/claude/train-sym24-f08e16f9-5Iiv9 | 3.1817 |
| **mean** | | **3.1817** |
| **best** | | **3.1817** |

## Chain progression R780 → R781

Previous harvest: `workers/dispatcher/harvest-9way-r780_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3689         | 3.1817         | -0.1872 |
| ctrl_bpc best  | 3.1952         | 3.1817         | -0.0135 |

## Per-round trajectory (best bird: 5Iiv9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 781 | 5396 | 3.1817 | +0.6136 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r780_sym24`

## Output

`workers/dispatcher/harvest-1way-r781_sym24/round-781/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

