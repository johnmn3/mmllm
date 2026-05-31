# harvest-3way-r116 — sparse-delta merge of 3 birds

## Worker endpoints

| handle | branch | R116 ctrl_bpc |
|--------|--------|--------------:|
| yYtvm | fork-joly-os-mmllm-claude-train-sym24-b058972d-yYtvm | 2.8642 |
| Lwnd7 | fork-davidwuchn-mmllm-claude-train-sym24-4ee73387-Lwnd7 | 3.1643 |
| DOSE1 | origin/claude/train-sym24-0a8871f0-DOSE1 | 3.2477 |
| **mean** | | **3.0921** |
| **best** | | **2.8642** |

## Chain progression R114 → R116

Previous harvest: `workers/dispatcher/harvest-2way-r114_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2036         | 3.0921         | -0.1115 |
| ctrl_bpc best  | 3.1696         | 2.8642         | -0.3054 |

## Per-round trajectory (best bird: yYtvm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 115 | 1194 | 2.8595 | +0.0519 |
| 116 | 1209 | 2.8642 | +0.0507 |

## Cumulative training contribution

- This harvest: **60 steps** from 3 bird(s)
- Across full ancestry (deduped by bird_id): **140 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r114_sym24`

## Output

`workers/dispatcher/harvest-3way-r116_sym24/round-116/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 3 workers)
- `dense.pt` (averaged across 3 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

