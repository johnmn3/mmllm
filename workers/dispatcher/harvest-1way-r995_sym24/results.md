# harvest-1way-r995 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R995 ctrl_bpc |
|--------|--------|--------------:|
| xTso1 | fork-joly-os-mmllm-claude-train-sym24-e56a8dec-xTso1 | 2.7592 |
| **mean** | | **2.7592** |
| **best** | | **2.7592** |

## Chain progression R994 → R995

Previous harvest: `workers/dispatcher/harvest-4way-r994_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.7709         | 2.7592         | -0.0117 |
| ctrl_bpc best  | 2.5717         | 2.7592         | +0.1875 |

## Per-round trajectory (best bird: xTso1)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 995 | 4238 | 2.7592 | +0.1667 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **160 steps** from 2 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r994_sym24`

## Output

`workers/dispatcher/harvest-1way-r995_sym24/round-995/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

