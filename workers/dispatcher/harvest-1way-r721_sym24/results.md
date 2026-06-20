# harvest-1way-r721 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R721 ctrl_bpc |
|--------|--------|--------------:|
| M7VUV | fork-slaa-us-mmllm-claude-train-sym24-80964fc8-M7VUV | 3.8523 |
| **mean** | | **3.8523** |
| **best** | | **3.8523** |

## Chain progression R720 → R721

Previous harvest: `workers/dispatcher/harvest-1way-r720_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5431         | 3.8523         | +0.3092 |
| ctrl_bpc best  | 3.5431         | 3.8523         | +0.3092 |

## Per-round trajectory (best bird: M7VUV)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 721 | 4370 | 3.8523 | +0.9832 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **720 steps** from 9 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r720_sym24`

## Output

`workers/dispatcher/harvest-1way-r721_sym24/round-721/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

