# harvest-2way-r1000 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1000 ctrl_bpc |
|--------|--------|--------------:|
| yEr2U | origin/claude/train-sym24-03fffc28-yEr2U | 2.5741 |
| bVZHH | fork-SeniorCareMarket-mmllm-claude-train-sym24-d5bac542-bVZHH | 2.7460 |
| **mean** | | **2.6601** |
| **best** | | **2.5741** |

## Chain progression R999 → R1000

Previous harvest: `workers/dispatcher/harvest-4way-r999_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.6289         | 2.6601         | +0.0312 |
| ctrl_bpc best  | 2.5863         | 2.5741         | -0.0122 |

## Per-round trajectory (best bird: yEr2U)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1000 | 6653 | 2.5741 | +0.1730 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r999_sym24`

## Output

`workers/dispatcher/harvest-2way-r1000_sym24/round-1000/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

