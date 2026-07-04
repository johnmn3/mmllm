# harvest-1way-r841 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R841 ctrl_bpc |
|--------|--------|--------------:|
| dRieZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-180db8c2-dRieZ | 3.3303 |
| **mean** | | **3.3303** |
| **best** | | **3.3303** |

## Chain progression R840 → R841

Previous harvest: `workers/dispatcher/harvest-1way-r840_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1526         | 3.3303         | +0.1777 |
| ctrl_bpc best  | 3.1526         | 3.3303         | +0.1777 |

## Per-round trajectory (best bird: dRieZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 841 | 4430 | 3.3303 | +0.4065 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r840_sym24`

## Output

`workers/dispatcher/harvest-1way-r841_sym24/round-841/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

