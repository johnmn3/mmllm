# harvest-6way-r842 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R842 ctrl_bpc |
|--------|--------|--------------:|
| XFyTv | fork-slaa-us-mmllm-claude-train-sym24-dee2f6d1-XFyTv | 2.9529 |
| Vnqn5 | fork-joly-os-mmllm-claude-train-sym24-537a2fb9-Vnqn5 | 2.9598 |
| uZA4F | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f63c6e9c-uZA4F | 2.9605 |
| 4Jqzp | origin/claude/train-sym24-1a346a0f-4Jqzp | 2.9869 |
| coj41 | fork-joly-os-mmllm-claude-train-sym24-dfbd2661-coj41 | 3.0974 |
| QXBre | fork-SeniorCareMarket-mmllm-claude-train-sym24-8d18ba46-QXBre | 3.3426 |
| **mean** | | **3.0500** |
| **best** | | **2.9529** |

## Chain progression R841 → R842

Previous harvest: `workers/dispatcher/harvest-5way-r841_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1685         | 3.0500         | -0.1185 |
| ctrl_bpc best  | 2.9606         | 2.9529         | -0.0077 |

## Per-round trajectory (best bird: XFyTv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 842 | 6546 | 2.9529 | +0.4400 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r841_sym24`
  - `workers/dispatcher/harvest-5way-r841_sym24`

## Output

`workers/dispatcher/harvest-6way-r842_sym24/round-842/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

