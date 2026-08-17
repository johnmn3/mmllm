# harvest-6way-r1231 — sparse-delta merge of 6 birds

## Worker endpoints

| handle | branch | R1231 ctrl_bpc |
|--------|--------|--------------:|
| RMAzZ | fork-joly-os-mmllm-claude-train-sym24-5a02ac7f-RMAzZ | 2.2547 |
| XCDG2 | fork-slaa-us-mmllm-claude-train-sym24-454f9fa2-XCDG2 | 2.2660 |
| rbdfq | origin/claude/train-sym24-0887576a-rbdfq | 2.2700 |
| iCeha | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-89afb87a-iCeha | 2.2765 |
| 07kfk | fork-SeniorCareMarket-mmllm-claude-train-sym24-6a9a375a-07kfk | 2.2768 |
| SEFr4 | origin/claude/train-sym24-37923e7d-SEFr4 | 2.6620 |
| **mean** | | **2.3343** |
| **best** | | **2.2547** |

## Chain progression R1230 → R1231

Previous harvest: `workers/dispatcher/harvest-5way-r1230_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4597         | 2.3343         | -0.1254 |
| ctrl_bpc best  | 2.2561         | 2.2547         | -0.0014 |

## Per-round trajectory (best bird: RMAzZ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1231 | 6338 | 2.2547 | +0.2653 |

## Cumulative training contribution

- This harvest: **480 steps** from 6 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1230_sym24`

## Output

`workers/dispatcher/harvest-6way-r1231_sym24/round-1231/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 6 workers)
- `dense.pt` (averaged across 6 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

