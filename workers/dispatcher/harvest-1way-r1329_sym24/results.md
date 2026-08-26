# harvest-1way-r1329 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1329 ctrl_bpc |
|--------|--------|--------------:|
| u2R2O | origin/claude/train-sym24-5ec1b14f-u2R2O | 3.2964 |
| **mean** | | **3.2964** |
| **best** | | **3.2964** |

## Chain progression R1328 → R1329

Previous harvest: `workers/dispatcher/harvest-7way-r1328_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4883         | 3.2964         | -0.1919 |
| ctrl_bpc best  | 3.3057         | 3.2964         | -0.0093 |

## Per-round trajectory (best bird: u2R2O)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1329 | 6285 | 3.2964 | +0.0899 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1328_sym24`

## Output

`workers/dispatcher/harvest-1way-r1329_sym24/round-1329/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

