# harvest-8way-r806 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R806 ctrl_bpc |
|--------|--------|--------------:|
| TAPK6 | fork-slaa-us-mmllm-claude-train-sym24-cca0426a-TAPK6 | 3.0659 |
| jDxmK | fork-davidwuchn-mmllm-claude-train-sym24-36ba3561-jDxmK | 3.0868 |
| Amwsp | origin/claude/train-sym24-57a67d5e-Amwsp | 3.0967 |
| HsYZ1 | fork-joly-os-mmllm-claude-train-sym24-a5e6e153-HsYZ1 | 3.0995 |
| nSv52 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-34c9889a-nSv52 | 3.1000 |
| Dx7Gs | fork-joly-os-mmllm-claude-train-sym24-3ed89c1c-Dx7Gs | 3.2113 |
| nQCQt | origin/claude/train-sym24-9342aaa3-nQCQt | 3.2176 |
| AfPyY | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-0ffb76ff-AfPyY | 3.4692 |
| **mean** | | **3.1684** |
| **best** | | **3.0659** |

## Chain progression R805 → R806

Previous harvest: `workers/dispatcher/harvest-5way-r805_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1507         | 3.1684         | +0.0177 |
| ctrl_bpc best  | 3.0971         | 3.0659         | -0.0312 |

## Per-round trajectory (best bird: TAPK6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 806 | 6621 | 3.0659 | +0.4858 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r805_sym24`
  - `workers/dispatcher/harvest-5way-r805_sym24`

## Output

`workers/dispatcher/harvest-8way-r806_sym24/round-806/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

