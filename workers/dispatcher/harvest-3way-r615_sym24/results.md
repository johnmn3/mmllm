# harvest-3way-r615 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R615 ctrl_bpc |
|--------|--------|--------------:|
| Ecxvb | fork-slaa-us-mmllm-claude-train-sym24-87858252-Ecxvb | 2.1282 |
| mWCOK | origin/claude/train-sym24-abd2ca5d-mWCOK | 2.1480 |
| CCohx | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ccdf857f-CCohx | 2.5937 |
| **mean** | | **2.2900** |
| **best** | | **2.1282** |

## Chain progression R614 → R615

Previous harvest: `workers/dispatcher/harvest-1way-r614_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1483         | 2.2900         | +0.1417 |
| ctrl_bpc best  | 2.1483         | 2.1282         | -0.0201 |

## Per-round trajectory (best bird: Ecxvb)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 615 | 5405 | 2.1282 | +0.0263 |

## Cumulative training contribution

- This harvest: **150 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **450 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r614_sym24`

## Output

`workers/dispatcher/harvest-3way-r615_sym24/round-615/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

