# harvest-3way-r842 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R842 ctrl_bpc |
|--------|--------|--------------:|
| uZA4F | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f63c6e9c-uZA4F | 2.9605 |
| coj41 | fork-joly-os-mmllm-claude-train-sym24-dfbd2661-coj41 | 3.0974 |
| QXBre | fork-SeniorCareMarket-mmllm-claude-train-sym24-8d18ba46-QXBre | 3.3426 |
| **mean** | | **3.1335** |
| **best** | | **2.9605** |

## Chain progression R841 → R842

Previous harvest: `workers/dispatcher/harvest-5way-r841_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1685         | 3.1335         | -0.0350 |
| ctrl_bpc best  | 2.9606         | 2.9605         | -0.0001 |

## Per-round trajectory (best bird: uZA4F)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 842 | 6694 | 2.9605 | +0.2819 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r841_sym24`

## Output

`workers/dispatcher/harvest-3way-r842_sym24/round-842/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

