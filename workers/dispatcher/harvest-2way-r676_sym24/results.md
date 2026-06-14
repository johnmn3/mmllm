# harvest-2way-r676 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R676 ctrl_bpc |
|--------|--------|--------------:|
| SblWU | fork-slaa-us-mmllm-claude-train-sym24-ee95c01f-SblWU | 3.8947 |
| nbgJ2 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-cffb0019-nbgJ2 | 3.9135 |
| **mean** | | **3.9041** |
| **best** | | **3.8947** |

## Chain progression R675 → R676

Previous harvest: `workers/dispatcher/harvest-8way-r675_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.9070         | 3.9041         | -0.0029 |
| ctrl_bpc best  | 3.8172         | 3.8947         | +0.0775 |

## Per-round trajectory (best bird: SblWU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 676 | 6409 | 3.8947 | +0.2089 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **400 steps** from 5 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r675_sym24`

## Output

`workers/dispatcher/harvest-2way-r676_sym24/round-676/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

