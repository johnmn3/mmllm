# harvest-7way-r1171 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R1171 ctrl_bpc |
|--------|--------|--------------:|
| QTB50 | fork-slaa-us-mmllm-claude-train-sym24-5aaeb5eb-QTB50 | 2.3347 |
| H7YH9 | fork-SeniorCareMarket-mmllm-claude-train-sym24-a7f508f4-H7YH9 | 2.3349 |
| qWIs9 | origin/claude/train-sym24-90423764-qWIs9 | 2.3409 |
| aS4aK | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-4facb61c-aS4aK | 2.5107 |
| 8wOfh | fork-SeniorCareMarket-mmllm-claude-train-sym24-31e67232-8wOfh | 2.5110 |
| zdgtt | fork-joly-os-mmllm-claude-train-sym24-1be47852-zdgtt | 2.5143 |
| lCb1l | fork-joly-os-mmllm-claude-train-sym24-cfe7e503-lCb1l | 2.7315 |
| **mean** | | **2.4683** |
| **best** | | **2.3347** |

## Chain progression R1170 → R1171

Previous harvest: `workers/dispatcher/harvest-7way-r1170_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.4127         | 2.4683         | +0.0556 |
| ctrl_bpc best  | 2.3084         | 2.3347         | +0.0263 |

## Per-round trajectory (best bird: QTB50)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1171 | 6782 | 2.3347 | +0.2549 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **1120 steps** from 14 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1170_sym24`
  - `workers/dispatcher/harvest-7way-r1170_sym24`

## Output

`workers/dispatcher/harvest-7way-r1171_sym24/round-1171/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

