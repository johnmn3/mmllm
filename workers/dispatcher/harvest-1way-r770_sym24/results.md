# harvest-1way-r770 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R770 ctrl_bpc |
|--------|--------|--------------:|
| aGTS9 | origin/claude/train-sym24-2ed42e6a-aGTS9 | 3.2739 |
| **mean** | | **3.2739** |
| **best** | | **3.2739** |

## Chain progression R769 → R770

Previous harvest: `workers/dispatcher/harvest-5way-r769_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3439         | 3.2739         | -0.0700 |
| ctrl_bpc best  | 3.2235         | 3.2739         | +0.0504 |

## Per-round trajectory (best bird: aGTS9)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 770 | 6635 | 3.2739 | +0.5398 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r769_sym24`

## Output

`workers/dispatcher/harvest-1way-r770_sym24/round-770/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

