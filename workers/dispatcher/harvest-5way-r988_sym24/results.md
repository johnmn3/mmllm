# harvest-5way-r988 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R988 ctrl_bpc |
|--------|--------|--------------:|
| Jbt9L | origin/claude/train-sym24-2faeb5a9-Jbt9L | 2.5960 |
| Ot8oJ | fork-slaa-us-mmllm-claude-train-sym24-bc58f975-Ot8oJ | 2.6118 |
| E4qbn | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-139e215e-E4qbn | 2.7715 |
| r9lpE | fork-joly-os-mmllm-claude-train-sym24-e8e76820-r9lpE | 2.8005 |
| pHqnb | origin/claude/train-sym24-dbe4d10d-pHqnb | 2.9822 |
| **mean** | | **2.7524** |
| **best** | | **2.5960** |

## Chain progression R987 → R988

Previous harvest: `workers/dispatcher/harvest-5way-r987_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6106         | 2.7524         | +0.1418 |
| ctrl_bpc best  | 2.5988         | 2.5960         | -0.0028 |

## Per-round trajectory (best bird: Jbt9L)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 988 | 4212 | 2.5960 | +0.1577 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r987_sym24`

## Output

`workers/dispatcher/harvest-5way-r988_sym24/round-988/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

