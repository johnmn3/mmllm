# harvest-1way-r866 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R866 ctrl_bpc |
|--------|--------|--------------:|
| 5bUOS | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-e0e73814-5bUOS | 2.9291 |
| **mean** | | **2.9291** |
| **best** | | **2.9291** |

## Chain progression R865 → R866

Previous harvest: `workers/dispatcher/harvest-8way-r865_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.0480         | 2.9291         | -0.1189 |
| ctrl_bpc best  | 2.8693         | 2.9291         | +0.0598 |

## Per-round trajectory (best bird: 5bUOS)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 866 | 6427 | 2.9291 | +0.2886 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r865_sym24`

## Output

`workers/dispatcher/harvest-1way-r866_sym24/round-866/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

