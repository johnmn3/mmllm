# harvest-11way-r1193 — sparse-delta merge of 11 birds

## Worker endpoints

| handle | branch | R1193 ctrl_bpc |
|--------|--------|--------------:|
| 3MwCx | fork-joly-os-mmllm-claude-train-sym24-dbc471a0-3MwCx | 2.2911 |
| 35WH2 | origin/claude/train-sym24-15616734-35WH2 | 2.2926 |
| PayJv | fork-slaa-us-mmllm-claude-train-sym24-455e459a-PayJv | 2.2982 |
| O1h6s | fork-slaa-us-mmllm-claude-train-sym24-e41eae3a-O1h6s | 2.2987 |
| yEXFT | origin/claude/train-sym24-91914b2f-yEXFT | 2.3101 |
| VuRgc | fork-joly-os-mmllm-claude-train-sym24-816d0e4f-VuRgc | 2.3117 |
| xDRjM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-30b5c9b1-xDRjM | 2.3137 |
| oiB0i | fork-SeniorCareMarket-mmllm-claude-train-sym24-c5d0b488-oiB0i | 2.3158 |
| XtYZO | fork-SeniorCareMarket-mmllm-claude-train-sym24-8324832a-XtYZO | 2.3179 |
| ToypL | origin/claude/train-sym24-78892369-ToypL | 2.6680 |
| FxuCl | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-71e8d7e5-FxuCl | 2.6905 |
| **mean** | | **2.3735** |
| **best** | | **2.2911** |

## Chain progression R1192 → R1193

Previous harvest: `workers/dispatcher/harvest-6way-r1192_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5233         | 2.3735         | -0.1498 |
| ctrl_bpc best  | 2.2912         | 2.2911         | -0.0001 |

## Per-round trajectory (best bird: 3MwCx)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1193 | 5445 | 2.2911 | +0.2795 |

## Cumulative training contribution

- This harvest: **880 steps** from 11 bird(s)
- Across full ancestry (deduped by bird_id): **1360 steps** from 17 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1192_sym24`
  - `workers/dispatcher/harvest-6way-r1192_sym24`

## Output

`workers/dispatcher/harvest-11way-r1193_sym24/round-1193/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 11 workers)
- `dense.pt` (averaged across 11 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

