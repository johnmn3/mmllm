# harvest-1way-r999 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R999 ctrl_bpc |
|--------|--------|--------------:|
| SNZig | origin/claude/train-sym24-7e3054c5-SNZig | 2.5863 |
| **mean** | | **2.5863** |
| **best** | | **2.5863** |

## Chain progression R998 → R999

Previous harvest: `workers/dispatcher/harvest-5way-r998_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8516         | 2.5863         | -0.2653 |
| ctrl_bpc best  | 2.5736         | 2.5863         | +0.0127 |

## Per-round trajectory (best bird: SNZig)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 999 | 6469 | 2.5863 | +0.1603 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r998_sym24`

## Output

`workers/dispatcher/harvest-1way-r999_sym24/round-999/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

