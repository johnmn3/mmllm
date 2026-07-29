# harvest-1way-r1054 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1054 ctrl_bpc |
|--------|--------|--------------:|
| YDRi9 | origin/claude/train-sym24-b7a9179b-YDRi9 | 2.8569 |
| **mean** | | **2.8569** |
| **best** | | **2.8569** |

## Chain progression R1053 → R1054

Previous harvest: `workers/dispatcher/harvest-6way-r1053_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6111         | 2.8569         | +0.2458 |
| ctrl_bpc best  | 2.4584         | 2.8569         | +0.3985 |

## Per-round trajectory (best bird: YDRi9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1054 | 5234 | 2.8569 | +0.1861 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1053_sym24`

## Output

`workers/dispatcher/harvest-1way-r1054_sym24/round-1054/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

