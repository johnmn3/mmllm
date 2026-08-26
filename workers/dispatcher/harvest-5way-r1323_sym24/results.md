# harvest-5way-r1323 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1323 ctrl_bpc |
|--------|--------|--------------:|
| t2Utm | fork-SeniorCareMarket-mmllm-claude-train-sym24-38588e8c-t2Utm | 3.4185 |
| MWOqP | fork-slaa-us-mmllm-claude-train-sym24-c308efae-MWOqP | 3.4424 |
| mVgJG | origin/claude/train-sym24-9de397a7-mVgJG | 3.7329 |
| BYnSm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8a7c17c8-BYnSm | 3.7410 |
| pbMHf | fork-joly-os-mmllm-claude-train-sym24-ddfcdf6b-pbMHf | 3.7506 |
| **mean** | | **3.6171** |
| **best** | | **3.4185** |

## Chain progression R1322 → R1323

Previous harvest: `workers/dispatcher/harvest-5way-r1322_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.4867         | 3.6171         | +0.1304 |
| ctrl_bpc best  | 3.4065         | 3.4185         | +0.0120 |

## Per-round trajectory (best bird: t2Utm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1323 | 6278 | 3.4185 | +0.0655 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1322_sym24`

## Output

`workers/dispatcher/harvest-5way-r1323_sym24/round-1323/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

