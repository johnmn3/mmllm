# harvest-1way-r25 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R25 ctrl_bpc |
|--------|--------|--------------:|
| blah1 | origin/claude/smoke-r25-blah1 | 1.1872 |
| **mean** | | **1.1872** |
| **best** | | **1.1872** |

## Chain progression R22 → R25

Previous harvest: `workers/dispatcher/harvest-3way-r22`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.3162         | 1.1872         | -0.1290 |
| ctrl_bpc best  | 1.2928         | 1.1872         | -0.1056 |

## Per-round trajectory (best bird: blah1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 23 | 572 | 1.2244 | +0.0078 |
| 24 | 559 | 1.2395 | +0.0091 |
| 25 | 612 | 1.1872 | +0.0086 |

## Cumulative training contribution

- This harvest: **21 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **21 steps** from 1 unique bird(s)

## Output

`workers/dispatcher/harvest-1way-r25/round-25/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

