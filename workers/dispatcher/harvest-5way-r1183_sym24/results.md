# harvest-5way-r1183 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1183 ctrl_bpc |
|--------|--------|--------------:|
| BI83R | fork-slaa-us-mmllm-claude-train-sym24-8201986f-BI83R | 2.3234 |
| gjqxF | origin/claude/train-sym24-22dfc7a6-gjqxF | 2.3330 |
| PkLII | fork-joly-os-mmllm-claude-train-sym24-cac30855-PkLII | 2.5004 |
| s3WI7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8d7dfe43-s3WI7 | 2.5082 |
| UjaWD | fork-SeniorCareMarket-mmllm-claude-train-sym24-c707da69-UjaWD | 2.6842 |
| **mean** | | **2.4698** |
| **best** | | **2.3234** |

## Chain progression R1182 → R1183

Previous harvest: `workers/dispatcher/harvest-4way-r1182_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5068         | 2.4698         | -0.0370 |
| ctrl_bpc best  | 2.3076         | 2.3234         | +0.0158 |

## Per-round trajectory (best bird: BI83R)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1183 | 6771 | 2.3234 | +0.2481 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1182_sym24`

## Output

`workers/dispatcher/harvest-5way-r1183_sym24/round-1183/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

