# harvest-2way-r1038 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1038 ctrl_bpc |
|--------|--------|--------------:|
| lIP4v | origin/claude/train-sym24-4124fad4-lIP4v | 2.5060 |
| QYJAz | origin/claude/train-sym24-d4ad9ceb-QYJAz | 2.8769 |
| **mean** | | **2.6914** |
| **best** | | **2.5060** |

## Chain progression R1037 → R1038

Previous harvest: `workers/dispatcher/harvest-2way-r1037_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5354         | 2.6914         | +0.1560 |
| ctrl_bpc best  | 2.5136         | 2.5060         | -0.0076 |

## Per-round trajectory (best bird: lIP4v)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1038 | 5357 | 2.5060 | +0.1819 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1037_sym24`

## Output

`workers/dispatcher/harvest-2way-r1038_sym24/round-1038/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

