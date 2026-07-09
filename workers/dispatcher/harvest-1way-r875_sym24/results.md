# harvest-1way-r875 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R875 ctrl_bpc |
|--------|--------|--------------:|
| Cvg2j | origin/claude/train-sym24-1a46df14-Cvg2j | 2.8410 |
| **mean** | | **2.8410** |
| **best** | | **2.8410** |

## Chain progression R874 → R875

Previous harvest: `workers/dispatcher/harvest-3way-r874_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1077         | 2.8410         | -0.2667 |
| ctrl_bpc best  | 3.0236         | 2.8410         | -0.1826 |

## Per-round trajectory (best bird: Cvg2j)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 875 | 6398 | 2.8410 | +0.3917 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **800 steps** from 10 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r874_sym24`

## Output

`workers/dispatcher/harvest-1way-r875_sym24/round-875/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

