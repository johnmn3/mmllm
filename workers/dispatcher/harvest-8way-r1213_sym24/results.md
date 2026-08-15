# harvest-8way-r1213 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1213 ctrl_bpc |
|--------|--------|--------------:|
| P9TGB | fork-slaa-us-mmllm-claude-train-sym24-c5ff5730-P9TGB | 2.2718 |
| QXNMJ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-6305f377-QXNMJ | 2.3026 |
| 3f3b1 | origin/claude/train-sym24-4ac19592-3f3b1 | 2.4623 |
| gjbEi | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ab49dd6d-gjbEi | 2.4623 |
| du5zb | fork-SeniorCareMarket-mmllm-claude-train-sym24-d4187b68-du5zb | 2.4649 |
| pLIor | fork-SeniorCareMarket-mmllm-claude-train-sym24-eed7f87b-pLIor | 2.4673 |
| WBW9s | fork-joly-os-mmllm-claude-train-sym24-95b8af46-WBW9s | 2.4701 |
| nurcJ | fork-slaa-us-mmllm-claude-train-sym24-c0eb4db8-nurcJ | 2.6666 |
| **mean** | | **2.4460** |
| **best** | | **2.2718** |

## Chain progression R1212 → R1213

Previous harvest: `workers/dispatcher/harvest-3way-r1212_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4120         | 2.4460         | +0.0340 |
| ctrl_bpc best  | 2.2943         | 2.2718         | -0.0225 |

## Per-round trajectory (best bird: P9TGB)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1213 | 3647 | 2.2718 | +0.2813 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1212_sym24`
  - `workers/dispatcher/harvest-3way-r1212_sym24`

## Output

`workers/dispatcher/harvest-8way-r1213_sym24/round-1213/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

