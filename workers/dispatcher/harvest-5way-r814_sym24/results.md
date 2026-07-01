# harvest-5way-r814 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R814 ctrl_bpc |
|--------|--------|--------------:|
| 4Jdn1 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-fcc7f02d-4Jdn1 | 3.0590 |
| XLWLt | fork-slaa-us-mmllm-claude-train-sym24-074c6f90-XLWLt | 3.0656 |
| W0sts | fork-joly-os-mmllm-claude-train-sym24-e60572d9-W0sts | 3.0733 |
| mDw58 | fork-SeniorCareMarket-mmllm-claude-train-sym24-f4bbae07-mDw58 | 3.1807 |
| MMF7T | origin/claude/train-sym24-077c2902-MMF7T | 3.1852 |
| **mean** | | **3.1128** |
| **best** | | **3.0590** |

## Chain progression R813 → R814

Previous harvest: `workers/dispatcher/harvest-5way-r813_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2120         | 3.1128         | -0.0992 |
| ctrl_bpc best  | 3.0582         | 3.0590         | +0.0008 |

## Per-round trajectory (best bird: 4Jdn1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 814 | 6378 | 3.0590 | +0.4975 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r813_sym24`

## Output

`workers/dispatcher/harvest-5way-r814_sym24/round-814/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

