# harvest-2way-r1352 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1352 ctrl_bpc |
|--------|--------|--------------:|
| WPY5x | origin/claude/train-sym24-758d4751-WPY5x | 3.2384 |
| EQMIa | origin/claude/train-sym24-88ad1c41-EQMIa | 3.2436 |
| **mean** | | **3.2410** |
| **best** | | **3.2384** |

## Chain progression R1351 → R1352

Previous harvest: `workers/dispatcher/harvest-4way-r1351_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2788         | 3.2410         | -0.0378 |
| ctrl_bpc best  | 3.2310         | 3.2384         | +0.0074 |

## Per-round trajectory (best bird: WPY5x)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1352 | 6302 | 3.2384 | +0.1059 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1351_sym24`
  - `workers/dispatcher/harvest-3way-r1351_sym24`

## Output

`workers/dispatcher/harvest-2way-r1352_sym24/round-1352/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

