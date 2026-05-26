# harvest-2way-r183 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R183 ctrl_bpc |
|--------|--------|--------------:|
| X3cmJ | origin/claude/train-39fef1ec-X3cmJ | 1.1046 |
| XzGIa | origin/claude/train-2eb06089-XzGIa | 1.1729 |
| **mean** | | **1.1387** |
| **best** | | **1.1046** |

## Chain progression R182 → R183

Previous harvest: `workers/dispatcher/harvest-1way-r182`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.1746         | 1.1387         | -0.0359 |
| ctrl_bpc best  | 1.1746         | 1.1046         | -0.0700 |

## Per-round trajectory (best bird: X3cmJ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 179 | 613 | 1.1567 | +0.0034 |
| 180 | 548 | 1.1165 | +0.0064 |
| 181 | 555 | 1.1331 | +0.0022 |
| 182 | 559 | 1.0936 | +0.0017 |
| 183 | 522 | 1.1046 | +0.0041 |

## Cumulative training contribution

- This harvest: **42 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **3663 steps** from 101 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r178`
  - `workers/dispatcher/harvest-1way-r182`

## Output

`workers/dispatcher/harvest-2way-r183/round-183/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

