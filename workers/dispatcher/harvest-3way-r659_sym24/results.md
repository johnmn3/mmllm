# harvest-3way-r659 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R659 ctrl_bpc |
|--------|--------|--------------:|
| 0I0kU | origin/claude/train-sym24-289952cd-0I0kU | 4.0764 |
| HFjFf | fork-SeniorCareMarket-mmllm-claude-train-sym24-85a7a004-HFjFf | 4.0825 |
| nBfq2 | fork-joly-os-mmllm-claude-train-sym24-d375d677-nBfq2 | 4.1041 |
| **mean** | | **4.0877** |
| **best** | | **4.0764** |

## Chain progression R658 → R659

Previous harvest: `workers/dispatcher/harvest-6way-r658_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.1495         | 4.0877         | -0.0618 |
| ctrl_bpc best  | 4.0878         | 4.0764         | -0.0114 |

## Per-round trajectory (best bird: 0I0kU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 659 | 6561 | 4.0764 | +0.0773 |

## Cumulative training contribution

- This harvest: **240 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r658_sym24`

## Output

`workers/dispatcher/harvest-3way-r659_sym24/round-659/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

