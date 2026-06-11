# harvest-1way-r652 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R652 ctrl_bpc |
|--------|--------|--------------:|
| PjyVM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-587f38c1-PjyVM | 4.2079 |
| **mean** | | **4.2079** |
| **best** | | **4.2079** |

## Chain progression R651 → R652

Previous harvest: `workers/dispatcher/harvest-5way-r651_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.2619         | 4.2079         | -0.0540 |
| ctrl_bpc best  | 4.2378         | 4.2079         | -0.0299 |

## Per-round trajectory (best bird: PjyVM)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 652 | 4433 | 4.2079 | +0.0759 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-5way-r651_sym24`

## Output

`workers/dispatcher/harvest-1way-r652_sym24/round-652/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

