# harvest-4way-r861 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R861 ctrl_bpc |
|--------|--------|--------------:|
| Binqf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-90655b9f-Binqf | 2.8882 |
| ptG0K | origin/claude/train-sym24-a021124f-ptG0K | 2.8887 |
| 2Jt74 | fork-slaa-us-mmllm-claude-train-sym24-13ac2e05-2Jt74 | 2.8897 |
| tlpmu | fork-SeniorCareMarket-mmllm-claude-train-sym24-28dbe938-tlpmu | 2.8958 |
| **mean** | | **2.8906** |
| **best** | | **2.8882** |

## Chain progression R860 → R861

Previous harvest: `workers/dispatcher/harvest-2way-r860_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8956         | 2.8906         | -0.0050 |
| ctrl_bpc best  | 2.8907         | 2.8882         | -0.0025 |

## Per-round trajectory (best bird: Binqf)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 861 | 6511 | 2.8882 | +0.3328 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r860_sym24`

## Output

`workers/dispatcher/harvest-4way-r861_sym24/round-861/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

