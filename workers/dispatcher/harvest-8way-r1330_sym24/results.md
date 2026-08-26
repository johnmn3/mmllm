# harvest-8way-r1330 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1330 ctrl_bpc |
|--------|--------|--------------:|
| GrUWT | fork-slaa-us-mmllm-claude-train-sym24-5a5ed151-GrUWT | 3.2691 |
| GqKvB | fork-joly-os-mmllm-claude-train-sym24-a331375c-GqKvB | 3.2765 |
| hWvJc | fork-slaa-us-mmllm-claude-train-sym24-29bcf7c7-hWvJc | 3.2987 |
| lcRAw | fork-SeniorCareMarket-mmllm-claude-train-sym24-4411d5e3-lcRAw | 3.3071 |
| UuNXX | fork-SeniorCareMarket-mmllm-claude-train-sym24-7b7fbbed-UuNXX | 3.3176 |
| PsRO7 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5c65dc66-PsRO7 | 3.3611 |
| fuKFZ | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-02129278-fuKFZ | 3.4190 |
| yuVTb | fork-joly-os-mmllm-claude-train-sym24-e602d7a4-yuVTb | 3.6510 |
| **mean** | | **3.3625** |
| **best** | | **3.2691** |

## Chain progression R610 → R1330

Previous harvest: `workers/dispatcher/harvest-2way-merge-r610_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.1372         | 3.3625         | +1.2253 |
| ctrl_bpc best  | 2.1268         | 3.2691         | +1.1423 |

## Per-round trajectory (best bird: GrUWT)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1330 | 6781 | 3.2691 | +0.0868 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r1329_sym24`

## Output

`workers/dispatcher/harvest-8way-r1330_sym24/round-1330/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

