# harvest-7way-r1325 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1325 ctrl_bpc |
|--------|--------|--------------:|
| lLPmX | fork-SeniorCareMarket-mmllm-claude-train-sym24-c9ae9e7d-lLPmX | 3.3586 |
| QeSR3 | fork-joly-os-mmllm-claude-train-sym24-601a6ea9-QeSR3 | 3.3875 |
| hYa91 | origin/claude/train-sym24-6378b726-hYa91 | 3.4145 |
| 9VnwQ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-571d7d92-9VnwQ | 3.4351 |
| npoDg | fork-SeniorCareMarket-mmllm-claude-train-sym24-347ca4c3-npoDg | 3.4966 |
| NdLHn | origin/claude/train-sym24-4f080207-NdLHn | 3.7051 |
| yQqmc | fork-slaa-us-mmllm-claude-train-sym24-ad875e40-yQqmc | 3.7179 |
| **mean** | | **3.5022** |
| **best** | | **3.3586** |

## Chain progression R1324 → R1325

Previous harvest: `workers/dispatcher/harvest-5way-r1324_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5080         | 3.5022         | -0.0058 |
| ctrl_bpc best  | 3.3336         | 3.3586         | +0.0250 |

## Per-round trajectory (best bird: lLPmX)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1325 | 5298 | 3.3586 | +0.0828 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1324_sym24`
  - `workers/dispatcher/harvest-5way-r1324_sym24`

## Output

`workers/dispatcher/harvest-7way-r1325_sym24/round-1325/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

