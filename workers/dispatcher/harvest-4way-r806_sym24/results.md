# harvest-4way-r806 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R806 ctrl_bpc |
|--------|--------|--------------:|
| Amwsp | origin/claude/train-sym24-57a67d5e-Amwsp | 3.0967 |
| nSv52 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-34c9889a-nSv52 | 3.1000 |
| Dx7Gs | fork-joly-os-mmllm-claude-train-sym24-3ed89c1c-Dx7Gs | 3.2113 |
| nQCQt | origin/claude/train-sym24-9342aaa3-nQCQt | 3.2176 |
| **mean** | | **3.1564** |
| **best** | | **3.0967** |

## Chain progression R805 → R806

Previous harvest: `workers/dispatcher/harvest-5way-r805_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.1507         | 3.1564         | +0.0057 |
| ctrl_bpc best  | 3.0971         | 3.0967         | -0.0004 |

## Per-round trajectory (best bird: Amwsp)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 806 | 6507 | 3.0967 | +0.5726 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **880 steps** from 11 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r805_sym24`
  - `workers/dispatcher/harvest-5way-r805_sym24`

## Output

`workers/dispatcher/harvest-4way-r806_sym24/round-806/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

