# harvest-1way-r698 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R698 ctrl_bpc |
|--------|--------|--------------:|
| vKbQh | origin/claude/train-sym24-35921d64-vKbQh | 3.9762 |
| **mean** | | **3.9762** |
| **best** | | **3.9762** |

## Chain progression R697 → R698

Previous harvest: `workers/dispatcher/harvest-1way-r697_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.6939         | 3.9762         | +0.2823 |
| ctrl_bpc best  | 3.6939         | 3.9762         | +0.2823 |

## Per-round trajectory (best bird: vKbQh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 698 | 4360 | 3.9762 | +0.7991 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r697_sym24`

## Output

`workers/dispatcher/harvest-1way-r698_sym24/round-698/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

