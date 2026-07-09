# harvest-2way-r878 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R878 ctrl_bpc |
|--------|--------|--------------:|
| 7uLN8 | fork-joly-os-mmllm-claude-train-sym24-4d68acaf-7uLN8 | 2.8434 |
| AjafD | origin/claude/train-sym24-43831538-AjafD | 3.2227 |
| **mean** | | **3.0331** |
| **best** | | **2.8434** |

## Chain progression R877 → R878

Previous harvest: `workers/dispatcher/harvest-7way-r877_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9874         | 3.0331         | +0.0457 |
| ctrl_bpc best  | 2.8559         | 2.8434         | -0.0125 |

## Per-round trajectory (best bird: 7uLN8)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 878 | 6501 | 2.8434 | +0.3100 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r877_sym24`

## Output

`workers/dispatcher/harvest-2way-r878_sym24/round-878/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

