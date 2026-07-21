# harvest-5way-r984 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R984 ctrl_bpc |
|--------|--------|--------------:|
| NiOjF | fork-joly-os-mmllm-claude-train-sym24-d25063cd-NiOjF | 2.5851 |
| wLOi0 | fork-slaa-us-mmllm-claude-train-sym24-0dd2210f-wLOi0 | 2.7821 |
| 3tvVH | origin/claude/train-sym24-ec0a7a23-3tvVH | 2.8018 |
| aiDGu | fork-SeniorCareMarket-mmllm-claude-train-sym24-0af2756c-aiDGu | 2.8066 |
| xRPYH | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f7718d1a-xRPYH | 2.9726 |
| **mean** | | **2.7896** |
| **best** | | **2.5851** |

## Chain progression R983 → R984

Previous harvest: `workers/dispatcher/harvest-7way-r983_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8300         | 2.7896         | -0.0404 |
| ctrl_bpc best  | 2.6125         | 2.5851         | -0.0274 |

## Per-round trajectory (best bird: NiOjF)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 984 | 6469 | 2.5851 | +0.1758 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-3way-r983_sym24`

## Output

`workers/dispatcher/harvest-5way-r984_sym24/round-984/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

