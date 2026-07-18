# harvest-7way-r958 — sparse-delta merge of 7 birds

## Worker endpoints

| handle | branch | R958 ctrl_bpc |
|--------|--------|--------------:|
| 8wKBm | fork-slaa-us-mmllm-claude-train-sym24-41130e9b-8wKBm | 2.6279 |
| LIL09 | fork-SeniorCareMarket-mmllm-claude-train-sym24-3cedb93b-LIL09 | 2.6316 |
| 3dW4f | origin/claude/train-sym24-9d7b3341-3dW4f | 2.6366 |
| 3MUA6 | origin/claude/train-sym24-c2016cab-3MUA6 | 2.8307 |
| y5GK9 | fork-SeniorCareMarket-com-mmllm-claude-train-sym24-b459faf1-y5GK9 | 2.8427 |
| zsB15 | fork-joly-os-mmllm-claude-train-sym24-6891af8f-zsB15 | 2.8438 |
| DtF34 | fork-joly-os-mmllm-claude-train-sym24-76a54fe9-DtF34 | 2.8654 |
| **mean** | | **2.7541** |
| **best** | | **2.6279** |

## Chain progression R957 → R958

Previous harvest: `workers/dispatcher/harvest-5way-r957_sym24`

| metric         | prior          | this           | Δ        |
|----------------|---------------:|---------------:|---------:|
| ctrl_bpc mean  | 2.8089         | 2.7541         | -0.0548 |
| ctrl_bpc best  | 2.6423         | 2.6279         | -0.0144 |

## Per-round trajectory (best bird: 8wKBm)

| round | wall_s | ctrl_bpc | Δ_net   |
|-------|-------:|---------:|--------:|
| 958 | 3541 | 2.6279 | +0.1681 |

## Cumulative training contribution

- This harvest: **560 steps** from 7 bird(s)
- Across full ancestry (deduped by bird_id): **960 steps** from 12 unique bird(s)
- Ancestor harvest(s):
  - `workers/dispatcher/harvest-1way-r957_sym24`
  - `workers/dispatcher/harvest-5way-r957_sym24`

## Output

`workers/dispatcher/harvest-7way-r958_sym24/round-958/`:
- `delta-sparse-net.{0..31}.pt` (row-aware FedAvg merge of 7 workers)
- `dense.pt` (averaged across 7 birds)
- Reference for delta encoding: `workers/dispatcher/harvest-0way-r0_sym24/round-0`

