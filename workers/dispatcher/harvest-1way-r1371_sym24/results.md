# harvest-1way-r1371 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1371 ctrl_bpc |
|--------|--------|--------------:|
| BKnxs | origin/claude/train-sym24-8a175792-BKnxs | 3.2121 |
| **mean** | | **3.2121** |
| **best** | | **3.2121** |

## Chain progression R1370 → R1371

Previous harvest: `workers/dispatcher/harvest-3way-r1370_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2657         | 3.2121         | -0.0536 |
| ctrl_bpc best  | 3.1133         | 3.2121         | +0.0988 |

## Per-round trajectory (best bird: BKnxs)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1371 | 6509 | 3.2121 | +0.1143 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1370_sym24`

## Output

`workers/dispatcher/harvest-1way-r1371_sym24/round-1371/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

