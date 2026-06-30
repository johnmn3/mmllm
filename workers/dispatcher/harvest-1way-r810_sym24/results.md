# harvest-1way-r810 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R810 ctrl_bpc |
|--------|--------|--------------:|
| IB98R | fork-slaa-us-mmllm-claude-train-sym24-66bd0b9f-IB98R | 3.4509 |
| **mean** | | **3.4509** |
| **best** | | **3.4509** |

## Chain progression R809 → R810

Previous harvest: `workers/dispatcher/harvest-2way-r809_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3095         | 3.4509         | +0.1414 |
| ctrl_bpc best  | 3.1896         | 3.4509         | +0.2613 |

## Per-round trajectory (best bird: IB98R)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 810 | 5141 | 3.4509 | +0.4953 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r809_sym24`

## Output

`workers/dispatcher/harvest-1way-r810_sym24/round-810/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

