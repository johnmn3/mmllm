# harvest-1way-r1411 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1411 ctrl_bpc |
|--------|--------|--------------:|
| pFrCF | origin/claude/train-sym24-02ba4f48-pFrCF | 3.3031 |
| **mean** | | **3.3031** |
| **best** | | **3.3031** |

## Chain progression R1410 → R1411

Previous harvest: `workers/dispatcher/harvest-1way-r1410_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.8414         | 3.3031         | -0.5383 |
| ctrl_bpc best  | 3.8414         | 3.3031         | -0.5383 |

## Per-round trajectory (best bird: pFrCF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1411 | 6209 | 3.3031 | +0.1724 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1410_sym24`

## Output

`workers/dispatcher/harvest-1way-r1411_sym24/round-1411/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

