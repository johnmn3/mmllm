# harvest-1way-r1032 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R1032 ctrl_bpc |
|--------|--------|--------------:|
| QbRGT | origin/claude/train-sym24-5199ac07-QbRGT | 2.8923 |
| **mean** | | **2.8923** |
| **best** | | **2.8923** |

## Chain progression R1031 → R1032

Previous harvest: `workers/dispatcher/harvest-5way-r1031_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5429         | 2.8923         | +0.3494 |
| ctrl_bpc best  | 2.4946         | 2.8923         | +0.3977 |

## Per-round trajectory (best bird: QbRGT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1032 | 6586 | 2.8923 | +0.1775 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1031_sym24`

## Output

`workers/dispatcher/harvest-1way-r1032_sym24/round-1032/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

