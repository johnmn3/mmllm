# harvest-5way-r1097 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1097 ctrl_bpc |
|--------|--------|--------------:|
| yRTL7 | origin/claude/train-sym24-405576eb-yRTL7 | 2.4016 |
| gcfxx | origin/claude/train-sym24-535b7896-gcfxx | 2.5942 |
| VncPh | fork-slaa-us-mmllm-claude-train-sym24-d649d481-VncPh | 2.5954 |
| DTRKt | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-80e33648-DTRKt | 2.6061 |
| X6Nql | fork-SeniorCareMarket-mmllm-claude-train-sym24-d571505d-X6Nql | 2.8326 |
| **mean** | | **2.6060** |
| **best** | | **2.4016** |

## Chain progression R1096 → R1097

Previous harvest: `workers/dispatcher/harvest-7way-r1096_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.5498         | 2.6060         | +0.0562 |
| ctrl_bpc best  | 2.3998         | 2.4016         | +0.0018 |

## Per-round trajectory (best bird: yRTL7)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1097 | 6554 | 2.4016 | +0.2396 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **560 steps** from 7 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r1096_sym24`

## Output

`workers/dispatcher/harvest-5way-r1097_sym24/round-1097/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

