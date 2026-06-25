# harvest-7way-r759 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R759 ctrl_bpc |
|--------|--------|--------------:|
| wSFVv | fork-slaa-us-mmllm-claude-train-sym24-f79fbf7d-wSFVv | 3.2800 |
| aQvod | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-9099cd32-aQvod | 3.2945 |
| DxZNT | fork-davidwuchn-mmllm-claude-train-sym24-d0707c83-DxZNT | 3.3224 |
| QQPmm | origin/claude/train-sym24-cb7b23ba-QQPmm | 3.3939 |
| T2wSQ | fork-joly-os-mmllm-claude-train-sym24-b12c5b85-T2wSQ | 3.3945 |
| DM5oN | origin/claude/train-sym24-1686e261-DM5oN | 3.6570 |
| 8yrqm | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-f913a41e-8yrqm | 3.6624 |
| **mean** | | **3.4292** |
| **best** | | **3.2800** |

## Chain progression R758 → R759

Previous harvest: `workers/dispatcher/harvest-6way-r758_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3938         | 3.4292         | +0.0354 |
| ctrl_bpc best  | 3.2876         | 3.2800         | -0.0076 |

## Per-round trajectory (best bird: wSFVv)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 759 | 6616 | 3.2800 | +0.5957 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **640 steps** from 8 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r758_sym24`

## Output

`workers/dispatcher/harvest-7way-r759_sym24/round-759/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

