# harvest-2way-r856 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R856 ctrl_bpc |
|--------|--------|--------------:|
| V77EH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f7213d7d-V77EH | 2.9060 |
| JGA8B | fork-slaa-us-mmllm-claude-train-sym24-498fca7f-JGA8B | 3.0759 |
| **mean** | | **2.9909** |
| **best** | | **2.9060** |

## Chain progression R855 → R856

Previous harvest: `workers/dispatcher/harvest-3way-r855_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1722         | 2.9909         | -0.1813 |
| ctrl_bpc best  | 2.9259         | 2.9060         | -0.0199 |

## Per-round trajectory (best bird: V77EH)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 856 | 6592 | 2.9060 | +0.2705 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r855_sym24`

## Output

`workers/dispatcher/harvest-2way-r856_sym24/round-856/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

