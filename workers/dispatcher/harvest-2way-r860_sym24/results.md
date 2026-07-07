# harvest-2way-r860 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R860 ctrl_bpc |
|--------|--------|--------------:|
| a1gR6 | fork-SeniorCareMarket-mmllm-claude-train-sym24-27538893-a1gR6 | 2.8907 |
| j7nW8 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-14b3c07c-j7nW8 | 2.9004 |
| **mean** | | **2.8956** |
| **best** | | **2.8907** |

## Chain progression R859 → R860

Previous harvest: `workers/dispatcher/harvest-6way-r859_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9351         | 2.8956         | -0.0395 |
| ctrl_bpc best  | 2.8979         | 2.8907         | -0.0072 |

## Per-round trajectory (best bird: a1gR6)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 860 | 6700 | 2.8907 | +0.5230 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **1040 steps** from 13 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-6way-r859_sym24`

## Output

`workers/dispatcher/harvest-2way-r860_sym24/round-860/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

