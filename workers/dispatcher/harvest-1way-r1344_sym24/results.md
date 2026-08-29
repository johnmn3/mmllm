# harvest-1way-r1344 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1344 ctrl_bpc |
|--------|--------|--------------:|
| GQryj | fork-slaa-us-mmllm-claude-train-sym24-ab5dd27c-GQryj | 3.2132 |
| **mean** | | **3.2132** |
| **best** | | **3.2132** |

## Chain progression R610 → R1344

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.2132         | +1.0760 |
| ctrl_bpc best  | 2.1268         | 3.2132         | +1.0864 |

## Per-round trajectory (best bird: GQryj)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1344 | 5554 | 3.2132 | +0.0963 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **80 steps** from 1 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1343_sym24`

## Output

`workers/dispatcher/harvest-1way-r1344_sym24/round-1344/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

