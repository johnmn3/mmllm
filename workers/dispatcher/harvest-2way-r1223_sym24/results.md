# harvest-2way-r1223 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1223 ctrl_bpc |
|--------|--------|--------------:|
| pJrlg | origin/claude/train-sym24-f20b7b22-pJrlg | 2.2768 |
| t8thk | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-be7f0dda-t8thk | 2.2873 |
| **mean** | | **2.2820** |
| **best** | | **2.2768** |

## Chain progression R1222 → R1223

Previous harvest: `workers/dispatcher/harvest-5way-r1222_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3487         | 2.2820         | -0.0667 |
| ctrl_bpc best  | 2.2577         | 2.2768         | +0.0191 |

## Per-round trajectory (best bird: pJrlg)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1223 | 6527 | 2.2768 | +0.2481 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **240 steps** from 3 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1222_sym24`

## Output

`workers/dispatcher/harvest-2way-r1223_sym24/round-1223/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

