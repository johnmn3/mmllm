# harvest-1way-r1358 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1358 ctrl_bpc |
|--------|--------|--------------:|
| LjtaT | origin/claude/train-sym24-7efb0113-LjtaT | 3.2703 |
| **mean** | | **3.2703** |
| **best** | | **3.2703** |

## Chain progression R1357 → R1358

Previous harvest: `workers/dispatcher/harvest-4way-r1357_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3670         | 3.2703         | -0.0967 |
| ctrl_bpc best  | 3.2695         | 3.2703         | +0.0008 |

## Per-round trajectory (best bird: LjtaT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1358 | 6302 | 3.2703 | +0.1012 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1357_sym24`

## Output

`workers/dispatcher/harvest-1way-r1358_sym24/round-1358/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

