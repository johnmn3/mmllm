# harvest-2way-r814 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R814 ctrl_bpc |
|--------|--------|--------------:|
| 4Jdn1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fcc7f02d-4Jdn1 | 3.0590 |
| MMF7T | origin/claude/train-sym24-077c2902-MMF7T | 3.1852 |
| **mean** | | **3.1221** |
| **best** | | **3.0590** |

## Chain progression R813 → R814

Previous harvest: `workers/dispatcher/harvest-5way-r813_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2120         | 3.1221         | -0.0899 |
| ctrl_bpc best  | 3.0582         | 3.0590         | +0.0008 |

## Per-round trajectory (best bird: 4Jdn1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 814 | 6378 | 3.0590 | +0.4975 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r813_sym24`

## Output

`workers/dispatcher/harvest-2way-r814_sym24/round-814/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

