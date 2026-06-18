# harvest-1way-r705 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R705 ctrl_bpc |
|--------|--------|--------------:|
| yQZl4 | fork-slaa-us-mmllm-claude-train-sym24-574c59f2-yQZl4 | 3.6627 |
| **mean** | | **3.6627** |
| **best** | | **3.6627** |

## Chain progression R704 → R705

Previous harvest: `workers/dispatcher/harvest-1way-r704_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5994         | 3.6627         | +0.0633 |
| ctrl_bpc best  | 3.5994         | 3.6627         | +0.0633 |

## Per-round trajectory (best bird: yQZl4)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 705 | 6426 | 3.6627 | +0.6293 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r704_sym24`

## Output

`workers/dispatcher/harvest-1way-r705_sym24/round-705/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

