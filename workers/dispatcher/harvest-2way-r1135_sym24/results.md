# harvest-2way-r1135 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1135 ctrl_bpc |
|--------|--------|--------------:|
| BKcva | origin/claude/train-sym24-8da0386b-BKcva | 2.3584 |
| 6JAAD | fork-joly-os-mmllm-claude-train-sym24-158039ec-6JAAD | 2.3718 |
| **mean** | | **2.3651** |
| **best** | | **2.3584** |

## Chain progression R1134 → R1135

Previous harvest: `workers/dispatcher/harvest-5way-r1134_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5507         | 2.3651         | -0.1856 |
| ctrl_bpc best  | 2.3468         | 2.3584         | +0.0116 |

## Per-round trajectory (best bird: BKcva)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1135 | 3648 | 2.3584 | +0.2374 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1134_sym24`

## Output

`workers/dispatcher/harvest-2way-r1135_sym24/round-1135/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

