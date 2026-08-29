# harvest-2way-r1345 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1345 ctrl_bpc |
|--------|--------|--------------:|
| t2Z4f | origin/claude/train-sym24-59c2efc0-t2Z4f | 3.2448 |
| eaY1v | origin/claude/train-sym24-f7676886-eaY1v | 3.2736 |
| **mean** | | **3.2592** |
| **best** | | **3.2448** |

## Chain progression R1344 → R1345

Previous harvest: `workers/dispatcher/harvest-3way-r1344_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2879         | 3.2592         | -0.0287 |
| ctrl_bpc best  | 3.2132         | 3.2448         | +0.0316 |

## Per-round trajectory (best bird: t2Z4f)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1345 | 6233 | 3.2448 | +0.1038 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1344_sym24`
  - `workers/dispatcher/harvest-3way-r1344_sym24`

## Output

`workers/dispatcher/harvest-2way-r1345_sym24/round-1345/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

