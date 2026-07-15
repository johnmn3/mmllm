# harvest-1way-r927 — sparse-delta merge of 1 birds

## Worker endpoints

| handle | branch | R927 ctrl_bpc |
|--------|--------|--------------:|
| gmPQU | fork-SeniorCareMarket-mmllm-claude-train-sym24-448d08ba-gmPQU | 2.7396 |
| **mean** | | **2.7396** |
| **best** | | **2.7396** |

## Chain progression R926 → R927

Previous harvest: `workers/dispatcher/harvest-4way-r926_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9775         | 2.7396         | -0.2379 |
| ctrl_bpc best  | 2.7653         | 2.7396         | -0.0257 |

## Per-round trajectory (best bird: gmPQU)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 927 | 3659 | 2.7396 | +0.1557 |

## Cumulative training contribution

- This harvest: **80 steps** from 1 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r926_sym24`

## Output

`workers/dispatcher/harvest-1way-r927_sym24/round-927/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 1 workers)
- `dense.pt` (averaged across 1 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

