# harvest-2way-r845 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R845 ctrl_bpc |
|--------|--------|--------------:|
| lKWuC | fork-slaa-us-mmllm-claude-train-sym24-8e114bda-lKWuC | 2.9493 |
| OH2a7 | origin/claude/train-sym24-d971c400-OH2a7 | 3.1131 |
| **mean** | | **3.0312** |
| **best** | | **2.9493** |

## Chain progression R844 → R845

Previous harvest: `workers/dispatcher/harvest-5way-r844_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1018         | 3.0312         | -0.0706 |
| ctrl_bpc best  | 2.9499         | 2.9493         | -0.0006 |

## Per-round trajectory (best bird: lKWuC)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 845 | 3662 | 2.9493 | +0.2351 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r844_sym24`

## Output

`workers/dispatcher/harvest-2way-r845_sym24/round-845/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

