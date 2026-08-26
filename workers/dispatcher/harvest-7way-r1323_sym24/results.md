# harvest-7way-r1323 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1323 ctrl_bpc |
|--------|--------|--------------:|
| OPhD4 | origin/claude/train-sym24-99ab8e6d-OPhD4 | 3.3853 |
| byTYT | fork-joly-os-mmllm-claude-train-sym24-97e38418-byTYT | 3.4117 |
| t2Utm | fork-SeniorCareMarket-mmllm-claude-train-sym24-38588e8c-t2Utm | 3.4185 |
| MWOqP | fork-slaa-us-mmllm-claude-train-sym24-c308efae-MWOqP | 3.4424 |
| mVgJG | origin/claude/train-sym24-9de397a7-mVgJG | 3.7329 |
| BYnSm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8a7c17c8-BYnSm | 3.7410 |
| pbMHf | fork-joly-os-mmllm-claude-train-sym24-ddfcdf6b-pbMHf | 3.7506 |
| **mean** | | **3.5546** |
| **best** | | **3.3853** |

## Chain progression R1322 → R1323

Previous harvest: `workers/dispatcher/harvest-5way-r1322_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4867         | 3.5546         | +0.0679 |
| ctrl_bpc best  | 3.4065         | 3.3853         | -0.0212 |

## Per-round trajectory (best bird: OPhD4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1323 | 5248 | 3.3853 | +0.0628 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1322_sym24`
  - `workers/dispatcher/harvest-5way-r1322_sym24`

## Output

`workers/dispatcher/harvest-7way-r1323_sym24/round-1323/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

