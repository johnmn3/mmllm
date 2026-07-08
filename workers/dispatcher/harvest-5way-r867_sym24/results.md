# harvest-5way-r867 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R867 ctrl_bpc |
|--------|--------|--------------:|
| NNmAu | origin/claude/train-sym24-28a657ce-NNmAu | 2.8680 |
| hSz81 | fork-slaa-us-mmllm-claude-train-sym24-7bf62935-hSz81 | 2.8764 |
| A6M3F | fork-SeniorCareMarket-mmllm-claude-train-sym24-486ca9e1-A6M3F | 2.8791 |
| yAjDM | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-ea3d0384-yAjDM | 3.2431 |
| DWSjL | fork-joly-os-mmllm-claude-train-sym24-6d421bbf-DWSjL | 3.2608 |
| **mean** | | **3.0255** |
| **best** | | **2.8680** |

## Chain progression R866 → R867

Previous harvest: `workers/dispatcher/harvest-1way-r866_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.9291         | 3.0255         | +0.0964 |
| ctrl_bpc best  | 2.9291         | 2.8680         | -0.0611 |

## Per-round trajectory (best bird: NNmAu)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 867 | 6772 | 2.8680 | +0.3750 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r866_sym24`

## Output

`workers/dispatcher/harvest-5way-r867_sym24/round-867/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

