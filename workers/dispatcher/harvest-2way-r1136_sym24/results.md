# harvest-2way-r1136 — sparse-delta merge of 2 birds

## Worker endpoints

| handle | branch | R1136 ctrl_bpc |
|--------|--------|--------------:|
| CvBQm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-2b439957-CvBQm | 2.3420 |
| AUCRE | fork-slaa-us-mmllm-claude-train-sym24-f0633ba9-AUCRE | 2.5679 |
| **mean** | | **2.4550** |
| **best** | | **2.3420** |

## Chain progression R1135 → R1136

Previous harvest: `workers/dispatcher/harvest-5way-r1135_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.3973         | 2.4550         | +0.0577 |
| ctrl_bpc best  | 2.3522         | 2.3420         | -0.0102 |

## Per-round trajectory (best bird: CvBQm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1136 | 4230 | 2.3420 | +0.2460 |

## Cumulative training contribution

- This harvest: **160 steps** from 2 bird(s)
- Across full ancestry (deduped by bird_id): **320 steps** from 4 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1135_sym24`

## Output

`workers/dispatcher/harvest-2way-r1136_sym24/round-1136/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 2 workers)
- `dense.pt` (averaged across 2 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

