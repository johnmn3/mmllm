# harvest-2way-r638 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R638 ctrl_bpc |
|--------|--------|--------------:|
| CIFIX3 | origin/claude/train-sym24-ee404a1d-CIFIX3 | 11.4569 |
| CIFIX2 | origin/claude/train-sym24-8b62a1da-CIFIX2 | 17.0747 |
| **mean** | | **14.2658** |
| **best** | | **11.4569** |

## Chain progression R634 → R638

Previous harvest: `workers/dispatcher/harvest-1way-r634_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5945         | 14.2658         | +11.6713 |
| ctrl_bpc best  | 2.5945         | 11.4569         | +8.8624 |

## Per-round trajectory (best bird: CIFIX3)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 638 | 368 | 11.4569 | -0.0098 |

## Cumulative training contribution

- This harvest: **16 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **16 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-merge-r637_sym24`

## Output

`workers/dispatcher/harvest-2way-r638_sym24/round-638/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

