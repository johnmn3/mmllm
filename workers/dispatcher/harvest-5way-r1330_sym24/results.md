# harvest-5way-r1330 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R1330 ctrl_bpc |
|--------|--------|--------------:|
| GrUWT | fork-slaa-us-mmllm-claude-train-sym24-5a5ed151-GrUWT | 3.2691 |
| UuNXX | fork-SeniorCareMarket-mmllm-claude-train-sym24-7b7fbbed-UuNXX | 3.3176 |
| qKetZ | origin/claude/train-sym24-fc134e4a-qKetZ | 3.3764 |
| fuKFZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-02129278-fuKFZ | 3.4190 |
| yuVTb | fork-joly-os-mmllm-claude-train-sym24-e602d7a4-yuVTb | 3.6510 |
| **mean** | | **3.4066** |
| **best** | | **3.2691** |

## Chain progression R1329 → R1330

Previous harvest: `workers/dispatcher/harvest-1way-r1329_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.2964         | 3.4066         | +0.1102 |
| ctrl_bpc best  | 3.2964         | 3.2691         | -0.0273 |

## Per-round trajectory (best bird: GrUWT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1330 | 6781 | 3.2691 | +0.0868 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **480 steps** from 6 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1329_sym24`

## Output

`workers/dispatcher/harvest-5way-r1330_sym24/round-1330/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

