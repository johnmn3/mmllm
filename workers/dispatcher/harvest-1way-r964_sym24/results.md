# harvest-1way-r964 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R964 ctrl_bpc |
|--------|--------|--------------:|
| KrLFO | origin/claude/train-sym24-f4707f43-KrLFO | 3.0202 |
| **mean** | | **3.0202** |
| **best** | | **3.0202** |

## Chain progression R963 → R964

Previous harvest: `workers/dispatcher/harvest-4way-r963_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8691         | 3.0202         | +0.1511 |
| ctrl_bpc best  | 2.8219         | 3.0202         | +0.1983 |

## Per-round trajectory (best bird: KrLFO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 964 | 4243 | 3.0202 | +0.1406 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r963_sym24`

## Output

`workers/dispatcher/harvest-1way-r964_sym24/round-964/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

