# harvest-1way-r910 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R910 ctrl_bpc |
|--------|--------|--------------:|
| FM8Uw | origin/claude/train-sym24-dcc8226e-FM8Uw | 2.7511 |
| **mean** | | **2.7511** |
| **best** | | **2.7511** |

## Chain progression R909 → R910

Previous harvest: `workers/dispatcher/harvest-6way-r909_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8388         | 2.7511         | -0.0877 |
| ctrl_bpc best  | 2.7607         | 2.7511         | -0.0096 |

## Per-round trajectory (best bird: FM8Uw)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 910 | 6713 | 2.7511 | +0.2301 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r909_sym24`

## Output

`workers/dispatcher/harvest-1way-r910_sym24/round-910/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

