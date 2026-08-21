# harvest-5way-r1277 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1277 ctrl_bpc |
|--------|--------|--------------:|
| rJrjO | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b5f71bd0-rJrjO | 2.2215 |
| hsCut | fork-slaa-us-mmllm-claude-train-sym24-62577385-hsCut | 2.2280 |
| cwygn | origin/claude/train-sym24-19817bfe-cwygn | 2.2471 |
| 9BvAM | fork-SeniorCareMarket-mmllm-claude-train-sym24-9fd44df0-9BvAM | 2.4167 |
| fuezd | fork-SeniorCareMarket-mmllm-claude-train-sym24-5c39c7ce-fuezd | 2.4241 |
| **mean** | | **2.3075** |
| **best** | | **2.2215** |

## Chain progression R1276 → R1277

Previous harvest: `workers/dispatcher/harvest-11way-r1276_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3970         | 2.3075         | -0.0895 |
| ctrl_bpc best  | 2.2483         | 2.2215         | -0.0268 |

## Per-round trajectory (best bird: rJrjO)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1277 | 6305 | 2.2215 | +0.2566 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-11way-r1276_sym24`
  - `workers/dispatcher/harvest-5way-r1276_sym24`

## Output

`workers/dispatcher/harvest-5way-r1277_sym24/round-1277/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

