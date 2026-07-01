# harvest-7way-r820 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R820 ctrl_bpc |
|--------|--------|--------------:|
| Sddud | fork-joly-os-mmllm-claude-train-sym24-ecb1556e-Sddud | 3.0266 |
| uR8Fn | fork-SeniorCareMarket-mmllm-claude-train-sym24-66b5caaa-uR8Fn | 3.0330 |
| 6ysxB | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6a4d1e97-6ysxB | 3.0409 |
| aEdhQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-7213d2d0-aEdhQ | 3.0414 |
| j7L5F | fork-slaa-us-mmllm-claude-train-sym24-334781d7-j7L5F | 3.1541 |
| jZ9mB | fork-slaa-us-mmllm-claude-train-sym24-60071c17-jZ9mB | 3.1562 |
| 0bFG4 | origin/claude/train-sym24-2ed1f8f3-0bFG4 | 3.3991 |
| **mean** | | **3.1216** |
| **best** | | **3.0266** |

## Chain progression R819 → R820

Previous harvest: `workers/dispatcher/harvest-11way-r819_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1748         | 3.1216         | -0.0532 |
| ctrl_bpc best  | 3.0247         | 3.0266         | +0.0019 |

## Per-round trajectory (best bird: Sddud)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 820 | 6779 | 3.0266 | +0.5065 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r819_sym24`

## Output

`workers/dispatcher/harvest-7way-r820_sym24/round-820/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

