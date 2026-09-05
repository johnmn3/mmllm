# harvest-8way-r1398 — sparse-delta merge of 8 birds

## Worker endpoints

| handle | branch | R1398 ctrl_bpc |
|--------|--------|--------------:|
| hV1AE | fork-SeniorCareMarket-mmllm-claude-train-sym24-b78025a2-hV1AE | 3.3661 |
| 52IlV | origin/claude/train-sym24-9647e91a-52IlV | 3.3928 |
| 9YxyZ | fork-joly-os-mmllm-claude-train-sym24-2aa5f33f-9YxyZ | 3.4280 |
| IFpVj | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-01091368-IFpVj | 3.4501 |
| 7DkVh | fork-joly-os-mmllm-claude-train-sym24-9b9ad9b7-7DkVh | 3.5519 |
| xXfyZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-f1a8afcf-xXfyZ | 3.8774 |
| 4s4ZL | origin/claude/train-sym24-ad4c0f87-4s4ZL | 4.0398 |
| zaiyR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5ab87e4c-zaiyR | 4.5983 |
| **mean** | | **3.7130** |
| **best** | | **3.3661** |

## Chain progression R1397 → R1398

Previous harvest: `workers/dispatcher/harvest-8way-r1397_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5085         | 3.7130         | +0.2045 |
| ctrl_bpc best  | 3.2680         | 3.3661         | +0.0981 |

## Per-round trajectory (best bird: hV1AE)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1398 | 3550 | 3.3661 | +0.0748 |

## Cumulative training contribution

- This harvest: **640 steps** from 8 bird(s)
- Across full ancestry (deduped by bird_id): **1280 steps** from 16 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1397_sym24`
  - `workers/dispatcher/harvest-8way-r1397_sym24`

## Output

`workers/dispatcher/harvest-8way-r1398_sym24/round-1398/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 8 workers)
- `dense.pt` (averaged across 8 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

