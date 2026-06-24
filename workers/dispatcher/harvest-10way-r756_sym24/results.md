# harvest-10way-r756 — sparse-delta merge of 10 birds

## Worker endpoints

| handle | branch | R756 ctrl_bpc |
|--------|--------|--------------:|
| kjRVQ | origin/claude/train-sym24-1646a595-kjRVQ | 3.2952 |
| 5Z293 | fork-davidwuchn-mmllm-claude-train-sym24-37b5a63f-5Z293 | 3.3004 |
| 62tyg | fork-slaa-us-mmllm-claude-train-sym24-e402818a-62tyg | 3.3055 |
| nd8JW | fork-joly-os-mmllm-claude-train-sym24-84e4a437-nd8JW | 3.3338 |
| LThMf | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-8e763c96-LThMf | 3.3894 |
| vjO5U | fork-davidwuchn-mmllm-claude-train-sym24-a41274ad-vjO5U | 3.4029 |
| QezR1 | fork-SeniorCareMarket-mmllm-claude-train-sym24-be7f82db-QezR1 | 3.4055 |
| oq34c | fork-joly-os-mmllm-claude-train-sym24-ce3e39ca-oq34c | 3.6679 |
| LmSi2 | fork-slaa-us-mmllm-claude-train-sym24-2a74d3de-LmSi2 | 3.6789 |
| ONmhc | fork-joly-os-mmllm-claude-train-sym24-8d387438-ONmhc | 3.6862 |
| **mean** | | **3.4466** |
| **best** | | **3.2952** |

## Chain progression R755 → R756

Previous harvest: `workers/dispatcher/harvest-5way-r755_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 3.3802         | 3.4466         | +0.0664 |
| ctrl_bpc best  | 3.3004         | 3.2952         | -0.0052 |

## Per-round trajectory (best bird: kjRVQ)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 756 | 6555 | 3.2952 | +0.5440 |

## Cumulative training contribution

- This harvest: **800 steps** from 10 bird(s)
- Across full ancestry (deduped by bird_id): **1200 steps** from 15 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-10way-r755_sym24`
  - `workers/dispatcher/harvest-5way-r755_sym24`

## Output

`workers/dispatcher/harvest-10way-r756_sym24/round-756/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 10 workers)
- `dense.pt` (averaged across 10 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

