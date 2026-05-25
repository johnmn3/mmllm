# harvest-4way-r126 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R126 ctrl_bpc |
|--------|--------|--------------:|
| KGE3e | origin/claude/train-7e2ba70a-KGE3e | 1.3243 |
| y6A1S | fork-joly-os-mmllm-claude-train-0c901e7b-y6A1S | 1.3850 |
| GVhjF | fork-slaa-us-mmllm-claude-train-51ce0deb-GVhjF | 1.4209 |
| LKAKO | fork-SeniorCareMarket-com-mmllm-claude-train-2d3d9a88-LKAKO | 1.4857 |
| **mean** | | **1.4040** |
| **best** | | **1.3243** |

## Chain progression R124 → R126

Previous harvest: `workers/dispatcher/harvest-fold4way-r124`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 1.5426         | 1.4040         | -0.1386 |
| ctrl_bpc best  | 1.3377         | 1.3243         | -0.0134 |

## Per-round trajectory (best bird: KGE3e)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 122 | 672 | 1.3287 | +0.0023 |
| 123 | 610 | 1.3632 | +0.0084 |
| 124 | 511 | 1.3462 | +0.0026 |
| 125 | 544 | 1.2905 | +0.0182 |
| 126 | 547 | 1.3243 | -0.0026 |

## Cumulative training contribution

- This harvest: **140 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **3187 steps** from 85 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-7way-r121`

## Output

`workers/dispatcher/harvest-4way-r126/round-126/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-5way-r10/round-10`

