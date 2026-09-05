# harvest-4way-r1398 — sparse-delta merge of 4 birds

## Worker endpoints

| handle | branch | R1398 ctrl_bpc |
|--------|--------|--------------:|
| 7DkVh | fork-joly-os-mmllm-claude-train-sym24-9b9ad9b7-7DkVh | 3.5519 |
| xXfyZ | fork-SeniorCareMarket-mmllm-claude-train-sym24-f1a8afcf-xXfyZ | 3.8774 |
| 4s4ZL | origin/claude/train-sym24-ad4c0f87-4s4ZL | 4.0398 |
| zaiyR | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-5ab87e4c-zaiyR | 4.5983 |
| **mean** | | **4.0168** |
| **best** | | **3.5519** |

## Chain progression R1397 → R1398

Previous harvest: `workers/dispatcher/harvest-8way-r1397_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.5085         | 4.0168         | +0.5083 |
| ctrl_bpc best  | 3.2680         | 3.5519         | +0.2839 |

## Per-round trajectory (best bird: 7DkVh)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 1398 | 6318 | 3.5519 | +0.0640 |

## Cumulative training contribution

- This harvest: **320 steps** from 4 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-4way-r1397_sym24`

## Output

`workers/dispatcher/harvest-4way-r1398_sym24/round-1398/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 4 workers)
- `dense.pt` (averaged across 4 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

