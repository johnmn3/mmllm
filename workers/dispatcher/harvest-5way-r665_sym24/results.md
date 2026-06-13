# harvest-5way-r665 — sparse-delta merge of 5 birds

## Worker endpoints

| handle | branch | R665 ctrl_bpc |
|--------|--------|--------------:|
| 80vBv | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-65c20a86-80vBv | 3.9679 |
| m4wnp | fork-davidwuchn-mmllm-claude-train-sym24-105b59d1-m4wnp | 3.9683 |
| 3pisK | origin/claude/train-sym24-3f844fa4-3pisK | 4.2514 |
| eVx8J | fork-slaa-us-mmllm-claude-train-sym24-0565d755-eVx8J | 4.2750 |
| GWA1r | fork-joly-os-mmllm-claude-train-sym24-6613bc3b-GWA1r | 4.2896 |
| **mean** | | **4.1504** |
| **best** | | **3.9679** |

## Chain progression R664 → R665

Previous harvest: `workers/dispatcher/harvest-11way-r664_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 4.0352         | 4.1504         | +0.1152 |
| ctrl_bpc best  | 3.9325         | 3.9679         | +0.0354 |

## Per-round trajectory (best bird: 80vBv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 665 | 4133 | 3.9679 | +0.1111 |

## Cumulative training contribution

- This harvest: **400 steps** from 5 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-2way-r664_sym24`
  - `workers/dispatcher/harvest-3way-r664_sym24`

## Output

`workers/dispatcher/harvest-5way-r665_sym24/round-665/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 5 workers)
- `dense.pt` (averaged across 5 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

